from typing import List, Optional

try:
    import restaurante_app.modelos.producto as modelos_producto
    from restaurante_app.modelos.usuario import Usuario
    from restaurante_app.servicios.archivo_servicio import ArchivoServicio
except ImportError:
    import modelos.producto as modelos_producto
    from modelos.usuario import Usuario
    from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self):
        self._productos: List[modelos_producto.Producto] = []
        self._usuarios: List[Usuario] = []
        self._cargar_datos()

    def _cargar_datos(self) -> None:
        self._productos = ArchivoServicio.cargar_productos()
        self._usuarios = ArchivoServicio.cargar_usuarios()

    def validar_acceso(self, usuario_id: str, contraseña: str) -> Optional[Usuario]:
        if not usuario_id.strip() or not contraseña.strip():
            return None
        try:
            identificacion = int(usuario_id)
        except ValueError:
            return None

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion and usuario.validar_acceso(contraseña):
                return usuario
        return None

    def listar_productos(self) -> List[modelos_producto.Producto]:
        return list(self._productos)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)