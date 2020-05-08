# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:37:11 2020

@author: Alena
"""

import Glassdoor_scraper as gs
import pandas as pd
path= "C:/Users/Alena/Documents/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist', 50, False, path, 15)

