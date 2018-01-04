def time_string_to_seconds(time_string):
    return {
        '10 Minutos':600,
        'Una Hora':3600,
        'Un día':86400,
        'Una semana':604800,
        'Dos semanas': 1209600,
        'Un mes':2419200
    }[time_string]


