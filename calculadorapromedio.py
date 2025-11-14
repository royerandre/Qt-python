import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # 1. Obtenemos las notas (Si están vacías, dará error y saltará al except)
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        n3 = float(entry_n3.get())
        
        promedio = 0
        opcion = variable_formula.get() # Obtenemos qué círculo se marcó (1, 2 o 3)

        # 2. Lógica de las Fórmulas (Idéntica a tu QML)
        if opcion == 1:
            # Fórmula 1x2x2 (Suma pesos = 5)
            promedio = (n1 * 1 + n2 * 2 + n3 * 2) / 5
            formula_usada = "1x2x2"
            
        elif opcion == 2:
            # Fórmula 2x2x1 (Suma pesos = 5)
            promedio = (n1 * 2 + n2 * 2 + n3 * 1) / 5
            formula_usada = "2x2x1"
            
        elif opcion == 3:
            # Fórmula 1x2x3 (Suma pesos = 6)
            promedio = (n1 * 1 + n2 * 2 + n3 * 3) / 6
            formula_usada = "1x2x3"
        else:
            messagebox.showwarning("Atención", "¡Por favor selecciona una fórmula!")
            return

        # 3. Mostrar resultado
        label_resultado.config(text=f"Nota Final ({formula_usada}): {promedio:.2f}", fg="#0078d7")

    except ValueError:
        messagebox.showerror("Error", "Asegúrate de ingresar solo números en las casillas.")

# --- CONFIGURACIÓN DE LA VENTANA ---
ventana = tk.Tk()
ventana.title("CalcUAC Python")
ventana.geometry("350x450")
ventana.configure(bg="#f0f0f0") # Color de fondo gris suave

# Título
tk.Label(ventana, text="Calculadora de Notas", font=("Segoe UI", 16, "bold"), bg="#f0f0f0").pack(pady=15)

# --- SELECCIÓN DE FÓRMULA (RADIO BUTTONS) ---
tk.Label(ventana, text="Seleccione fórmula:", bg="#f0f0f0", font=("Segoe UI", 10)).pack()

# Esta variable guardará la opción elegida (1, 2 o 3)
variable_formula = tk.IntVar() 
variable_formula.set(1) # Marcamos la primera por defecto para que no falle

frame_radios = tk.Frame(ventana, bg="#f0f0f0")
frame_radios.pack(pady=5)

tk.Radiobutton(frame_radios, text="1x2x2", variable=variable_formula, value=1, bg="#f0f0f0").pack(anchor="w")
tk.Radiobutton(frame_radios, text="2x2x1", variable=variable_formula, value=2, bg="#f0f0f0").pack(anchor="w")
tk.Radiobutton(frame_radios, text="1x2x3", variable=variable_formula, value=3, bg="#f0f0f0").pack(anchor="w")

# --- CAJAS DE NOTAS ---
tk.Label(ventana, text="Ingrese sus notas:", bg="#f0f0f0", font=("Segoe UI", 10, "bold")).pack(pady=(15, 5))

frame_notas = tk.Frame(ventana, bg="#f0f0f0")
frame_notas.pack()

tk.Label(frame_notas, text="Nota 1:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
entry_n1 = tk.Entry(frame_notas, width=10, justify="center")
entry_n1.grid(row=0, column=1)

tk.Label(frame_notas, text="Nota 2:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
entry_n2 = tk.Entry(frame_notas, width=10, justify="center")
entry_n2.grid(row=1, column=1)

tk.Label(frame_notas, text="Nota 3:", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
entry_n3 = tk.Entry(frame_notas, width=10, justify="center")
entry_n3.grid(row=2, column=1)

# --- BOTÓN CALCULAR ---
btn_calcular = tk.Button(ventana, text="Calcular Promedio", command=calcular, bg="#0078d7", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=20, pady=5)
btn_calcular.pack(pady=20)

# --- RESULTADO ---
label_resultado = tk.Label(ventana, text="Tu promedio aparecerá aquí", font=("Segoe UI", 12), bg="#f0f0f0")
label_resultado.pack()

# Iniciar la aplicación
ventana.mainloop()