# -*- coding: utf-8 -*-
# Copyright © 2021-2026 Geospatial Research Institute Toi Hangarau
# LICENSE: https://github.com/GeospatialResearch/eddie_template/blob/master/LICENSE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Endpoints and flask configuration for this template example app"""
import os
import pathlib

from flask import Blueprint

from eddie.check_celery_alive import check_celery_alive

blueprint = Blueprint('eddie_template', __name__)

# Code for optional web endpoints can be added here. If these are not required, this module can be removed.
# Annotate requests with the @check_celery_alive decorator if you want to ensure that celery is running.
