from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ArchiveIndexView,
    DayArchiveView,
    DetailView,
    ListView,
    MonthArchiveView,
    YearArchiveView,
)
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse, Http404


# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))  # CBV


# @method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()

# @login_required
# def post_list(request: HttpResponse) -> HttpResponse:
#     qs = Post.objects.all()
#     q = request.GET.get("q", "")
#     if q != "":
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(
#         request,
#         "instagram/post_list.html",
#         {
#             "post_list": qs,
#             "q": q,
#         },
#     )


# def post_detail(request: HttpResponse, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, "instagram/post_detail.html", {"post": post})

# post_detail = DetailView.as_view(
#     model=Post, queryset=Post.objects.filter(is_public=True)
# )  # CBV


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):  # Override
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_detail = PostDetailView.as_view()  # CBV

post_archive = ArchiveIndexView.as_view(
    model=Post, date_field="created_at", paginate_by=10
)

post_archive_year = YearArchiveView.as_view(
    model=Post, date_field="created_at", make_object_list=True
)

post_archive_month = MonthArchiveView.as_view(model=Post, date_field="created_at")

post_archive_day = DayArchiveView.as_view(model=Post, date_field="created_at")
