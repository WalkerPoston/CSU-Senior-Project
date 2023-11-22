Pi Tag
======
- **Date:** November 21, 2023
- **Name:** Walker Poston
- **Major:** Cybersecurity
- **Degree:** BS
- **Advisor:** Dr. Hayes

---------------------
### Table of Contents
- [Statement of Purpose](#statement-of-purpose)
- [Research and Background](#research-and-background)
- [Project Language(s), Software, and Hardware](#project-languages-software-and-hardware)
- [Project Requirements](#project-requirements)
- [Project Implementation Description and Explanation](#project-implementation-description-and-explanation)
- [Test Plan](#test-plan)
- [Test Results](#test-results)
- [Challenges Overcome](#challenges-overcome)
- [Future Enhancements](#future-enhancements)

----------------------------
### Statement of Purpose ###

Theft is a major problem that plagues society and many businesses, resulting in millions lost every year. Many businesses have come to accept that some of the products they sell will be stolen and have included that loss in their budgets as "shrink" or "shrinkage". To reduce the amount of shrinkage, these businesses could invest in something that they could use to recover stolen goods. With the "PI Tag," these businesses would be able to track, locate, and recover stolen products and reduce the amount of shrinkage in their business. 

-------------------------------
### Research and Background ###

I didn't have much background in GPS tracking before deciding to do it for my senior project, so I had to do a lot of research to find sources on the subject. While researching for sources, I found the site that I would ultimately use to help me complete my project. Click [here](https://sparklers-the-makers.github.io/blog/robotics/realtime-gps-tracker-with-raspberry-pi/) to view the site. The site has instructions on how to configure the Raspberry Pi with the GPS module so it can receive GPS coordinates. The site also included all of the hardware and software that I would need to get it working, including some of the HTML code for the webpage. After completing that part of the project, the next thing I had to do was figure out how to make a webserver that would host the project. I ended up researching and using Python Flask for my webserver. At the time I didn't have any knowledge of how to make a webserver so I just followed along with the tutorial that Flask has. Click [here](https://flask.palletsprojects.com/en/2.3.x/) to see that tutorial. This tutorial has you set up a blog server so I followed along with it to see if I could use anything from it. 
<br>
One of the most important things I had to figure out was adding a database that would store the GPS coordinates. While researching for databases I could use I found MongoDB and a guide to setting it up to work with my Flask server. The site ultimately didn't work out and I had to go back to the drawing board. While in a meeting with Dr. Hayes, he found a site that better explained how to set up MongoDB with a Flask application. Click [here](https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application#step-1-setting-up-pymongo-and-flask) to visit the site. I used this site to help me with the initial setup and then changed it to work with my project. Once the Raspberry Pi sends a GPS coordinate to the server, the server takes the coordinate and stores it in the database. 
<br> 
Before the server was able to receive GPS coordinates from the Raspberry Pi, I had to figure out how to send them. I researched how to send a POST request with Python and found multiple sources. Once I added what I found to my code I tried running it and there was no output. The error I got was pretty lengthy but boiled down to the Raspberry Pi not being able to connect to my server. It took a few weeks of troubleshooting and brainstorming new ideas that might fix the issue but nothing worked. One of them, which could have helped, was running the server from the Windows Command Prompt instead of WSL Ubuntu. On the day that it started to work while meeting with Dr. Hayes, we tried uninstalling every version of Python that was installed on my computer and just installed the version that the Raspberry Pi was using, which was v3.9.2, and it started working.  

---------------------------------------------------
### Project Language(s), Software, and Hardware ###
- **Language(s):**
  - Python
  - HTML
- **Software:**
  -  Windows OS
  -  Raspberry Pi OS
  -  Thonny
  -  Visual Studio Code
  -  Windows Command Prompt
- **Hardware:**
  - Raspberry Pi 4 Model B
  - NEO 6M GPS Module 

--------------------------------------------------------------
### [Project Requirements](/docs/Requirements_Document.md) ###

----------------------------------------------------------
### Project Implementation Description and Explanation ###

---------------------------------------
### [Test Plan](/docs/Test_Plan.md) ###

---------------------------------------------
### [Test Results](/docs/Test_Results.md) ###

---------------------------
### Challenges Overcome ###

This project is without a doubt the most challenging assignment I think I have done throughout my time at Charleston Southern. There were a lot of challenges that I had to overcome in order to get get project where it is today. The first challenge I had to overcome was soldering the pins into my GPS module. To do that I had to first buy a soldering kit off of Amazon. Once it arrived I had to figure out how to hold the pins into the GPS module without the help of a stand or helping hands. So, I carefully balanced the pins in their holes by leaning the module on top of the pins and using gravity to keep them in place. This was the best method I could think of at the time and it worked out pretty well. If you look at the pins, you can see a slight bend in them.
Another challenge that I had to overcome was setting up the GPS module to work with the Raspberry Pi. It took a good amount of time to set up, even with following along with the website. After following along with the website to the end, I went to run the program to see if it would give me GPS coordinates and when I ran it, it didn't give me any coordinates. So I went back through the steps that the website gave, thinking I missed something or made a typo. It turned out that the coordinates coming from the GPS were encoded and couldn't get read when ser.readline() was called. I found the answer to my problem in the comments at the bottom of the website. Someone was having the same problem as me and to fix it, I just had to add .decode('unicode_escape') to the end of ser.readline(). Since the coordinates were encoded, they would be decoded with .decode('unicode_escape') and could be read. I ran the program after adding that snippet of code and it started to work.
Another challenge I had to overcome was trying to get my Raspberry Pi to send a post request containing GPS coordinates to my flask server. This took several weeks of troubleshooting with Dr. Hayes. We tried a whole array of things that didn't work. I created firewall rules allowing connections to the port where the server was running thinking that my computer's firewall was the reason that it couldn't connect, turns out that wasn't the reason. I thought the problem was with my home network, so we used an old router to create a private network and it didn't change anything. I thought the problem was with the network or something else, but it turns out that the problem was with the Python version or versions. Dr. Hayes wanted me to try and run it using the most recent version of Python(v3.12) and when that didn't work, we uninstalled every installation of Python that I had on my computer and just installed one. After doing that I ran my server code and then ran the code on the pi and by the grace of God, I was getting POST requests on my server and 200 status codes on the pi.


---------------------------
### Future Enhancements ###


[Back to Top](#pi-tag)
