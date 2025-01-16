from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.contrib.auth.models import User

@login_required
def chat_view(request):
    users = User.objects.exclude(id=request.user.id)  # Get all users except the current user
    messages = ChatMessage.objects.filter(receiver=request.user)  # Retrieve all messages for the current user

    return render(request, 'chat/chat.html', {
        'users': users,
        'messages': messages
    })
