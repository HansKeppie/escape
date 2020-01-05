# Fortnite Escape Room

This is a simple tool for running a fortnite escape room.

There is a page (admin.html) to manage the escape room from the control room.

There is a page (room.html) that should be running on a screen inside the escape room.

There is a small python script (escapeserver.py) that should be running on a computer on the same network.


## Steps

1. Build the 'escape' conda environment: conda env create -f environment.yml

1. Activate the conda environment: source activate escape

1. Start the python script: python escapeserver.py

1. Now open the room.html page on a computer with screen inside the escape room.

1. Fill in the correct IP address of the server, press 'Full Screen' and 'Start'.

1. Now open the admin.html page on a computer in the control room.

1. Fill in the correct IP address of the server.

1. Fill in the time for the escape room.

1. When the team is ready and inside the room, press start.

1. The clock will be running.

1. From the admin.html page, you can give hints (typ text + enter).

1. From the admin.html page, you can play some sound (Shield, Chest, Dance).

1. From the admin.html page, you can declare victory.

1. From the admin.html page, you can give sanctions (-1 minute, -5 minutes).

1. From the admin.html page, you can stop the clock (to be able to restart).



## Camera

We've always used a separate camera channel using a surveillance IP Camera and a separate phone or tablet.

But you can also use two phones, connect them using skype over wifi.
Make sure the camera and microphone is active on the phone inside the room.
You should deactivate the camera and microphone on the phone inside the control room.
Simply unmute the microphone when you want to give hints.  


## Have fun!
