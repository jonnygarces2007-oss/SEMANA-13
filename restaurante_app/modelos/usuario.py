class Usuario:
    def __init__(self, identificacion: int, nombre: str, correo: str, contraseña: str = ""):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def __str__(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

    def validar_acceso(self, contraseña_ingresada: str) -> bool:
        return self.contraseña == contraseña_ingresada

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "contraseña": self.contraseña
        }

    @classmethod
    def from_dict(cls, datos: dict):
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"],
            contraseña=datos.get("contraseña", "")
        )