from django.contrib import admin
from .models import PropertyFeatures, PropertyLayouts, PropertyPartners, PropertyManagers, Property, PropertyType, \
    PropertyImages


@admin.register(PropertyFeatures)
class PropertyFeaturesAdmin(admin.ModelAdmin):
    ...


@admin.register(PropertyLayouts)
class PropertyLayoutsAdmin(admin.ModelAdmin):
    ...


@admin.register(PropertyPartners)
class PropertyPartnersAdmin(admin.ModelAdmin):
    ...


@admin.register(PropertyManagers)
class PropertyManagersAdmin(admin.ModelAdmin):
    ...


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    ...


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(PropertyImages)
class PropertyImagesAdmin(admin.ModelAdmin):
    ...