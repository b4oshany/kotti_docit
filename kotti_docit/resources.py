# -*- coding: utf-8 -*-

"""
Created on 2016-09-20
:author: Oshane Bailey (oshane@alteroo.com)
"""

from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Document
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from zope.interface import implements

from kotti_docit import _



class AdminManual(Document):
    """ Documents that are only visible by admins. """
    implements(IDefaultWorkflow)
    id = Column(Integer, ForeignKey('documents.id'), primary_key=True)


    type_info = Document.type_info.copy(
        name=u'AdminManual',
        title=_(u'Admin Manual'),
        add_view=u'add_admin_manual',
        addable_to=[u'Document']
    )
