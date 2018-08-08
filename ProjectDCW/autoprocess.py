import DCW.core.load as ld
from DCW.core.load import *
loaddata('train.csv',labellist=['SalePrice'],IDlist=['Id'])

import DCW.core.missing as ms
ms.Missing_Process(drop_threshold=0.90,filllist=[],fillnum='mean',fillcat='Missing')

import DCW.core.single as sg
sg.single_process(drop_threshold=0.99,single_ratio=0.95,collect=True,show_plot=False,show_table=False,drop=True)
sg.duplicate_process()

import DCW.core.outlier as ot
ot.Outlier_Drop(feature='all',label='SalePrice',method='dropall')
ld.df_train.to_csv('afterprocess.csv',index=False)