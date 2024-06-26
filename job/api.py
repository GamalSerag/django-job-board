from .serializer import JobSerializers
from .models import Job
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def joblistapi(request):
    all_jobs = Job.objects.all()
    data = JobSerializers(all_jobs,many=True).data
    return Response({'data':data})