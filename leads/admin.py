from django.contrib import admin

from leads.models import Lead
from django.db import models

from django.forms import Textarea

class LeadAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

# admin.site.register(Lead)
# admin.site.register(Product)

admin.site.register(Lead, LeadAdmin)
