import falcon, json


def time_string_to_seconds(time_string):
    return {
        '10 Minutos':600,
        'Una Hora':3600,
        'Un día':86400,
        'Una semana':604800,
        'Dos semanas': 1209600,
        'Un mes':2419200
    }[time_string]


def req_to_json(req):
    if req.content_length in (None, 0):
        return

    body = req.stream.read()
    print("BOYD", body)
    if not body:
        raise falcon.HTTPBadRequest('Empty request body',
                                    'A valid JSON document is required.')

    try:
        req.context['doc'] = json.loads(body.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        raise falcon.HTTPError(falcon.HTTP_753,
                               'Malformed JSON',
                               'Could not decode the request body. The '
                               'JSON was incorrect or not encoded as '
                               'UTF-8.')
    print(req.context['doc'])
    return req.context['doc']

