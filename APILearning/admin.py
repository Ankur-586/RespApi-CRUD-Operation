from django.contrib import admin
from .models import ModuleApis

@admin.register(ModuleApis)
class ModuleApisAdmin(admin.ModelAdmin):
    list_display = ['version', 'license', 'copyright', 'information', 'author', 'author_email', 
                        'document_url', 'title', 'description']



# -----------------------------------------------------------------------
# Using generic class-based views

# class moduleapi(generics.ListCreateAPIView):
#     queryset = ModuleApis.objects.all()
#     serializer_class = ModuleApiSerializer


# class moduleapiDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ModuleApis.objects.all()
#     serializer_class = ModuleApiSerializer

# --------------------------------------------------------------------------------

# class moduleapi(APIView):

#     def get(self, request, format=None):
#         snippets = ModuleApis.objects.all()
#         serializer = ModuleApiSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ModuleApiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)