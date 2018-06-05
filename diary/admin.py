from django.contrib import admin
from django import forms
from diary.models import (
    Date,
    Dedication,
    TypeDedication,
    Role,
    Schedule,
    TypeSchedule,
    SmallNote,
    Task,
    TypeTask
)

class SmallNoteInline(admin.TabularInline):
    model = SmallNote
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if (
            db_field.name == 'type'
        ):

            try:
                kwargs['queryset'] = Role.objects.filter(
                                                    user=request.user,
                                                    status=1
                                                )
            except IndexError:
                pass

        return super(
                SmallNoteInline,
                self
            ).formfield_for_foreignkey(
                db_field,
                request,
                **kwargs
            )


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if (
            db_field.name == 'type'
        ):

            try:
                kwargs['queryset'] = TypeSchedule.objects.filter(
                                                    user=request.user,
                                                    status=1
                                                )
            except IndexError:
                pass

        return super(
                ScheduleInline,
                self
            ).formfield_for_foreignkey(
                db_field,
                request,
                **kwargs
            )


class DedicationInline(admin.TabularInline):
    model = Dedication
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if (
            db_field.name == 'type'
        ):

            try:
                kwargs['queryset'] = TypeDedication.objects.filter(
                                                    user=request.user,
                                                    status=1
                                                )
            except IndexError:
                pass

        return super(
                DedicationInline,
                self
            ).formfield_for_foreignkey(
                db_field,
                request,
                **kwargs
            )

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if (
            db_field.name == 'type'
        ):

            try:
                kwargs['queryset'] = TypeTask.objects.filter(
                                                    user=request.user,
                                                    status=1
                                                )
            except IndexError:
                pass

        return super(
                TaskInline,
                self
            ).formfield_for_foreignkey(
                db_field,
                request,
                **kwargs
            )


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('date', 'stars',)
    inlines = [
                SmallNoteInline,
                TaskInline,
                ScheduleInline,
                DedicationInline,
            ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(DateAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(DateAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs


@admin.register(TypeTask)
class TypeTaskAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(TypeTaskAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TypeTaskAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs

@admin.register(TypeDedication)
class TypeDedicationAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(TypeDedicationAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TypeDedicationAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoleAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(RoleAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs

@admin.register(TypeSchedule)
class TypeScheduleAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(TypeScheduleAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TypeScheduleAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs

