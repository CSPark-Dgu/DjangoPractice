from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse, Http404


# post_list = ListView.as_view(model=Post) #CBV


def post_list(request: HttpResponse) -> HttpResponse:
    qs = Post.objects.all()
    q = request.GET.get("q", "")
    if q != "":
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(
        request,
        "instagram/post_list.html",
        {
            "post_list": qs,
            "q": q,
        },
    )


# def post_detail(request: HttpResponse, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, "instagram/post_detail.html", {"post": post})

post_detail = DetailView.as_view(model=Post)  # CBV
