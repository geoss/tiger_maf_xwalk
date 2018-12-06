import address_tlid_utils as tlid_utils
import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import LineString

den_ad_pd = pd.read_csv("den_addresses_sample.csv")
#den_ad_pd = den_ad_pd.set_index(['MAF_NAME', 'BLKID'])
xwalk = pd.read_csv("den_xwalk.csv")
maf_xwalk = pd.merge(den_ad_pd, xwalk,  how='left', left_on=['MAF_NAME','BLKID'], right_on = ['MAF_NAME','BLKID'])
maf_xwalk = maf_xwalk.set_index(['MAF_NAME', 'BLKID'])
maf_xwalk  = maf_xwalk .assign(TLIDs=maf_xwalk.TLIDs.str.strip('[]').str.split(','))

edges = gpd.read_file("denver_tiger/tl_2017_08031_edges/tl_2017_08031_edges.shp")
edges = edges.set_index(['TLID']) #i think meaningful index will speed retrieval

single_match = tlid_utils.get_single_TLID_addresses(maf_xwalk)
multi_match = tlid_utils.get_multi_TLID_addresses(maf_xwalk)

geom_list = tlid_utils.get_candidate_geoms(multi_match, edges)
#tlid_utils.get_lat_long(maf_xwalk)

point1  = np.array((1,1))
point2 = np.array((0,0))
line1 = LineString([(0, 0), (1.1, 1.1)])
line2 = LineString([(10, 10), (15, 15), (18, 18)])
line3 = LineString([(0, 0), (1.3, 1.3), (1.1, 1.2)])
line_list = {'TLID1': line1, 'TLID2': line2, 'TLID3': line3}

tlid_utils.straight_line_distance(point1, point2)

a = tlid_utils.find_closest(line_list, point1)

tlid_utils.straight_line_distance(np.array((1,1)), np.array((0,0)))
ID_candidates.append