from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import BlogData #Comment
#from .forms import CommentForm
import parser

class BlogListView(ListView):
    model = BlogData
    context_object_name = 'posts'
    paginate_by = 15
    #template_name = 'parsed_data/blogdata_list.html'

    ordering = ['-published_date']




class BlogDetailView(DetailView): #,FormMixin
    model = BlogData
    context_object_name = 'post'
    template_name = 'parsed_data/blogdata_detail.html'



