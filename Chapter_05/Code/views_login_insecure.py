
def login(request):
    user = User.objects.get(username=request.POST['username'])
    if user.password == request.POST['password']:
        return JsonResponse({'message': 'Login successful'})
    return JsonResponse({'message': 'Invalid credentials'}, status=401)
