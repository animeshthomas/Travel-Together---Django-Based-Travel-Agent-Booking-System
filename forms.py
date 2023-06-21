from django import forms
from agent.models import User,Agent,Postpackage

class Signupform(forms.ModelForm):
    model= User

    class Meta:
        model = User
        fields = [
            'uname',
            'phoneno',
            'state',
            'district',
            'address',
            'photo',
            'email',
            'password',

        ]
class Agentform(forms.ModelForm):
    model = Agent
    class Meta:
        model = Agent
        fields = [
            'aname',
            'phoneno',
            'state',
            'district',
            'area',
            'address',
            'photo',
            'agender',
            'verification',
            'certification',
            'email',
            'password',
        ]
class Packageform(forms.ModelForm):
    model = Postpackage
    class Meta:
        abstract = True
        model = Postpackage
        fields = ['name', 'area', 'description', 'ptype', 'photo1', 'photo2', 'photo3', 'photo4']
