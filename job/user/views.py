from django.shortcuts import render,redirect
from django.views import View
from .forms import JobForm
from .models import Jobs





# Create your views here.
class userhomeview(View):
    def get(self,request):
        return render(request,"userhome.html")


class jobregview(View):
    def get(self,request):
        form=JobForm()
        return render(request,"jobreg.html",{"form":form})
    def post(self,request):
        form_data=JobForm(data=request.POST)
        if form_data.is_valid():
            name=(form_data.cleaned_data.get('name'))
            ag=(form_data.cleaned_data.get('age'))
            ph=(form_data.cleaned_data.get('phone'))
            pl=(form_data.cleaned_data.get('place'))
            em=(form_data.cleaned_data.get('email'))
            JobForm.objects.create(name=name,age=ag,phone=ph,place=pl,email=em)
            # return HttpResponse("submitted")
            return redirect('uhome')
        print(form_data.errors)
        # return HttpResponse("invalid user input")
        return render(request,"jobreg.html",{"form":form_data})
    


class JobListView(View):
    def get(self,request):
        data=Jobs.objects.all
        print(data)
        return render(request,"joblist.html",{"jobs":data})
    