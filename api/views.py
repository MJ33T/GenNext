from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Comment, Task
from .serializers import CommentSerializer, UserRegistrationSerializer, TaskSerializer
from django.contrib.auth import get_user_model



User = get_user_model()

class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class TaskCreateAPIView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TaskDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if task is not None:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        task = self.get_object(pk)
        if task is not None:
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if task is not None:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class TaskListAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

class UserDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserRegistrationSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)


class UserTaskListAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            tasks = Task.objects.filter(assign=user)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        

class TaskAssignAPIView(APIView):
    def put(self, request, task_id, user_id):
        try:
            task = Task.objects.get(pk=task_id)
            user = User.objects.get(pk=user_id)
            task.assign = user
            task.save()
            return Response({"message": "Task assigned successfully"})
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

class TaskUpdateAssignedUserAPIView(APIView):
    def put(self, request, task_id, user_id):
        try:
            task = Task.objects.get(pk=task_id)
            user = User.objects.get(pk=user_id)
            task.assign = user
            task.save()
            return Response({"message": "Assigned user updated successfully"})
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        

class TaskFilterByUserAPIView(APIView):
    def get(self, request, user_id):
        tasks = Task.objects.filter(assign_id=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskFilterByCompletionAPIView(APIView):
    def get(self, request):
        completed = request.query_params.get('completed')
        if completed is not None:
            is_completed = completed.lower() == 'true'
            tasks = Task.objects.filter(complete_status=is_completed)
        else:
            tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskFilterByDueDateAPIView(APIView):
    def get(self, request):
        due_date = request.query_params.get('due_date')
        if due_date is not None:
            tasks = Task.objects.filter(due_date=due_date)
        else:
            tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

class TaskListAPIView(APIView):
    def get(self, request):
        sort_by = request.query_params.get('sort_by')
        if sort_by == 'due_date':
            tasks = Task.objects.order_by('due_date')
        else:
            tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

class CommentCreateAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class CommentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return None

    def get(self, request, pk):
        comment = self.get_object(pk)
        if comment is not None:
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        comment = self.get_object(pk)
        if comment is not None:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if comment is not None:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

