from django.contrib import admin
from .models import addStd

@admin.register(addStd)
class addStdAdmin(admin.ModelAdmin):
    list_display=('stdID','stdName','stdFather','stdDOB','stdGender','stdCNIC','stdAddress','stdMobile','stdEmail','stdEmergencyContactPerson','stdEmergencyContactPersonNumber','stdPhoto','stdCourse')