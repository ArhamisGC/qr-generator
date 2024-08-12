import qrcode
import qrcode.constants
import tkinter as tk
from PIL import ImageTk, Image

url = input("Input a URL:")

qr = qrcode.QRCode(
    version=3,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 5
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="#512da8",back_color="black")
img.save("qrcode.png")

root = tk.Tk()

img_tk = ImageTk.PhotoImage(img)

label = tk.Label(root, image=img_tk)
label.pack()

width,height = img.size

root.geometry(f"{width}x{height}")

root.mainloop()