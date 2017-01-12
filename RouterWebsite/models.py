from django.db import models

# Create your models here.

class Rule(models.Model):
    content = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.content

class Device(models.Model):
     username = models.CharField(max_length=200)
     domain = models.IPAddressField()
     activity = models.BooleanField(default=True)
     visited = models.BooleanField(default=False)
     visited_number = models.DecimalField(decimal_places=0,max_digits=10)
     bandwidth_usage = models.DecimalField(decimal_places=0,max_digits=2)
     compliance = models.BooleanField(default=True)
     priority = models.BooleanField(default=False)
     block = models.BooleanField(default=False)
     user_rule = models.ForeignKey(Rule)

     class Meta:
         ordering = ['-visited_number']
    
     def __unicode__(self):
        return self.username
     

class Notification(models.Model):
    dev = models.ForeignKey(Device)
    content = models.TextField()

    def __unicode__(self):
        return self.content

class Traffic(models.Model):
    url = models.CharField(max_length=100)
    bandwidth = models.DecimalField(decimal_places=0,max_digits=10)
    time = models.DecimalField(decimal_places=0,max_digits=10)

    def __unicode__(self):
        return self.url

class SSID(models.Model):
    ssid_name = models.CharField(max_length=100)
    ssid_network = models.CharField(max_length=20)
    ssid_type = models.BooleanField(default=True)
    ssid_password = models.CharField(max_length=100)
    ssid_active = models.BooleanField(default=True)
    ssid_guest = models.BooleanField(default=False)

    def __unicode__(self):
        return self.ssid_name




