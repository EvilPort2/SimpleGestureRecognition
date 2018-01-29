# Simple Gesture Recognition
A very simple gesture recognition technique using opencv and python

# Outcome
Before going on into much details and wasting your time just watch this video to get an idea of what I have done. Here is the <a href = "https://www.youtube.com/watch?v=qFmtNNxpsvk">first video and <a href = "https://www.youtube.com/watch?v=DRL9zuB1g6A">the second one</a>. Watch and also follow me :p

# What have I done
Since I am wearing a yellow cap in my fingers, I use that to segment the yellow colour which makes it a lot easier to get the gesture. Here are the steps that I have followed:<br>

1. Take one frame at a time and convert it from RGB colour space to HSV colour space for better yellow colour segmentation.<br>
2. Use a mask for yellow colour.<br>
3. Bluring and thresholding.<br>
4. If a yellow colour is found and it crosses a reasonable threshold, we start to create a gesture.<br>
5. The direction of movement of the yellow cap is calculated by taking the difference between the old center and the new center of the yellow colour after every 5th iteration.<br>
6. The directions are taken and stored in a list until the yellow cap disappears from the frame.<br>
7. The direction list is processed and the processed direction list is used to take a certain action.<br>

# Gestures that I have right now
1. Square - Start menu<br>
2. Cross - Close<br>
3. C - Copy<br>
4. A - Select all<br>
5. N - Create new file<br>
6. V - Paste<br>
7. L - Lock the computer<br>
8. T - Display task manager<br>
9. \> - Alt+tab<br>
10. < - Alt+Shift+Tab<br>
11. <> - Take a photo
12. [] - Screenshot
13. Square and line - Open text editor

# Prerequisites
1. Since I am using threads in the program the first thing you need to do is go to the site mentioned and apply the solution given. Here is the website https://stackoverflow.com/questions/36809788/importerror-no-module-named-thread<br>
2. You need additional imutils functionalities. These can be found here https://github.com/jrosebr1/imutils.<br>

# Usage
First run the range-detector.py to set the range for the mask for colour segmentation and then press q when the perfect range is found. The easiest way to use it is to put the yellow paper in front of the camera and then slowly increasing the lower parameters(H_MIN, V_MIN, S_MIN) one by one and then slowly decreasing the upper parameters (H_MAX, V_MAX, S_MAX). When the adjusting has been done you will find that only the yellow paper will have a corresponding white patch and rest of the image will be dark. Then start the gesture_action.py. No need to change anything in the gesture_action.py file.

    python3 range-detector.py -f HSV -w
    python3 gesture_action.py

# Got a question?
If you have any questions that are bothering you please contact me on my <a href = "facebook.com/dibakar.saha.750">facebook profile</a>. Just do not ask me questions like where do I live, who do I work for etc. Also no questions like what does this line do. If you think a line is redundant or can be removed to make the program better then you can obviously ask me or make a pull request.
