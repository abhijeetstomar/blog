from django import forms
from .models import Comment

# we've inherited the base Form class
class EmailPostForm(forms.Form):
    # character field
    # each field has a default widget which decides how the field 
    # will be displayed in html
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    # comments field is optional
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')