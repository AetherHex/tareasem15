import customtkinter as ctk

ventana = ctk.CTk()
ventana.geometry("620x540")
ventana.title("App")
ventana.minsize(500, 400)

# 1. Configuración global de CustomTkinter
ctk.set_appearance_mode(
    "Dark"
)  # Opciones: "System" (automático), "Dark" (oscuro), "Light" (claro)
ctk.set_default_color_theme("green")  # Opciones: "blue", "green", "dark-blue"

# # 2. Configuración de estilo moderno para mejorar los componentes ttk
# style = ttk.Style()
# style.theme_use("winnative")  # Evita el estilo pixelado clásico de Windows antiguo

# # formulario
frame_formulario = ctk.CTkFrame(ventana)
frame_formulario.pack(fill="x", padx=15, pady=10)

# # Agregamos un componente dentro del frame para que tenga contenido

lbl_titulo_frame = ctk.CTkLabel(
    frame_formulario,
    text="Ingrese su nombre",
    font=ctk.CTkFont(weight="bold", size=(24)),
)
lbl_titulo_frame.pack(padx=10, pady=(5, 10), anchor="w")

# Instrucción
lbl_instruccion = ctk.CTkLabel(frame_formulario, text="Introduce los datos:")
lbl_instruccion.pack(padx=10, pady=5, anchor="w")

input_datos = ctk.CTkEntry(frame_formulario, placeholder_text="Escribe aqui...")
input_datos.pack(fill=("x"), padx=15, pady=(5, 10))

boton = ctk.CTkButton(
    ventana, text="Enviar datos", command=lambda: print("!datos enviados!")
)
boton.pack(padx=15, pady=10)


ventana.mainloop()
