import io
import os
import zipfile
from rest_framework import generics, permissions, views, status
from rest_framework.decorators import renderer_classes, parser_classes, permission_classes, authentication_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth import login
from django.contrib.sessions.models import Session
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from app.models import Scenario, VocalFile, MediaFile, Profile
from app.serializers import ScenarioSerializer, VocalSerializer, MediaSerializer, LoginSerializer, UserSerializer
from app.renderers import ScenarioXMLRenderer, OvsXMLRenderer
from app.parsers import ScenarioXMLParser
from app.archive import read_archive, manifest_to_internal, missing_referenced_files, ScenarioArchiveError

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
class ScenarioExport(generics.RetrieveAPIView):
    """Export a Scenario as a Scenario Archive: a zip of main.xml plus the
    images/vocals/media directories, per OVS Scenario Specification SS2.2-2.5."""
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

    def retrieve(self, request, *args, **kwargs):
        scenario = self.get_object()
        serializer = self.get_serializer(scenario)
        manifest_xml = OvsXMLRenderer().render(serializer.data)

        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr('main.xml', manifest_xml)
            scenario_dir = os.path.join(settings.MEDIA_ROOT, str(scenario.pk))
            for sub_dir in ('images', 'vocals', 'media'):
                dir_path = os.path.join(scenario_dir, sub_dir)
                filenames = sorted(os.listdir(dir_path)) if os.path.isdir(dir_path) else []
                if not filenames:
                    zf.writestr(sub_dir + '/', '')  # dir must exist even if empty, per spec
                for filename in filenames:
                    file_path = os.path.join(dir_path, filename)
                    if os.path.isfile(file_path):
                        zf.write(file_path, arcname='%s/%s' % (sub_dir, filename))
        buf.seek(0)

        response = HttpResponse(buf.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="scenario-%s.zip"' % scenario.pk
        return response

@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser])
class ScenarioImport(views.APIView):
    """Create a Scenario from an uploaded Scenario Archive (zip of main.xml +
    images/vocals/media directories, per OVS Scenario Specification SS2.2-2.5)."""

    def post(self, request):
        upload = request.data.get('archive')
        if not upload:
            return Response({'archive': ['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)

        try:
            root, files = read_archive(upload)
        except ScenarioArchiveError as exc:
            return Response({'detail': str(exc)}, status=status.HTTP_400_BAD_REQUEST)

        payload, file_refs = manifest_to_internal(root)

        missing = missing_referenced_files(file_refs, files)
        if missing:
            return Response(
                {'detail': 'Archive references files that are missing from the zip', 'missing': missing},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ScenarioSerializer(data=payload)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            scenario = serializer.save()
            profile = scenario.profile

            if file_refs['avatar']:
                avatar = profile.avatar
                avatar.filename = SimpleUploadedFile(file_refs['avatar'], files['images'][file_refs['avatar']])
                avatar.save()

            if file_refs['summary']:
                summary = profile.summary
                summary.image = SimpleUploadedFile(file_refs['summary'], files['images'][file_refs['summary']])
                summary.save()

            for vocal in file_refs['vocals']:
                VocalFile.objects.create(
                    scenario=scenario,
                    title=vocal.get('title', ''),
                    filename=SimpleUploadedFile(vocal['filename'], files['vocals'][vocal['filename']]),
                )

            for media in file_refs['media']:
                MediaFile.objects.create(
                    scenario=scenario,
                    title=media.get('title', ''),
                    filename=SimpleUploadedFile(media['filename'], files['media'][media['filename']]),
                )

        scenario.refresh_from_db()
        return Response(ScenarioSerializer(instance=scenario).data, status=status.HTTP_201_CREATED)

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