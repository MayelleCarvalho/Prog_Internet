from django.forms import ModelForm
from myapp.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


    def is_valid(self):
        pass
