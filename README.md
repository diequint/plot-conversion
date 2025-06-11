# Land Plot Coordinate Conversion

This project converts UTM coordinates (WGS 84 / UTM zone 15N) from a CSV file to geographic coordinates (lat/lon, WGS 84) and generates GeoJSON files with the plot's vertices and polygon. It also exports the polygon to KML and Shapefile (ZIP), and generates a text file with polygon statistics.

## Requirements
- Python 3.8+
- pip

## Installation and Usage

1. **Clone or download this repository.**

2. **Create a virtual environment (recommended):**

   On Windows:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
   On Linux/Mac:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Place your CSV file in the `data/` folder**
   - The file must have at least the columns `X`, `Y` (UTM coordinates) and optionally `VERT` (vertex name).

5. **(Optional) Set the output path for the vertices GeoJSON using an environment variable:**
   - By default, the vertices GeoJSON will be saved as `outputs/vertices.geojson`.
   - To change the output path, set the environment variable `VERTICES_GEOJSON_PATH` before running the script:
     - On Windows PowerShell:
       ```powershell
       $env:VERTICES_GEOJSON_PATH="outputs/my_vertices.geojson"
       python main.py
       ```
     - On Linux/Mac:
       ```sh
       export VERTICES_GEOJSON_PATH=outputs/my_vertices.geojson
       python main.py
       ```

6. **Run the main script:**
   ```sh
   python main.py
   ```

7. **Output files:**
   - `outputs/vertices.geojson`: GeoJSON with the vertices and their names (path can be changed with env variable).
   - `outputs/predio.geojson`: GeoJSON with the plot polygon.
   - `outputs/predio.kml`: KML file with the plot polygon.
   - `outputs/predio.zip`: Shapefile (all necessary files compressed in a ZIP) with the plot polygon.
   - `outputs/polygon_stats.txt`: Text file with the number of vertices, perimeter (in km), and area (in ha) of the polygon.

## Features
- Converts UTM (EPSG:32615) coordinates to WGS84 (EPSG:4326).
- Exports the plot polygon to GeoJSON, KML, and Shapefile (ZIP).
- Exports the vertices to GeoJSON (customizable path).
- Generates a text file with polygon statistics: number of vertices, perimeter (km), and area (ha).
- Keeps the outputs folder clean by only keeping the zipped shapefile.

## Future extensions
- Export vertices to KML and Shapefile.
- Support for other reference systems.
- Graphical or web interface.

## Author
Diego Quintana
Contact: software@diequint.com

## License
This project is licensed under the [GNU GPL v3](LICENSE). This means you can:
- Freely use the code for any purpose
- Modify the code
- Distribute the code
- Sublicense the code
- Use the code for commercial purposes
