from django import forms

from .models import Post
from .models import Post2
from .models import Post3

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','author')

class PostForm2(forms.ModelForm):

    class Meta:
        model = Post2
        fields = ('title', 'text','author')

class PostForm3(forms.ModelForm):

    class Meta:
        model = Post3
        fields = ('title', 'text','author')