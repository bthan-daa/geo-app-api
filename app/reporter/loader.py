"""
Load in shapefile to db
"""
import os
from django.contrib.gis.utils import LayerMapping
from .models import Parks

# Auto-generated `LayerMapping` dictionary for Parks model
parks_mapping = {
    'ogf_id': 'OGF_ID',
    'admin_zone': 'ADMIN_ZONE',
    'geometry_u': 'GEOMETRY_U',
    'effective_field': 'EFFECTIVE_',
    'system_dat': 'SYSTEM_DAT',
    'objectid': 'OBJECTID',
    'shapearea': 'SHAPEAREA',
    'shapelen': 'SHAPELEN',
    'geom': 'MULTIPOLYGON',
}

parks_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    'data',
    'park.shx'),)


def run(verbose=True):
    lm = LayerMapping(
        Parks, parks_shp,
        parks_mapping,
        transform=False,
        encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
