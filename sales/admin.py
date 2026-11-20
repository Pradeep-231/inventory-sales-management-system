# Register your models here.

from django.contrib import admin
from django import forms
from products.models import Product
from .models import Sale


class ProductPriceSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )

        if value and value.value:
            product = Product.objects.filter(pk=value.value).only("price").first()

            if product:
                option["attrs"]["data-price"] = str(product.price)

        return option


class SaleAdminForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product"].widget = ProductPriceSelect(
            choices=self.fields["product"].choices
        )


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    form = SaleAdminForm

    class Media:
        js = ("sales/js/sale_price.js",)
