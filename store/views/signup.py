from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


# sigunUP get request method

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    # POST request method
    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        customer = Customer(first_name=first_name,
                            last_name = last_name,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)
        # SAVING
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = dict(error=error_message, values=value)
            return render(request, "signup.html", data)

    def validateCustomer(seif, customer):
        error_message = None
        if not customer.first_name:
            error_message = "first name required !!"
        elif len(customer.first_name) < 1:
            error_message = "first name must be 1 long character"
        elif not customer.last_name:
            error_message = "last name required !!"
        elif len(customer.last_name) < 1:
            error_message = "please fill out full last name"
        elif not customer.phone:
            error_message = "phone number required!!"
        elif len(customer.phone) < 10:
            error_message = "reuired number 10"
        elif len(customer.password) < 6:
            error_message = "password must be 6 charcter long"
        elif len(customer.email) < 5:
            error_message = "email must be 5 charcter long"
        elif customer.isExists():
            error_message = "Email address already exist..."
        return error_message