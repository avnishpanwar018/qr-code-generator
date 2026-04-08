import qrcode

target_url=input("Enter the URL : ").strip()
output_path="qrcode.png"

qr_code=qrcode.QRCode()
qr_code.add_data(target_url)

qr_image=qr_code.make_image()
qr_image.save(output_path)

print("QR Code is generated!")