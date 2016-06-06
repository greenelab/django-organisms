from tastypie.resources import ModelResource, ALL

from organisms.models import Organism


class OrganismResource(ModelResource):

    class Meta:
        queryset = Organism.objects.all()
        filtering = {'scientific_name': ALL, 'slug': ALL, 'taxonomy_id': ALL}
        allowed_methods = ['get']
        detail_uri_name = 'slug'
