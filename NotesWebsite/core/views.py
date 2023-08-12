from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
from .models import Notes


def login(request):
    """
    Handles user login functionality.

    Parameters:
    - request (HttpRequest): The incoming HTTP request object.

    Returns:
    - HttpResponse: Redirects to 'index' page if login is successful, otherwise renders 'login.html'.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["username"] = username
            return redirect(index)
        else:
            messages.add_message(request, messages.WARNING, "Invalid Credentials")
    return render(request, "login.html")


@never_cache
def index(request):
    """
    Renders the user's notes on the index page if authenticated, otherwise redirects to the login page.

    Parameters:
    - request (HttpRequest): The incoming HTTP request object.

    Returns:
    - HttpResponse: Renders 'index.html' with user's notes and username if authenticated, otherwise redirects to 'login' page.
    """
    if "username" in request.session:
        user = User.objects.get(username=request.session["username"])
        notes = [(i.id, i.title) for i in Notes.objects.filter(user=user)]
        return render(
            request,
            "index.html",
            context={"username": request.session["username"], "notes": notes},
        )
    return redirect(login)


@never_cache
def logout(request):
    """
    Handles user logout functionality.

    Parameters:
    - request (HttpRequest): The incoming HTTP request object.

    Returns:
    - HttpResponse: Redirects to 'login' page after logging out.
    """
    if "username" in request.session:
        try:
            del request.session["username"]
        except:
            pass
    return redirect(login)


def signup(request):
    """
    Handles user signup functionality.

    Parameters:
    - request (HttpRequest): The incoming HTTP request object.

    Returns:
    - HttpResponse: Redirects to 'index' page if signup is successful, otherwise renders 'signup.html'.
    """
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            messages.add_message(request, messages.WARNING, "Password not matching")
        elif User.objects.filter(username=username):
            messages.add_message(request, messages.WARNING, "username is taken")
        elif User.objects.filter(email=email):
            messages.add_message(request, messages.WARNING, "email is taken")
        else:
            password = make_password(password, salt=None, hasher="pbkdf2_sha256")
            user = User(username=username, email=email, password=password)
            user.save()
            request.session["username"] = username
            return redirect("/")

    return render(request, "signup.html")


@never_cache
def make_note(request):
    """
    Handles creating a new note for the authenticated user.

    Parameters:
    - request (HttpRequest): The incoming HTTP request object.

    Returns:
    - HttpResponse: Redirects to 'index' page if note creation is successful, otherwise renders 'make_note.html'.
    """
    if "username" in request.session:
        if request.method == "POST":
            title = request.POST["title"]
            note = request.POST["note"]

            new_note = Notes(
                user=User.objects.get(username=request.session["username"]),
                title=title,
                caption=note,
            )
            new_note.save()
            return redirect("/")
        return render(request, "make_note.html")
    else:
        return redirect("/")


@never_cache
def note(request, pk):
    """
    Handles viewing and updating a specific note for the authenticated user.

    Parameters:
    - request (HttpRequest): The incoming HTTP request object.
    - pk (int): The primary key of the note to be viewed/updated.

    Returns:
    - HttpResponse: Renders 'note.html' with the note's details if authenticated and note exists, otherwise redirects to 'login' page.
    """
    if "username" in request.session:
        note = Notes.objects.get(id=pk)

        if request.method == "POST":
            new_title = request.POST["title"]
            new_note = request.POST["note"]
            note.title = new_title
            note.caption = new_note
            note.save()

        context = {"title": note.title, "note": note.caption}
        return render(request, "note.html", context=context)
    else:
        return redirect("/")


@never_cache
def delnote(request, pk):
    """
    Handles deleting a specific note for the authenticated user.

    Parameters:
    - request (HttpRequest): The incoming HTTP request object.
    - pk (int): The primary key of the note to be deleted.

    Returns:
    - HttpResponse: Redirects to 'index' page after deleting the note.
    """
    if "username" in request.session:
        note = Notes.objects.filter(id=pk)
        if note is not None:
            noterow = Notes.objects.get(id=pk)
            noterow.delete()
    return redirect("/")
