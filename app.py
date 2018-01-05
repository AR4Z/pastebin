import json
import os
from utils.utils import time_string_to_seconds
from data.schemas import Paste
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

import falcon
from falcon_cors import CORS

client = MongoClient(os.getenv('DB_host'), 27017)
db = client.pastebin

paste_schema = Paste()


def req_to_json(req):
    data = req.stream.read(req.content_length or 0)
    print(data)
    try:
        raw_json = req.stream.read()
    except Exception as ex:
        raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

    try:
        result_json = json.loads(raw_json, encoding='utf-8')
    except ValueError:
        raise falcon.HTTPError(
            falcon.HTTP_400,
            'Malformed JSON',
            'Could not decode the request body. The ',
            'JSON was incorrect.'
        )

    return result_json


class PasteCreatorResource:
    def on_post(self, req, resp):
        paste = req_to_json(req)
        date_expiration = str((datetime.now() +
                                    timedelta(seconds=time_string_to_seconds(
                                        paste["time_expiration"]))).strftime('%Y-%m-%d %H:%M:%S'))
        print(date_expiration)
        paste.update({
            '_id': str(ObjectId()),
            'date_expiration': date_expiration
        })

        valid_paste, errors = paste_schema.load(paste)

        if errors:
            resp.body = json.dumps(errors)
            resp.status = falcon.HTTP_400
            print(errors)
            return

        result = db.pastes.insert_one(valid_paste)

        if not result.acknowledged:
            resp.body = {
                'message': 'Create paste is not posible'
            }
            resp.status = falcon.HTTP_404
            return

        resp.status = falcon.HTTP_201
        resp.body = json.dumps({
            'message': 'Ok',
            'paste': dumps(valid_paste)
        })


class PasteViewResource:
    def on_post(self, req, resp, paste_id):
        result = db.pastes.find_one({'_id': paste_id})
        print(result)
        if not result or (datetime.strptime(result["date_expiration"], '%Y-%m-%d %H:%M:%S') <= datetime.now()):
            resp.status = falcon.HTTP_404
            return

        resp.status = falcon.HTTP_200
        resp.body = json.dumps({
            'message': 'Ok',
            'paste': dumps(result)
        })


cors = CORS(allow_origins_list=['http://127.0.0.1:8000'])

api = falcon.API(middleware=[cors.middleware])

api.add_route('/', PasteCreatorResource())
api.add_route('/{paste_id}', PasteViewResource())
