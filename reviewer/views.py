from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  View
)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from reviewer import models, forms

# Create your views here.
# @method_decorator(login_required, name='dispatch')
class Index(ListView):
  model = models.Restaurant
  template_name = 'index.html'

class Restaurant(DetailView):
  model = models.Restaurant
  template_name = 'restaurant.html'

class AddReview(CreateView):
  model = models.Review
  fields = ['title', 'body', 'stars']
  template_name = 'review.html'

  def get_success_url(self):
    return '/restaurant/{}'.format(self.kwargs['pk'])

  def form_valid(self, form):
    """If the form is valid, save the associated model."""
    restaurant = models.Restaurant.objects.get(pk = self.kwargs['pk'])
    user = self.request.user
    review = form.save(commit = False)
    review.restaurant = restaurant
    review.user = user
    review.save()
    self.object = review
    return super().form_valid(form)


@login_required
def add_review(request, pk):
  restaurant = models.Restaurant.objects.get(pk = pk)
  review_form = forms.ReviewForm()

  if request.method == "POST":
    review_form = forms.ReviewForm(request.POST)

    if review_form.is_valid():
      # models.Review.objects.create(
      #   user = request.user,
      #   restaurant = restaurant,
      #   title = review_form.cleaned_data['title'],
      #   stars = review_form.cleaned_data['stars'],
      #   body = review_form.cleaned_data['body']
      # )
      review = review_form.save(commit = False)
      review.user = request.user
      review.restaurant = restaurant
      review.save()
      return HttpResponseRedirect('/restaurant/{}'.format(restaurant.id))

  context = {
    "restaurant": restaurant,
    "form": review_form
  }
  return render(request, 'review.html', context)
