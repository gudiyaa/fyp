from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,PersonalForm,QualificationForm,ResearchForm
from .models import Personal,Qualification,Research_Publications
from decimal import *
import scholarly

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {})

class Home(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html",{})

class About(View):
    def get(self,request,*args,**kwargs):
        return render(request,"about.html",{})

class Contact(View):
    def get(self,request,*args,**kwargs):
        return render(request,"contacts.html",{})

class Director(View):
    def get(self,request,*args,**kwargs):
        return render(request,"director_profile.html",{})
class Registrar(View):
    def get(self,request,*args,**kwargs):
        return render(request,"Registrar.html",{})
class Core(View):
    def get(self,request,*args,**kwargs):
        return render(request,"core_members.html",{})
class Gallery(View):
    def get(self,request,*args,**kwargs):
        return render(request,"gallery.html",{})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def personaldata(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
                post=form.save(commit=False)
                post.user=request.user
                post.save()
                return redirect('/')
    
    else:
        form = PersonalForm()
    return render(request, 'personal.html', {'form': form})

def qualificationdata(request):
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/')
    
    else:
        form = QualificationForm()
    return render(request, 'qualification.html', {'form': form})

def qualification_edit(request) :
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/')
    
    else:
        form = QualificationForm()
    return render(request, 'qualification.html', {'form': form})

def researchdata(request):
    if request.method == 'POST':
        form = ResearchForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.score=0
            post.score1=0
            post.score2=0
            post.score3=0
            post.score4=0
            post.score5=0
            post.score6=0
            post.score7=0
            post.score8=0
            post.score9=0
            post.score10=0
            post.score11=0
            post.score12=0
            post.score13=0
            post.score14=0
            post.score15=0
            post.score16=0
            post.score17=0
            post.score18=0
            post.score19=0
            post.score20=0
            post.score21=0
            post.score22=0
            post.score1 += post.rd_onlypi*8
            post.score1 += post.rd_pi*5
            if post.no_of_rest_pi:
                post.score1 += post.rd_co_pi*3/post.no_of_rest_pi
            
            post.score1 += post.rd_onlyinventor*8
            post.score1 += post.rd_inventor*5
            if post.no_of_rest_inventor:
                post.score1 += post.rd_co_inventor*3/post.no_of_rest_inventor

        
            post.score2 = post.no_of_5lakhs*2
            
            
            post.score3 += post.phd_sole_supervisor*8
            post.score3 += post.phd_first_supervisor*5
            if post.no_of_rest_supervisor:
                post.score3 += post.phd_co_supervisor*3/post.no_of_rest_supervisor

            
            post.score4 += post.as_sole_journal_author*4
            post.score4 += post.as_first_journal_author*2
            if post.no_of_rest_journal_author:
                post.score4 += post.as_co_journal_author*2/post.no_of_rest_journal_author

            
            post.score5 += post.as_sole_conf_author*1
            post.score5 += post.as_first_conf_author*Decimal(0.6)
            if post.no_of_rest_conf_author:
                post.score5 += post.as_co_conf_author*Decimal(0.4)/post.no_of_rest_conf_author

            post.score6 += post.sem_hod*2
            post.score6 += post.sem_dean*2
            post.score6 += post.sem_cw*2
            post.score6 += post.sem_tpi*2
            post.score6 += post.sem_advisor*2
            post.score6 += post.sem_cvo*2
            post.score6 += post.sem_pi*2
            post.score6 += post.sem_teqip*2

            post.score7 += post.sem_warden*1
            post.score7 += post.sem_asst_warden*1
            post.score7 += post.sem_asso_dean*1
            post.score7 += post.sem_chairman*1
            post.score7 += post.sem_fac_inch_inst_activities*1

            post.score8 += post.sem_chairman_comm*Decimal(0.5)
            post.score8 += post.sem_fac_inch_comm*Decimal(0.5)

            post.score9 += post.sem_dept_activities*Decimal(0.5)
            post.score9 += post.sem_dept_comm*Decimal(0.5)

            post.score10 += post.workshop*2

            post.score11 += post.for2week_nat_prgm*2
            post.score11 += post.for1week_nat_prgm*1

            post.score12 += post.conf_as_chairman*3

            post.score13 += post.teaching_year*4

            post.score14 += post.labs*4

            post.score15 += post.theory_credit_hrs*1

            post.score16 += post.pg*Decimal(0.5)

            post.score17 += post.ug*Decimal(0.25)

            post.score18 += post.books_international*6

            post.score19 += post.books_national*2

            post.score20 += post.outreach_activities*1

            post.score21 += post.fellowship*10

            if post.sem_tpi:
                post.score22 += post.above85*4
                post.score22 += post.above75*2

            post.score = post.score1 + post.score2 + post.score3 + post.score4 + post.score5 + post.score6 + post.score7 +post.score8 + post.score9 + post.score10 + post.score11 + post.score12 + post.score13 + post.score14 + post.score15 + post.score16 + post.score17 + post.score18 + post.score19 + post.score20 + post.score21 + post.score22

        form.save()
        return redirect('/')
    
    else:
        form = ResearchForm()
    return render(request, 'research.html', {'form': form})

def scoredata(request):
    form=ResearchForm()
    search_query = scholarly.search_author('G Sikka')
    author = next(search_query).fill()
    author1 = [pub.bib['title'] for pub in author.publications]
    return render(request, 'score.html', {'author1': author1})