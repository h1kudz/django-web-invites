from django.urls import path
from .views import *
urlpatterns = [

    path('', Invites.as_view(), name='invites'),
    path('web/', CreateInvites.as_view(), name='add_invites'),
    path('web/<int:pk>/', ViewInvites.as_view(), name='view_invites'),
    # path('web/<int:invites_id>/', view_invites, name='view_invites'),
]