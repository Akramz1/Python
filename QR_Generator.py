import qrcode

Data = input("Enter the URL: ").strip()
Filename = input("Enter the filename: ").strip()
qr = qrcode.QRCode(
    version=1,  # From here you change the size
    # this specify the amount of error you want it to handle
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # the size of boxes inside the qr
    border=4,  # the thickness of the border
)
qr.add_data(Data)
# colors of your code
image = qr.make_image(fill_color='black', back_color='white')
image.save(f'{Filename}.jpg')
print(f"QR code saved as {Filename}")
