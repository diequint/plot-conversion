from pyproj import Transformer

def utm_to_latlon(x, y, zone=15, northern=True):
    """Converts UTM coordinates to lat/lon (WGS84)."""
    epsg_code = f"326{zone:02d}" if northern else f"327{zone:02d}"
    transformer = Transformer.from_crs(f"epsg:{epsg_code}", "epsg:4326", always_xy=True)
    lon, lat = transformer.transform(x, y)
    return lon, lat 