import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
import shutil

# Coordenadas base para Taquara, RS
latitude_base = -29.6517
longitude_base = -50.7764

# Margem para variação das coordenadas
latitude_margin = 0.02
longitude_margin = 0.02

# Número de amostras
num_samples = 500

# Gerar dados fictícios
ids = list(range(1, num_samples + 1))
latitudes = np.random.uniform(low=latitude_base - latitude_margin, high=latitude_base + latitude_margin, size=num_samples)
longitudes = np.random.uniform(low=longitude_base - longitude_margin, high=longitude_base + longitude_margin, size=num_samples)
statuses = np.random.choice(['infected', 'not infected'], size=num_samples)

# Criar o DataFrame
df = pd.DataFrame({
    'id': ids,
    'latitude': latitudes,
    'longitude': longitudes,
    'status': statuses
})

def visualize_data(df):
    # Criação de um GeoDataFrame
    gdf = gpd.GeoDataFrame(df, 
                           geometry=gpd.points_from_xy(df.longitude, df.latitude))
    
    # Criação de um mapa base
    m = folium.Map(location=[-29.73, -51.12], zoom_start=12)
    
    # Adicionando pontos ao mapa
    for _, row in gdf.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"ID: {row['id']}<br>Status: {row['status']}",
            icon=folium.Icon(color='red' if row['status'] == 'infected' else 'green')
        ).add_to(m)
    
    # Salvando o mapa em um arquivo HTML
    map_file = 'dengue_map2.html'
    m.save(map_file)
    
    # Fornecendo o caminho para download
    print(f"Arquivo HTML disponível para download: /home/your-username/{map_file}")

# Chamar a função com o DataFrame fictício
visualize_data(df)
