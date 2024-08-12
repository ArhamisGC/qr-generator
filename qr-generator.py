import tkinter as tk
from PIL import Image, ImageTk

# Crear una ventana básica
root = tk.Tk()
root.title("Prueba de Tkinter y Pillow")

# Crear una imagen de prueba con Pillow
image = Image.new("RGB", (100, 100), "blue")
photo = ImageTk.PhotoImage(image)

# Mostrar la imagen en la ventana
label = tk.Label(root, image=photo)
label.pack()

# Ejecutar la aplicación
root.mainloop()