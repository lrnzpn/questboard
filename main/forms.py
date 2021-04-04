from django import forms
from .models import *

class QuestboardForm(forms.Form):
    name = forms.CharField(label="Questboard name",max_length=140,
                          widget= forms.TextInput
                           (attrs={'class':'form-control mb-3'}))
    description = forms.CharField(label="Description",
                          widget= forms.Textarea
                           (attrs={'class':'form-control mb-3'}))
    required_stars = forms.IntegerField(label="Required stars", 
                                        min_value=1, max_value=40,  
                                        widget= forms.NumberInput
                           (attrs={'class':'form-control mb-3'}))
    
    class Meta:
        model = Questboard
        fields = ['name', 'description', 'required_stars']
        
class QuestForm(forms.Form):
    name = forms.CharField(label="Quest name",max_length=140,
                          widget= forms.TextInput
                           (attrs={'class':'form-control mb-3'}))
    description = forms.CharField(label="Description",
                          widget= forms.Textarea
                           (attrs={'class':'form-control mb-3'}))
    stars = forms.IntegerField(label="Stars", min_value=1, max_value=7, 
                               widget= forms.NumberInput
                           (attrs={'class':'form-control mb-3'}))
    
    class Meta:
        model = Questboard
        fields = "__all__"