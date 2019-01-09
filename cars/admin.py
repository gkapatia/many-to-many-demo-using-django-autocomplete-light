from dal import autocomplete
from django import forms
from django.contrib import admin

from cars.models import Car, CarAvailableColorMapping
from colors.models import Color


class CarAdminForm(forms.ModelForm):
    available_color_input = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='/colors/color-autocomplete/'),
        required=False,
    )

    class Meta:
        model = Car
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        initial = None

        if instance:
            initial = {'available_color_input': instance.available_colors.all()}
        super().__init__(initial=initial, *args, **kwargs)


class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm
    list_display = ('id', 'name', 'available_color_input', 'user', 'created_at')
    list_editable = ('name',)

    def available_color_input(self, obj):
        pass

    def get_changelist_form(self, request, **kwargs):
        kwargs.setdefault('form', CarAdminForm)
        return super().get_changelist_form(request, **kwargs)

    def save_model(self, request, obj, form, change):
        if 'available_color_input' in form.changed_data:
            new_data = form.cleaned_data.get('available_color_input', [])
            car = obj
            old_data = car.available_colors.all()
            delete_data = list(set(old_data) - set(new_data))
            add_data = list(set(new_data) - set(old_data))
            for data in add_data:
                CarAvailableColorMapping.objects.create(car=car, color=data, user=request.user)
            for data in delete_data:
                CarAvailableColorMapping.objects.get(car=car, color=data).delete()
        super().save_model(request, obj, form, change)


admin.site.register(Car, CarAdmin)
