from collective.sales import shopitem
from collective.sales.testing import SALES_INTEGRATION_TESTING
from collective.sales.tests.helpers import RoleSwitcher
from plone.dexterity.interfaces import IDexterityFTI
from plone.dexterity.utils import createContentInContainer
from zope.component import createObject
from zope.component import queryUtility
import unittest2 as unittest


class TestSimpleShopItem(unittest.TestCase):

    layer = SALES_INTEGRATION_TESTING

    def test_fti(self):
        fti = queryUtility(IDexterityFTI,
                           name='collective.sales.simpleshopitem')
        self.assertNotEquals(None, fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI,
                           name='collective.sales.simpleshopitem')

        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(shopitem.ISimpleShopItem.providedBy(new_object))
        self.assertFalse(shopitem.IMultiShopItem.providedBy(new_object))
        self.assertFalse(shopitem.IMultiShopItemVariant.providedBy(new_object))

    def test_not_globally_creatable(self):
        portal = self.layer['portal']

        with RoleSwitcher(portal, ('Manager', )):
            with self.assertRaises(ValueError):
                createContentInContainer(
                    portal,
                    'collective.sales.simpleshopitem',
                    title='shopitem-one',
                    itemnumber='s1',
                    price=1.5)

    def test_in_category_creatable(self):
        portal = self.layer['portal']

        with RoleSwitcher(portal, ('Manager', )):
            category = createContentInContainer(
                portal,
                'collective.sales.shopcategory',
                title='category-one')

            createContentInContainer(
                category,
                'collective.sales.simpleshopitem',
                title='shopitem-two',
                itemnumber='s2',
                price=1.5)

            portal.manage_delObjects([category.id])


class TestMultiShopItem(unittest.TestCase):

    layer = SALES_INTEGRATION_TESTING

    def test_ftis(self):
        self.assertNotEquals(None, queryUtility(
                IDexterityFTI, name='collective.sales.multishopitem'))

        self.assertNotEquals(None, queryUtility(
                IDexterityFTI, name='collective.sales.multishopitemvariant'))

    def test_multishopitem_factory(self):
        fti = queryUtility(IDexterityFTI,
                           name='collective.sales.multishopitem')

        factory = fti.factory
        new_object = createObject(factory)

        self.assertTrue(shopitem.IMultiShopItem.providedBy(new_object))
        self.assertFalse(shopitem.ISimpleShopItem.providedBy(new_object))
        self.assertFalse(shopitem.IMultiShopItemVariant.providedBy(new_object))

    def test_variant_factory(self):
        fti = queryUtility(IDexterityFTI,
                           name='collective.sales.multishopitemvariant')

        factory = fti.factory
        new_object = createObject(factory)

        self.assertTrue(shopitem.IMultiShopItemVariant.providedBy(new_object))
        self.assertFalse(shopitem.IMultiShopItem.providedBy(new_object))
        self.assertFalse(shopitem.ISimpleShopItem.providedBy(new_object))

    def test_not_globally_creatable(self):
        portal = self.layer['portal']

        with RoleSwitcher(portal, ('Manager', )):
            with self.assertRaises(ValueError):
                createContentInContainer(
                    portal,
                    'collective.sales.multishopitem',
                    title='multiSI',
                    itemnumber='m1',
                    price=1.5)

            with self.assertRaises(ValueError):
                createContentInContainer(
                    portal,
                    'collective.sales.multishopitemvariant',
                    title='variant',
                    itemnumber='v1',
                    price=1.5)

    def test_in_category_creatable(self):
        portal = self.layer['portal']

        with RoleSwitcher(portal, ('Manager', )):
            category = createContentInContainer(
                portal,
                'collective.sales.shopcategory',
                title='category-two')

            item = createContentInContainer(
                category,
                'collective.sales.multishopitem',
                title='multitem',
                itemnumber='m2',
                price=1.5)

            self.assertTrue(shopitem.IMultiShopItem.providedBy(item))

            createContentInContainer(
                item,
                'collective.sales.multishopitemvariant',
                title='variant1',
                itemnumber='m2.1',
                price=1)

            createContentInContainer(
                item,
                'collective.sales.multishopitemvariant',
                title='variant2',
                itemnumber='m2.1',
                price=2)

            portal.manage_delObjects([category.id])
