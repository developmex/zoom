import json
from pprint import pprint


archivo = "datos.json"



with open(archivo) as data_file:
    data = json.load(data_file)


pprint(data["meetings"])