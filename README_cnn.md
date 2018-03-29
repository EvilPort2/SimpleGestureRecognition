# Simple Gesture Recognition using Convolutional Neural Network
Motion gesture recognition using Convolutional Neural Network

## Outcome
Look <a href="https://youtu.be/pNvlsXe6Zn4">here</a> and <a href="https://youtu.be/YUM57Uc8Spo">here</a>.

## Dataset used
For this project I used the EMNIST (Extended MNIST) dataset. It is freely available on the Internet. You should read about it here <a href="https://arxiv.org/pdf/1702.05373.pdf">https://arxiv.org/pdf/1702.05373.pdf</a>. If you want to download the original dataset click <a href="https://cloudstor.aarnet.edu.au/plus/index.php/s/54h3OuGJhFLwAlQ/download">here</a>.<br>
For this project I am using only the 'letters' dataset.

## Requirements
1. Python 3.x
2. Keras with Tensorflow as backend
3. OpenCV 3.4
4. h5py
5. Jupyter-Notebook (to view and train_model.ipynb and store_images.ipynb)
6. pyautogui
7. A good CPU
8. A good GPU (not compulsory but recommended)
9. Patience. A lot of it......

## What I am doing here
1. If you see the videos you will see that I am wearing a purple thingy in my finger. It is just a white paper painted purple. I am using color segmentation to separate the purple paper from everything in the frame. Indirectly, this means I am tracking the movement of my finger. 
2. The movement is recorded. The parts where the finger moved is represented by the white lines in the black part of the 'img' window, which I like to call 'blackboard'.
3. So the movement of the finger is now converted into a black and white image.
4. This black and white image is then processed so that it can be fed to the neural network (which I have trained myself) for prediction. The neural network has an acuuracy of ~94%.
5. Based on the prediction a specific action is taken.

## Significance of the files
1. <b>train_model.ipynb</b> - This is a ipython notebook so you need jupyter-notebook installed to use this file. Use this file if you want to retrain the model.
2. <b>store_images.ipynb</b> - This is a ipython notebook so you need jupyter-notebook installed to use this file. Use this file if you want to see how the pictures in the training dataset looks like. The files will be stored in a newly created folder called 'emnist_dataset'.
3. <b>webcam_video_stream.py</b> - This file contains a class called WebcamVideoStream. It's job is to send frames from the webcam source to the program that is calling it. It uses thread to minimize latency when it is called. It is mainly called by the gesture_action_cnn.py file.
4. <b>action.py</b> - This file stores the actions that need to be taken by a specific gesture.
5. <b>range-detector.py</b> - This file is used to set the HSV color range. The easiest way to use it is to put the yellow paper in front of the camera and then slowly increasing the lower parameters(H_MIN, V_MIN, S_MIN) one by one and then slowly decreasing the upper parameters (H_MAX, V_MAX, S_MAX). When the adjusting has been done you will find that only the yellow paper will have a corresponding white patch and rest of the image will be dark. 
	
		python range-detector.py -f HSV -w

6. <b>cnn_model_keras21.h5</b> - This is the trained model.
7. <b>gesture_action_cnn</b> - This is the file that you need to use to run this project. The trained neural network is loaded and then it is used for prediction. It calls the do_action() of action.py to take a specific action for a gesture. It has 3 modes of usage:-
	1. <i>Doodle / None </i> - This is the simplest mode. Nothing really happens here. You can create doodles here. This is the default mode.
	2. <i>typing</i> - This mode is specially used with some other text editor. Make sure that the text editor is the current focussed window. The letters made by moving your finger is directly typed into the text editor. Press 't' to come to this mode.
	3. <i>keyboard_shortcut</i> - This is my favourite mode. So here you make a letter of the English alphabet, and corresponding to the alphabet a keyboard shortcut is emulated if there is any. There are 15 keyboard shortcuts programmed. Press 's' to get into this mode. The shortcuts are discussed later.

			python gesture_action_cnn.py
		
## How to use this project
1. First set the HSV masking range for the paper that you are wearing in your finger. To do that run this file	
			
		python range-detector.py -f HSV -w
The easiest way to use it is to put the yellow paper in front of the camera and then slowly increasing the lower parameters(H_MIN, V_MIN, S_MIN) one by one and then slowly decreasing the upper parameters (H_MAX, V_MAX, S_MAX). When the adjusting has been done you will find that only the yellow paper will have a corresponding white patch and rest of the image will be dark. 
2. Now run the gesture_action_cnn file.
		
		python gesture_action_cnn.py

## Keyboard Shortcuts
1. A = Ctrl + A (Select all)
2. C = Ctrl + C (Copy)
3. E = Open Explorer
4. F = Open Facebook
5. L = Win + L (Lock the computer)
6. M = Win (Start Menu)
7. N = Ctrl + N (New File)
8. O = Take a screenshot
9. P = Take a photo with a 5 sec delay
10. R = Win + R (Open Run dialog)
11. S = Ctrl + S (Save file)
12. T = Ctrl + Shift + T (Open Task Manager)
13. V = Ctrl + V (Paste)
14. X = Ctrl + X (Cut)
15. Z = Ctrl + Z (Undo)
