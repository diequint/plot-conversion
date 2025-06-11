def save_polygon_stats(gdf_points, gdf_polygon, output_path, utm_epsg=32615):
    """
    Calculate and save the number of vertices, perimeter (km), and area (ha) of a polygon.
    gdf_points: GeoDataFrame of points (vertices)
    gdf_polygon: GeoDataFrame with the polygon
    output_path: Path to save the stats txt
    utm_epsg: EPSG code for UTM projection (default: 32615)
    """
    num_vertices = len(gdf_points)
    gdf_polygon_utm = gdf_polygon.to_crs(epsg=utm_epsg)
    perimeter_km = gdf_polygon_utm.length.iloc[0] / 1000
    area_ha = gdf_polygon_utm.area.iloc[0] / 10000
    with open(output_path, 'w') as f:
        f.write(f"Number of vertices: {num_vertices}\n")
        f.write(f"Perimeter (km): {perimeter_km:.3f}\n")
        f.write(f"Area (ha): {area_ha:.3f}\n") 