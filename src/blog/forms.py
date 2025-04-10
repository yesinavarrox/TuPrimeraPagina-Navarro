from django.contrib.auth.forms import AuthenticationForm


class ClienteForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ["username", "password"]
