#from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import *


from models import * #Question, Answer

def test(request, *args, **kwargs):


  return render_to_response('h.html')
#  return HttpResponse('OK')


def question(request, id):
  q = get_object_or_404(Question, id=id)
  try:
    a = Answer.objects.filter(question=id)[:]
  except Answer.DoesNotExist:
    a = none
  return render(request, 'q.html', {
      'q' : q,
      'a' : a,
  })

def questions_list(request, **opt):
  qs = Question.objects
  try:
    opt['name']
    qs = qs.all()
    baseurl = '/?page='
  except:
    qs = qs.order_by('-rating')
    baseurl = '/popular/?page='
#  try:
#    qs = qs[:]
#  except Question.DoesNotExist:
#    qs = none
  page = paginate(request, qs)

  return render(request, 'qs.html', {
      'posts' : page.object_list,
#      'paginator' : paginator,
      'page' : page,
  })

def paginate(request, qs):
  try:
    limit = int(request.GET.get('limit', 10))
  except ValueError:
    limit = 10
  if limit > 100:
    limit = 10
  try:
    page = int(request.GET.get('page', 1))
  except ValueError:
    raise Http404
  paginator = Paginator(qs, limit)
  try:
    page = paginator.page(page)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)
  return page




