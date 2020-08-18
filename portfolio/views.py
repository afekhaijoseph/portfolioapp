from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from .forms import PersonForm,OccupationForm,SkillsForm,WorkExpForm,AcadExpForm,ContactForm
from .models import Person, Occupation, WorkExp, AcadExp, Contact, Skills


def portfolio(request, pk):
    if pk:
        user=User.objects.get(pk=pk)
        context={'users' :user}
    return render(request, 'portfolio/portfolio.html', context)


@login_required
def portfolio_form(request):
   #user=User.objects.get(pk=request.user.id)
    SkillsFormSet = modelformset_factory(Skills, form=SkillsForm) 
    WorkExpFormSet = modelformset_factory(WorkExp, form=WorkExpForm)
    AcadExpFormSet = modelformset_factory(AcadExp, form=AcadExpForm)


    if request.method == 'POST':
        print(request.POST)
        person_form = PersonForm(request.POST, request.FILES)
        occupation_form = OccupationForm(request.POST)
        contact_form = ContactForm(request.POST)
        skillset = SkillsFormSet(request.POST, prefix='skill')
        workexpset = WorkExpFormSet(request.POST, prefix='workexp')
        acadexpset = AcadExpFormSet(request.POST, prefix='acadexp')
        

        if person_form.is_valid() and occupation_form.is_valid() and skillset.is_valid() and workexpset.is_valid() and acadexpset.is_valid() and contact_form.is_valid():
            person=person_form.save(commit=False)
            person.user=request.user
            person.save()

            occupation=occupation_form.save(commit=False)
            occupation.user=request.user
            occupation.save()

            contact=contact_form.save(commit=False)
            contact.user=request.user
            contact.save()

            instances = skillset.save(commit=False)
            for instance in instances:
                instance.user=request.user
                instance.save()

            instances = workexpset.save(commit=False)
            for instance in instances:
                instance.user=request.user
                instance.save()
            

            instances = acadexpset.save(commit=False)
            for instance in instances:
                instance.user=request.user
                instance.save()
                
        return redirect('portfolio', pk=user.id)   

    else:
        person_form = PersonForm()
        occupation_form = OccupationForm()
        skillset = SkillsFormSet(prefix='skill', queryset=Skills.objects.none())
        workexpset = WorkExpFormSet(prefix='workexp', queryset=WorkExp.objects.none())
        acadexpset = AcadExpFormSet(prefix='acadexp', queryset=AcadExp.objects.none())
        contact_form = ContactForm()
    
    context={
        'person_form' : person_form,
        'occupation_form' : occupation_form,
        'skillset' : skillset,
        'workexpset' : workexpset,
        'acadexpset' : acadexpset,
        'contact_form' : contact_form
    }

    return render(request, 'portfolio/portfolio_form.html', context) 

@login_required
def portfolio_update_form(request):
    pk=request.user.id
    SkillsFormSet = modelformset_factory(Skills, form=SkillsForm, can_delete=True) 
    WorkExpFormSet = modelformset_factory(WorkExp, form=WorkExpForm, can_delete=True)
    AcadExpFormSet = modelformset_factory(AcadExp, form=AcadExpForm, can_delete=True)

    if request.method == 'POST':
        person_form = PersonForm(request.POST, request.FILES)
        occupation_form = OccupationForm(request.POST)
        contact_form = ContactForm(request.POST)
        skillset = SkillsFormSet(request.POST, prefix='update-skill')
        workexpset = WorkExpFormSet(request.POST, prefix='update-workexp') 
        acadexpset = AcadExpFormSet(request.POST, prefix='update-acadexp')
        

        if person_form.is_valid() and occupation_form.is_valid() and skillset.is_valid() and workexpset.is_valid() and acadexpset.is_valid() and contact_form.is_valid():
            person=person_form.save(commit=False)
            person.user=request.user
            person.save()

            occupation=occupation_form.save(commit=False)
            occupation.user=request.user
            occupation.save()

            contact=contact_form.save(commit=False)
            contact.user=request.user
            contact.save()

            instances = skillset.save(commit=False)
            for obj in skillset.deleted_objects:
                obj.delete()
    
            for instance in instances:
                instance.user=request.user
                instance.save()
             
            instances = workexpset.save(commit=False)
            for obj in workexpset.deleted_objects:
                obj.delete()

            for instance in instances:
                instance.user=request.user
                instance.save()
            
            instances = acadexpset.save(commit=False)
            for obj in acadexpset.deleted_objects:
                obj.delete()

            for instance in instances:
                instance.user=request.user
                instance.save()

        return redirect('portfolio', pk=pk)            

    else:
        person_form  = PersonForm(instance=request.user.person)
        occupation_form = OccupationForm(instance=request.user)
        skillset = SkillsFormSet(prefix='update-skill', queryset=Skills.objects.filter(user=request.user))
        workexpset = WorkExpFormSet(prefix='update-workexp', queryset=WorkExp.objects.filter(user=request.user))
        acadexpset = AcadExpFormSet(prefix='update-acadexp', queryset=AcadExp.objects.filter(user=request.user))
        contact_form = ContactForm(instance=request.user.contact)

        context = {
            'person_form' : person_form,
            'occupation_form' : occupation_form,
            'skillset': skillset,
            'workexpset' : workexpset,
            'acadexpset' : acadexpset,
            'contact_form' : contact_form,
            }

    return render(request, 'portfolio/portfolio_update.html', context)