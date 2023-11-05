from product.models import Product, Creator, Caffeine, CoffeeType, RoastingDegree, Origin
from product.api.serializers import ProductSerializer, CreatorSerializer, CaffeineSerializer, CoffeeTypeSerializer, RoastingDegreeSerializer, OriginSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status



@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializers = ProductSerializer(product, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = ProductSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = ProductSerializer(product)
        return Response(serializers.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = ProductSerializer(instance=product, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Creator-----------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def creator_list(request):
    if request.method == 'GET':
        creators = Creator.objects.all()
        serializers = CreatorSerializer(creators, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = CreatorSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def creator_detail(request, pk):
    try:
        creator = Creator.objects.get(pk=pk)
    except Creator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = CreatorSerializer(creator)
        return Response(serializers.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = CreatorSerializer(instance=creator, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        creator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def caffeine_list(request):
    if request.method == 'GET':
        caffeines = Caffeine.objects.all()
        serializers = CaffeineSerializer(caffeines, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = CaffeineSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def caffeine_detail(request, pk):
    try:
        caffeine = Caffeine.objects.get(pk=pk)
    except Caffeine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = CaffeineSerializer(caffeine)
        return Response(serializers.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = CaffeineSerializer(instance=caffeine, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        caffeine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def coffeeType_list(request):
    if request.method == 'GET':
        coffeeType = CoffeeType.objects.all()
        serializers = CoffeeTypeSerializer(coffeeType, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = CoffeeTypeSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def coffeeType_detail(request, pk):
    try:
        coffeeType = CoffeeType.objects.get(pk=pk)
    except CoffeeType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = CoffeeTypeSerializer(coffeeType)
        return Response(serializers.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = CoffeeTypeSerializer(instance=coffeeType, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        coffeeType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def roastingDegree_list(request):
    if request.method == 'GET':
        roastingDegree = RoastingDegree.objects.all()
        serializers = RoastingDegreeSerializer(roastingDegree, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = RoastingDegreeSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def roastingDegree_detail(request, pk):
    try:
        roastingDegree = RoastingDegree.objects.get(pk=pk)
    except RoastingDegree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = RoastingDegreeSerializer(roastingDegree)
        return Response(serializers.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = RoastingDegreeSerializer(instance=roastingDegree, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        roastingDegree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#----------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def origin_list(request):
    if request.method == 'GET':
        origin = Origin.objects.all()
        serializers = OriginSerializer(origin, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = OriginSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def origin_detail(request, pk):
    try:
        origin = Origin.objects.get(pk=pk)
    except Origin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = OriginSerializer(Origin)
        return Response(serializers.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = OriginSerializer(instance=origin, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        origin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
