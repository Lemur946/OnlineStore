from django import forms
from .models import Product
from .constants import FORBIDDEN_WORDS


class ProductForm(forms.ModelForm):
    """
    A form for creating and editing products with custom validation and styling.
    """

    class Meta:
        model = Product
        # We indicate all the fields that we want to see in the form.
        fields = ('name', 'description', 'image', 'category', 'price', 'is_available')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # We go through all the form fields and add the 'form-control' class to them.
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        """
        Checks the 'name' field for prohibited words.
        """
        cleaned_data = self.cleaned_data['name']

        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Слово "{word}" запрещено к использованию в названии.')

        return cleaned_data

    def clean_description(self):
        """
        Checks the 'description' field for prohibited words.
        """
        cleaned_data = self.cleaned_data['description']

        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Слово "{word}" запрещено к использованию в описании.')

        return cleaned_data

    def clean_price(self):
        """
        Checks that the price is not negative.
        """
        cleaned_data = self.cleaned_data['price']

        if cleaned_data < 0:
            raise forms.ValidationError('Цена продукта не может быть отрицательной.')

        return cleaned_data

    def clean_image(self):
        """
        Checks the format and size of the uploaded image.
        """
        image = self.cleaned_data.get('image', False)
        if image:
            # Check file size (no more than 5 MB)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Размер изображения не должен превышать 5 МБ.")

            # Checking the file format
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Недопустимый формат файла. Разрешены только PNG, JPG, JPEG.")

        return image
