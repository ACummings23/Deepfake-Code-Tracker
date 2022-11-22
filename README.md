#Deepfake Audio Project Description

The goal of this project is to create a convolutional neural network model for detecting deepfake audio and to achieve the following learning outcomes:<br />
-learn how to build and modify a CNN for performance <br />
-familiarize myself with pytorch environment and tensor datatype<br />
-learn how to use WWT remote server environments <br />
-learn various techniques for image/audio classification data augmentation<br />

Work Description:<br />
-for this project, I identified the fakeCeleb dataset https://arxiv.org/abs/2108.05080 as the main dataset source. This set has ~20,000 fake and real videos and was chosen because of popularity in field and valuable metadata(race,gender included). In the next phase of this project, the video aspect of this data will be important as I aim to combine Deepfake video detection with audio detection
-I then spent time to understand how to extract the audio files from these videos and then turn them into .wav files, turning the problem into image classification<br />
-I selected two models to train the data on, one custom CNN in pytorch and then a pretrained EfficientNet model<br />
-Once initial models had been trained, I achieved 90% accuracy with the custom CNN and 99% accuracy with the pretrained effNet <br />
-Consulting with Mayank and Sai, I went back and modified the training and validation sets, making sure for the first iteration that the model had new voices for the validation set<br />
-I retrained the models and decided that F2 score will be my metric to maximize because this score weights recall heavier than precision, which is ideal because conceptually I want as few deepfakes being labels as real as possible <br />
-I implemented data augmentations such as masking and then modified the CNN to be less complex and include dropout, getting an F2 accuracy of .91<br />

Challenges:
-my current implementation of the CNN makes it difficult to change the threshold for classifying the labels of the output, although the classes are balanced I would like to be sure that I am maximizing the F2 score with the correct threshold <br />
-I would like to include more data augmentations, however its taking taking more time than expected to understand how to optmize the hyperparameters with each new augmentation to improve model performance<br />




# Deepfake-Code-Tracker
Repo containing scripts I wrote during Deepfake Audio Project-Will update weekly with new code <br />
last updated-(11/22/2022)<br />
new files:<br />
-pytorchCNN-main file used for current model<br />
-validationSet-file showing several validation splits used throughout project<br />
-training and validation data-most recent iteration of validation and training sets in.csv format used in models<br />
-efficientNetB2-model updated with #2 validation data split: further iteration on this model not used as pretrained accuracy unaffected by any dataset change(99%)<br />
# Deepfake
