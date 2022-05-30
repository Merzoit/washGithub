from dataclasses import field
from django import forms
from core.models import Blank

class BlankCreateForm(forms.ModelForm):

    class Meta:
        model = Blank
        fields = ("__all__")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control inForm'

        self.fields['grz'].widget.attrs['class'] = 'form-item__grz'
        self.fields['car_mark'].widget.attrs['class'] = 'form-item__carmark'
        self.fields['price'].widget.attrs['class'] = 'form-item__price'
        self.fields['b_trunk'].widget.attrs['class'] = 'form-item__bag'
        self.fields['b_carpets'].widget.attrs['class'] = 'form-item__mat'
        self.fields['b_cleaning'].widget.attrs['class'] = 'form-item__cleaner'
        self.fields['notes'].widget.attrs['class'] = 'form-item__comment'
        self.fields['car_class'].widget.attrs['class'] = 'form-item__autoclass'
        self.fields['wash_type'].widget.attrs['class'] = 'form-item__washtype'
        self.fields['wash_man'].widget.attrs['class'] = 'form-item__washman'
        self.fields['b_trunk'].widget.attrs['class'] = 'block-item'
        self.fields['b_carpets'].widget.attrs['class'] = 'block-item'
        self.fields['b_cleaning'].widget.attrs['class'] = 'block-item'

        
        self.fields['grz'].widget.attrs['class'] += " grz"
        self.fields['wash_man'].widget.attrs['class'] += ' washman'
        self.fields['car_mark'].widget.attrs['class'] += ' carmark'
        self.fields['b_trunk'].widget.attrs['class'] = 'form-check-input'
        self.fields['date'].widget.attrs['id'] = 'date'
        self.fields['date'].widget.attrs['type'] = 'date'