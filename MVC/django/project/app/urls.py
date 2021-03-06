from django.urls import path, include
from app.views.static_page_views import (
    home,
    help,
    about,
    contact
)
from app.views.app_views import (
    ListViews
)
from app.views.user_views import (
    UserCreateView
)


app_urls = [
    path('', home, name='root_path'),
    path('help/', help, name='help_path'),
    path('about/', about, name='about_path'),
    path('contact/', contact, name='contact_path'),
    path('signup/', UserCreateView.as_view(), name='signup_path')
    # path('', ListViews.as_view(), name='root_path')
]
