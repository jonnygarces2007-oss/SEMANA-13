import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable, Optional

try:
    from ..servicios.restaurante_servicio import RestauranteServicio
    from ..modelos.usuario import Usuario
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio
    from modelos.usuario import Usuario


class LoginView:
    def __init__(self, ventana_padre: tk.Tk, servicio: RestauranteServicio, al_ingresar: Callable[[Usuario], None]):
        self.ventana = ventana_padre
        self.servicio = servicio
        self.al_ingresar = al_ingresar
        self.usuario_actual: Optional[Usuario] = None
        self._construir()

    def _construir(self) -> None:
        self.ventana.title("🍽️ Inicio de Sesión - Restaurante")
        self.ventana.geometry("420x320")
        self.ventana.resizable(False, False)

        marco = ttk.Frame(self.ventana, padding=40)
        marco.pack(expand=True, fill=tk.BOTH)

        ttk.Label(marco, text="🍽️ SISTEMA DE RESTAURANTE", font=("Arial", 14, "bold")).pack(pady=(0, 30))

        ttk.Label(marco, text="Identificación de Usuario:").pack(anchor=tk.W)
        self.entrada_usuario = ttk.Entry(marco, width=40)
        self.entrada_usuario.pack(pady=5, fill=tk.X)

        ttk.Label(marco, text="Contraseña:").pack(anchor=tk.W, pady=(15, 0))
        self.entrada_contraseña = ttk.Entry(marco, width=40, show="*")
        self.entrada_contraseña.pack(pady=5, fill=tk.X)

        self.etiqueta_mensaje = ttk.Label(marco, text="", foreground="red")
        self.etiqueta_mensaje.pack(pady=10)

        ttk.Button(marco, text="Ingresar", command=self._al_pulsar_ingresar).pack(pady=10, fill=tk.X)

    def _al_pulsar_ingresar(self) -> None:
        usuario_id = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()

        if not usuario_id.strip() or not contraseña.strip():
            self.etiqueta_mensaje.config(text="⚠️ Complete ambos campos.")
            return

        usuario = self.servicio.validar_acceso(usuario_id, contraseña)
        if usuario:
            self.usuario_actual = usuario
            self.al_ingresar(usuario)
        else:
            self.etiqueta_mensaje.config(text="❌ Credenciales incorrectas.")

    def limpiar(self) -> None:
        self.entrada_usuario.delete(0, tk.END)
        self.entrada_contraseña.delete(0, tk.END)
        self.etiqueta_mensaje.config(text="")