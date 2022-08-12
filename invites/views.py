from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import InvitesForm
from invites.models import Invites
from .models import Invites as InvitesModel


# def index(request):
#     return render(request, 'invites/add_invites.html', {'title': 'Web-пригласительное'})

class Invites(ListView):
    model = Invites
    template_name = 'invites/main.html'
    context_object_name = 'invites'

class ViewInvites(DetailView):
    model = InvitesModel
    context_object_name = 'invites_item'
    template_name = 'invites/invites_detail.html'

# def view_invites(request, invites_id):
#     invites_item = get_object_or_404(InvitesModel, pk=invites_id)
#     # invites_item = InvitesModel.objects.get(pk=invites_id)
#     return render(request, 'invites/invites_detail.html', {"invites_item": invites_item })
class CreateInvites(CreateView):
    form_class = InvitesForm
    template_name = 'invites/add_invites.html'
    raise_exception = True

