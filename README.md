# ll2location

## **Installation**
``pip install ll2location``

## **Usage example: Find from all country**
```
from latlong.gadm import Gadm
from latlong.latlong import LatLong

#init all gadm package in all country, it may take a long time, maybe a few hours
gadm = Gadm()  
gadm.get_shp_fully()

#init lat long
lat = 10.773213
long = 106.671818

#from lat long to location
latlng = LatLong()
code, country_info, detail_info = latlng.to_location(10.773213, 106.671818)
print(detail_info)
```
The output could be:
```
{'GID_3': 'VNM.25.10.4_1',
  'GID_0': 'VNM',
  'COUNTRY': 'Vietnam',
  'GID_1': 'VNM.25_1',
  'NAME_1': 'Hồ Chí Minh',
  'NL_NAME_1': 'NA',
  'GID_2': 'VNM.25.10_1',
  'NAME_2': 'Quận 10',
  'NL_NAME_2': 'NA',
  'NAME_3': 'Phường 12',
  'VARNAME_3': 'Ward 12',
  'NL_NAME_3': 'NA',
  'TYPE_3': 'Phường',
  'ENGTYPE_3': 'Ward',
  'CC_3': 'NA',
  'HASC_3': 'NA'}
```

## **Usage example: Find from specific country code**

```
from latlong.latlong import LatLong
from latlong.gadm import Gadm, GetGadm

#show country code infomation
get_gadm = GetGadm()
codes_detail = get_gadm.get_codes_detail()
print(codes_detail)

#init gadm package in specific country
code = "VNM"
gadm = Gadm()
gadm.get_shp_by_code(code)

#from lat long to location in specific country
latlng = LatLong()
detail_info = latlng.to_location_by_country_code(code, lat, long)

print(detail_info)
```
The output could be:
```
{'GID_3': 'VNM.25.10.4_1',
 'GID_0': 'VNM',
 'COUNTRY': 'Vietnam',
 'GID_1': 'VNM.25_1',
 'NAME_1': 'Hồ Chí Minh',
 'NL_NAME_1': 'NA',
 'GID_2': 'VNM.25.10_1',
 'NAME_2': 'Quận 10',
 'NL_NAME_2': 'NA',
 'NAME_3': 'Phường 12',
 'VARNAME_3': 'Ward 12',
 'NL_NAME_3': 'NA',
 'TYPE_3': 'Phường',
 'ENGTYPE_3': 'Ward',
 'CC_3': 'NA',
 'HASC_3': 'NA'}
```

## **LICENSE**
From https://gadm.org/license.html.

GADM license
The data are freely available for academic use and other non-commercial use. Redistribution or commercial use is not allowed without prior permission.

Using the data to create maps for publishing of academic research articles is allowed. Thus you can use the maps you made with GADM data for figures in articles published by PLoS, Springer Nature, Elsevier, MDPI, etc. You are allowed (but not required) to publish these articles (and the maps they contain) under an open license such as CC-BY as is the case with PLoS journals and may be the case with other open access articles. Data for the following countries is covered by a a different license Austria: Creative Commons Attribution-ShareAlike 2.0 (source: Government of Ausria)
