#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import psycopg2
import sys
import regex
import os
import shutil
from pathlib import Path

with open('credentials.txt', 'r') as f:
    host, port, database, user, password = f.readline().split('::')


def get_paths(host, port, database, user, password):
    query = '''select "Name","Directory" from public."File"
                where "Type_ID"=4'''
    try:
        with psycopg2.connect(dbname=database, user=user,
                              password=password, host=host, port=port) as conn:
            with conn.cursor() as curs:
                curs.execute(query)
                selected = curs.fetchall()
                print(f'selected {len(selected)} records')
    except psycopg2.DatabaseError as db_error:
        print(db_error)
        sys.exit(1)

    return selected

selected = get_paths(host, port, database, user, password)
selected[:2]
select = pd.DataFrame.from_records(selected)


def extract_iid(row):
    return regex.findall(r'^[0-9]{3,8}',row)[0]


select['IID'] = select[0].apply(extract_iid)
df = pd.read_csv('cases.csv')
df['IID'] = df['IID'].apply(str)
merged = df.merge(select, how='left', on='IID')
dff = merged[merged[1].notna()]
dff_ = dff.iloc[:2, :]
dff_
dest = dff.iloc[2:, ]

def creator(row):
    base_dir = '/core-pool/tmp/school'
    iid = row['IID']
    location = row[1]
    enid = row['Запуск']
    name = row[0]
    Path(f'{base_dir}/{enid}/{iid}').mkdir(parents=True, exist_ok=True)
    shutil.copy2('/mnt'+location[13:], f'{base_dir}/{enid}/{iid}/{name}')
    print(f'success copy {name}')


dest.apply(creator, axis=1)

# os.mkdir('/core-pool/tmp/school/100041')
# import subprocess
# subprocess.call('cd /core-pool/tmp/school', shell=True)
# subprocess.call('mkdir 100041', shell=True)




