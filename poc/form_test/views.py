from django.shortcuts import render

from .forms import B2WCredentialForm, MeliCredentialForm


def form_test(request):
    b2wForm = B2WCredentialForm(request.POST or None)
    meliForm = MeliCredentialForm(request.POST or None)

    b2wForm.is_valid()
    meliForm.is_valid()

    return render(
        request, "form_test/form.html", {"forms": {"b2w": b2wForm, "meli": meliForm,}},
    )
