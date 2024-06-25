import sqlite3

from tables.eight_speed import insertEightSpeedData, createEightSpeedTable, get_distributor_8spd, get_brand_8spd, get_speed_8spd, get_ratio_8spd
from tables.nine_speed import insertNineSpeedData, createNineSpeedTable, get_distributor_9spd, get_brand_9spd, get_speed_9spd, get_ratio_9spd
from tables.ten_speed import insertTenSpeedData, createTenSpeedTable, get_distributor_10spd, get_brand_10spd, get_speed_10spd, get_ratio_10spd
from tables import distributor_table

# createEightSpeedTable()
# insertEightSpeedData()
# get_distributor_8spd("Madison")
# get_brand_8spd("Microshift")
# get_speed_8spd(8)
# get_ratio_8spd("12-46")

# createNineSpeedTable()
# insertNineSpeedData()
# get_distributor_9spd("SRAM")
# get_brand_9spd("SRAM")
# get_speed_9spd()
# get_ratio_9spd("11-38")

# createTenSpeedTable()
# insertTenSpeedData()
# get_distributor_10spd("Bob-Elliot")
# get_brand_10spd("Sunrace")
# get_speed_10spd(10)
# get_ratio_10spd("11-42")