from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language


# Inline to be used inside Author model
class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    # List view customizations
    list_display = ["get_author", "date_of_birth", "date_of_death", 'pk']

    def get_author(self, obj):
        return f"{obj.last_name}, {obj.first_name}"
    get_author.short_description = 'Full Name'  # To set a column name
    get_author.admin_order_field = 'last_name'  # To allow sorting

    # Detail view customizations
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BookInline]


# Inline to be used inside Author model
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# @ line Identical to admin.site.register(Book, BookAdmin)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # List view customizations
    list_display = ("title", "author", "isbn", "display_genre", "copy_count")

    # Detail view customizations
    filter_horizontal = ["genre",]
    inlines = [BookInstanceInline]

    @admin.display(description="Copies")
    def copy_count(self, obj):
        return obj.bookinstance_set.count()


# @ line Identical to admin.site.register(BookInstance, BookInstanceAdmin)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # List view customizations
    list_display = ["instance", "imprint", "status", "borrower", "due_back"]
    list_filter = ["status", "due_back"]

    @admin.display(description="Book Instance")
    def instance(self, obj):
        return f"{obj.book} - {obj.id} "
    # instance.short_description = 'Book Instance'

    # Detail view customizations
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': [('status', 'due_back', 'borrower'),]
        })
    )


# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)

admin.site.register(Genre)
admin.site.register(Language)

admin.site.register(Author, AuthorAdmin)
