from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from zope.configuration import xmlconfig


class SalesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.sales
        xmlconfig.file('configure.zcml',
                       collective.sales,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.sales:default')


SALES_FIXTURE = SalesLayer()
SALES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SALES_FIXTURE,), name='Sales:Integration')
