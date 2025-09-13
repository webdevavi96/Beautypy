from django.shortcuts import redirect, render
from django import forms


class BeautyForm:
    def __init__(self, model, fields, success_redirect, template="beauty_form.html"):
        self.model = model
        self.fields = fields
        self.success_redirect = success_redirect
        self.template = template

        class DynamicForm(forms.ModelForm):
            class Meta:
                model = None
                fields = []

        DynamicForm.Meta.model = model
        DynamicForm.Meta.fields = fields

        self.form_class = DynamicForm

    def handle_request(self, request):
        if request.method == "POST":
            form = self.form_class(request.POST)

            if form.is_valid():
                form.save()

                if self.success_redirect:
                    return redirect(self.success_redirect)

                else:
                    form = self.form_class()

            return render(request, self.template, {"form": form})
