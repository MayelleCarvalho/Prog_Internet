from django.forms import ModelForm
from myapp.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if(not email.__str__().__contains__('@')):
            mensagem = 'Email inválido, por favor tente novamente!'
            self.add_error('email', mensagem)