from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from api.models import Register
from api.serializers import RegisterSerializer2

# Create your views here.
@csrf_exempt
def register(request):
	if request.method == "GET":
		registers = Register.objects.all()
		ser = RegisterSerializer2(registers, many=True)
		return JsonResponse(ser.data, safe=False)
	elif request.method == "POST":
		print(request)
		data = JSONParser().parse(request)
		ser = RegisterSerializer2(data=data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
	return JsonResponse(ser.errors, status=400)