import json

def json_to_py(cd_json):
    '''Читает json с путем  'cd_json' и возвращает список словарей'''
    with open(cd_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
    
def read_config(cd_config, observer_longitude=True, observer_latitude=True, 
                observer_altitude=True, time_zone = True, step = True,
                end_time_hours=True, telegram_bot_token=True,
                venv_name = True):
    '''
    функция читает конфиг и возвращает список с нужными параметрами упорядоченными так же как и сам конфиг
    '''
    config = json_to_py(cd_config)
    out = []
    
    if observer_longitude == True:
        out.append(config.get('observer longitude'))
    
    if observer_latitude == True:
        out.append(config.get('observer latitude'))
    
    if observer_altitude == True:
        out.append(config.get('observer altitude'))
    
    if time_zone == True:
        out.append(config.get("time zone utc"))

    if step == True:
        out.append(config.get('step'))
    
    if end_time_hours == True:
        out.append(config.get('calculations for next (hours)'))
    
    if telegram_bot_token == True:
        out.append(config.get('telegram bot token'))
    
    if venv_name == True:
        out.append(config.get('venv name'))
    
    return out

        