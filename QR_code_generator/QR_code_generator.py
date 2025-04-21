import qrcode

data = input("Enter the URL    :").strip()
filename = input("Enter the file name   :").strip()

qr=qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black",back_color="white")
if not filename.lower().endswith(".png"):
    filename += ".png"
    image.save(filename)
else:
        image.save(filename)
print(f"QR code is saved in {filename}")