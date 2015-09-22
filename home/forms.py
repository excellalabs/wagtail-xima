__author__ = 'Nick'

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Field

class FormOrder(forms.Form):
    quantity = forms.IntegerField(label="Enter a quantity here")
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'Submit Order', css_class='btn_primary',
                            onclick="return confirm('Are you sure?')"))
    helper.add_input(Button('cancel', 'Cancel', css_class='btn-default', onclick="window.history.back()"))