from django.contrib import admin

from .models import Road, Report, Rating, Suggestion, City


class ReportInline(admin.StackedInline):
    model = Report
    extra = 0


class RatingInline(admin.StackedInline):
    model = Rating
    extra = 0


@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'city', )
    list_filter = ('status', 'city')
    search_fields = ('name', )
    inlines = [ReportInline, RatingInline]


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'text', 'photo')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'road',
                    'city_name', 'rate', 'comment')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_filter = ('road__city__name',)
    list_display = ('username', 'phone', 'date', 'road',
                    'city_name', 'photo', 'text')
