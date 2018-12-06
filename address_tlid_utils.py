import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import math


def is_multi_TLID_candidates(edges_row_TLIDs):
    if len(edges_row_TLIDs) == 0:
        #print('No possible TLIDs')
        return False
    if len(edges_row_TLIDs) == 1:
        #print('Only one option')
        return False
    else:
        return True

def get_single_TLID_addresses(xwalk):
    address_point_TLID_candidates = xwalk.loc[:,'TLIDs'].to_dict()
    address_point_TLID = {}
    for id, candidates in address_point_TLID_candidates.items():
        if isinstance(candidates, list):
            if len(candidates) == 1 and candidates[0]:
                address_point_TLID[id] = candidates[0]
    return address_point_TLID

def get_multi_TLID_addresses(xwalk):
    address_point_TLID_candidates = xwalk.loc[:,'TLIDs'].to_dict()
    address_point_TLIDs = {}
    for id, candidates in address_point_TLID_candidates.items():
        if isinstance(candidates, list):
            if len(candidates) > 1:
                address_point_TLIDs[id] = candidates
    return address_point_TLIDs

'''
def get_lat_long(MAF_NAME, BLKID, maf_xwalk):
    return maf_xwalk.loc[MAF_NAME, BLKID), ["LATITUDE", "LONGITUDE"]].values()
'''

def get_candidate_geoms(multi_TLID_addresses, edges):
    geom_list = {}
    for idx, row in multi_TLID_addresses.items():
        for id in row:
            geom_list[id] = (edges.loc[int(id), 'geometry'])
    return geom_list

def find_closest(linedict, point):
    closest_line = None
    min_dist = np.inf
    for idx, aline in linedict.items():
        for vert in aline.coords:
            if straight_line_distance(vert, point) < min_dist:
                min_dist = straight_line_distance(vert, point)
                closest_line = idx
    return closest_line

def straight_line_distance(coord1, coord2):
    return np.sqrt(np.sum((coord1 - coord2) ** 2))
