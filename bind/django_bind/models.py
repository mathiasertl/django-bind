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

from django.db import models


class BaseModel(models.Model):
    # Just adds created/updated to every model that inherits from this class
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Macro(BaseModel):
    name = models.CharField(max_length=255)
    template = models.TextField()

    def __str__(self):
        return self.name


class View(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Zone(BaseModel):
    domain = models.CharField(max_length=255)
    template = models.TextField()

    zones = models.ManyToManyField(View, blank=True)

    def __str__(self):
        return self.domain
