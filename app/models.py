from django.db import models
from django.contrib.auth.models import User



departamentos=[
('Cardiologista','Cardiologista'),
('Dermatologista','Dermatologista'),
('Especialista em emergencia','Especialista em emergencia'),
('Imunologistas','Imunologistas'),
('Anesteologistas','Anesteologistas'),
('Cirurgião','Cirurgião')
]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.Cascade)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    adress = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, null= True)
    department = models.CharField(max_length=50, choices=departments, default='Cirurgião')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    symptoms = models.CharField(max_length=200, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " (" + self.symptoms + ")"


