from django.shortcuts import render
from django.views.generic import View
from movie_app.forms import MoviesCreateForm,TheatreForm
from movie_app.models import MoviesCreate,Theatre

# Create your views here.

class MoviesCreateView(View):
    template_name="movies.html"
    form_class=MoviesCreateForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class
        return render(request,self.template_name,{'form':form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data

            title=data.get("title")
            language=data.get("language")
            year=data.get("year")
            review=data.get("review")

            movies_instance=MoviesCreate(title=title,language=language,year=year,review=review)

            movies_instance.save()


        return render(request,self.template_name,{"form":form_instance})
    

class MoviesListView(View):
    template_name="movies_list.html"
    def get(self,request,*args,**kwargs):
        movie_list=MoviesCreate.objects.all()
        return render(request,self.template_name,{"list":movie_list})
    

class TheatreView(View):
    template_name="theatre.html"
    form_class=TheatreForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)

        if form_instance.is_valid():
            data=form_instance.cleaned_data

            name=data.get("name")
            location=data.get("location")
            screen_type=data.get("screen_type")
            sound_system=data.get("sound_system")
            seating=data.get("seating")

            theatre_instance=Theatre(name=name,location=location,screen_type=screen_type,sound_system=sound_system,seating=seating)

            theatre_instance.save()

        return render(request,self.template_name,{"form":form_instance})
    

class TheatreList(View):
    template_name="theatre_list.html"
    form_class=Theatre
    def get(self,request,*args,**kwargs):

        theatre_list=Theatre.objects.all()

        return render(request,self.template_name,{"list":theatre_list})

