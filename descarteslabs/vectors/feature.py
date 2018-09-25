import copy

from shapely.geometry import shape

from descarteslabs.common.dotdict import DotDict


class Feature(object):
    """
    An object matching the format of a GeoJSON Feature with geometry and properties.

    Attributes
    ----------
    geometry : shapely.geometry.Polygon or dict
        If the Shapely package is installed, it will be a shapely Object,
        otherwise a dict of a simple GeoJSON geometry type
    properties : DotDict
        Fields describing the geometry.
    """

    def __init__(self, geometry, properties, id=None):
        """
        Example
        -------
        >>> polygon = {
        ...    'type': 'Polygon',
        ...    'coordinates': [[[-95, 42], [-93, 42], [-93, 40], [-95, 41], [-95, 42]]]}
        >>> properties = {"temperature": 70.13, "size": "large"}
        >>> Feature(geometry=polygon, properties=properties)
        """
        if geometry is None:
            raise ValueError("geometry should not be None")

        self.geometry = shape(geometry)

        self.properties = DotDict(properties)
        self.id = id

    @classmethod
    def _create_from_jsonapi(cls, response):
        geometry = response.attributes.get('geometry')
        properties = response.attributes.get('properties')

        self = cls(geometry=geometry, properties=properties, id=response.id)

        return self

    @property
    def geojson(self):
        """
        Returns the ``Feature`` as a GeoJSON dict.

        Example
        -------
        >>> polygon = {
        ...    'type': 'Polygon',
        ...    'coordinates': [[[-95, 42], [-93, 42], [-93, 40], [-95, 41], [-95, 42]]]}
        >>> properties = {"temperature": 70.13, "size": "large"}
        >>> feature = Feature(geometry=polygon, properties=properties)
        >>> feature.geojson
        {'id': None,
        'geometry': {
            'coordinates': [[[-95.0, 42.0], [-93.0, 42.0], [-93.0, 40.0],[-95.0, 41.0],[-95.0, 42.0]]],
            'type': 'Polygon'},
        'properties': {
            'size': 'large',
            'temperature': 70.13
        }}
        """
        properties = copy.deepcopy(self.properties)

        geometry = self.geometry.__geo_interface__

        return dict(properties=properties, geometry=geometry, id=self.id)

    @property
    def __geo_interface__(self):
        return self.geojson['geometry']

    def _repr_json_(self):
        return DotDict(self.geojson)

    def __repr__(self):
        return "Feature({})".format(repr(DotDict(self.geojson)))
