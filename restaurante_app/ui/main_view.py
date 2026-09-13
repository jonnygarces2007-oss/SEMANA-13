import tkinter as tk
from tkinter import ttk
from typing import Callable, List

try:
    from ..servicios.restaurante_servicio import RestauranteServicio
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio
    from modelos.producto import Producto
    from modelos.usuario import Usuario


class MainView:
    def __init__(self, ventana_padre: tk.Tk, servicio: RestauranteServicio, usuario_actual: Usuario, al_cerrar_sesion: Callable[[], None]):
        self.ventana = ventana_padre
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion
        self.marco_activo: tk.Widget | None = None
        self._construir()

    def _construir(self) -> None:
        self.ventana.title(f"🍽️ Panel Principal — {self.usuario_actual.nombre}")
        self.ventana.geometry("720x500")

        # --- Barra superior ---
        barra = ttk.Frame(self.ventana, padding=10)
        barra.pack(fill=tk.X)
        ttk.Label(barra, text=f"Bienvenido: {self.usuario_actual.nombre}", font=("Arial", 11, "bold")).pack(side=tk.LEFT)
        ttk.Button(barra, text="Cerrar Sesión", command=self._cerrar_sesion).pack(side=tk.RIGHT)

        # --- Botones de menú ---
        marco_botones = ttk.Frame(self.ventana, padding=10)
        marco_botones.pack(fill=tk.X)
        ttk.Button(marco_botones, text="📦 Productos", command=self._mostrar_productos).pack(side=tk.LEFT, padx=5)
        ttk.Button(marco_botones, text="👥 Usuarios", command=self._mostrar_usuarios).pack(side=tk.LEFT, padx=5)
        ttk.Button(marco_botones, text="🛒 Ventas (pendiente)", state=tk.DISABLED).pack(side=tk.LEFT, padx=5)

        # --- Área de contenido ---
        self.contenido = ttk.Frame(self.ventana, padding=15)
        self.contenido.pack(expand=True, fill=tk.BOTH)

        self._mostrar_bienvenida()

    def _limpiar_contenido(self) -> None:
        for hijo in self.contenido.winfo_children():
            hijo.destroy()

    def _mostrar_bienvenida(self) -> None:
        self._limpiar_contenido()
        ttk.Label(self.contenido, text="✅ Conexión establecida", font=("Arial", 13)).pack(pady=20)
        ttk.Label(self.contenido, text=f"Productos registrados: {self.servicio.cantidad_productos()}").pack(pady=5)
        ttk.Label(self.contenido, text=f"Usuarios registrados: {self.servicio.cantidad_usuarios()}").pack(pady=5)
        ttk.Label(self.contenido, text="Seleccione una opción arriba.").pack(pady=20)

    def _mostrar_productos(self) -> None:
        self._limpiar_contenido()
        ttk.Label(self.contenido, text="📦 Lista de Productos", font=("Arial", 12, "bold")).pack(pady=(0, 10))

        tabla = ttk.Treeview(self.contenido, columns=("cod", "nom", "cat", "pre", "stk"), show="headings", height=12)
        tabla.heading("cod", text="Código")
        tabla.heading("nom", text="Nombre")
        tabla.heading("cat", text="Categoría")
        tabla.heading("pre", text="Precio")
        tabla.heading("stk", text="Stock")

        tabla.column("cod", width=70)
        tabla.column("nom", width=200)
        tabla.column("cat", width=150)
        tabla.column("pre", width=90)
        tabla.column("stk", width=70)

        tabla.pack(expand=True, fill=tk.BOTH)

        productos: List[Producto] = self.servicio.listar_productos()
        for p in productos:
            tabla.insert("", tk.END, values=(p.codigo, p.nombre, p.categoria, f"${p.precio:.2f}", p.stock))

    def _mostrar_usuarios(self) -> None:
        self._limpiar_contenido()
        ttk.Label(self.contenido, text="👥 Lista de Usuarios", font=("Arial", 12, "bold")).pack(pady=(0, 10))

        tabla = ttk.Treeview(self.contenido, columns=("id", "nom", "cor"), show="headings", height=12)
        tabla.heading("id", text="Identificación")
        tabla.heading("nom", text="Nombre")
        tabla.heading("cor", text="Correo")

        tabla.column("id", width=130)
        tabla.column("nom", width=250)
        tabla.column("cor", width=230)
        tabla.pack(expand=True, fill=tk.BOTH)

        usuarios: List[Usuario] = self.servicio.listar_usuarios()
        for u in usuarios:
            tabla.insert("", tk.END, values=(u.identificacion, u.nombre, u.correo))

    def _cerrar_sesion(self) -> None:
        self.al_cerrar_sesion()