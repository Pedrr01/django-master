from django import forms
from cars.models import Brand, Car

# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_years = forms.IntegerField()
#     model_years = forms.IntegerField()
#     plate = forms.CharField()
#     value = forms.FloatField()
#     photo = forms.ImageField()

#     def save(self):
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_years = self.cleaned_data['factory_years'],
#             model_years = self.cleaned_data['model_years'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save()
#         return car

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = "__all__"

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor minimo do carro deve ser de R$20.000')
        return value

    def clean_factory_years(self):
        factory_years = self.cleaned_data.get('factory_years')
        if factory_years < 2000:
            self.add_error('factory_years', 'Apenas aceitamos o cadastro de carros a parti do ano 2000')
        return factory_years