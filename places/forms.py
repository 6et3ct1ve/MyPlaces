from django import forms

class PlaceForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label='Place Name'
    )
    
    description = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label='Description'
    )
    
    TYPE_CHOICES = [
        ('relax', 'Relax'),
        ('romantic', 'Romantic'),
        ('study', 'Study'),
    ]
    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        required=True,
        label='Type'
    )
    
    location = forms.CharField(
        max_length=200,
        required=False,
        label='Location (optional)'
    )
    
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        required=True,
        label='Rating (1-5)'
    )