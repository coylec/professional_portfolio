from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        label='Message',
        required=True,
        widget=forms.Textarea
    )

    captcha = ReCaptchaField()