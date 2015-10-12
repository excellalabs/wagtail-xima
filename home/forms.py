__author__ = 'Nick'

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Field, Layout, Div
from crispy_forms.bootstrap import FormActions

from models import *

class FormOrder(forms.Form):
    inventory = forms.ModelChoiceField(label="Inventory Item", queryset=InventoryItem.objects.live())
    quantity = forms.IntegerField(label="Enter a quantity here")
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        Field('inventory', css_class='form-control', style="width: 16%"),
        Field('quantity', css_class='form-control', style="width: 16%"),
        FormActions(
            Div(
                Submit('save', 'Submit Order', css_clss='btn_primary',
                       onclick="return confirm('Are you sure?')", style="margin-top:1%;"),
                Button('cancel', 'Cancel', css_class='btn-default',
                       onclick="window.history.back()", style="margin-top:1%;")
            )
        )
    )
