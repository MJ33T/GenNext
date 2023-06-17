"""
URL configuration for NextGen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from api.views import CommentDetailAPIView, CommentCreateAPIView, RegisterUserAPIView, TaskAssignAPIView, TaskCreateAPIView, TaskDetailAPIView, TaskFilterByCompletionAPIView, TaskFilterByDueDateAPIView, TaskFilterByUserAPIView, TaskListAPIView, TaskUpdateAssignedUserAPIView, UserDetailAPIView, UserTaskListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Other URL patterns
    path('api/register/', RegisterUserAPIView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('api/tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),

    path('api/users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('api/users/<int:pk>/tasks/', UserTaskListAPIView.as_view(), name='user-tasks'),

    path('api/tasks/<int:task_id>/assign/<int:user_id>/', TaskAssignAPIView.as_view(), name='task-assign'),
    path('api/tasks/<int:task_id>/update_assigned_user/<int:user_id>/', TaskUpdateAssignedUserAPIView.as_view(), name='task-update-assigned-user'),

    path('api/tasks/filter/user/<int:user_id>/', TaskFilterByUserAPIView.as_view(), name='task-filter-by-user'),
    path('api/tasks/filter/completed/', TaskFilterByCompletionAPIView.as_view(), name='task-filter-by-completion'),
    path('api/tasks/filter/due_date/', TaskFilterByDueDateAPIView.as_view(), name='task-filter-by-due-date'),

    path('api/tasks/sort/', TaskListAPIView.as_view(), name='task-sort'),

    path('api/comment/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('api/comment/', CommentDetailAPIView.as_view(), name='comment-list'),
    path('api/Comment/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),


    


]
