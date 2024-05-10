import json
from GestionUsuarios import PedirDocumento

JSON_UBICACION = "Datos/UsuariosServiciosProductos.json"

def SignIn():
    Documento_Ingresado = PedirDocumento()
    file = open(JSON_UBICACION)
    file_antes_mod = json.load(file)
    Usuarios = file_antes_mod["Usuarios"]
    for user in Usuarios:
        if user["Documento"] == Documento_Ingresado and user["Rol"] == "User":
            print(user["Documento"])