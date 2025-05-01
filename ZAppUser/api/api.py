from ZAppUser.models import Product
from django.shortcuts import redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ZAppUser.api.serializers import ProductSerializers1 , ProductSerializers2

@api_view(['GET','POST','PUT','DELETE','PATCH'])
def product_api_view(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            # product = Product.objects.get(pk=pk)
            product = get_object_or_404(Product, pk=pk)
            context = {'request':request}
            serializer = ProductSerializers1(product, context=context)
            return Response(serializer.data, status=status.HTTP_200_OK)
        products = Product.objects.all()
        # data = [{'id': product.id , 'name':product.name} for product in products]
        context = {'request':request}
        serializer = ProductSerializers1(products, many=True, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = ProductSerializers1(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        if pk is None:
            return Response({'message': 'You must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)
        # product = Product.objects.get(pk=pk)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializers1(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        if pk is None:
            return Response({'message':'You must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)
        # product = Product.objects.get(pk=pk)
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'message':'Product deleted successfuly'}, status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        if pk is None:
            return Response({'message':'You must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)
        # product = Product.objects.get(pk=pk)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializers1(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)