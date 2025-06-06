# BRA-Dataset

BRA-Dataset is a dataset about the animals that most suffer accidents on Brazilian highways. 
It has 5 classes of medium and large animals, with 1823 imagens. It is free and open-source.

## NEWS

Data Augmentation script with geometric transformations 


Tutorial for COCO format conversion

## Metrics achieved:

## Technical features:

1823 Images Total

2060 Labels Total

Classes:

Tapir----------------------------------------------> 403 Images / 478 Labels


Jaguarundi-----------------------------------------> 311 Images / 341 Labels


Maned Wolf-----------------------------------------> 340 Images / 410 Labels


Puma-----------------------------------------------> 476 Images / 495 Labels


Giant Anteater-------------------------------------> 293 Images / 336 Labels

## Convert darknet format for COCO format

clone the repository YOLO2COCO

With the diretory struture

<code>Dataset
---images
---labels
---class.names
---gen_config.data
---train.txt
---valid.txt</code>

execute the command in YOLO2COCO folder: python darknet2coco.py --data_path ../Dataset/gen_config.data

## Download BRA-DATASET or BRA-DATASET with geometric transformations data augmentation
link: https://mega.nz/folder/ilJilJqB#y-OyAryhoH5H8skaJJg2RQ

## Videos for test your detector

https://mega.nz/file/3xREFRrJ#pAmxuOanRehFlo75LUAfBokq2huZ22jUfcuPRFNQ5ow - For Tapir Class with oclusion problem

https://mega.nz/file/PhhFhSgQ#1NScqSqNIOcpWgE7JR_ntbogw-b7ecKdle0mn6PRSjI - For Giant Anteater with small object and camouflage

## About

This project is a master's project in computer science and computational mathematics at the University of São Paulo - Brazil (PPG-CCMC, ICMC-USP)

#### Authors: Gabriel Souto Ferrante
#### Paper: Brazilian Road Animals (BRA): An Image Dataset of Most Commonly Run Over Animals | DOI: 10.1109/SIBGRAPI55357.2022.9991774
