from rest_framework import generics, permissions, views, status
from rest_framework.decorators import renderer_classes, parser_classes, permission_classes, authentication_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from django.contrib.auth import login
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from app.models import Scenario, VocalFile, MediaFile, Profile
from app.serializers import ScenarioSerializer, VocalSerializer, MediaSerializer, LoginSerializer, UserSerializer
from app.renderers import ScenarioXMLRenderer, OvsXMLRenderer
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
@renderer_classes([OvsXMLRenderer])
class ScenarioExport(generics.RetrieveAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
class ScenarioVocals(views.APIView):

    def get(self, request, pk, format=None):
        scenario = get_object_or_404(Scenario, pk=pk)
        qs = VocalFile.objects.filter(scenario_id=scenario.pk)
        serializer = VocalSerializer(qs, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        scenario = get_object_or_404(Scenario, pk=pk)
        putdata = request.data
        putdata['scenario'] = scenario.pk
        serializer = VocalSerializer(data=putdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
class ScenarioMedia(views.APIView):

    def get(self, request, pk, format=None):
        scenario = get_object_or_404(Scenario, pk=pk)
        qs = MediaFile.objects.filter(scenario_id=scenario.pk)
        serializer = MediaSerializer(qs, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        scenario = get_object_or_404(Scenario, pk=pk)
        putdata = request.data
        putdata['scenario'] = scenario.pk
        serializer = MediaSerializer(data=putdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
class ScenarioImages(views.APIView):

    def patch(self, request, pk, format=None):
        scenario = get_object_or_404(Scenario, pk=pk)
        avatar_file = request.data.get('avatar')
        summary_file = request.data.get('summary')
        if not avatar_file and not summary_file:
            return Response('May only patch avatar or summary image', status=status.HTTP_400_BAD_REQUEST)

        profile = Profile.objects.filter(scenario_id=scenario.pk).first()
        if avatar_file:
            avatar = profile.avatar
            avatar.filename = avatar_file
            avatar.save()
        if summary_file:
            summary = profile.summary
            summary.image = summary_file
            summary.save()
        scenario.refresh_from_db()
        serializer = ScenarioSerializer(instance=scenario)
        return Response(serializer.data)

@permission_classes([])
class AuthCheck(views.APIView):

    def get(self, request):
        if request.user.is_authenticated:
            user = UserSerializer(request.user, context={'request': request})
            return Response({"isAuthenticated": True, "user": user.data})
        else:
            return Response({"isAuthenticated": False})

@permission_classes([permissions.AllowAny])
@authentication_classes([])
class LoginView(views.APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({"detail": "Login successful."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def expire_session_view(request, session_key):
    try:
        session = Session.objects.get(session_key=session_key)
        session.delete()
    except Session.DoesNotExist:
        pass
    return HttpResponseRedirect('/admin/sessions/session/')