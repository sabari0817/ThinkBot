from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from disease_prediction import views as disease_views  # Import the disease prediction views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('mood/', include('mood.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('stress/', include('stress.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('disease_prediction/', include('disease_prediction.urls')),  # Add disease prediction path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
