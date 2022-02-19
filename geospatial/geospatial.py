import rasterio
from rasterio.plot import show

fp = 'geospatial/Landsat_ETM_2001-08-26_multispectral.tif'
img = rasterio.open(fp)
show(img)
