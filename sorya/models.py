from django.db import models

from django.contrib.auth.models import User

from django.conf import settings


class Category(models.Model):
    isim = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.isim 



class Soru(models.Model):
    # user =  models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #gizlilik_sozlesmesi = models.BooleanField("Gizlilik Sozlesmesini Okudum Onayliyorum*" , null=True)
    #sartlar_sozlesmesi = models.BooleanField("Sartlar ve Kosullar Sozlesmesini Okudum Onayliyorum*", null=True)
    isim = models.CharField(max_length=100)
    kategori = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # website = models.CharField(max_length=200, default='ananas.website', null=True)
   # eposta = models.CharField(max_length=200, null=True)
   # telefon = models.CharField(max_length=200, null=True)
    soru = models.TextField(max_length=1000, null=True)
   # aciklama = models.TextField(max_length=1000, null=True)
    # il = models.ForeignKey(Il, on_delete=models.SET_NULL, null=True)
   # ilce = models.ForeignKey(Ilce, on_delete=models.SET_NULL, null=True)
   # resim = models.ImageField(default='ananas.jpg',
                            #  upload_to='profile_images')

    def __str__(self):
        return self.isim 

class Yanit(models.Model):
    sorular = models.ForeignKey(Soru, related_name="comments",null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return ' {} on {}'.format(self.text, self.sorular)
  