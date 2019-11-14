from django import forms
from  .models import BlogData, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nickname', 'text')