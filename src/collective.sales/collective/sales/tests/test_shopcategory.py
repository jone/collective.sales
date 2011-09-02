from collective.sales.testing import SALES_INTEGRATION_TESTING
from collective.sales.tests.helpers import RoleSwitcher
import unittest2 as unittest


class TestShopCategory(unittest.TestCase):

    layer = SALES_INTEGRATION_TESTING

    def test_category_creatable(self):
        portal = self.layer['portal']

        id = 'first-category'
        self.assertNotIn(id, portal.keys())

        with RoleSwitcher(portal, ('Manager',)):
            portal.invokeFactory(
                'collective.sales.shopcategory',
                id,
                title=u'first category')

        self.assertIn(id, portal.keys())

        portal.manage_delObjects([id,])

    def test_category_nestable(self):
        portal = self.layer['portal']

        first_id = 'first'
        second_id = 'second'
        self.assertNotIn(first_id, portal.keys())

        # create first
        with RoleSwitcher(portal, ('Manager',)):
            portal.invokeFactory(
                'collective.sales.shopcategory',
                first_id,
                title=u'First')

        self.assertIn(first_id, portal.keys())

        # create second
        with RoleSwitcher(portal, ('Manager',)):
            portal.get(first_id).invokeFactory(
                'collective.sales.shopcategory',
                second_id,
                title=u'Second')

        self.assertIn(second_id, portal.get(first_id).keys())

        portal.manage_delObjects([first_id])
