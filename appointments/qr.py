import qrcode

whatsapp_link = "https://wa.me/8591403229?text=Book%20Appointment"

img = qrcode.make(whatsapp_link)
img.save("ai_law_assist_qr.png")

print("QR generated")
