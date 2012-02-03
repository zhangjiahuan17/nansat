#-------------------------------------------------------------------------------
# Name:        mapper_modisL1
# Purpose:     Mapping for MODIS-L1 data
#
# Author:      antonk
#
# Created:     13.12.2011
# Copyright:   (c) NERSC 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from vrt import *

class Mapper(VRT):
    ''' VRT with mapping of WKV for MODIS Level 1 (QKM, HKM, 1KM) '''

    def __init__(self, rawVRTFileName, fileName, dataset, metadata, vrtBandList):
        ''' Create MODIS_L1 VRT '''
        #get 1st subdataset and parse to VRT.__init__() for retrieving geo-metadata
        subDs = gdal.Open(dataset.GetSubDatasets()[0][0])
        VRT.__init__(self, subDs, metadata, rawVRTFileName)
       
        #list of available modis names:resolutions
        modisResolutions = {'MYD02QKM':250, 'MOD02QKM':250,
                            'MYD02HKM':500, 'MOD02HKM':500,
                            'MYD021KM':1000, 'MOD021KM':1000};
        
        #should raise error in case of not MODIS_L1
        mResolution = modisResolutions[metadata["SHORTNAME"]];
        
        subDsString = 'HDF4_EOS:EOS_SWATH:"%s":MODIS_SWATH_Type_L1B:%s'
        
        #provide all mappings
        metaDict250 = [
        {'source': subDsString % (fileName, 'EV_250_RefSB'), 'sourceBand': 1, 'wkv': 'radiance', 'parameters':{'wavelength': '645'}},
        {'source': subDsString % (fileName, 'EV_250_RefSB'), 'sourceBand': 2, 'wkv': 'radiance', 'parameters':{'wavelength': '858'}}
        ];
        
        metaDict500 = [
        {'source': subDsString % (fileName, 'EV_250_Aggr500_RefSB'), 'sourceBand': 1, 'wkv': 'radiance', 'parameters':{'wavelength': '645'}},
        {'source': subDsString % (fileName, 'EV_250_Aggr500_RefSB'), 'sourceBand': 2, 'wkv': 'radiance', 'parameters':{'wavelength': '858'}},
        {'source': subDsString % (fileName, 'EV_500_RefSB'), 'sourceBand': 1, 'wkv': 'radiance', 'parameters':{'wavelength': '469'}},
        {'source': subDsString % (fileName, 'EV_500_RefSB'), 'sourceBand': 2, 'wkv': 'radiance', 'parameters':{'wavelength': '555'}},
        {'source': subDsString % (fileName, 'EV_500_RefSB'), 'sourceBand': 3, 'wkv': 'radiance', 'parameters':{'wavelength': '1240'}},
        {'source': subDsString % (fileName, 'EV_500_RefSB'), 'sourceBand': 4, 'wkv': 'radiance', 'parameters':{'wavelength': '1640'}},
        {'source': subDsString % (fileName, 'EV_500_RefSB'), 'sourceBand': 5, 'wkv': 'radiance', 'parameters':{'wavelength': '2130'}}
        ];

        metaDict1000 = [
        {'source': subDsString % (fileName, 'EV_250_Aggr1km_RefSB'), 'sourceBand': 1, 'wkv': 'radiance', 'parameters':{'wavelength': '645'}},
        {'source': subDsString % (fileName, 'EV_250_Aggr1km_RefSB'), 'sourceBand': 2, 'wkv': 'radiance', 'parameters':{'wavelength': '858'}},

        {'source': subDsString % (fileName, 'EV_500_Aggr1km_RefSB'), 'sourceBand': 1, 'wkv': 'radiance', 'parameters':{'wavelength': '469'}},
        {'source': subDsString % (fileName, 'EV_500_Aggr1km_RefSB'), 'sourceBand': 2, 'wkv': 'radiance', 'parameters':{'wavelength': '555'}},
        {'source': subDsString % (fileName, 'EV_500_Aggr1km_RefSB'), 'sourceBand': 3, 'wkv': 'radiance', 'parameters':{'wavelength': '1240'}},
        {'source': subDsString % (fileName, 'EV_500_Aggr1km_RefSB'), 'sourceBand': 4, 'wkv': 'radiance', 'parameters':{'wavelength': '1640'}},
        {'source': subDsString % (fileName, 'EV_500_Aggr1km_RefSB'), 'sourceBand': 5, 'wkv': 'radiance', 'parameters':{'wavelength': '2130'}},

        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 1, 'wkv': 'radiance', 'parameters':{'wavelength': '412'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 2, 'wkv': 'radiance', 'parameters':{'wavelength': '443'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 3, 'wkv': 'radiance', 'parameters':{'wavelength': '488'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 4, 'wkv': 'radiance', 'parameters':{'wavelength': '531'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 5, 'wkv': 'radiance', 'parameters':{'wavelength': '551'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 6, 'wkv': 'radiance', 'parameters':{'wavelength': '667'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 7, 'wkv': 'radiance', 'parameters':{'wavelength': '667'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 8, 'wkv': 'radiance', 'parameters':{'wavelength': '678'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 9, 'wkv': 'radiance', 'parameters':{'wavelength': '678'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 10, 'wkv': 'radiance', 'parameters':{'wavelength': '748'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 11, 'wkv': 'radiance', 'parameters':{'wavelength': '869'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 12, 'wkv': 'radiance', 'parameters':{'wavelength': '905'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 13, 'wkv': 'radiance', 'parameters':{'wavelength': '936'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 14, 'wkv': 'radiance', 'parameters':{'wavelength': '940'}},
        {'source': subDsString % (fileName, 'EV_1KM_RefSB'), 'sourceBand': 15, 'wkv': 'radiance', 'parameters':{'wavelength': '1375'}},

        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 1, 'wkv': 'radiance', 'parameters':{'wavelength': '3750'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 2, 'wkv': 'radiance', 'parameters':{'wavelength': '3959'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 3, 'wkv': 'radiance', 'parameters':{'wavelength': '3959'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 4, 'wkv': 'radiance', 'parameters':{'wavelength': '4050'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 5, 'wkv': 'radiance', 'parameters':{'wavelength': '4465'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 6, 'wkv': 'radiance', 'parameters':{'wavelength': '4515'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 7, 'wkv': 'radiance', 'parameters':{'wavelength': '6715'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 8, 'wkv': 'radiance', 'parameters':{'wavelength': '7325'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 9, 'wkv': 'radiance', 'parameters':{'wavelength': '8550'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 10, 'wkv': 'radiance', 'parameters':{'wavelength': '9730'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 11, 'wkv': 'radiance', 'parameters':{'wavelength': '11030'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 12, 'wkv': 'radiance', 'parameters':{'wavelength': '12020'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 13, 'wkv': 'radiance', 'parameters':{'wavelength': '13335'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 14, 'wkv': 'radiance', 'parameters':{'wavelength': '13635'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 15, 'wkv': 'radiance', 'parameters':{'wavelength': '13935'}},
        {'source': subDsString % (fileName, 'EV_1KM_Emissive'), 'sourceBand': 16, 'wkv': 'radiance', 'parameters':{'wavelength': '14235'}}
        ];

        #get proper mapping depending on resolution
        metaDict = {
            250: metaDict250,
            500: metaDict500,
            1000: metaDict1000,
        }[mResolution];
        
        #set number of bands
        if vrtBandList == None:
            vrtBandList = range(1,len(metaDict)+1);

        self._createVRT(metaDict, vrtBandList);

        return
