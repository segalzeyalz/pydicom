import os
import pydicom
from pydicom.data import get_testdata_files
filename = get_testdata_files("rtplan.dcm")[0]
ds = pydicom.dcmread(filename)
print(ds)