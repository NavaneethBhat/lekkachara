from django.db import models

class Ledjure(models.Model):
    ''' A ledjure of transactions'''

    shoky = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True,)      # Yeah not More than 4 digits!
    shoky_description = models.TextField(blank=True,null=True)                          #You better have a good explaination
    necessity = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True,default=0.0)  # 5 digits for now!
    necessity_description = models.TextField(max_length=140,null=True,blank=True,)        #Its important i can understand, explain less twitter style
    time_stamp = models.DateField(null=True,blank=True,)


