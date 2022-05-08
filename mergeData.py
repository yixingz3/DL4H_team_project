#!/usr/bin/env python3

from csv import DictReader, reader
from fileinput import nextfile
import re
import csv
import pandas as pd

def GetSymptoms():

    ''' 
    due to the sensitivity of the MIMIC-III dataset
    we won't include it in the repo
    please obtain access and refer to NOTEEVENTS.csv and DIAGNOSES_ICD.csv
    as the original input of this script
    '''
    inputFile = 'data/NOTEEVENTS.csv'
    with open(inputFile, 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        column_names = csv_dict_reader.fieldnames

        csv_file = "noteEventsResult.csv"
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = column_names)
                writer.writeheader()

                for i, row in enumerate(csv_dict_reader):
                    if (row['TEXT']):
                        s = row['TEXT'].lower().strip().split('\n')
                        start = 'chief complaint:'

                        for j, line in enumerate(s):
                            if line.startswith(start) and row['CATEGORY'] == 'Discharge summary':
                                row['TEXT'] = s[j + 1]
                                writer.writerow(row)
        
        except IOError:
            print("I/O error")

def mergeColsAllSeq():
    filteredEventNotes = pd.read_csv('noteEventsResult.csv')
    disgnosesWithICD = pd.read_csv('data/DIAGNOSES_ICD.csv')

    mergedData = pd.merge(filteredEventNotes, disgnosesWithICD, 
                    on=['SUBJECT_ID', 'HADM_ID'], 
                    how='inner')

    df = pd.DataFrame(mergedData)

    ''' 
    the processed sample dataset can be found in the google drive
    with only @illinois access to protect the data
    '''
    outputFile = 'mergedDatasetAllSeq.csv'
    df.to_csv(outputFile, encoding='utf-8', index = False)

def mergeColsFirstSeq():
    filteredEventNotes = pd.read_csv('noteEventsResult.csv')
    disgnosesWithICD = pd.read_csv('data/DIAGNOSES_ICD.csv')

    mergedData = pd.merge(filteredEventNotes, disgnosesWithICD[disgnosesWithICD["SEQ_NUM"] == 1], 
                    on=['SUBJECT_ID', 'HADM_ID'], 
                    how='inner')

    df = pd.DataFrame(mergedData)

    ''' 
    the processed sample dataset can be found in the google drive
    with only @illinois access to protect the data
    '''
    outputFile = 'mergedDatasetFirstSeq.csv'
    df.to_csv(outputFile, encoding='utf-8', index = False)

'''
run the two following functions in sequence to produce our processed dataset
due to the missing third column that maps the SEQ_NUM
we are not able to make this processed dataset sensible for 
training and evaluating the model
'''

# GetSymptoms()
# mergeColsAllSeq()
# mergeColsFirstSeq()