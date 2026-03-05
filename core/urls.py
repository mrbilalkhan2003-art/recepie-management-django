from django.contrib import admin
from django.urls import path
from veges.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    # 👇 Homepage → Login page
    path('', login_page, name="login_page"),

    # 👇 Authentication
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register"),
    path('logout/', logout_page, name="logout_page"),

    # 👇 Recepie page (after login)
    path('recepies/', recepies, name='recepies'),
    path('delete-recepie/<id>/', delete_recepie, name="delete_recepie"),
    path('update-recepie/<id>/', update_recepie, name="update_recepie"),

    # 👇 Admin
    path('admin/', admin.site.urls),

    # ------- COMMENTED ROUTES (not needed for deployment now) -------

    # path('home/', home, name="home"),
    # path('send-email/', send_email, name='send_email'),
    # path('Contact/', Contact, name="Contact"),
    # path('About/', About, name="About"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()