from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from account.authenticate import CustomAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

import logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info('New Product Added.')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        logger.warning('Error while creating product data.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def list_product(request):
    objects = Product.objects.all()
    serializer = ProductSerializer(objects, many=True)
    logger.info('Product data listed.')
    return Response(serializer.data,status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def retrieve_product(request,pk):
    obj = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(obj)
    logger.info('Product data retrieved.')
    return Response(serializer.data,status=200)


@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def update_product(request, pk):
    obj = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        logger.info('Product data updated.')
        return Response(serializer.data,status=200)
    else:
        logger.warning('Error while updating product data.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def delete_product(request, pk):
    obj = get_object_or_404(Product,id=pk)
    obj.delete()
    logger.info('Product data deleted.')
    return Response(status=status.HTTP_204_NO_CONTENT)


from django.core.mail import send_mail
from django.conf import settings


@api_view(['GET'])
def demo(request):
        
    send_mail(
        "msg",
        "hello",
        settings.EMAIL_HOST_USER ,
        [ "malipriyanka881995@gmail.com", ]
    )

    return Response(data={"msg":"mail sended"})




