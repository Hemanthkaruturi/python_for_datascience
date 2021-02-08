# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:13:47 2020

@author: 600037209
"""

from fonoapi import FonoAPI


fon = FonoAPI('a9ecbe184b02a072bbc8824317ea0533120e4da5750c25af')

brands = ['Apple', 'Samsung', 'LG', 'Huawei', 'Ericsson', 'MI', 'Vivo', 'Oppo','Htc','Nokia','Realme','Oneplus','Honor','Motorola','Lenovo','Lava','Asus','Intex','Huawei','Blackberry','Sony','']
brand_devices = []
for brand in brands:
    devices = fon.getlatest(brand)
    brand_devices.append(devices)
	
import pandas as pd
columns = ['DeviceName','Brand','cpu','status','body_c','_3_5mm_jack_','dimensions','_4g_bands','weight','resolution', 'announced', 'talk_time','price']
brand_devices = [devices.dataframe(columns) for devices
                 in brand_devices if devices.not_null]
all_brands = pd.concat(brand_devices)

all_brands.to_csv('Mobile_data.csv',index=False)
