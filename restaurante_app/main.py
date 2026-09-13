import tkinter as tk

try:
    from .servicios.restaurante_servicio import RestauranteServicio
    from .ui.login_view import LoginView
    from .ui.main_view import MainView
    from .modelos.usuario import Usuario
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio
    from ui.login_view import LoginView
    from ui.main_view import MainView
    from modelos.usuario import Usuario


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.servicio = RestauranteServicio()
        self.vista_actual = None
        self._mostrar_login()

    def _limpiar_vista(self) -> None:
        for hijo in self.ventana.winfo_children():
            hijo.destroy()

    def _mostrar_login(self) -> None:
        self._limpiar_vista()
        self.vista_actual = LoginView(self.ventana, self.servicio, self._al_ingresar)

    def _al_ingresar(self, usuario: Usuario) -> None:
        self._limpiar_vista()
        self.vista_actual = MainView(self.ventana, self.servicio, usuario, self._al_cerrar_sesion)

    def _al_cerrar_sesion(self) -> None:
        self._mostrar_login()
        if hasattr(self.vista_actual, "limpiar"):
            self.vista_actual.limpiar()

    def ejecutar(self) -> None:
        self.ventana.mainloop()


if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()