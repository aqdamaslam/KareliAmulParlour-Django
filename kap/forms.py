from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(label = 'Enter Your Name', required = True)
    ice_cream_name = forms.CharField(label = 'Enter Your Ice Cream Name', required = True)
    contact_num = forms.IntegerField(label = 'Enter Your Mobile Number', required = True)
    contact_email = forms.EmailField(label = 'Enter Your E-Mail ID', required = True)
    contact_query = forms.CharField(label = 'Type Your Query Here', required = True)
