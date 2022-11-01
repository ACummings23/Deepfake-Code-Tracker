####Andrew Cummings####

###this file was used to feed in .mp4 files from our input data and generate all .wav waves to be used in the models, as well as their labels
###inputs are required on line 34 and line 62 to switch input data classes
###using the metadata and .wav files generated from this file, we can easily split our model inputs by calling through the .wav files' locations stored in our new metadata
import random
import pathlib
import itertools
import collections
import os
import cv2
import numpy as np
import imageio
from IPython import display
from urllib import request 
import moviepy.editor as mp
from collections import Counter
import pandas as pd



#load attached metadata file that contains category of each mp4 file,file location,file name, file id
####A>Real Video Real Audio
####B>Real Video Fake Audio
####C>Fake Video Real Audio
####D>Fake Video Fake Audio
metaDataList=pd.read_csv("//code//dataset//FakeAVCeleb//meta_data.csv")
labelDataList=metaDataList
#set labels for audio
labelDataList=metaDataList
labelDataList['Audio_Label']=''
labelDataList['Video_Label']=''
for i in range(0,len(metaDataList)):
    if (metaDataList['category'][i]=='A'):
        labelDataList['Audio_Label'][i]=0
        labelDataList['Video_Label'][i]=0
    if (metaDataList['category'][i]=='C'):
        labelDataList['Audio_Label'][i]=0
        labelDataList['Video_Label'][i]=1
    if (metaDataList['category'][i]=='B'):
        labelDataList['Audio_Label'][i]=1
        labelDataList['Video_Label'][i]=0
    else:
        labelDataList['Audio_Label'][i]=1
        labelDataList['Video_Label'][i]=1
        
labelDataList['wavLocation']=''
labelDataList['fullPath']='/code/dataset/'+labelDataList['Unnamed: 9']+'/'+labelDataList['path']
#create new columns to be attach address of wavLocation, and create new column that merges two columns to get the complete path that our wavwriter function will access     
labelDataList['wavLocation']=''
labelDataList['fullPath']='/code/dataset/'+labelDataList['Unnamed: 9']+'/'+labelDataList['path']

###### wavewriter function
#requires input file location, output file location, and name of file
def wavWriterSINGLE(inputDirectory,outputLocation,FileName):
    clip=mp.VideoFileClip(inputDirectory)
    clip.audio.write_audiofile(outputLocation+FileName+".wav")

###### subset of data 
####A>Real Video Real Audio
####B>Real Video Fake Audio
####C>Fake Video Real Audio
####D>Fake Video Fake Audio
#for sake of timeouts hit while computing, each of the 4 classes of input data are processed separately
testSub=labelDataList[labelDataList['category']=='C']#change 'C' to any of the four letters to generate files and metadata
testSub=testSub.sort_values(by='source')
testSub=testSub.reset_index(drop=True)

#### .wav creation loop #####
#generate the output file,and add output files location back into metadata
for i in range(0,len(testSub)):
    wavFileOutput='/code/dataset/'+testSub['Unnamed: 9'][i]+'/'
    wavWriterSINGLE(testSub['fullPath'][i],wavFileOutput,testSub['path'][i])
    testSub['wavLocation'][i]=wavFileOutput+testSub['path'][i]+'.wav'

####output metadata to CSV
testSub.to_csv('/code/dataset/CDir.csv') #change name of metadata file generated to 'ADir',etc. for each of the four types of data inputted
