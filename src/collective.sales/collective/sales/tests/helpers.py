from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


class RoleSwitcher(object):

    def __init__(self, portal, roles, user=TEST_USER_ID):
        self.portal = portal
        self.roles = roles
        self.user = user

    def __enter__(self):
        self.previous_roles = ('Member', 'Authenticated')

        user = self.portal.acl_users.getUserById(TEST_USER_ID)
        if user:
            self.previous_roles = user.getRoles()

        setRoles(self.portal, self.user, self.roles)

    def __exit__(self, type_, value, traceback):
        setRoles(self.portal, self.user, self.previous_roles)
