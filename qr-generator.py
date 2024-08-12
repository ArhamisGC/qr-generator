import qrcode

texto = "https://github.com/ArhamisGC"
imagen = qrcode.make(texto)
imagen.save("codigo.png")