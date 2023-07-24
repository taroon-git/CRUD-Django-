from django.shortcuts import render,redirect

from .models import *
# Create your views here.

# def InsertView(request):
#     return render(request,'app/insert.html')

def InsertView(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')


    ## Creating object of model
    ## Inserting data into model
        newuser = Student.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact)
        newuser.save()

    # after insert show on HTML
        # return render(request,'app/show.html')
        return redirect('showpage')
    else:
        return render(request,'app/insert.html')
    



def ShowPage(request):
    ## Select * from Table_name
    ## In Django, ORM query
    all_data = Student.objects.all()
    return render(request,'app/show.html',{'key1': all_data})




## Edit Page View
def EditPage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,'app/edit.html',{'key2' : get_data})


## Update Data View

def UpdateView(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

    ## Query for update
    udata.save()
    return redirect('showpage')


### Delete data View

def DeleteView(request,pk):
    ddata = Student.objects.get(id=pk)
    ## Query for delete
    ddata.delete()
    return redirect('showpage')