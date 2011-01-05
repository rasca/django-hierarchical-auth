from django.contrib import admin
from django.conf import settings

from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.forms import UserChangeForm

from mptt.forms import TreeNodeMultipleChoiceField

if getattr(settings, 'MPTT_USE_FEINCMS', False):
    from mptt.admin import FeinCMSModelAdmin
    class GroupMPTTModelAdmin(GroupAdmin, FeinCMSModelAdmin):
        pass
else:
    from mptt.admin import MPTTModelAdmin
    class GroupMPTTModelAdmin(GroupAdmin, MPTTModelAdmin):
        pass

admin.site.unregister(Group)
admin.site.register(Group, GroupMPTTModelAdmin)

class UserWithMPTTChangeForm(UserChangeForm):
    groups = TreeNodeMultipleChoiceField(queryset=Group.tree.all())

class UserWithMPTTAdmin(UserAdmin):
    form = UserWithMPTTChangeForm

admin.site.unregister(User)
admin.site.register(User, UserWithMPTTAdmin)
