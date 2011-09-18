from django.contrib import admin
from yabl.authors.models import Author

#class AuthorAdmin(admin.ModelAdmin):
#    pass
admin.site.register(Author)
