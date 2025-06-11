import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import os
import zipfile
from converters.utm_to_latlon import utm_to_latlon
from utils import save_polygon_stats

def export_to_kml(gdf, output_path):
    """Export a GeoDataFrame to KML format."""
    gdf.to_file(output_path, driver='KML')

def export_to_shapefile(gdf, output_path):
    """Export a GeoDataFrame to Shapefile format."""
    gdf.to_file(output_path, driver='ESRI Shapefile')

def zip_shapefile(shp_path):
    """Compress all files related to a shapefile into a ZIP archive and remove the originals."""
    base = os.path.splitext(shp_path)[0]
    exts = ['.shp', '.shx', '.dbf', '.prj', '.cpg', '.qix', '.fix']
    files = [base + ext for ext in exts if os.path.exists(base + ext)]
    zip_path = base + '.zip'
    with zipfile.ZipFile(zip_path, 'w') as zf:
        for f in files:
            zf.write(f, os.path.basename(f))
    # Remove the original shapefile components
    for f in files:
        os.remove(f)
    return zip_path

# Input and output paths
DATA_PATH = os.path.join('data', 'Coordenadas-predio.csv')
OUTPUT_PATH = os.path.join('outputs', 'predio.geojson')
VERTICES_PATH = os.path.join('outputs', 'vertices.geojson')
KML_PATH = os.path.join('outputs', 'predio.kml')
SHP_PATH = os.path.join('outputs', 'predio.shp')
STATS_PATH = os.path.join('outputs', 'polygon_stats.txt')

# Read CSV
df = pd.read_csv(DATA_PATH)

# X axis = lon, Y axis = lat
# Convert UTM coordinates to lat/lon
df[['lon', 'lat']] = df.apply(lambda row: pd.Series(utm_to_latlon(row['X'], row['Y'], zone=15, northern=True)), axis=1)

# Create GeoDataFrame of points
gdf_points = gpd.GeoDataFrame(df, geometry=[Point(xy) for xy in zip(df['lon'], df['lat'])], crs='epsg:4326')

# Create polygon (using the order of the vertices)
polygon = Polygon(gdf_points.geometry.tolist())
gdf_polygon = gpd.GeoDataFrame(geometry=[polygon], crs='epsg:4326')

# Save points and polygon as GeoJSON
os.makedirs('outputs', exist_ok=True)
gdf_points[['VERT', 'geometry']].to_file(VERTICES_PATH, driver='GeoJSON')
gdf_polygon.to_file(OUTPUT_PATH, driver='GeoJSON')

# Export polygon to KML and Shapefile
export_to_kml(gdf_polygon, KML_PATH)
export_to_shapefile(gdf_polygon, SHP_PATH)

# Zip the shapefile and remove originals
zip_path = zip_shapefile(SHP_PATH)

# Save polygon stats using the utility function
save_polygon_stats(gdf_points, gdf_polygon, STATS_PATH, utm_epsg=32615)

print(f"Vertices GeoJSON saved at: {VERTICES_PATH}")
print(f"Polygon GeoJSON saved at: {OUTPUT_PATH}")
print(f"Polygon KML saved at: {KML_PATH}")
print(f"Polygon Shapefile ZIP saved at: {zip_path}")
print(f"Polygon stats saved at: {STATS_PATH}")