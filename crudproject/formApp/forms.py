from django import forms
from .models import addStd
class addStdForm(forms.ModelForm):
    class Meta:
        model=addStd
        fields=['stdID','stdName','stdFather','stdDOB','stdGender','stdCNIC','stdAddress','stdMobile','stdEmail','stdEmergencyContactPerson','stdEmergencyContactPersonNumber','stdPhoto','stdCourse']

        labels={
            'stdID':'ID ','stdName':'Name ','stdFather':'Father ','stdDOB':'DOB','stdGender':'Gender','stdCNIC':'CNIC','stdAddress':'Address','stdMobile':'Mobile','stdEmail':'Email','stdEmergencyContactPerson':'EmergencyContactPerson','stdEmergencyContactPersonNumber':'EmergencyContactPersonNumber','stdPhoto':'Photo','stdCourse':'Course'
        }

        widgets={
            'stdID':forms.NumberInput(attrs={'class':'form-control'}),
            'stdName':forms.TextInput(attrs={'class':'form-control'}),
            'stdFather':forms.TextInput(attrs={'class':'form-control'}),
            'stdDOB':forms.TextInput(attrs={'class':'form-control'}),
            'stdGender':forms.TextInput(attrs={'class':'form-control'}),
            'stdCNIC':forms.TextInput(attrs={'class':'form-control'}),
            'stdAddress':forms.TextInput(attrs={'class':'form-control'}),
            'stdMobile':forms.TextInput(attrs={'class':'form-control'}),
            'stdEmail':forms.TextInput(attrs={'class':'form-control'}),
            'stdEmergencyContactPerson':forms.TextInput(attrs={'class':'form-control'}),
            'stdEmergencyContactPersonNumber':forms.TextInput(attrs={'class':'form-control'}),
            'stdPhoto':forms.TextInput(attrs={'class':'form-control'}),
            'stdCourse':forms.TextInput(attrs={'class':'form-control'}),

            }

    
