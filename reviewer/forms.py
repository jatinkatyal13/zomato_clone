from django import forms

from reviewer import models

class ReviewForm(forms.ModelForm):
  class Meta:
    model = models.Review
    fields = ['title', 'body', 'stars']
