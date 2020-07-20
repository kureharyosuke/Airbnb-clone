from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Space", {"fields": ("geusts", "beds", "bedrooms", "baths")}),
        (
            "More About the Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Detail", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "geusts",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("^city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
