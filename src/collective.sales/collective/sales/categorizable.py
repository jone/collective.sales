from collective.sales import _
from collective.sales.shopcategory import IShopCategory
from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.form.widget import PLACEHOLDER
from z3c.formwidget.query.widget import QueryTerms
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import alsoProvides


class ICategorizable(form.Schema):
    """Behavior for making an item categorizable, which means shop
    categories can be selected for this item. The item will be
    displayed in the selected shop categories.

    If the parent of the item is a shop category, the item will by
    default be listed in this category.
    """

    categories = RelationList(
        title=_(u'categorizable_categories_label',
                default=u'Categories'),
        description=_(u'categorizable_categories_hepl',
                      default=u''),

        value_type=RelationChoice(
            title=u'Category',

            source=ObjPathSourceBinder(
                object_provides=IShopCategory.__identifier__,
                navigation_tree_query=dict(
                    object_provides=IShopCategory.__identifier__))),
        )


alsoProvides(ICategorizable, form.IFormFieldProvider)


@form.default_value(field=ICategorizable['categories'])
def default_categories(data):
    if IShopCategory.providedBy(data.context):
        # The path to our default-value object is the token
        # of the vocabulary term.
        token = u'/'.join(data.context.getPhysicalPath())

        # WARNING: by default, in this state there are no
        # terms, because we use a source binder and not a
        # static vocabulary.
        # For providing a default object, we need to recreate
        # the terms, containing the term of our default
        # object.

        # This may look hackish, but it seems to be the cleanest
        # we to do it - z3c.formwidget.query has the same strategy.

        source = data.widget.bound_source
        terms = set([source.getTermByToken(token)])
        data.widget.terms = QueryTerms(data.context, data.request,
                                       data.widget.form, data.field,
                                       data.widget, terms)

        # We want the value to be selected by default. Just
        # returning the value does not work, so we need to act
        # like we'd have the value from the request by returning
        # the placeholder and setting the value by ourselves.
        data.widget.value = [token]
        return PLACEHOLDER

    else:
        return []
