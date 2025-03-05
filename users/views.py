from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})



def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})

def imageprediction(request):
    from django.conf import settings
    if request.method=='POST':
        image_file = request.FILES['file']
        # let's check if it is a csv file
        # if not image_file.name.endswith('.png'):
        #     messages.error(request, 'THIS IS NOT A PNG  FILE')
        fs = FileSystemStorage(location="media/rice_test/")
        filename = fs.save(image_file.name, image_file)
        file = settings.MEDIA_ROOT + '//' + 'rice_test' + '//' + filename
        # detect_filename = fs.save(image_file.name, image_file)
        uploaded_file_url = "/media/rice_test/" + filename  # fs.url(filename)
        print("Image path ", uploaded_file_url)
        from .utility.imageLaneDetection import image
        result = image(file)
      
        return render(request, "users/UploadForm.html", {'path': uploaded_file_url})
    else:
        return render(request, "users/UploadForm.html",{})


def videoprediction(request):
    from django.conf import settings
    if request.method=='POST':
        image_file = request.FILES['file']
        # let's check if it is a csv file
        # if not image_file.name.endswith('.png'):
        #     messages.error(request, 'THIS IS NOT A PNG  FILE')
        fs = FileSystemStorage(location="media/rice_test/")
        filename = fs.save(image_file.name, image_file)
        file = settings.MEDIA_ROOT + '//' + 'rice_test' + '//' + filename
        # detect_filename = fs.save(image_file.name, image_file)
        uploaded_file_url = "/media/rice_test/" + filename  # fs.url(filename)
        print("Image path ", uploaded_file_url)
        from .utility.videoLaneDetection import video
        result = video(file)
       
        return render(request, "users/video.html", {'path': uploaded_file_url})
    else:
        return render(request, "users/video.html",{})



