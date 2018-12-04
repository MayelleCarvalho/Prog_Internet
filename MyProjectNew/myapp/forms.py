from django.forms import ModelForm, Textarea
from django.forms import TextInput
from django.forms import Field
from myapp.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'email')
        widgets = {
            'title': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'text': Textarea(attrs={'class' : 'form-control', 'aria-label' : 'Com textarea'}),
            'email': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder' : 'example@gmail.com', 'aria-label' : 'Usuário', 'aria-describedby' : 'basic-addon1'}),
        }
        labels = {
            'title': ('Título da Postagem'),
            'text': ('Texto da Postagem'),
            'email': ('Login de Usuário (Email)'),
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if(not email.__str__().__contains__('@')):
            mensagem = 'Email inválido, por favor tente novamente!'
            self.add_error('email', mensagem)