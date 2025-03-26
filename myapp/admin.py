from django.contrib import admin
from .models import DressVerity, DressReview,Store,DressCertificate

# Register your models here.

class DressReviewInline(admin.TabularInline):
    model = DressReview 
    extra = 2

class DressVerityAdmin(admin.ModelAdmin):
    list_display = ('name','type', 'date_added')
    inlines = [DressReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('dress_varieties',)
    
class DressCertificateAdmin(admin.ModelAdmin):
    list_display = ('dress', 'certificate_number')

admin.site.register(DressVerity, DressVerityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(DressCertificate, DressCertificateAdmin)
