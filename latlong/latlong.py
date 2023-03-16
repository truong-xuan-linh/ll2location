import os
import geopandas as gpd
from shapely.geometry import Point

from latlong.gadm import Gadm
from latlong.root_dir import find_ROOT_dir

class LatLong():
    def __init__(self) -> None:
        self.gadm = Gadm()
        self.ROOT_dir = find_ROOT_dir()
        self.storage = f"{self.ROOT_dir}/storage"
    
    def polygon_check(self, lat, lng, polygon):
        point = Point(lng, lat)
        if polygon.contains(point):
            return True
        return False
    
    def to_location_by_country_code(self, code, lat, lng):
        folder_dir = os.path.join(self.storage, code)
        list_file = os.listdir(folder_dir)
        list_file.sort()
        shp_file = list_file[-3]
        counties = gpd.GeoDataFrame.from_file(os.path.join(folder_dir, shp_file))
        for i, row in counties.iterrows():
            info = row.to_dict()
            polygon = info["geometry"]
            del info["geometry"]
            check = self.polygon_check(lat, lng, polygon)
            if check:
                return info
        return None
    
    def to_country(self, lat, lng):
        codes = os.listdir(self.storage)
        for code in codes:
            folder_dir = os.path.join(self.storage, code)
            list_file = os.listdir(folder_dir)
            list_file.sort()
            shp_file = list_file[3]
            counties = gpd.GeoDataFrame.from_file(os.path.join(folder_dir, shp_file))
            for i, row in counties.iterrows():
                info = row.to_dict()
                polygon = info["geometry"]
                del info["geometry"]
                check = self.polygon_check(lat, lng, polygon)
                if check:
                    return code, info
        return None, None
    
    def to_location(self, lat, lng):
        code, country_info = self.to_country(lat, lng)
        if code is not None:
            detail_info = self.to_location_by_country_code(code, lat, lng)
            return code, country_info, detail_info
        return None, None, None