from Products.CMFPlone.utils import getToolByName

PROFILE_ID = 'profile-collective.superfish:default'


def _cookResources(portal):
    jstool = getToolByName(portal, 'portal_javascripts')
    jstool.cookResources()
    csstool = getToolByName(portal, 'portal_css')
    csstool.cookResources()


def to_2(context):
    portal = getToolByName(context, 'portal_url').getPortalObject()
    _cookResources(portal)


def to_5(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'plone.app.registry')
