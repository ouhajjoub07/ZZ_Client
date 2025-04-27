import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt #==> Hadi Zdtha fach bghit ndir save fichier (create_product.py)
def home(request):
    headers = request.headers
    params = request.GET.get('q')
    # post_data = request.POST ==> 
    
    if request.method == "POST" :
        post_data = request.body
        data = json.loads(post_data)
        
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        
        product = Product.objects.create(
            name=name,
            price=price,
            description=description
        )
        
        return JsonResponse({
            'id' : product.id,
            'name' : product.name,
            'price' : product.price,
            'description' : product.description
        })
        
    products = Product.objects.all()
    data = [{ 
        'id' : product.id,'name' : product.name} for product in products
        ]
    
    # print(headers)
    # print('--------------')
    # print(params)
    # print('--------------')
    # print(post_data)
    # print('--------------')
    
    # print(data)
    
    # return JsonResponse({'info':'Django' ,'name':'donald' ,'age':25 ,'params':params})
    
    # return JsonResponse(data) # ==> Pour Method POST
    
    return JsonResponse(data, safe=False) # ==> Pour method GET