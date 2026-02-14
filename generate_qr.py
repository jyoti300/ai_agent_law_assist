import qrcode

# Replace with YOUR BUSINESS WhatsApp number
#whatsapp_link = "https://wa.me/8591403229?text=Book%20Appointment"

#img = qrcode.make(whatsapp_link)


img = qrcode.make("https://ai-agent-law-assist.onrender.com/book/")
img.save("ai_law_assist_live_qr.png")

print("Live QR generated successfully")
