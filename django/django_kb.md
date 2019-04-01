
## Django Doc
  - https://docs.djangoproject.com/en/dev/contents/

## Admin
- localhost:800/admin
- use createsuperuser command to create a login user for this
- groups and users auto created
- models needs to be added to be viewed here
- admin commands:
```bash
> django-admin startproject MyProject        # Start a new Project
```

### Management 
```bash
> python manage.py runserver                 # run django server
> python manage.py startapp main_app         # run an application
> python manage.py shell                     # run python django shell
> python manage.py createsuperuser           # create admin level super user

> python manage.py makemigrations            # make a migration file from model update
> python manage.py showmigrations            # show migrations
> python manage.py sqlmigrate myapp 0001     # show sql equivalent of myapp>0001 migration
> python manage.py migrate                   # Run that migration

```

## Shell
```python
>>> myModel.objects.all()
>>> myModel.objects.all.count()
>>> myModel.objects.filter(status='F')
>>> myModel.objects.exclude(status='F')
>>> myModel.objects.filter(foreignKey__fieldname='F')

# delete an object
>>> myObj=myModel.objects.filter(id='1')
>>> myObj.delete()

# and / or conditions
>>> from django.db.models import Q
>>> myModel.objects.filter(Q(condition1=True) | Q(condition2=True))
>>> myModel.objects.filter(Q(condition1=True) & ~Q(condition2=False))
```

### Custom Query sets
- All the queries related to myModel can be put in a custom query set
- This is better as it performs lazy queries (only executes SQL when needed).

```python
# define query set class
class myModelQuerySet(models.QuerySet):
    def get_ojbs_with_some_condition(self):
        return self.filter(status='T')

# Connect query set call to the model
class myModel(models.Model):
    objects = myModelQuerySet.as_manager()

# usage
myModel.objects.get_ojbs_with_some_condition()
```

## Django Architecture

### MVC <-> Django
Model = Model
View = Template
Controller = View

- Model : represents data, maps model classes to DB tables
- Template: Generates HTML; Presentation logic only
- View: takes HTTP req and returns responses; Calls template and model

### Django Structure
- Project
  - project dir
    - settings.py
      - installed apps list, each new app needs to be added here
      - 'TEMPLATES' > 'DIR' settings 
        ```python
        TEMPLATES = [
            {
                'DIRS' : [os.path.join(BASE_DIR, "templates)],
            }
        ]
        ```
      - Static files directory:
        ```python
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static")
        ]
        ```

      - LOGIN_URL : take user here for login
      - LOGIN_REDIRECT_URL : take user here after login
      - LOGOUT_REDIRECT_URL : take user here after logout

    - urls.py
      - matches the requested URL to the correct view
        ```python
        from myapp import views
        urlpatterns=[
            url(r'^index/', views.index)
        ]
        ```
      - 'r' is for role strings, in python a role string lets the use 
        of special characters
      - by default r'index' means work with any url that has the word index. 
        eg. /aindex, /indexb, /abindexcd
        so to make it more start with index we add ^index
    
      - root url dispatcher r'^$', will match empty string and thus will 
        respond to http://127.0.0.1:8000

      - Best practices:
        - Good to have an project url dispatcher and an app url dispatcher
          ```python
            from django.conf.urls import include, url
                urlpatterns=[
                url(r'^app/', include(main_app.urls))
            ]
          ```

      - wsgi.py

  - app
    - views.py
      - takes in a web request and responds, 
      - eg: for index localhost:8000/index
        ```python 
        def index(request):
            return HTTPResponse('<h1> Hello world!</h1>')
        ```

    - 'static' dir
      - contains files like styles.css, bootstrap.min.css
      - django auto looks for static files in here
      - Use following at the top of every django template
        ```html
        {% load staticfiles %}
        
        <html>
        <head>
        <link href="{% static 'subfolder/style.css' %}" rel="stylesheet"> 
        </head>
        </html>
        ```

    - urls.py
      - app level urls

    - forms.py
      - built in ModelForm class can be used to generate forms from Models
      - if you want to define any forms in django app
      - this is similar to defining a model
      - create a post url in urls.py
      - create a view that handles the post url
      - to display create a template by adding form \tag and csrf_token
      - forms.as_p in template formats the form as paragraph on UI. basically 
        each field on a separate line. 
      - widgets such as date widget can be added to add form field widgets. 
      - meta forms can be used to create forms directly from model classes

    - Templates folder
      - can be called using render function in views
      - django built in template tags and filters
        for, if, filter, firstof, forloop.counter, ifchanged, include, etc. 
        https://docs.djangoproject.com/en/2.1/ref/templates/builtins/
      - template inheritance
        templates can extend other templates to keep the code modular and simpler 
      - block content is the content specifc for own page
     
    - models.py
      - https://docs.djangoproject.com/en/2.1/ref/models/fields/

    - admin.py
      - in order to see models in admin UI, register the models here
      - following will show id and fields1-3 on Admin UI for myModel. 
        but it will show all fields for myModel2
      - myModel > field1 and field2 will be editable as well
        ```python
        from .models import myModel

        @admin.register(myModel)
        class myModelAdmin(admin.ModelAdmin):
            list_display = ('id', 'field1', 'field2', 'field3')
            list_editable = ('field1', 'field2')

        admin.site.register(myModel2)
        ```

    - apps.py
    - migrations folder



## Authentication
- Inbuilt auth user model
  - any model can import the model and use objects of built in user model
    ```python
    from django.contrib.auth.models import User
    ```
- is_authenticated
  ```python
  from django.shortcuts import render, redirect

  def welcome(request):
      if request.user.is_authenticated:
          return redirect(app/login.html)
      else:
          return render(request, 'app/welcome.html')
  ```

- login__required
  ```python
  from django.contrib.auth.decorators import login_required

  @login_required
  def home(request):
      # code...
      return render(request, 'myapp/mypage.html', my_app_json_data)
  ```

- Built in LoginView and LogoutView can be used with a custom template

## Imports
- from django.http import HTTPResponse
- from django.contrib import admin
- from django.conf.urls import include, url
- from django.db import models
- from django.contrib.auth.models import User


- to make code python2 and python3 compatible
  from django.utils.encoding import python2_unicode_compatible
  ```python
  @python2_unicode_compatible
  class myclass(model.Model):
  ```

