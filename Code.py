import qrcode
img = input("Enter the URL to Generate QRcode: ")
# Enter the URL or any test here to Generate the QRcode.
gen = qrcode.make(img)
gen.save("Qrcode.jpg")
