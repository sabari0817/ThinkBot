from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Message
import json
import logging

logger = logging.getLogger(__name__)

@login_required
def group_chat(request):
    """Render the group chat interface."""
    return render(request, 'chat/group_chat.html')

@login_required
def fetch_messages(request):
                """Return all chat messages as JSON."""
                messages = Message.objects.select_related('sender').order_by('timestamp').values(
                        'id', 'sender__username', 'content', 'timestamp'
                            )
                return JsonResponse(list(messages), safe=False)

@csrf_exempt
@login_required
@require_http_methods(["POST"])
def send_message(request):
        """Handle sending a new message."""
        try:
                                                data = json.loads(request.body)
                                                content = data.get('content', '').strip()

                                                if not content:
                                                                        return JsonResponse({'error': 'Message content cannot be empty.'}, status=400)

                                                                        message = Message.objects.create(sender=request.user, content=content)
                                                                        return JsonResponse({
                                                                                                        'id': message.id,
                                                                                                                    'sender': request.user.username,
                                                                                                                                'content': message.content,
                                                                                                                                            'timestamp': message.timestamp
                                                                                                                                                    }, status=201)

        except json.JSONDecodeError:
                                                                                                                                                                logger.error("Invalid JSON in request body.")
                                                                                                                                                                return JsonResponse({'error': 'Invalid JSON.'}, status=400)

        except Exception as e:
                                                                                                                                                                                logger.exception("Unexpected error occurred while sending message.")
                                                                                                                                                                                return JsonResponse({'error': 'An unexpected error occurred.'}, status=500)