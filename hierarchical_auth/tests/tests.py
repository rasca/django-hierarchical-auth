from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


class UserTestCase(TestCase):
    """
    Test the added user functionality.
    """

    def setUp(self):
        create_test_objects()


    def test_get_all_groups(self):
        """
        Test if get_all_groups() returns the user's group and all parent groups.
        """

        # user_1 should be member of 3 groups.
        user_1 = User.objects.get(username='user_1')
        group_names = map(lambda g: g.name, user_1.get_all_groups())

        self.assertEquals(3, len(group_names))
        self.assertFalse('group_1' in group_names)
        self.assertTrue('group_2' in group_names)
        self.assertTrue('group_3' in group_names)
        self.assertTrue('group_4' in group_names)

        # test get_all_groups with only_ids=True
        self.assertEqual(set([2, 3, 4]), user_1.get_all_groups(only_ids=True))


        # user_2 should be member of 1 group.
        user_2 = User.objects.get(username='user_2')
        group_names = map(lambda g: g.name, user_2.get_all_groups())

        self.assertEquals(1, len(group_names))
        self.assertFalse('group_1' in group_names)
        self.assertFalse('group_2' in group_names)
        self.assertFalse('group_3' in group_names)
        self.assertTrue('group_4' in group_names)


    def test_has_perm(self):
        """
        Test if permissions attached to descendant groups are inherited by the
        user's group.
        """

        user_1 = User.objects.get(username='user_1')
        self.assertFalse(user_1.has_perm('app_1.perm_1'))
        self.assertTrue(user_1.has_perm('app_1.perm_2'))
        self.assertTrue(user_1.has_perm('app_1.perm_3'))
        self.assertTrue(user_1.has_perm('app_1.perm_4'))

        user_2 = User.objects.get(username = 'user_2')
        self.assertFalse(user_2.has_perm('app_1.perm_1'))
        self.assertFalse(user_2.has_perm('app_1.perm_2'))
        self.assertFalse(user_2.has_perm('app_1.perm_3'))
        self.assertTrue(user_2.has_perm('app_1.perm_4'))



def create_test_objects():
    """
    Creates a test environment.
    """

    # group_1               has_perm: perm_1
    # +-- group_2           has_perm: perm_2
    # +---+-- group_3       has_perm: perm_3
    # +---+---+-- group_4   has_perm: perm_4

    # user_1 is member of group_2
    # user_2 is member of group_4

    user_1 = User.objects.create(
        username    = 'user_1',
        password    = 'password'
    )

    user_2 = User.objects.create(
        username    = 'user_2',
        password    = 'password'
    )

    group_1 = Group.objects.create(
        name        = 'group_1',
    )
    group_2 = Group.objects.create(
        name        = 'group_2',
        parent      = group_1,
    )
    group_3 = Group.objects.create(
        name        = 'group_3',
        parent      = group_2,
    )
    group_4 = Group.objects.create(
        name        = 'group_4',
        parent      = group_3,
    )

    user_1.groups.add(group_2)
    user_2.groups.add(group_4)

    ct = ContentType.objects.create(name='type_1', app_label='app_1', model='model_1')

    group_1.permissions.add(
        Permission.objects.create(
            name            = 'perm_1',
            codename        = 'perm_1',
            content_type    = ct,
        )
    )
    group_2.permissions.add(
        Permission.objects.create(
            name            = 'perm_2',
            codename        = 'perm_2',
            content_type    = ct,
        )
    )
    group_3.permissions.add(
        Permission.objects.create(
            name            = 'perm_3',
            codename        = 'perm_3',
            content_type    = ct,
        )
    )
    group_4.permissions.add(
        Permission.objects.create(
            name            = 'perm_4',
            codename        = 'perm_4',
            content_type    = ct,
        )
    )
