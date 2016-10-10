# -*- coding: utf-8 -*-

"""
Created on 2016-09-20
:author: Oshane Bailey (oshane@alteroo.com)
"""

import colander
from kotti.views.edit import DocumentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config

from kotti_docit import _
from kotti_docit.resources import AdminManual


class AdminManualSchema(DocumentSchema):
    """ Schema for AdminManual. """


@view_config(name=AdminManual.type_info.add_view,
             permission=AdminManual.type_info.add_permission,
             renderer='kotti:templates/edit/node.pt')
class AdminManualAddForm(AddFormView):
    """ Form to add a new instance of AdminManual. """

    schema_factory = AdminManualSchema
    add = AdminManual
    item_type = _(u"AdminManual")


@view_config(name='edit', context=AdminManual, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class AdminManualEditForm(EditFormView):
    """ Form to edit existing AdminManual objects. """

    schema_factory = AdminManualSchema
