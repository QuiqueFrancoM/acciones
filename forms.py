from django import forms
from .models import acciones
class AccionesForm(forms.ModelForm):
    class Meta:
        model = acciones
        fields = "__all__"
        # exclude = ['owner_comment']
        #labels = {
        #     "user_name": "Your Name",
        #     "review_text": "Your Feedback",
        #     "rating": "Your Rating"
        # }
        # error_messages = {
        #     "user_name": {
        #       "required": "Your name must not be empty!",
        #       "max_length": "Please enter a shorter name!"
        #     }
        #}