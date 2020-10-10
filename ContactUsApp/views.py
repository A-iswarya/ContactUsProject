from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import ContactUsForm
from .models import ContactUs
from django.http import JsonResponse



import re

def index(request):
    contacts = ContactUs.objects.values('Name').order_by('-id');
    form = ContactUsForm();
    context = {'contacts' : contacts, 'form' : form}
    return render(request,'ContactUsApp/index.html',context);

# @require_POST
def addDetails(request):
    Inserted = {'Name': True, 'Email' : True, 'PhoneNumber' : True, 'Description' : True};
    try:
        form = ContactUsForm(request.POST);
        if form.is_valid():
            new_enquiry = ContactUs();
            data = request.POST['Name'];
            if len(data)<3:
                # raise Exception("Length should be greater than 3 characters.");
                Inserted['Name'] = "Length should be greater than 3 characters.";
            elif len(data)>100:
                Inserted['Name'] = "Length should be less than 100 characters.";
                # raise Exception("Length should be less than 100 characters.");
            elif not(re.match("^[a-zA-z][a-zA-Z\s]*$",data)):
                Inserted['Name'] = "The name should only contain characters and space.";
                # raise Exception("The name should only contain characters and space.");
            else:
                new_enquiry.Name = data;
            data = request.POST['Email'];
            if data == '':
                Inserted['Email'] = "Email is mandatory."
                # raise Exception("Email is mandatory.");
            elif not(re.match("^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\.([a-zA-Z]{2,5})$",data)):
                Inserted['Email'] = "Invalid Email.";
                # raise Exception("Invalid Email.");
            else:
                new_enquiry.Email = data;
            data = request.POST['PhoneNumber'];
            if(data):
                if type(data)!=int:
                    Inserted['PhoneNumber'] = "Invalid Phone Number";
                    # raise Exception("Phone number must be nuumeric.");
                elif not(re.match("[0-9]{10}",data)):
                    Inserted['PhoneNumber'] = "Invalid Phone Number";
                    # raise Exception("Invalid Phone Number");
                else:
                    new_enquiry.PhoneNumber = data;
            data = request.POST['Description'];
            if len(data)<20:
                Inserted['Description'] = "Description should be greater than 20 characters.";
                # raise Exception("Description should be greater than 3 characters.");
            elif not(re.match("^[^\s]+.*$",data)):
                Inserted['Description'] = "Invalid Text.";

            else:
                new_enquiry.Description = data;

            if (all(value == True for value in Inserted.values())):
                new_enquiry.save();
                return JsonResponse({"message": "success", "status":"success"});
            else:
                print(Inserted)
                # jsonobj = json.dumps(a);
                raise Exception("")
                return JsonResponse({"message":"failure","status":"error"});


    except Exception as e:
        response = JsonResponse({"error": Inserted});
        response.status_code = 400;
        return response;
