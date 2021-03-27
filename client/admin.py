from django.contrib import admin
from .models import User, Category, Unit

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'photo',
        'is_staff',
        'is_superuser'
    ]
    class Meta:
        model = User


admin.site.register(User, UserAdmin)

def make_active(modeladmin, request, queryset):
    queryset.update(status=Category.STATUS_ACTIVE)

def make_inactive(modeladmin, request, queryset):
    queryset.update(status=Category.STATUS_INACTIVE)

make_active.short_description = "Faollashtirish"
make_inactive.short_description = "Nofaollashtirish"

class CategoryAdmin(admin.ModelAdmin):
    actions = [make_active, make_inactive]
    fields = [
        'parent',
        'name_uz',
        'name_ru',
        'status'
    ]
    list_display = [
        'id',
        'admin',
        'parent',
        'name_uz',
        'name_ru',
        'status'
    ]

    def save_form(self, request, form, change):
        category = form.save(commit=False)
        category.admin = request.user
        category.save()

        return super().save_form(request, form, change)
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class UnitAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name_uz',
        'name_ru'
    ]
    class Meta:
        model = Unit

admin.site.register(Unit, UnitAdmin)

