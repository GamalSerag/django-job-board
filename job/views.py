from django.shortcuts import render
from .models import Job

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    context =  {"jobs":job_list}
    return render(request, template_name='job/job_list.html',context=context)


def job_detail(request, id):
    return render(request, template_name='job/job_detail.html')
