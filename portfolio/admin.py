from django.contrib import admin
from .models import Person, Occupation, Skills, WorkExp, AcadExp, Contact

admin.site.register(Person)
admin.site.register(Occupation)
admin.site.register(Skills)
admin.site.register(WorkExp)
admin.site.register(AcadExp)
admin.site.register(Contact)
