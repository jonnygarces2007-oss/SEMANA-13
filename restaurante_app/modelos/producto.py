class Producto:
    def __init__(self, codigo: int, nombre: str, categoria: str, precio: float, stock: int = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self) -> str:
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, datos: dict):
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            stock=datos.get("stock", 0)
        )