from APILearning.models import ModuleApis
from rest_framework import serializers

class ModuleApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleApis
        fields = ('version', 'license', 'copyright', 'information', 'author', 'author_email', 
                        'document_url', 'title', 'description')