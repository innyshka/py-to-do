from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    set_done_or_not,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,

)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/set-done_or_not/",
        set_done_or_not,
        name="set-done_or_not"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),



]

app_name = "task"
