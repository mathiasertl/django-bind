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


from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from reversion.admin import VersionAdmin
from django_object_actions import DjangoObjectActions

from .models import Macro
from .models import View
from .models import Zone


@admin.register(Macro)
class MacroAdmin(VersionAdmin):
    pass


@admin.register(View)
class ViewAdmin(VersionAdmin):
    pass


@admin.register(Zone)
class ZoneAdmin(DjangoObjectActions, VersionAdmin):
    change_actions = ['render_template']

    def render_template(self, request, obj):
        return HttpResponse(obj.render_template, view=request.GET.get('view'))
    render_template.label = _('Render')
