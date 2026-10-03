import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

data = "PHAINON OF AEDES ELYSIAE"

qr = qrcode.QRCode()
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
img.save("phainon.png")

img2 = Image.open("phainon.png")
decoded = decode(img2)
print(decoded[0].data.decode('utf-8'))