from product.models import Product, Creator, Caffeine, CoffeeType, RoastingDegree, Origin
from product.api.serializers import ProductSerializer, CreatorSerializer, CaffeineSerializer, CoffeeTypeSerializer, RoastingDegreeSerializer, OriginSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage



@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        product = Product.objects.all()

        items_per_page = 20
        paginator = Paginator(product, items_per_page)

        try:
            current_page_products = paginator.page(page)
        except EmptyPage:
            return Response({"error": "Page not found"}, status=404)

        product_serializer = ProductSerializer(current_page_products, many=True)
        serialized_products = product_serializer.data

        return JsonResponse({
            "products": serialized_products,
            "pagination_info": {
                "total_pages": paginator.num_pages,
                "current_page": current_page_products.number
            }
        })
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = ProductSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

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




from django.core.paginator import Paginator, EmptyPage
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse

@api_view(["GET"])
def search(request):
    search_word = request.GET.get('search_word')
    filters = request.GET.getlist('filters')
    page = int(request.GET.get('page', 1))

    # Fetch all available filter options
    coffee_types = CoffeeType.objects.all()
    caffeine_options = Caffeine.objects.all()
    creator_options = Creator.objects.all()
    origin_options = Origin.objects.all()
    roasting_degree_options = RoastingDegree.objects.all()

    # Serialize filter options
    coffee_type_serializer = CoffeeTypeSerializer(coffee_types, many=True)
    caffeine_serializer = CaffeineSerializer(caffeine_options, many=True)
    creator_serializer = CreatorSerializer(creator_options, many=True)
    origin_serializer = OriginSerializer(origin_options, many=True)
    roasting_degree_serializer = RoastingDegreeSerializer(roasting_degree_options, many=True)
    

    filter_options = {
        'CoffeeType': coffee_type_serializer.data,
        'Caffeine': caffeine_serializer.data,
        'Creator': creator_serializer.data,
        'Origin': origin_serializer.data,
        'RoastingDegree': roasting_degree_serializer.data,
    }

    product_list = Product.objects.filter(name__icontains=search_word)

    if filters:
        # print ("filters",filters)
        for i in filters :
            moded_filters=i.split(',')
            for filter_item in moded_filters:
                filter_parts = filter_item.split('=')
                # print ("parts",filter_parts)
                if len(filter_parts) == 2:
                    filter_name, filter_value = filter_parts
                    print("name",filter_name)
                    print("value",filter_value)

                    if filter_value:
                        # Check if the filter value is not empty before applying the filter
                        if filter_name == 'CoffeeType':
                            coffee_type_values = filter_value.split('_')
                            product_list = product_list.filter(coffee_type_id__in=coffee_type_values)
                        elif filter_name == 'Caffeine':
                            caffeine_values = filter_value.split('_')
                            product_list = product_list.filter(caffeine_id__in=caffeine_values)
                        elif filter_name == 'Creator':
                            creator_values = filter_value.split('_')
                            product_list = product_list.filter(creator_id__in=creator_values)
                        elif filter_name == 'Origin':
                            origin_values = filter_value.split('_')
                            product_list = product_list.filter(origin_id__in=origin_values)
                        elif filter_name == 'RoastingDegree':
                            roasting_degree_values = filter_value.split('_')
                            product_list = product_list.filter(roasting_degree_id__in=roasting_degree_values)
                        else:
                            return JsonResponse({"error": f"Invalid filter: {filter_name}"}, status=400)

    items_per_page = 20
    paginator = Paginator(product_list, items_per_page)

    try:
        current_page_products = paginator.page(page)
    except EmptyPage:
        return JsonResponse({"error": "Page not found"}, status=404)

    product_serializer = ProductSerializer(current_page_products, many=True)
    serialized_products = product_serializer.data

    return JsonResponse({
        "products": serialized_products,
        "search_word": search_word,
        "filter_options": filter_options,
        "pagination_info": {
            "total_pages": paginator.num_pages,
            "current_page": current_page_products.number
        }
    })
