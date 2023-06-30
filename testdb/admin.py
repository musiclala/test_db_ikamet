from django.contrib import admin
from .models import Manager, Property, Type, Image, Layout, Feature, Partner



@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    ...


@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):
    ...


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    ...


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    ...


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    ...


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    ...


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ...