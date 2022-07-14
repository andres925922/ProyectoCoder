from django import forms

class Formulario_Cliente(forms.Form):
    id_number = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=75)
    identity = forms.CharField(max_length=50)
    email = forms.EmailField()
    sexo = forms.ChoiceField(choices= (
        (1, "FEMENINO"), (2, "MASCULINO"),
    ))
    tel = forms.CharField(max_length=50)
    estado = forms.ChoiceField(
        choices = (
            (1, "ACTIVO"), 
            (2, "BAJA"), 
            (3, "MOROSO"),
        )
    )

class Formulario_Busqueda_cliente(forms.Form):
    dni = forms.CharField(max_length=50)
