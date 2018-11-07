# -*- coding: utf-8 -*-
#
# This file is part of django-bind (https://github.com/mathiasertl/django-bind).
#
# django-bind is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# django-bind is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with django-bind.  If not,
# see <http://www.gnu.org/licenses/>.

from copy import copy

from django import template
from django.utils.safestring import mark_safe

from ..models import Macro

register = template.Library()


@register.simple_tag(takes_context=True)
def caa(context, issue=';', issuewild=';'):
    value = """
{domain}.   IN  CAA 0 issue "{issue}"
{domain}.   IN  CAA 0   issuewild "{issuewild}" """.format(
        domain=context['domain'],
        issue=issue,
        issuewild=issuewild
    )
    return mark_safe(value.strip())


@register.simple_tag(takes_context=True)
def macro(context, name, **kwargs):
    context = copy(context)
    context.update(kwargs)

    macro = Macro.objects.get(name=name)

    t = template.Template(macro.template)
    return mark_safe(t.render(context))


@register.simple_tag
def set(val=None):
    return val
