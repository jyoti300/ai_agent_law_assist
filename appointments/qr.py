import qrcode

whatsapp_link = "https://wa.me/+918591403228?text=Book%20Appointment"

img = qrcode.make(whatsapp_link)
img.save("ai_law_assist_live_qr.png")

print("QR generated")
