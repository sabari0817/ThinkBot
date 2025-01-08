from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from disease_prediction import views as disease_views  # Import the disease prediction views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('mood/', include('mood.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('stress/', include('stress.urls')),
    path('disease_prediction/', include('disease_prediction.urls')),  # Add disease prediction path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
