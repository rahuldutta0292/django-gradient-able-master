
from django.forms import ModelForm
from .models import Deposit
from .models import StatutoryDeposit


class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'



