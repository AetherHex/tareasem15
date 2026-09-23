import json

from pydantic.dataclasses import dataclass

from modelos.producto import Producto

_ = json


@dataclass
class Archivo_Servicio:
    def __init__(self) -> None:
        self.ruta_productos = r"datos/productos.json"

    def cargar_productos(self) -> list[Producto]:
        # cargamos el archivo en una variable nombrada archivo
        with open(self.ruta_productos, "r", encoding="utf-8") as archivo:
            # para convertir el archivo en diccionario
            datos_leidos = json.load(archivo)
            # aqui guardaremos los productos como una lista
            lista_productos = []

            for dato in datos_leidos:
                nuevo_producto = Producto(**dato)
                lista_productos.append(nuevo_producto)

        return lista_productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        pass
