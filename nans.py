#!/usr/bin/env python
# coding: utf-8


import shutil
from pathlib import Path



lst = [(18565,'/storage-pool/storage/ngs-data/NextSeq/fastq/220617_NB551260_0078_AHFNWVAFX3/Panel/18565/18565_S32_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/fastq/220617_NB551260_0078_AHFNWVAFX3/Panel/18565/18565_S32_R2_001.fastq.gz'),
(18609,'/storage-pool/storage/ngs-data/NextSeq/fastq/220617_NB551260_0078_AHFNWVAFX3/Panel/18609/18609_S46_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/fastq/220617_NB551260_0078_AHFNWVAFX3/Panel/18609/18609_S46_R2_001.fastq.gz'),
(18430,'/storage-pool/storage/ngs-data/NextSeq/fastq/220506_NB551260_0077_AHFTTMAFX3/Panel/18430/18430_S39_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/fastq/220506_NB551260_0077_AHFTTMAFX3/Panel/18430/18430_S39_R2_001.fastq.gz'),
(18461, '/storage-pool/storage/ngs-data/NextSeq/fastq/220617_NB551260_0078_AHFNWVAFX3/Panel/18461/18461_S86_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/fastq/220617_NB551260_0078_AHFNWVAFX3/Panel/18461/18461_S86_R2_001.fastq.gz'),
(18462, '/storage-pool/storage/ngs-data/NextSeq/fastq/220617_NB551260_0078_AHFNWVAFX3/Panel/18462/18462_S3_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/fastq/220617_NB551260_0078_AHFNWVAFX3/Panel/18462/18462_S3_R2_001.fastq.gz'),
(16639,'/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16639/16639_S5_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16639/16639_S5_R2_001.fastq.gz'),
(16685,'/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16685/16685_S11_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16685/16685_S11_R2_001.fastq.gz'),
(16617,'/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16617/16617_S1_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16617/16617_S1_R2_001.fastq.gz'),
(16627,'/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16627/16627_S3_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16627/16627_S3_R2_001.fastq.gz'),
(17953,'/storage-pool/storage/ngs-data/NovaSeq/fastq/220315_A01642_0008_AHN5MJDRXY/17953/17953_S24_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NovaSeq/fastq/220315_A01642_0008_AHN5MJDRXY/17953/17953_S24_R2_001.fastq.gz'),
(17651,'/storage-pool/storage/ngs-data/NovaSeq/fastq/220602_A01642_0012_BH5CTFDMXY/WES/17651/17651_S7_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NovaSeq/fastq/220602_A01642_0012_BH5CTFDMXY/WES/17651/17651_S7_R2_001.fastq.gz'),
(17772,'/storage-pool/storage/ngs-data/NovaSeq/fastq/220315_A01642_0008_AHN5MJDRXY/17772/17772_S7_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NovaSeq/fastq/220315_A01642_0008_AHN5MJDRXY/17772/17772_S7_R2_001.fastq.gz'),
(16646,'/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16646/16646_S7_R1_001.fastq.gz','/storage-pool/storage/ngs-data/NextSeq/runs/100026-100029-concat/16646/16646_S7_R2_001.fastq.gz')]

for item in lst:
    base_dir = '/core-pool/tmp/summer-school'
    iid = str(item[0])
    location_1 = item[1].replace('storage-pool','mnt')
    location_2 = item[2].replace('storage-pool', 'mnt')
    name_1 = item[1].split('/')[-1]
    name_2 = item[2].split('/')[-1]
    Path(f'{base_dir}/{iid}').mkdir(parents=True, exist_ok=True)
    shutil.copy2(location_1, f'{base_dir}/{iid}/{name_1}')
    print(f'success copy {name_1}')
    shutil.copy2(location_2, f'{base_dir}/{iid}/{name_2}')
    print(f'success copy {name_2}')