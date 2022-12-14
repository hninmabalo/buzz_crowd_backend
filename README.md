# buzz_crowd
Buzz Crowd social media app
<br />
<p align="center">
  <h2 align="center">Buzz Crowd (Backend)</h2>
<br>
<Br>


<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Technologies Used</a></li>
      </ul>
    </li>
    <li><a href="#ERD">ERD</a></li>
    <li><a href="#Wireframes">Wireframes</a></li>
    <li><a href="#Screen">Screen</a></li>
    <li><a href="#Code">Code</a></li>
     <li><a href="#future-enhancements">Future Enhancements</a></li>
     <li><a href="#Credits">Credits</a></li>

 </ol>
</details>


# **About The Project**
`Buzz Crowd` is a social media app with full of activities and feeds that you can participate in with the community.


# **Built With**
* [Heroku](https://dashboard.heroku.com/apps)
* Django 
* Python 


# **ERD**
* ![ERD]()

# **Wireframes**
* Home Page
![Wireframes](/img/Buzz%20Crowd%20Home%20Page.png)
* Singup/ Login Page
![Wireframes](/img/Buzz%20Crowd%20Signup%3ALogin%20page.png)
* Profile page
![Wireframes](/img/Buzz%20Crowd%20Profile%20Page.png)

# **Screen**
* Login Screen
![Screen](/img/Buzz%20Crowd%20Login%20Screen.png)
* Home Screen
![Screen](/img/Buzz%20Crowd%20Home%20Screen%20.png)

# **Code**
* Login View
```python
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
          auth.login(request, user)
          return HttpResponseRedirect('/')
        else:
          messages.info(request, 'Invalid User')
          return HttpResponseRedirect('/login/')   

    else:
        return render(request, 'login.html')
```

* Create Post with login required
```python
@login_required(login_url='/login/')
def create_post(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        content = request.POST['content']

        new_post = Post.objects.create(user=user, image=image, content=content)
        new_post.save()

        return HttpResponseRedirect('/')
    else:
        return render(request, 'create.html')
```

# **Future Enhancements**
* Ability for users to share posts
* Ability for users to comments on posts

# **Credits**
* Images are downloaded from [Imgur: The magic of the internet](https://imgur.com/YWuotPe.jpg)
