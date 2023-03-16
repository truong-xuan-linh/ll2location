import os
import json
import tqdm
import zipfile
import requests
import geopandas as gpd
from bs4 import BeautifulSoup
from latlong.root_dir import find_ROOT_dir

class GetGadm():
    def __init__(self) -> None:
        self.url = "https://gadm.org/download_country.html"
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        self.options =  self.soup.find_all("option")
    
    def get_codes(self):
        codes = []
        for option in self.options:
            code = option["value"].split("_")[0]
            if code != "":
                codes.append(code)
        return codes
    
    def get_codes_detail(self):
        codes = {}
        for option in self.options:
            code = option["value"].split("_")[0]
            if code != "":
                codes[option.text] = code
        return codes
    
    def __get_url__(self):
        return self.url

class Gadm():
    def __init__(self) -> None:
        self.origin_url = 'https://geodata.ucdavis.edu/gadm/gadm4.1/shp/'
        self.getgadm = GetGadm()
        self.ROOT_dir = find_ROOT_dir()
        self.storage = f"{self.ROOT_dir}/storage"
        
    def get_shp_by_code(self, code):
        folder_name = f"{self.storage}/{code}"
        if os.path.isdir(folder_name):
            if len(os.listdir(folder_name)) != 0:
                print(f"The {code} is already exists")
                return
        print(f"Downloading {code}")
        os.makedirs(folder_name, exist_ok=True)
        des_name = f"gadm41_{code}_shp.zip"
        file_name = os.path.join(folder_name, des_name)
        url = os.path.join(self.origin_url, des_name)
        response = requests.get(url)
        with open(file_name, "wb") as f:
            f.write(response.content)
            
        with zipfile.ZipFile(file_name, "r") as f:
            f.extractall(folder_name)
    
    def get_shp_fully(self):
        codes = self.getgadm.get_codes()
        for code in codes:
            self.get_shp_by_code(code)
    
    def get_df_fully(self):
        merge_name = "./merge"
        os.makedirs(merge_name, exist_ok=True)
        codes = os.listdir(self.storage)
        merge_df = gpd.GeoDataFrame()
        print("Merging ...")
        for code in tqdm.tqdm(codes):
            folder_dir = os.path.join(self.storage, code)
            list_file = os.listdir(folder_dir)
            list_file.sort()
            shp_file = list_file[-3]
            counties = gpd.GeoDataFrame.from_file(os.path.join(folder_dir, shp_file))
            cols_to_convert = counties.select_dtypes(exclude='object').columns.drop('geometry')
            counties[cols_to_convert] = counties[cols_to_convert].astype('object')
            if merge_df.empty:
                merge_df = counties
                continue
            merge_df = merge_df.merge(counties, how="outer")
            
        merge_df.to_file(f"{merge_name}/merge.shp")
        print("Merged")