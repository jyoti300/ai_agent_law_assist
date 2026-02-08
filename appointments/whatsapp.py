from twilio.twiml.messaging_response import MessagingResponse
from ai_agent.law_agent import law_agent

def whatsapp_bot(request):
    msg = request.POST.get("Body")
    response = MessagingResponse()
    response.message(law_agent(msg))
    return response
