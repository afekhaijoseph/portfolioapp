from django.contrib import admin
from django.urls import path, include
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolioform/', views.portfolio_form, name='portfolioform'),
    path('portfolioupdateform/', views.portfolio_update_form, name='portfolioupdateform'),
    path('', include('user.urls'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

