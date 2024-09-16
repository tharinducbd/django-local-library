import datetime

from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import BookInstance

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
        help_text="Enter a date between now and 4 weeks (default 3)."
    )

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date: renewal with past date'))
        
        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date: renewal more than 4 weeks ahead'))
        
        # Remember to always return the cleaned data.
        return data


# Identical to above form
# But variable 'renewal_date' of the view needs to be renamed as 'due_back'!
# class RenewBookForm(ModelForm):
#     class Meta:
#         model = BookInstance
#         fields = ['due_back',]
#         labels = {
#             'due_back': _('New renewal date'),
#         }
#         help_texts = {
#             'due_back': _('Enter a date between now and 4 weeks (default 3).'),
#         }
