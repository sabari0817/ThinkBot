from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import random

@login_required
def chatbot(request):
    return render(request, 'chatbot/chatbot.html')

@login_required
def chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        
        # Basic response logic (can be enhanced with more sophisticated AI/ML)
        responses = [
            "I understand you're feeling that way. Would you like to talk more about it?",
            "That sounds challenging. Remember, it's okay to take things one step at a time.",
            "I'm here to listen. Would you like to explore some coping strategies?",
            "Your feelings are valid. Have you considered talking to a mental health professional?",
            "Sometimes taking a deep breath and focusing on the present moment can help.",
            "You're not alone in this. Many people experience similar feelings.",
            "Would you like to try some relaxation exercises together?",
            "Remember to be kind to yourself during difficult times.",
            "Have you tried writing down your thoughts in the mood tracker?",
            "It's brave of you to share your feelings. How can I support you better?"
        ]
        
        bot_message = random.choice(responses)
        return JsonResponse({'message': bot_message})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
