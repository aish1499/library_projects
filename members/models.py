from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class Member(models.Model):
    user= models.ForeignKey(User, verbose_name=_("Profile"), on_delete=models.CASCADE)
   # name = models.CharField(_("Member Name"), max_length=50),
    age = models.PositiveSmallIntegerField(_("Age")),
    gender = models.CharField(_("Gender"), choices=(('male','Male'),('female','Female')),max_length=200),
    state = models.CharField(_("State"), max_length=50),
    phone_no = models.CharField(("Phone no."),max_length=50),
    #email = models.EmailField(_("Email"), max_length=254),
    district = models.CharField(_("District"), max_length=50),
    language = models.CharField(_("Languages Konwn"), max_length=50),
    occupatiions =models.CharField(_("Occupation"), max_length=50)

class Rented_Books(models.Model):
    user= models.ForeignKey(User, verbose_name=_("Profile"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=_("Book"), on_delete=models.CASCADE)
    date = models.DateField(_("Rented_on"), auto_now=False, auto_now_add=False)