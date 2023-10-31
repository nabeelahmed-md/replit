from django import forms
from .models import Region,Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['region', 'street_address']

class HistoryForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Select Region")
    day = forms.ChoiceField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')])