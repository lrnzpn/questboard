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
                                        max_length=40, 
                                        widget= forms.NumberInput
                           (attrs={'class':'form-control mb-3'}))
    
    class Meta:
        model = Questboard
        fields = "__all__"
        
class QuestForm(forms.Form):
    name = forms.CharField(label="Quest name",max_length=140,
                          widget= forms.TextInput
                           (attrs={'class':'form-control mb-3'}))
    description = forms.CharField(label="Description",
                          widget= forms.Textarea
                           (attrs={'class':'form-control mb-3'}))
    stars = forms.IntegerField(label="Stars", max_length=7, 
                               widget= forms.NumberInput
                           (attrs={'class':'form-control mb-3'}))
    
    class Meta:
        model = Questboard
        fields = "__all__"