from django.forms import ModelForm, fields

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name': 'Name',
            'user_email': 'Email',
            'text': 'Comment'
        }
        error_messages = {
            'text': {
                'max_length': 'limit of 400 caracters is reached!',
            }
        }
