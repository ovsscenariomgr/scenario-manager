from rest_framework import generics, permissions, views, status
from rest_framework.decorators import renderer_classes, parser_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import Http404
from app.models import Scenario, VocalFile, MediaFile
from app.serializers import ScenarioSerializer, VocalSerializer, MediaSerializer
from app.renderers import ScenarioXMLRenderer
from app.parsers import ScenarioXMLParser

@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@renderer_classes([ScenarioXMLRenderer, JSONRenderer])
@parser_classes([ScenarioXMLParser, JSONParser])
class ScenarioList(generics.ListCreateAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@renderer_classes([ScenarioXMLRenderer, JSONRenderer])
@parser_classes([ScenarioXMLParser, JSONParser])
class ScenarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
class ScenarioVocals(views.APIView):

    def get_object(self, pk):
        try:
            return Scenario.objects.get(pk=pk)
        except Scenario.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        scenario = self.get_object(pk)
        filename = request.data.get('filename')
        title = request.data.get('title')
        vocalfile = VocalFile.objects.create(scenario=scenario, filename=filename, title=title)
        serializer = VocalSerializer(instance=vocalfile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
