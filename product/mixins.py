from django.http import JsonResponse

class JsonResponseMixin:
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return JsonResponse(serializer.data, safe=False)