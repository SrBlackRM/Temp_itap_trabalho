from httpx import get
from os import system

YEAR_START = 1973
YEAR_END = 2024

def get_data_list_rows(rows):
    new_rows = []
    start = YEAR_START
    for count, row in enumerate(rows):
        month = row['c'][0]['v']
        max = row['c'][1]['v']
        min = row['c'][2]['v']
        new_rows.append({"year":start+count, "month":month,"max":max, "min":min})
    return new_rows
    
    
def get_maximun_max(data_list):
    maximun = 0
    info = {}
        
    for dict in data_list:
        max = dict["max"]
        if max >= maximun:
            maximun = max
            try:
                info["max"] = maximun
                info["year"] = dict["year"]
                info["month"] = dict["month"]
            except:
                info["month"] = dict["max_month"]

    return info

def get_minimun_min(data_list):
    minimun = 50
    info = {}
    
    for dict in data_list:
        min = dict["min"]
        if min <= minimun:
            minimun = min
            try:
                info["min"] = minimun
                info["year"] = dict["year"]
                info["month"] = dict["month"]
            except:
                info["month"] = dict["min_month"]
    
    return info


def get_full_list_max_min():
    max_min_years_list = []

    for i in range(YEAR_START, YEAR_END+1):
        url = f'https://www.tempo.com/peticiones/datosgrafica_sactual_16.php?id_estacion=571e07b8c76c49177837d4e1&accion=RTA&id_localidad=115841&anno={i}'
        rows = get(url).json()['rows']
        rows = get_data_list_rows(rows)
        max_info = get_maximun_max(rows)
        min_info = get_minimun_min(rows)
        max_min_years_list.append({"year":i, "max":max_info["max"],"min":min_info["min"], "max_month":max_info["month"], "min_month":min_info["month"]})
   
    return max_min_years_list

def show_result(list):
    for i in list:
        print(f'ANO {i["year"]}\nmáximo: {i["max"]}\nmínimo: {i["min"]}\n\n')
        
        
full_list_all_years = get_full_list_max_min()
min_info = get_minimun_min(full_list_all_years) 
max_info = get_maximun_max(full_list_all_years) 

system('clear')
print(f'Máximo e Mínimo de temperatura já registrado em Itapecerica da Serra desde {YEAR_START}:')
print(f'Mínima: {min_info['min']}°C em {min_info['month']} de {min_info['year']}')
print(f'Máximo: {max_info['max']}°C em {max_info['month']} de {max_info['year']}')
print('\n\n')