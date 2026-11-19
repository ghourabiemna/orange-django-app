from django.db import models

class Interface(models.Model):
    interface_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ne_name = models.CharField(max_length=100)
    ipv4_address = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    subnet_mask = models.CharField(max_length=18, blank=True, null=True)
    mac_address = models.CharField(max_length=17, blank=True)
    rate = models.CharField(max_length=50, blank=True)
    admin_status = models.CharField(max_length=50, blank=True)
    ipv4_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.interface_name
class Reservation(models.Model):
    interface_name1 = models.CharField(max_length=100)
    description1 = models.TextField(blank=True)
    ne_name1 = models.CharField(max_length=100)
    def __str__(self):
        return self.interface_name1