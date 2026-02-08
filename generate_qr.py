import qrcode

# Replace with YOUR BUSINESS WhatsApp number
whatsapp_link = "https://wa.me/919876543210?text=Book%20Appointment"

img = qrcode.make(whatsapp_link)
img.save("ai_law_assist_qr.png")

print("QR code generated successfully")
