from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from ai_agent.law_agent import law_agent
from .utils import is_booking_intent
from django.http import HttpResponse


def ai_law_assist(request):
    user_msg = request.GET.get("msg")

    ai_reply = law_agent(user_msg)

    if is_booking_intent(user_msg):
        ai_reply += "\n\nSend details as:\nName | Email | Date | Time"

    return JsonResponse({"reply": ai_reply})



def qr_view(request):
    return HttpResponse("QR page is working ✅")
