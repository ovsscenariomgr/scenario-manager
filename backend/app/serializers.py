from .models import Title, Header, Scenario
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('name', 'top', 'left',)

class HeaderSerializer(WritableNestedModelSerializer):
    title = TitleSerializer()
    class Meta:
        model = Header
        fields = ('author', 'title', 'date_of_creation', 'description',)

class ScenarioSerializer(WritableNestedModelSerializer):
    header = HeaderSerializer()
    class Meta:
        model = Scenario
        fields = ('id', 'header',)
