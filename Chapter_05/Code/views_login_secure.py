
from django.contrib.auth.hashers import check_password
def login(request):
    try:
        user = User.objects.get(username=request.POST['username'])
        if check_password(request.POST['password'], user.password):
            return JsonResponse({'message': 'Login successful'})
        return JsonResponse({'message': 'Invalid credentials'}, status=401)
    except User.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)
