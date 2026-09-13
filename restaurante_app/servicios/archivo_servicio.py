import json
from pathlib import Path
from typing import List

try:
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
except ImportError:
    from modelos.producto import Producto
    from modelos.usuario import Usuario

BASE_DIR = Path(__file__).resolve().parents[1]
RUTA_PRODUCTOS = BASE_DIR / "datos" / "productos.json"
RUTA_USUARIOS = BASE_DIR / "datos" / "usuarios.json"


class ArchivoServicio:

    @staticmethod
    def cargar_productos() -> List[Producto]:
        productos: List[Producto] = []
        try:
            with open(RUTA_PRODUCTOS, mode="r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
            for registro in registros:
                productos.append(Producto.from_dict(registro))
        except FileNotFoundError:
            print("ℹ️ productos.json no existe.")
        except json.JSONDecodeError:
            print("⚠️ productos.json dañado.")
        return productos

    @staticmethod
    def cargar_usuarios() -> List[Usuario]:
        usuarios: List[Usuario] = []
        try:
            with open(RUTA_USUARIOS, mode="r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
            for registro in registros:
                usuarios.append(Usuario.from_dict(registro))
        except FileNotFoundError:
            print("ℹ️ usuarios.json no existe.")
        except json.JSONDecodeError:
            print("⚠️ usuarios.json dañado.")
        return usuarios