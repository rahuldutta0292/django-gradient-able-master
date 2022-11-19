
from django.forms import ModelForm
from .models import Deposit
from .models import StatutoryDeposit


class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'


class StatutoryDepositForm(ModelForm):
    class Meta:
        model = StatutoryDeposit
        fields = '__all__'


