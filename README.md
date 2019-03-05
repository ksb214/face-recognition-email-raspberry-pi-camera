# Recognise face of visitor with Raspberry Pi and receive email alert

Camera records images constantly and then passes it to the OpenCV for face recognition. 
Once it recognizes a face in the image, it sends alert to the email address with the image in the attachment. 
You can modify this code further to include any other object recognition such as cat etc.

You can download the code which uses OpenCV 2.4.9 from here. Before you use it, you need to generate a password for 
the app from Gmail.

Gmail provides the following guidelines to generate the app password for emailing directly from Raspberry Pi. 
Use “other” option to generate the password for the app to login to Gmail and send an email.
