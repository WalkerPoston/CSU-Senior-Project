Pi Tag
======
- **Date:** November 21, 2023
- **Name:** Walker Poston
- **Major:** Cybersecurity
- **Degree:** BS
- **Advisor:** Dr. Hayes

---------------------
## Table of Contents
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
## Statement of Purpose 

&nbsp;&nbsp;&nbsp;&nbsp; Theft is a major problem that plagues society and many businesses, resulting in millions lost every year. Many businesses have come to accept that some of the products they sell will be stolen and have included that loss in their budgets as "shrink" or "shrinkage". To reduce the amount of shrinkage, these businesses could invest in something that they could use to recover stolen goods. With the "PI Tag," these businesses would be able to track, locate, and recover stolen products and reduce the amount of shrinkage in their business. GPS tags can improve the search process for stolen items by reducing the amount of money and time it takes to find the missing item.
Thieves are a part of society that will always exist no matter what laws are put in place to stop them and the items they steal may never be seen again. Unfortunately, searching for stolen items can be very time-consuming and cost-effective, sometimes never turning up at all. Stolen vehicles can sometimes take more than a week to find.
<br>
In 2019, there was approximately $6.4 billion in vehicles thefts and approximately $3 billion is stolen from Walmart each year (Borelli, 2021 & Thomas, 2021). As a way to combat these losses, GPS tags can be placed on an item and can be tracked. With GPS tags on items, once they are stolen, they can be tracked and recovered, reducing the amount of money stolen each year.
Theft is a major problem that plagues society and many businesses, costing millions and even billions of dollars every year. By implementing GPS tags for individuals and businesses to use, the overall cost of losses can be reduced.

-------------------------------
## Research and Background 

&nbsp;&nbsp;&nbsp;&nbsp; I didn't have much background in GPS tracking before deciding to do it for my senior project, so I had to do a lot of research to find sources on the subject. While researching for sources, I found the site that I would ultimately use to help me complete my project. Click [here](https://sparklers-the-makers.github.io/blog/robotics/realtime-gps-tracker-with-raspberry-pi/) to view the site. The site has instructions on how to configure the Raspberry Pi with the GPS module so it can receive GPS coordinates. The site also included all of the hardware and software that I would need to get it working, including some of the HTML code for the webpage. After completing that part of the project, the next thing I had to do was figure out how to make a webserver that would host the project. I ended up researching and using Python Flask for my webserver. At the time I didn't have any knowledge of how to make a webserver so I just followed along with the tutorial that Flask has. Click [here](https://flask.palletsprojects.com/en/2.3.x/) to see that tutorial. This tutorial has you set up a blog server so I followed along with it to see if I could use anything from it. 
<br>
&nbsp;&nbsp;&nbsp;&nbsp; One of the most important things I had to figure out was adding a database that would store the GPS coordinates. While researching for databases I could use I found MongoDB and a guide to setting it up to work with my Flask server. The site ultimately didn't work out and I had to go back to the drawing board. While in a meeting with Dr. Hayes, he found a site that better explained how to set up MongoDB with a Flask application. Click [here](https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application#step-1-setting-up-pymongo-and-flask) to visit the site. I used this site to help me with the initial setup and then changed it to work with my project. Once the Raspberry Pi sends a GPS coordinate to the server, the server takes the coordinate and stores it in the database. 
<br> 
&nbsp;&nbsp;&nbsp;&nbsp; Before the server was able to receive GPS coordinates from the Raspberry Pi, I had to figure out how to send them. I researched how to send a POST request with Python and found multiple sources. Once I added what I found to my code I tried running it and there was no output. The error I got was pretty lengthy but boiled down to the Raspberry Pi not being able to connect to my server. It took a few weeks of troubleshooting and brainstorming new ideas that might fix the issue but nothing worked. One of them, which could have helped, was running the server from the Windows Command Prompt instead of WSL Ubuntu. On the day that it started to work while meeting with Dr. Hayes, we tried uninstalling every version of Python that was installed on my computer and just installed the version that the Raspberry Pi was using, which was v3.9.2, and it started working.  

---------------------------------------------------
## Project Language(s), Software, and Hardware 
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
## [Project Requirements](/docs/Requirements_Document.md) 

----------------------------------------------------------
## Project Implementation Description and Explanation 

### 1. Architecture Overview:
   - **System Components:**
      - NEO 6M GPS Module 
      - Raspberry Pi (Python Integration)
      - PubNub for Geolocation Services
      - Flask Server
      - MongoDB for data storage
      - Google Maps API key
      - Webpage

   - **Communication Flow:**
      - The NEO 6M GPS Module gets GPS data from the satellites and sends it to the Raspberry Pi via a direct wired connection (Fig 1). Then the Raspberry Pi processes the data and sends the GPS coordinates to PubNub. The coordinates are also sent to the Flask server via a POST request. The Flask server takes the GPS coordinates and inserts them into the Mongo database. The webpage takes the coordinates that were sent to PubNub and, with help from a script, uses them to mark the real-time location on the map.

### 2. Flask Server:
   - **Purpose:**
      - The Flask server is an important part of the project but its functionality is very simple. It has routes for displaying various HTML templates and handling form submissions to update the MongoDB collection with GPS coordinates. The templates are rendered with data retrieved from the MongoDB collection. 

   - **Endpoints and Routes:**
      - The Index Route handles POST requests and form submissions and extracts latitude and longitude from the form data. It inserts the data into MongoDB collection and then redirects to the same route to display the updated coordinates. The Show Map Route takes the user to the main page by rendering the 'map.html' template, the template for the main page (Fig 2. Main page). The Show Share Route takes the user to the page where they can share the location of their device by rendering the 'share.html' template, the template for the "Share Location" page (Fig 3. Share Location page). The Show MissingItem Route renders the 'MissingItem.html' template, the template for the "Missing Item" page (Fig 4. Missing Item page). The Back-to-Map Route is for the "Back to Map" button that, when clicked, renders the 'map.html' template, taking the user back to the main page.

### 3. Raspberry Pi Integration:
   - **Data Acquisition:**
      - The Raspberry Pi interacts with the GPS module by establishing a serial connection. It then reads NMEA sentences from the module, parsing these sentences to extract latitude and longitude information, and then using the extracted coordinates for further actions, such as publishing them to a PubNub channel and sending them to a server via HTTP POST request. The code continuously repeats this process in a loop to keep receiving and processing GPS data

   - **PubNub Integration:**
      - PubNub is a real-time communication platform that provides the infrastructure and services to enable seamless and efficient real-time communication between devices, applications, and users. The Raspberry Pi interacts with PubNub by configuring PubNub with the required keys and settings, subscribing to a specific channel (raspi-tracker), and then continuously publishing GPS coordinates to that channel in a loop. The PubNub service ensures that these coordinates are delivered to any devices or applications that are subscribed to the same channel in near real-time. 

### 4. PubNub Geolocation Services:
   - **Role in the System:**
      - In my project, PubNub is acting as the communication backbone, enabling real-time updates of GPS data from the Raspberry Pi to other parts of my system, such as a web application, mobile app, or any other service that needs to consume or react to the real-time location information. This real-time communication is vital for applications such as live tracking, monitoring, or any use case where immediate updates are required based on changing geolocation data.

### 5. Google Maps API Integration:
   - **Mapping Functionality:**
      - The Google Maps API is used to initialize a map, place a marker, and update the map in real-time based on incoming GPS coordinates. The PubNub integration ensures that the webpage can receive real-time updates from the Raspberry Pi, allowing the user to track the movement of the device on the map dynamically. 
      -  The integration process involves initializing the Google Map, setting up a marker, and updating the map in real-time based on incoming GPS coordinates from PubNub. The combination of Google Maps API and PubNub enables the dynamic display of the device's movement on the map in real time. The polyline drawn on the map helps visualize the path taken by the tracked device. The integration creates a seamless and interactive experience for tracking GPS coordinates on the web page.

### 6. Data Storage and Retrieval:
   - **MongoDB Integration:**
      - MongoDB is integrated into the Flask server to store GPS coordinates. The server establishes a connection to MongoDB, and when new coordinates are received through the /update route, they are inserted into the "coords" collection. The stored coordinates can be retrieved and displayed on the webpage. This integration allows for persistent storage of GPS data, enabling historical tracking and analysis (Fig 5. Mongo database). 

### 7. User Interaction:
   - **Client-Side Interaction:**
      - Once the user is on the main page of the website, there are a few things that they are able to do. The first thing they can do is click the green button that says "Start Tracking" and track the position of their device. When that button is clicked, the map will shift to the location of the device. If the device is moving, then on the map the red marker will also be moving followed by a blue trail marking the path the device took (Fig 6. Active Tracking). If the user wants to increase the size of the map, then they can click the "Fullscreen" button in the top right corner of the map window to make the map larger (Fig 7. Fullscreen). If the user needs to zoom in on the marker, they can click on the "Zoom in" button at the bottom right of the screen or map window (Fig 8. Zoomed in view). Likewise, if they are zoomed in too much they can click the "Zoom out" button located under the zoom in button (Fig 9. Zoomed out view) While in the regular or fullscreen view, there are a few things the user can do. The first thing they can do is change between the Street Map view and the Satellite view (Fig 10. Satellite View). In the Street Map view, if they hover over the "Map" button at the top right of the map window, they can select an option to show the terrain (Fig 11. Street Map with Terrain). In the Satellite view, if they hover over the "Satellite" button, they can select the option to turn on/off the labels (Fig 12. Satellite Map w/o labels). The user is also able to go into Street View. All they have to do is drag the yellow figure onto the map (Fig 13. Street View). <br> Under the "Start Tracking" button there are links that go to other pages. The first link takes the user to a page where the user can share the location of their device (Fig 14. Share Location Page). The user can return to the map by clicking "Back to Map". The other link will take the user to a page where they can chat with other people about missing/stolen items (Fig 15. Missing Item Page). The user can return to the map by clicking "Back to Map".
     
      - Describe how users interact with the system (e.g., accessing maps, submitting queries).


---------------------------------------
## [Test Plan](/docs/Test_Plan.md) 

---------------------------------------------
## [Test Results](/docs/Test_Results.md) 

---------------------------
## Challenges Overcome 

&nbsp;&nbsp;&nbsp;&nbsp; This project is without a doubt the most challenging assignment I think I have done throughout my time at Charleston Southern. There were a lot of challenges that I had to overcome in order to get get project where it is today. The first challenge I had to overcome was soldering the pins into my GPS module. To do that I had to first buy a soldering kit off of Amazon. Once it arrived I had to figure out how to hold the pins into the GPS module without the help of a stand or helping hands. So, I carefully balanced the pins in their holes by leaning the module on top of the pins and using gravity to keep them in place. This was the best method I could think of at the time and it worked out pretty well. If you look at the pins, you can see a slight bend in them.
Another challenge that I had to overcome was setting up the GPS module to work with the Raspberry Pi. It took a good amount of time to set up, even with following along with the website. After following along with the website to the end, I went to run the program to see if it would give me GPS coordinates and when I ran it, it didn't give me any coordinates. So I went back through the steps that the website gave, thinking I missed something or made a typo. It turned out that the coordinates coming from the GPS were encoded and couldn't get read when ser.readline() was called. I found the answer to my problem in the comments at the bottom of the website. Someone was having the same problem as me and to fix it, I just had to add .decode('unicode_escape') to the end of ser.readline(). Since the coordinates were encoded, they would be decoded with .decode('unicode_escape') and could be read. I ran the program after adding that snippet of code and it started to work.
<br>
&nbsp;&nbsp;&nbsp;&nbsp; Another challenge I had to overcome was trying to get my Raspberry Pi to send a post request containing GPS coordinates to my flask server. This took several weeks of troubleshooting with Dr. Hayes. We tried a whole array of things that didn't work. I created firewall rules allowing connections to the port where the server was running thinking that my computer's firewall was the reason that it couldn't connect, turns out that wasn't the reason. I thought the problem was with my home network, so we used an old router to create a private network and it didn't change anything. I thought the problem was with the network or something else, but it turns out that the problem was with the Python version or versions. Dr. Hayes wanted me to try and run it using the most recent version of Python(v3.12) and when that didn't work, we uninstalled every installation of Python that I had on my computer and just installed one. After doing that I ran my server code and then ran the code on the pi and by the grace of God, I was getting POST requests on my server and 200 status codes on the pi.


---------------------------
## Future Enhancements 

&nbsp;&nbsp;&nbsp;&nbsp; My project is nowhere near where I envisioned it. When I came up with the idea of doing a GPS-tracking device for my senior project, I pictured the end product looking something like an Apple Air Tag. To get it to that state it needs to be scaled down by a significant amount. I know that I won't be able to get it to be as small as an Apple Air Tag but it can definitely be smaller than it is now. A couple of things I can do to scale it down is to use a smaller Raspberry Pi. Right now I am using the Raspberry Pi 4 Model B for my project but according the the site I used to set it up, I can also use the Raspberry Pi Zero which is significantly smaller than the Raspberry Pi 4. Another way I can scale it down is to use a smaller GPS module. The smallest GPS module on the market is the u-blox MIA-M10. Replacing the NEO 6M GPS Module that is currently being used in my project with the u-blox MIA-M10 will help with scaling down my project as a whole. 
<br>
&nbsp;&nbsp;&nbsp;&nbsp; There are a bunch of things that I need/can do in the future to make my project better. A couple of these enhancements are related to my requirements for the project. Some of the requirements I have listed failed during the testing phase of my project. I still need to add the "Devices" button, that displays all of the active devices and other features. I need to add the "Show My Location" button, the change name feature, the change color feature, and the "Key" button.  So, to enhance my project further, I will need to get those requirements working. Some of the requirements that passed during testing can be modified to further enhance the project. An example of this would be the "Share Location" page. Right now as it sits, when you type an email address in and hit submit, nothing happens. There is no backend code that does anything with the email address that is entered. It is the same for the "Lost and Found" page, once something is typed in the text box and is submitted nothing happens. 
<br>
&nbsp;&nbsp;&nbsp;&nbsp; While testing my project, I came up with another way that I could enhance it further. One of these ways is to run all the code only on the Raspberry Pi. I found out that for the project to work properly both the device running the server code and the Raspberry Pi have to be on the same network. To fix this issue, I can use the Raspberry Pi Zero W instead of the Raspberry Pi 4. Doing this should allow me to run all of the code on the Raspberry Pi Zero W instead of on two separate devices. Right now for the project to work properly, I have to run the server code on my computer and then run the code on the Raspberry Pi while having both of them connect to the hotspot on my phone. Doing it this way isn't feasible for tracking stolen merchandise from a retail store. By putting all of the code on a single device, that device can be configured to run the code when the device is booted up. This would mean that the user wouldn't have to manually run the code.
<br>
Another way to enhance the project is to change what is going to be tracked. My entire project from the beginning has been focused on being able to track merchandise stolen from stores but what might be better is if I change the focus to tracking something bigger, like vehicles or larger packages that are being shipped. Doing it this way would allow me to keep my project close to how it is now with little that I would have to change.
<br> 
<br>
Another thing that needs to be done is to add more security to the project. One way to do that is to make sure that all communication between the Raspberry Pi and the Flask server, as well as any communication involving sensitive data, is secured using TLS. Another security feature that needs to be implemented is to use HTTPS to serve the Flask server. This ensures that data transmitted between the web browser and the server is encrypted. Another security feature that might need to be implemented is authentication mechanisms to verify the identity of users or devices interacting with the system. Multifactor authentication would also add additional security. Additionally, I could also implement authorization checks to ensure that users or devices only access the data they are permitted to. Another way to add security to the project is to ensure that the database is properly secured by using authentication, setting up access controls, and encrypting data at rest. Another important security measure that needs to be added is to ensure that user inputs are properly validated before being processed by the server to prevent SQL injection, XSS, or other injection vulnerabilities. Another way that could increase security is to secure the Raspberry Pi itself by changing default passwords, disabling unnecessary services, and keeping the operating system and software up to date with security patches.

[Back to Top](#pi-tag)
