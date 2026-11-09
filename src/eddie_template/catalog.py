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

"""Defines TerriaJS Catalog items used by this template example app."""


def catalog() -> list[dict]:
    """Return TerriaJS Catalog items used by this template example app."""
    return [
        {
            "type": "group",
            "name": "EDDIE Template",
            "members": [
                {
                    "type": "wms",
                    "name": "OpenStreetMap",
                    "url": "https://ows.terrestris.de/osm/service",
                    "layers": "OSM-WMS"
                },
            ]
        }
    ]
