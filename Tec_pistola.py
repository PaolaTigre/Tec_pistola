import tkinter as tk

def disparar():
    if balas:
        bala = balas.pop(0)
        estado_actual.config(text=f"Bala disparada: {bala}")
    else:
        estado_actual.config(text="No quedan balas")

def recargar_una_vez():
    if len(balas) < 15:
        balas.append(max(balas) + 1 if balas else 1)
        estado_actual.config(text="Recarga exitosa")
    else:
        estado_actual.config(text="No se puede recargar pistola llena")

def recargar_cinco():
    if len(balas) < 11:
        balas.extend(range(max(balas) + 1, max(balas) + 6))
        estado_actual.config(text="Recargas 5 balas")
    else:
        estado_actual.config(text="No se puede recargar pistola llena")

def salir():
    ventana.quit()


ventana = tk.Tk()
ventana.title("Sistema de pistola")


balas = list(range(1, 11))

btn_disparar = tk.Button(ventana, text="Disparar", command=disparar)
btn_recargar_una_vez = tk.Button(ventana, text="Recargar una vez", command=recargar_una_vez)
btn_recargar_cinco = tk.Button(ventana, text="Recargar 5 balas", command=recargar_cinco)
btn_salir = tk.Button(ventana, text="Salir", command=salir)

estado_actual = tk.Label(ventana, text="Estado actual de la pistola")

btn_disparar.pack()
btn_recargar_una_vez.pack()
btn_recargar_cinco.pack()
btn_salir.pack()
estado_actual.pack()

ventana.mainloop()
