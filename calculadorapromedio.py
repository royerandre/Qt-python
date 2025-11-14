import tkinter as tk
from tkinter import messagebox

# --- AQUÍ VA LA LÓGICA (EL CEREBRO) ---
def calcular():
    try:
        # 1. Obtenemos lo que escribió el usuario en las cajas
        # .get() toma el texto
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        n3 = float(entry_n3.get())

        # 2. Aplicamos la fórmula (Ejemplo: 1x2x2)
        # Suma de pesos = 5
        promedio = (n1 * 1 + n2 * 2 + n3 * 2) / 5

        # 3. Mostramos el resultado en la etiqueta de abajo
        # .config() cambia las propiedades, como el texto
        label_resultado.config(text=f"Tu Nota Final es: {promedio:.2f}", fg="blue")

    except ValueError:
        # Si escriben letras o lo dejan vacío, salta este error
        messagebox.showerror("Error", "¡Por favor ingresa solo números!")

# --- AQUÍ VA EL DISEÑO (LA CARA) ---
ventana = tk.Tk()
ventana.title("Calculadora Python")
ventana.geometry("300x350") # Tamaño de la ventana

# Creamos los textos y las cajas (Entradas)
tk.Label(ventana, text="Ingrese sus notas:", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(ventana, text="Nota 1:").pack()
entry_n1 = tk.Entry(ventana) # Caja de texto
entry_n1.pack()

tk.Label(ventana, text="Nota 2:").pack()
entry_n2 = tk.Entry(ventana)
entry_n2.pack()

tk.Label(ventana, text="Nota 3:").pack()
entry_n3 = tk.Entry(ventana)
entry_n3.pack()

# Espacio vacío
tk.Label(ventana, text="").pack()

# El Botón
boton = tk.Button(ventana, text="Calcular Promedio", command=calcular, bg="lightgray")
boton.pack(ipadx=10, ipady=5) # ipadx/y es el relleno interno del botón

# Espacio para el resultado
tk.Label(ventana, text="").pack()
label_resultado = tk.Label(ventana, text="---", font=("Arial", 14))
label_resultado.pack()

# Esto mantiene la ventana abierta
ventana.mainloop()