from collective.sales.shopcategory import IShopCategory
from collective.sales.testing import SALES_INTEGRATION_TESTING
from collective.sales.tests.helpers import RoleSwitcher
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility
import unittest2 as unittest


class TestShopCategory(unittest.TestCase):

    layer = SALES_INTEGRATION_TESTING

    def test_fti(self):
        fti = queryUtility(IDexterityFTI,
                           name='collective.sales.shopcategory')
        self.assertNotEquals(None, fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI,
                           name='collective.sales.shopcategory')

        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IShopCategory.providedBy(new_object))

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
