from reversion.admin import VersionAdmin


class BaseAdmin(VersionAdmin):
    ordering = ('-updated_on',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()
