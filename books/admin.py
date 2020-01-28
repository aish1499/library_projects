from django.contrib import admin
from .models import Book, Review
import csv
from rangefilter.filter import DateRangeFilter
from django.http import HttpResponse
#from import_export.admin ImportExportModelAdmin

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
#class BookAdmin(ImportExportModelAdmin):

    list_display = ['name', 'pages', 'published_on']
    list_display_links = ['name']
    list_filter = ['genre', ('published_on', DateRangeFilter)]
    list_filter = ['genre']
    search_fields = [ 'name', ]
    actions = ['export_to_csv',]



def export_to_csv(self,request,queryset):
    meta = self.model.meta

    field_names = [field.name for field in meta.filds]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment;fileename={meta}.csv'
    writer = csv.writer(response)
    writer = writerow(field_name)
    for obj in queryset:
        writer.writrow([getattr(obj,field)for
        field in field_names])
        return response



# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['book','username']
   

# admin.site.register(Review, ReviewAdmin)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'username', 'stars', 'comment']
    list_display_links = ['book', 'username' ]
    list_editable = ['stars']
    
