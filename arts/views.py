from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView ,DeleteView,DetailView,UpdateView,CreateView
from .models import *
from .forms import *
class ArtistView(ListView):
    model = Art
    template_name = 'index.html'
    context_object_name = 'arts'
    def get_queryset(self):        
        abo = self.request.user.id 
        return Art.objects.filter(owner=abo)
    
class DetailsArtView(DetailView):
    model=Art
    template_name="art_details.html"
    context_object_name = 'art'
class DeleteArtView(DeleteView):
    model=Art
    template_name="index.html"
    success_url=reverse_lazy("list_arts")
class UpdateArtView(UpdateView):
    model = Art
    template_name = "art_update.html" 
    form_class=UpdateArt
    context_object_name = 'art'

    def get_success_url(self):
        return reverse_lazy("list_arts")
class CreateArtView(CreateView):
    model = Art
    template_name = "art_create.html" 
    form_class=AddArt
    context_object_name = 'art'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy("list_arts")