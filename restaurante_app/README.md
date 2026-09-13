# 🍽️ Sistema de Restaurante - Semana 13

**Asignatura:** Programación Orientada a Objetos
**Estudiante:** Kevin Bolivar Lascano Sanchez
**Fecha:** Septiembre 2026

---

## 🎯 Propósito
Incorporar **Interfaz Gráfica de Usuario (GUI)** mediante **Tkinter**, manteniendo la arquitectura modular y separación de responsabilidades. Se implementa pantalla de acceso, panel principal y visualización de datos cargados desde JSON.

---

## 📁 Estructura del Proyecto
restaurante_app/
├── datos/ ↔ Archivos JSON con productos y usuarios
├── modelos/ ↔ Clases Producto y Usuario
├── servicios/ ↔ Lectura de JSON y lógica de negocio
│ ├── archivo_servicio.py
│ └── restaurante_servicio.py
├── ui/ ↔ Vistas gráficas con Tkinter
│ ├── login_view.py ↔ Pantalla de inicio de sesión
│ └── main_view.py ↔ Panel principal tras acceso
├── main.py ↔ Prepara dependencias y controla el flujo
└── README.md
plaintext

---

## 🔄 Flujo de la Aplicación
Inicio → LoginView → valida con RestauranteServicio → MainView
↓
Productos | Usuarios | Ventas (pendiente)
↓
Cerrar Sesión → regresa a LoginView
plaintext

---

## 🔑 Credenciales de Prueba
| Identificación | Contraseña | Usuario |
|---|---|---|
| `123456789` | `123456` | Kevin Bolivar Lascano Sanchez |
| `987654321` | `654321` | Maria Lopez |

---

## 🚀 Ejecución
```bash
python main.py