from django.contrib import admin
from . models import Cart, Good, Goodcategory, Goodcounty
from . models import Goodparameter, Goodtheme, Review, Sell
from . models import Sellstatus, User, Sysdiagrams, Newscolibri
admin.site.register(Cart)
admin.site.register(Good)
admin.site.register(Goodcategory)
admin.site.register(Goodcounty)
admin.site.register(Goodparameter)
admin.site.register(Goodtheme)
admin.site.register(Review)
admin.site.register(Sell)
admin.site.register(User)
admin.site.register(Sellstatus)
admin.site.register(Sysdiagrams)
admin.site.register(Newscolibri)
