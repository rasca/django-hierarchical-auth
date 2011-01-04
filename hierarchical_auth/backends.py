from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission

class HierarchicalModelBackend(ModelBackend):
    """
    Subclass of ModelBackend that checks the hierarchy of groups, that is the
    groups asigned to the user and all their descendants.
    """

    def get_group_permissions(self, user_obj):
        """
        Returns a set of permission strings that this user has through his/her
        groups and their children.
        """
        if not hasattr(user_obj, '_group_perm_cache'):
            if user_obj.is_superuser:
                perms = Permission.objects.all()
            else:
                groups_ids = user_obj.get_all_groups(only_ids=True)
                perms = Permission.objects.filter(group__in=groups_ids)
            perms = perms.values_list('content_type__app_label', 'codename').order_by()
            user_obj._group_perm_cache = set(["%s.%s" % (ct, name) for ct, name in perms])
        return user_obj._group_perm_cache

