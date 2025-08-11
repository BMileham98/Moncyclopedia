from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row, Column
from .models import Comment, Observation

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['title', 'monster', 'observed_behaviour','additional_notes', 'location',
        'observation_date', 'danger_rating', 'expanded_danger_rating', 'image']
        widgets = {'observed_behaviour': forms.Textarea(attrs={'rows': 4}),
        'additional_notes': forms.Textarea(attrs={'rows': 4}),
        'observation_date': forms.DateInput(attrs={'type':'date'}),
        'danger_rating': forms.Select(choices=[(i, f"{i}/5") for i in range(1, 6)]),
        'expanded_danger_rating': forms.Textarea(attrs={'rows': 3}),
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'monster',
            Row(
                Column('location', css_class='form-group col-md-6'),
                Column('observation_date', css_class='form-group col-md-6')
            ),
            'observed_behaviour',
            'additional_notes',
            'image',
            'danger_rating',
            'expanded_danger_rating',
            Submit('submit', 'Save Observation', css_class='btn btn-primary')
            )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your thoughts...'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('content', css_class='form-control'),
            Submit('submit', 'Post Comment', css_class='btn btn-primary mt-2')
        )