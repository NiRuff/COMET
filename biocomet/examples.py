import pandas as pd

hs_1_genes = pd.Series(["COL4A1","CLK1","SMTN","PKD1","RAB11FIP4","CD34","NAV1","VAMP2","CEBPD","ERBB2","FBN1","STK38","NDE1","PNKD","THBS1","IQSEC3","SOBP","PSIP1","RFX2","RPS15A","MATN2","TUBB3","NFKBIA","KIF5C","TMEFF2","HK1","TNS1","LMNA","GADD45B","IMMT","BCAT2","IL1R1","TOB2","PGM2L1","PPP2R2C","AQP1","CA4","TCF7L2","TCOF1","MBNL3","RAB3IL1","SLC8A1","ABCC9","RTF1","IRAK4","APLNR","COL5A1","HDAC1","KHSRP","SERPINH1","RPS19","HSP90AB1","TUBB6","ANTXR1","MME","ADM","SH3D19","COL14A1","P4HA1","BASP1","SPTBN1","RELA","CNKSR3","GALNT6","SLITRK1","OPA1","STRBP","HIF3A","NLRC5","PDLIM1","PARVG","TUBA4A","ASB6","S1PR3","AHNAK","TSR1","CD4","HP1BP3","TMBIM1","TP53INP1","NPM1","SUSD4","TBX3","KCNAB1","SSBP3","SPN","SERBP1","ATP10B","EFCAB2","PTBP1","TLR6","DNAJB1","TFR2","SLC43A3","SLC11A1","TSC22D3","SLC7A1","PPP1R3D","FADS2","B2M","MKNK2","ELAVL3","PDGFRB","ATP8B1","ABCA1","EXOSC6","RNF141","SLC4A8","RPL10A","GAS7","KCNE4","ITGB4","MT2A","HMGB1","NAV2","MSN","HSDL2","ENG","PAQR6","ALPK1","MBP","DDIT4","HSPA1A","RAPH1","UBE2O","PDCD6","ARHGAP24","SH3GL3","RPL39","RNASET2","SLC17A7","ZBTB20","CTDSP1","TUBB","TNXB","RPL35","NT5E","USP4","MMRN2"])

hs_ad_circ_genes = pd.Series(['ADCY1', 'ADCY10', 'ADCY2', 'ADCY3', 'ADCY4', 'ADCY5', 'ADCY6','ADCY7', 'ADCY8', 'ADCY9', 'ADCYAP1', 'ADCYAP1R1', 'BHLHE40','BHLHE41', 'BTRC', 'CACNA1C', 'CACNA1D', 'CACNA1G', 'CACNA1H','CACNA1I', 'CALM1', 'CALM2', 'CALM3', 'CAMK2A', 'CAMK2B', 'CAMK2D','CAMK2G', 'CLOCK', 'CREB1', 'CRY1', 'CRY2', 'CSNK1D', 'CSNK1E','CUL1', 'DBP', 'FBXL3', 'FBXW11', 'FOS', 'GNAI1', 'GNAI2', 'GNAI3','GNAO1', 'GNAQ', 'GNAS', 'GNB1', 'GNB2', 'GNB3', 'GNB4', 'GNB5','GNG11', 'GNG12', 'GNG13', 'GNG2', 'GNG3', 'GNG4', 'GNG5', 'GNG7','GRIA1', 'GRIA2', 'GRIA3', 'GRIA4', 'GRIN1', 'GRIN2A', 'GRIN2B','GRIN2C', 'GRIN2D', 'GUCY1A2', 'GUCY1B1', 'ITPR1', 'ITPR3','KCNJ3', 'KCNJ6', 'KCNJ9', 'MAPK1', 'MAPK3', 'NFIL3', 'NOS1','NOS1AP', 'NPAS2', 'NR1D1', 'NR1D2', 'PER1', 'PER2', 'PER3','PLCB1', 'PLCB2', 'PLCB3', 'PLCB4', 'PRKAA1', 'PRKAA2', 'PRKAB1','PRKAB2', 'PRKACA', 'PRKACB', 'PRKACG', 'PRKAG1', 'PRKAG2','PRKCA', 'PRKCB', 'PRKCG', 'PRKG1', 'PRKG2', 'RBX1', 'RORA','RORB', 'RPS6KA5', 'RYR1', 'RYR2', 'RYR3', 'SKP1'])
hs_ad_circ_reg = pd.Series([-0.14285714,  0.33333333,  0.        , -0.25      ,  1.        ,       -0.14285714,  0.        ,  0.33333333,  0.5       , -0.33333333,       -0.8       ,  0.4       , -0.33333333,  0.33333333, -0.5       ,       -0.33333333,  0.2       , -0.11111111,  0.        ,  0.        ,        0.        , -0.6       , -0.33333333,  0.2       , -1.        ,       -0.6       , -0.2       , -0.33333333,  0.2       ,  1.        ,       -0.33333333,  0.        ,  1.        ,  0.        ,  0.        ,        0.        , -0.33333333,  0.42857143, -0.63636364,  0.        ,        0.4       , -0.66666667,  0.71428571, -0.77777778, -0.25      ,       -0.6       ,  0.5       ,  1.        , -0.14285714,  0.6       ,        1.        ,  0.14285714, -0.5       , -0.33333333, -0.42857143,        0.        ,  0.75      , -0.66666667, -0.42857143,  0.        ,       -1.        , -0.66666667, -0.25      ,  1.        ,  1.        ,        1.        ,  0.        , -1.        , -0.66666667,  1.        ,       -0.71428571, -0.71428571, -0.5       , -0.66666667,  0.        ,        0.        ,  0.        ,  0.5       ,  0.33333333,  1.        ,        0.33333333,  0.8       ,  1.        ,  0.2       , -0.27272727,        0.        ,  1.        ,  0.42857143, -0.33333333, -0.2       ,       -0.42857143, -0.6       , -0.66666667, -0.71428571,  0.33333333,       -0.2       ,  0.        ,  0.        , -0.6       , -0.42857143,        0.16666667,  0.33333333, -1.        ,  0.5       ,  1.        ,        0.81818182,  0.2       , -0.2       ,  0.66666667, -0.55555556])


hs_hd_circ_genes = pd.Series(['ADCY1', 'ADCY3', 'ADCY5', 'ADCYAP1', 'BHLHE40', 'BHLHE41', 'BTRC',       'CACNA1G', 'CACNA1H', 'CALM1', 'CALM3', 'CAMK2D', 'CREB1', 'CRY1',       'CRY2', 'CSNK1D', 'DBP', 'GNAI1', 'GNAI3', 'GNB1', 'GNG11',       'GNG12', 'GNG2', 'GNG3', 'GNG4', 'GNG5', 'GNG7', 'GRIA1', 'GRIA2',       'GRIA4', 'GRIN2A', 'GRIN2B', 'GRIN2D', 'ITPR1', 'KCNJ3', 'KCNJ9',       'NOS1', 'PER1', 'PLCB1', 'PLCB3', 'PLCB4', 'PRKACA', 'PRKCG',       'CALML3', 'RASD1'])
hs_hd_circ_reg = pd.Series([-1.        ,  0.        , -1.        , -1.        ,  0.        ,        1.        ,  0.        , -1.        , -0.5       , -1.        ,       -0.5       ,  0.33333333,  0.        ,  1.        , -1.        ,       -0.33333333, -1.        ,  0.        ,  0.5       ,  0.2       ,        1.        ,  0.33333333, -1.        , -1.        ,  0.        ,        1.        , -1.        , -1.        , -1.        , -1.        ,       -1.        , -1.        , -0.33333333,  0.        ,  0.        ,       -1.        , -1.        ,  1.        , -0.33333333,  1.        ,       -1.        , -1.        , -1.        , -1.        ,  0.        ])


hs_pd_circ_genes = pd.Series(['ADCY1', 'ADCY10', 'ADCY2', 'ADCYAP1', 'BTRC', 'CACNA1G', 'CALM1',       'CALM2', 'CALM3', 'CAMK2B', 'CAMK2D', 'CLOCK', 'CRY2', 'CSNK1D',       'DBP', 'FOS', 'GNAI1', 'GNAI2', 'GNAO1', 'GNAS', 'GNB1', 'GNB5',       'GNG13', 'GNG3', 'GNG4', 'GNG7', 'GRIA3', 'GRIN1', 'GRIN2A',       'GRIN2C', 'KCNJ6', 'NOS1', 'NPAS2', 'PER2', 'PER3', 'PLCB1',       'PLCB2', 'PLCB3', 'PRKACA', 'PRKACB', 'PRKCA', 'PRKG1', 'SKP1',       'GNG8', 'KCNJ5', 'MTNR1B'])
hs_pd_circ_reg = pd.Series([-1.        ,  0.        , -0.33333333, -1.        ,  0.        ,       -1.        ,  0.        ,  0.        , -1.        , -1.        ,       -1.        ,  0.        , -1.        , -1.        ,  0.        ,       -1.        , -1.        ,  0.        , -0.5       , -1.        ,       -1.        , -1.        , -1.        , -1.        , -1.        ,       -1.        , -1.        , -0.5       , -1.        ,  1.        ,       -1.        ,  0.        ,  0.        , -0.33333333,  0.        ,       -1.        , -1.        ,  1.        , -1.        , -0.5       ,       -0.33333333,  0.        ,  0.        , -1.        ,  0.        ,       -1.        ])


hs_als_circ_genes = pd.Series(['ADCY2', 'ADCY3', 'ADCY7', 'CALM2', 'GRIA3'])
hs_als_circ_reg = pd.Series([1., 0., 0., 0., 0.])


mm_1_genes = pd.Series(['ENSMUSG00000000078', 'ENSMUSG00000000184', 'ENSMUSG00000000792',
       'ENSMUSG00000001911', 'ENSMUSG00000001995', 'ENSMUSG00000002012',
       'ENSMUSG00000002881', 'ENSMUSG00000003233', 'ENSMUSG00000003279',
       'ENSMUSG00000003810', 'ENSMUSG00000005087', 'ENSMUSG00000005268',
       'ENSMUSG00000005640', 'ENSMUSG00000005917', 'ENSMUSG00000006930',
       'ENSMUSG00000007617', 'ENSMUSG00000007682', 'ENSMUSG00000010136',
       'ENSMUSG00000010461', 'ENSMUSG00000011256', 'ENSMUSG00000012126',
       'ENSMUSG00000013089', 'ENSMUSG00000013921', 'ENSMUSG00000015970',
       'ENSMUSG00000017446', 'ENSMUSG00000017724', 'ENSMUSG00000018398',
       'ENSMUSG00000018589', 'ENSMUSG00000018819', 'ENSMUSG00000019851',
       'ENSMUSG00000020131', 'ENSMUSG00000020182', 'ENSMUSG00000020227',
       'ENSMUSG00000020330', 'ENSMUSG00000020634', 'ENSMUSG00000021071',
       'ENSMUSG00000021217', 'ENSMUSG00000021256', 'ENSMUSG00000021366',
       'ENSMUSG00000021587', 'ENSMUSG00000021721', 'ENSMUSG00000021743',
       'ENSMUSG00000021936', 'ENSMUSG00000022180', 'ENSMUSG00000022246',
       'ENSMUSG00000022307', 'ENSMUSG00000022342', 'ENSMUSG00000022377',
       'ENSMUSG00000022419', 'ENSMUSG00000022462', 'ENSMUSG00000022514',
       'ENSMUSG00000023017', 'ENSMUSG00000023805', 'ENSMUSG00000023927',
       'ENSMUSG00000023949', 'ENSMUSG00000024427', 'ENSMUSG00000024601',
       'ENSMUSG00000024695', 'ENSMUSG00000024935', 'ENSMUSG00000025188',
       'ENSMUSG00000025404', 'ENSMUSG00000025610', 'ENSMUSG00000026141',
       'ENSMUSG00000026247', 'ENSMUSG00000026414', 'ENSMUSG00000026458',
       'ENSMUSG00000026589', 'ENSMUSG00000026605', 'ENSMUSG00000026643',
       'ENSMUSG00000026830', 'ENSMUSG00000026872', 'ENSMUSG00000026991',
       'ENSMUSG00000027188', 'ENSMUSG00000027318', 'ENSMUSG00000027327',
       'ENSMUSG00000027570', 'ENSMUSG00000027674', 'ENSMUSG00000028004',
       'ENSMUSG00000028399', 'ENSMUSG00000028402', 'ENSMUSG00000028546',
       'ENSMUSG00000028565', 'ENSMUSG00000028631', 'ENSMUSG00000029576',
       'ENSMUSG00000029608', 'ENSMUSG00000029822', 'ENSMUSG00000030108',
       'ENSMUSG00000030199', 'ENSMUSG00000030265', 'ENSMUSG00000030657',
       'ENSMUSG00000030669', 'ENSMUSG00000030775', 'ENSMUSG00000031224',
       'ENSMUSG00000031340', 'ENSMUSG00000031727', 'ENSMUSG00000031841',
       'ENSMUSG00000031962', 'ENSMUSG00000031980', 'ENSMUSG00000032105',
       'ENSMUSG00000032220', 'ENSMUSG00000032530', 'ENSMUSG00000032807',
       'ENSMUSG00000033316', 'ENSMUSG00000033420', 'ENSMUSG00000034107',
       'ENSMUSG00000034185', 'ENSMUSG00000034310', 'ENSMUSG00000034486',
       'ENSMUSG00000034664', 'ENSMUSG00000034684', 'ENSMUSG00000034902',
       'ENSMUSG00000035105', 'ENSMUSG00000035184', 'ENSMUSG00000035202',
       'ENSMUSG00000035357', 'ENSMUSG00000035594', 'ENSMUSG00000035722',
       'ENSMUSG00000035835', 'ENSMUSG00000035873', 'ENSMUSG00000036158',
       'ENSMUSG00000036198', 'ENSMUSG00000036357', 'ENSMUSG00000036502',
       'ENSMUSG00000036699', 'ENSMUSG00000036985', 'ENSMUSG00000037111',
       'ENSMUSG00000037217', 'ENSMUSG00000037239', 'ENSMUSG00000037649',
       'ENSMUSG00000037999', 'ENSMUSG00000038115', 'ENSMUSG00000038248',
       'ENSMUSG00000038331', 'ENSMUSG00000038623', 'ENSMUSG00000038738',
       'ENSMUSG00000038860', 'ENSMUSG00000038932', 'ENSMUSG00000039307',
       'ENSMUSG00000039316', 'ENSMUSG00000039385', 'ENSMUSG00000039809',
       'ENSMUSG00000040105', 'ENSMUSG00000040111', 'ENSMUSG00000040187',
       'ENSMUSG00000040938', 'ENSMUSG00000040998', 'ENSMUSG00000041220',
       'ENSMUSG00000041439', 'ENSMUSG00000041540', 'ENSMUSG00000041670',
       'ENSMUSG00000041911', 'ENSMUSG00000041959', 'ENSMUSG00000042249',
       'ENSMUSG00000042436', 'ENSMUSG00000042596', 'ENSMUSG00000042737',
       'ENSMUSG00000042757', 'ENSMUSG00000043004', 'ENSMUSG00000043587',
       'ENSMUSG00000043648', 'ENSMUSG00000043659', 'ENSMUSG00000043668',
       'ENSMUSG00000043873', 'ENSMUSG00000044201', 'ENSMUSG00000044252',
       'ENSMUSG00000044968', 'ENSMUSG00000045052', 'ENSMUSG00000045094',
       'ENSMUSG00000045215', 'ENSMUSG00000045613', 'ENSMUSG00000045761',
       'ENSMUSG00000045763', 'ENSMUSG00000045994', 'ENSMUSG00000046056',
       'ENSMUSG00000046709', 'ENSMUSG00000047090', 'ENSMUSG00000047446',
       'ENSMUSG00000047507', 'ENSMUSG00000047632', 'ENSMUSG00000047904',
       'ENSMUSG00000049044', 'ENSMUSG00000049420', 'ENSMUSG00000049532',
       'ENSMUSG00000050022', 'ENSMUSG00000050272', 'ENSMUSG00000050534',
       'ENSMUSG00000050640', 'ENSMUSG00000050824', 'ENSMUSG00000050840',
       'ENSMUSG00000051726', 'ENSMUSG00000051920', 'ENSMUSG00000051985',
       'ENSMUSG00000052415', 'ENSMUSG00000052563', 'ENSMUSG00000052921',
       'ENSMUSG00000053004', 'ENSMUSG00000053166', 'ENSMUSG00000053399',
       'ENSMUSG00000053693', 'ENSMUSG00000053783', 'ENSMUSG00000053930',
       'ENSMUSG00000053965', 'ENSMUSG00000054459', 'ENSMUSG00000054808',
       'ENSMUSG00000054934', 'ENSMUSG00000055632', 'ENSMUSG00000055805',
       'ENSMUSG00000056211', 'ENSMUSG00000056222', 'ENSMUSG00000056306',
       'ENSMUSG00000057729', 'ENSMUSG00000058488', 'ENSMUSG00000060044',
       'ENSMUSG00000061702', 'ENSMUSG00000061731', 'ENSMUSG00000062257',
       'ENSMUSG00000062563', 'ENSMUSG00000062778', 'ENSMUSG00000062866',
       'ENSMUSG00000063535', 'ENSMUSG00000063600', 'ENSMUSG00000063873',
       'ENSMUSG00000066235', 'ENSMUSG00000066652', 'ENSMUSG00000067594',
       'ENSMUSG00000067928', 'ENSMUSG00000070565', 'ENSMUSG00000070867',
       'ENSMUSG00000073771', 'ENSMUSG00000074227', 'ENSMUSG00000074625',
       'ENSMUSG00000074657', 'ENSMUSG00000074796', 'ENSMUSG00000074802',
       'ENSMUSG00000075324', 'ENSMUSG00000079056', 'ENSMUSG00000079157',
       'ENSMUSG00000079654', 'ENSMUSG00000089824', 'ENSMUSG00000091002',
       'ENSMUSG00000091387', 'ENSMUSG00000096351', 'ENSMUSG00000098132',
       'ENSMUSG00000115338'])

mm_1_reg = pd.Series([-0.50291888, -0.74438336, -0.72220667, -0.66955592, -0.50821837,
        0.41905522, -0.44313907, -0.27827641, -0.89714114, -0.25263468,
        0.9867025 ,  1.30421608,  1.48952124, -1.20968552,  0.69386376,
       -0.47546798, -0.56302434,  1.55232363, -0.85984461, -0.63635772,
        0.58437562, -0.43369808, -0.36556154, -0.44081614, -1.25846878,
       -0.64225824, -0.40490907, -0.75323791, -1.1172244 ,  0.67749527,
        0.6713831 ,  0.66010267,  0.91829501, -2.05102504, -0.32309355,
       -0.30713263, -0.54957921, -0.73994273, -0.75726473, -0.73437554,
       -0.71294794, -1.03468521, -0.476328  , -0.2431017 , -0.99485058,
       -0.65743281, -0.43124669, -0.32080246, -0.48065876, -0.4138469 ,
       -0.41633927,  0.18705994, -0.96611712, -0.67981597, -1.40968974,
       -0.65017362,  0.43479893, -0.20027031, -0.35925478,  0.42388746,
       -0.43007463, -1.49923249, -0.82266967,  0.67304547,  0.73191747,
        0.45306032, -0.9699245 , -1.08109222, -0.48570652, -0.36361824,
       -0.74134017, -0.24637784, -0.68989211, -1.2266243 ,  0.48925436,
        0.43197897, -0.60815135,  1.06122031, -0.48615221, -0.72365786,
       -0.90292785, -0.63732048, -0.94120252,  0.29611296, -1.02371045,
       -0.49968784,  0.52466473, -0.32277061, -0.4103447 , -0.83688526,
       -0.92650823,  0.98708816,  0.43510571,  1.22478769, -1.42018594,
       -0.33205324,  0.57978498,  0.6421382 ,  0.83808514, -0.51220463,
       -1.18963103, -1.94940984, -1.39890015, -0.52902497,  0.81927498,
        3.1071107 , -0.66389498,  1.01469982,  0.62522289,  0.76115321,
       -0.3624919 , -1.0500517 , -0.40471832,  0.87298816, -1.05572532,
       -1.60554216, -0.60187589,  0.35994534, -1.27692757, -0.47765904,
        2.42289572,  2.09256827,  0.76420158,  0.43896485, -0.26726486,
       -0.26768822, -0.50189943, -0.39980645,  0.37643932, -0.31792551,
        0.9916116 , -0.71062514, -1.51712238, -0.5656233 , -0.77469753,
       -0.76218289,  1.1542766 ,  0.29656812, -0.68789724, -0.69246583,
       -0.63405117, -0.33600847, -0.32598127, -0.41843155,  0.61290265,
       -0.82888157, -0.24281351, -0.41769294, -0.99539677, -0.60283267,
       -0.54309016, -0.59726971, -0.70273561, -1.6065544 , -0.02435915,
        0.51938425, -0.71259694, -0.68325886,  0.39814732,  0.67552858,
       -1.26826249, -0.57254722,  1.12273512, -2.38043691, -0.49424885,
       -0.45905321,  1.0760824 , -0.71491679, -0.8532414 , -0.49380482,
        0.50500794, -0.75195821, -0.49025511,  0.56919437, -0.42762806,
        0.53241669,  0.53009601,  0.77969485,  0.56337962, -0.70776878,
       -0.37158814, -0.82233531,  0.40717688,  0.39492774, -0.7245623 ,
       -1.34961558, -0.54548604,  1.58908269, -0.33193123, -0.48567617,
       -1.49325129, -1.66136415, -0.37262188, -0.62374732,  0.48222319,
       -0.40861704,  0.38398981,  1.68488716, -0.79433984, -1.42074128,
       -0.96046947, -0.74834668, -0.7357383 , -0.22582849, -0.63554575,
        0.77983357, -0.55379122, -0.46607884, -0.42475129, -0.86031364,
        0.74736945,  0.91794585,  1.33612015,  0.49672102, -0.76266311,
       -0.62527922, -0.77304133,  0.70765501, -0.62532583, -0.65779173,
       -0.50119015, -0.78207386,  0.29723782, -2.491874  ,  1.12668147,
       -0.39634166, -0.51729363, -1.38957617,  0.45508904,  0.63300174,
        1.05433319, -0.44774784,  0.9597889 , -0.84357957, -0.40474554,
       -0.50268237, -0.90048662,  0.87419044,  0.27216097,  0.8337613 ,
       -0.50179589,  0.681127  ,  1.51452502,  0.43383037])