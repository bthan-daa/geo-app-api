from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager


class Incidence(models.Model):
    """ Create new Incidence Model"""
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=250, null=True)
    date_reported = models.DateField(auto_now_add=True)
    location = gis_models.PointField(srid=4326)

    objects = GeoManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Incidences"


class Park(models.Model):
    """ Create new park model"""
    ogf_id = gis_models.IntegerField()
    admin_zone = gis_models.CharField(max_length=9)
    geometry_u = gis_models.DateField()
    effective_field = gis_models.DateField()
    system_dat = gis_models.DateField()
    objectid = gis_models.IntegerField()
    shapearea = gis_models.IntegerField()
    shapelen = gis_models.IntegerField()
    geom = gis_models.MultiPolygonField(srid=4326)
