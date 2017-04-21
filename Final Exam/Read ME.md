<img src="extra/cover.jpg" alt="alt text" align="middle"/>
<p align="center"><i>Does Weather Affect the Stock Market? </i></p>

## Table of Contents
1. [Idea](#1-Idea)
2. [Data Collection](#2-Data-Collection)
3. [Data Storing](#3-Data-Storing)
4. [Analysis 1](#4-Analysis-1)
5. [Analysis 2](#5-Analysis-2)
6. [Analysis 3](#6-Analysis-3)
7. [References](#7-references)

## 1 Motivation
Human facial expressions can be easily classified into 7 basic emotions: happy, sad, surprise, fear, anger, disgust, and neutral. Our facial emotions are expressed through activation of specific sets of facial muscles. These sometimes subtle, yet complex, signals in an expression often contain an abundant amount of information about our state of mind. Through facial emotion recognition, we are able to measure the effects that content and services have on the audience/users through an easy and low-cost procedure. For example, retailers may use these metrics to evaluate __customer interest__. Healthcare providers can provide better service by using additional information about __patients' emotional state__ during treatment. Entertainment producers can monitor __audience engagement__ in events to consistently create desired content.

> __“2016 is the year when machines learn to grasp human emotions”__
--Andrew Moore, the dean of computer science at Carnegie Mellon.

Humans are well-trained in reading the emotions of others, in fact, at just 14 months old, babies can already tell the difference between happy and sad. __But can computers do a better job than us in accessing emotional states?__ To answer the question, I designed a deep learning neural network that gives machines the ability to make inferences about our emotional states. In other words, I give them eyes to see what we can see.

## 2 The Database
The dataset I used for training the model is from a Kaggle Facial Expression Recognition Challenge a few years back (FER2013). It comprises a total of __35887 pre-cropped, 48-by-48-pixel grayscale images__ of faces each labeled with one of the 7 emotion classes: anger, disgust, fear, happiness, sadness, surprise, and neutral.

<p align="center">
<img src="https://github.com/JostineHo/mememoji/blob/master/figures/fer2013.png" width="500" align="middle"/>
<h4 align="center">Figure 1. An overview of FER2013.</h4>
</p>

As I was exploring the dataset, I discovered an imbalance of the “disgust” class (only 113 samples) compared to many samples of other classes. I decided to merge disgust into anger given that they both represent similar sentiment. To prevent data leakage, I built a data generator [fer2013datagen.py](https://github.com/JostineHo/mememoji/blob/master/src/fer2013datagen.py) that can easily separate training and hold-out set to different files. I used 28709 labeled faces as the training set and held out the remaining two test sets (3589/set) for after-training validation. The resulting is a __6-class, balanced dataset__, shown in Figure 2, that contains angry, fear, happy, sad, surprise, and neutral. Now we’re ready to train.

<img src="https://github.com/JostineHo/mememoji/blob/master/figures/trainval_distribution.png" alt="alt text" align="middle"/>
<h4 align="center">Figure 2. Training and validation data distribution.</h4>
