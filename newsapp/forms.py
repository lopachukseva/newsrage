from django import forms

from newsapp.models import Comments, Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback_text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}),
            'email': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Электронная почта'}),
            'feedback_text': forms.Textarea(
                attrs={'class': 'form-input', 'placeholder': 'Напишите здесь, что думаете о нас'}),
        }


class CommentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comments
        fields = ['comment', ]
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Напишите комментарий'}),
        }
