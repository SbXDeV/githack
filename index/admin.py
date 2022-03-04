from django.contrib import admin
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from . import models


# Инструкции
class GuidAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Guid
        fields = '__all__'


class GuidPostAdmin(admin.ModelAdmin):
    form = GuidAdminForm


# Новости
class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.News
        fields = '__all__'


class NewsPostAdmin(admin.ModelAdmin):
    form = NewsAdminForm


# Инструменты
class ToolsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Tools
        fields = '__all__'


class ToolsPostAdmin(admin.ModelAdmin):
    form = ToolsAdminForm


admin.site.register(models.Guid, GuidPostAdmin)
admin.site.register(models.News, NewsPostAdmin)
admin.site.register(models.Tools, ToolsPostAdmin)
