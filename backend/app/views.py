from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view, renderer_classes, parser_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework.response import Response
from app.models import Scenario
from app.serializers import ScenarioSerializer


# @api_view(['GET', 'POST'])
# @permission_classes([permissions.IsAuthenticated])
# @renderer_classes([JSONRenderer, XMLRenderer])
# @parser_classes([JSONParser, XMLParser])
# class ScenarioViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows Scenarios to be viewed or created.
#     """
#     queryset = Scenario.objects.all()
#     serializer_class = ScenarioSerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def scenario_list(request):
    if request.method == 'GET':
        scenarios = Scenario.objects.all()
        serializer = ScenarioSerializer(scenarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ScenarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def scenario_detail(request, pk):
    try:
        scenario = Scenario.objects.get(pk=pk)
    except Scenario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScenarioSerializer(scenario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ScenarioSerializer(scenario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        scenario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)