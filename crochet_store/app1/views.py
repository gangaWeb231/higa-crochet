
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Order


# HOME
def index(request):
    return render(request, "index.html")


# LOGIN PAGE
def user_login(request):

    # If already logged in
    if request.user.is_authenticated:
        return redirect("index")      # or redirect("orders")

    if request.method == "POST":

        action = request.POST.get("action")

        # ================= SIGNUP =================
        if action == "signup":

            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            # Check username exists
            if User.objects.filter(username=username).exists():

                return render(request, "login.html", {
                    "error": "Username already exists"
                })

            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # Login immediately
            # login(request, user)

            # Redirect to account page
            return redirect("login")



        # ================= LOGIN =================
        if action == "login":

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                # Redirect to account page
                return redirect("login")

            else:

                return render(request, "login.html", {
                    "error": "Invalid username or password"
                })


    return render(request, "login.html")



# LOGOUT
def user_logout(request):

    logout(request)

    return redirect("login")



# PLACE ORDER

@login_required
def place_order(request):

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        product = request.POST.get("product")

        Order.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            address=address,
            product=product
        )

    return redirect("index")



# ORDERS PAGE
@login_required
def orders(request):

    user_orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "orders.html", {
        "orders": user_orders
    })

