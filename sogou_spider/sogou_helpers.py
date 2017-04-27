# -*- coding: utf-8 -*-
__author__ = 'spacegoing'

import urllib.parse as ps
from itertools import combinations
import csv
import numpy as np
from numpy.random import choice

with open('./hs300_names.csv', newline='') as f:
    reader = csv.reader(f)
    name_list = np.array([r[0] for r in reader])

# Randomly choose 50 names
rand_name_list = choice(name_list, 50)

# Encode Chinese to urlstring
encode_list = [ps.quote('"%s"' % n) for n in rand_name_list]
coop = ps.quote('"合作"')
compete = ps.quote('"竞争"')

# Compute combinations of encoded names
combo_names = list(combinations(encode_list, 2))

# Generate Urls
url_template = 'https://www.sogou.com/web?query=%s+AND+%s+AND+%s'
coop_url_list = [url_template % (c[0], c[1], coop) for c in combo_names]
compete_url_list = [url_template % (c[0], c[1], compete) for c in combo_names]
