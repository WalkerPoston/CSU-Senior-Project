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
## Project Requirements

|             |             |
| ----------- | ----------- |
| ID      | 1          |
| Type    | Functional |
| Description | The prototype device’s location shall be displayed on the mobile app/webpage on a map. |
| Rationale | To be able to view its location. |
| Fit Criterion | The location of the product should correspond with its location on the app/webpage map. |
| Priority | 1 |
| Dependencies | 2 |

|      |      |
| ---- | ---- |
| ID | 2 |
| Type | Functional |
| Description | The prototype device, once configured and powered on, should begin transmitting a signal. |
| Rationale | To show that the prototype device is functioning. |
| Fit Criterion | The prototype device will be flashing a light, signifying that it is transmitting a signal. |
| Priority | 1 |
| Dependencies | None |

|   |   |
| - | - |
| ID | 3 |
| Type | Functional |
| Description | The mobile app/webpage must display the map immediately when opened. |
| Rationale | To be able to show that the map is displayed properly. |
| Fit Criterion |  When the mobile app/webpage is opened, the map will be displayed immediately. |
| Priority | 1 | 
| Dependnecies | 8 |

|   |   |
| - | - |
| ID | 4 |
| Type | Performance |
| Description | The mobile app/webpage must display any active device’s location on the map within 10-20 seconds of the mobile app/webpage being opened. |
| Rationale | To indicate the mobile app/webpage is running and receiving a signal from the active device(s). |
| Fit Criterion |  When the mobile app/webpage is opened, after 10-20 seconds, any active device’s location will be displayed on the map.|
| Priority | 2 |
| Dependencies | 3, 1, 7, and 8 |

|   |   |
| - | - |
| ID | 5 |
| Type | Functional |
| Description | The mobile app/webpage must maximize the map to full screen when the “Maximize” button is clicked. |
| Rationale | To allow the user to increase the size of the map. |
| Fit Criterion | When the “Maximize” button is clicked the map will be fitted to full screen. |
| Priority | 4 |
| Dependencies | 3 and 8 |

|   |   |
| - | - |
| ID | 6 |
| Type | Functional | 
| Description | The mobile app/webpage must minimize the map to its original size when the “Minimize” button is clicked. |
| Rationale | To allow the user to decrease the size of the map. |
| Fit Criterion | When the “Minimize” button is clicked the map will return to its original size. |
| Priority | 4 |
| Dependnecies | 3, 5, and 8 |

|   |   |
| - | - |
| ID | 7 |
| Type | Functional |
| Description | The prototype device must connect to the mobile app/webpage. |
| Rationale | To be able to show that the signal being sent by the device is being received by the mobile app/webpage. |
| Fit Criterion | When the device is on and transmitting and the mobile app/ webpage is opened and running, the device’s location will be displayed on the map. |
| Priority | 1 |
| Dependencies | 1, 2, 3, and 8 |

|   |   |
| - | - |
| ID | 8 |
| Type | Functional |
| Description |The mobile app/webpage must open when it is run. |
| Rationale | To show that the mobile app/webpage running and functioning properly without errors.  |
| Fit Criterion | When the mobile app/webpage is run, the default home page will be displayed with the map. |
| Priority | 1 | 
| Dependencies | None |

|   |   |
| - | - |
| ID | 9 |
| Type | Functional |
| Description | The mobile app/webpage must prompt the user to enter in an email address for someone they would like to receive a link to the device’s location when the “Share Device’s Location” button is clicked. |
| Rationale | To show that the “Share Device’s Location” button is functioning properly. |
| Fit Criterion | When the user clicks the “Share Device’s Location” button, they should then be prompted to enter an email address. |
| Priority | 4 | 
| Dependencies | None |

|   |   |
| - | - |
| ID | 10 | 
| Type | Functional |
| Description | The mobile app/webpage must go to the missing item page when the “Lost and Found” button is clicked. |
| Rationale | To show that the button goes to the correct page. |
| Fit Criterion | When the “Lost and Found” button is clicked, the user should be brought to the missing item page. |
| Priority | 4 |
| Dependencies | 8 | 

|   |   |
| - | - |
| ID | 11 |
| Type | Functional |
| Description | The mobile app/ webpage must return to the map when the “Back to Map” button is clicked. |
| Rationale | In order to get back to the map without having to restart the entire program. |
| Fit Criterion | While on a different page and the “Back to Map” button is clicked, the user should be brought back to the map page. |
| Priority | 3 |
| Dependencies | 8 and 3 |

|   |   |
| - | - |
| ID | 12 |
| Type | Functional | 
| Description | The mobile app/webpage must show all active devices in drop-down menu format when the “Devices” button is clicked. |
| Rationale | To show a list of all active devices. |
| Fit Criterion | When the “Devices” button is clicked, a drop-down menu of all the currently active devices should appear. |
| Priority | 4 |
| Dependencies | 3 and 8 |

|   |   |
| - | - |
| ID | 13 |
| Type | Functional |
| Description | When the “Devices” button is clicked the drop-down menu with all currently active devices appears and a device is clicked, the mobile app/webpage will have a “Change Name” button that allows the user to change the device name when clicked. |
| Rationale | To allow the user to distinguish what device is on which item. |
| Fit Criterion | When the “Change Name” button is clicked, a text box should appear and the user should be able to type in the text box. |
| Priority | 5 |
| Dependencies | 8 and 12 |

|   |   |
| - | - |
| ID | 14 |
| Type | Functional |
| Description | When a device from the “Devices” drop-down menu is clicked, the mobile app/webpage will only display that device’s location. | 
| Rationale | To allow the user to view a specific device’s location. |
| Fit Criterion | When a device from the drop-down is clicked, all dots belonging to other devices will disappear from the map. |
| Priority | 5 | 
| Dependencies | 3, 8, and 12 |

|   |   |
| - | - |
| ID | 15 | 
| Type | Functional |
| Description | When the “Devices” button is clicked and the drop-down menu with all currently active devices appears and a device is clicked, the mobile app/webpage will have a “Change Color” button that allows the user to change the color of the device’s locater dot on the map. |
| Rationale | To allow the user to be able to tell the difference between devices. |
| Fit Criterion | When the “Change Color” button is clicked, the user will be prompted to choose a color. |
| Priority | 5 |
| Dependencies | 1, 7, 8, and 12 |

|   |   |
| - | - |
| ID | 16 |
| Type | Performance |
| Description | The device's location on the map in the mobile app/webpage will be accurate to 10 – 15 feet. |
| Rationale | So, the user has a target area to search when looking for the device. |
| Fit Criterion | The location where the device actually is will be measured and compared to where its location is on the map. |
| Priority | 3 |
| Dependencies | 1, 2, 7, and 8 |

|   |   |
| - | - |
| ID | 17 |
| Type | Functional |
| Description | The map in the mobile app/webpage will zoom in when the user clicks the “Zoom In” button/icon. |
| Rationale | To allow the user to view the device's immediate surroundings. |
| Fit Criterion | When the “Zoom In” button/icon is clicked, the area surrounding the device will decrease. |
| Priority | 4 |
| Dependencies | 1, 2, 3, 4, 7, and 8 |

|   |   |
| - | - |
| ID | 18 |
| Type | Functional |
| Description | The map in the mobile app/webpage will zoom out when the user clicks the “Zoom Out” button/icon. |
| Rationale | To allow the user to view the device's surroundings on a larger scale. |
| Fit Criterion | When the “Zoom Out” button is clicked, the area surrounding the device will increase. |
| Priority | 4 |
| Dependencies | 1, 2, 3, 4, 7, and 8 |

|   |   |
| - | - |
| ID | 19 | 
| Type | Functional |
| Description | The mobile app/webpage will display a map key when the “Map Key” button/icon is clicked. |
| Rationale | To allow the user to be able to distinguish between the different roads, symbols, and colors that appear on the map. |
| Fit Criterion | When the “Map Key” button/icon is clicked, a drop-down menu will appear with the road/symbol/color and what they symbolize. |
| Priority | 5 |
| Dependencies | 1, 3, and 8 |

|   |   |
| - | - |
| ID | 20 |
| Type | Functional | 
| Description | The mobile app/webpage will show the user’s location when they click the “Show My Location” button is clicked. |
| Rationale | To show the location of the user in comparison to the location of their active devices. |
| Fit Criterion | When the “Show My Location” button is clicked, a dot will appear on the map indicating the location of the user and will be distinguishable from the other dots. |
| Priority | 4 |
| Dependencies | 1, 3, and 8 |
 
|   |   | 
| - | - |
| ID | 21 |
| Type | Security |
| Description | The mobile app/webpage must ask the user for permission to access the user’s device’s location. |
| Rationale | So the user is aware that the mobile app/webpage is accessing their personal device’s location. |
| Fit Criterion | When the user clicks the “Show My Location” button, they will be prompted to click yes or no to give permission for the mobile app/webpage to access their personal device’s location. |
| Priority | 4 |
| Dependencies | 1, 3, 8, and 20 |

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

   - **Communication Flow:**<br>
The NEO 6M GPS Module gets GPS data from the satellites and sends it to the Raspberry Pi via a direct wired connection (Fig 1).<br>
<figure>
  <img src = /media/RaspberryPi_and_GPSModule.jpg width = 400 height = 400>
  <figcaption>Fig 1. GPS Module connected to Raspberry Pi</figcaption>
</figure>
<br><br>Then the Raspberry Pi processes the data and sends the GPS coordinates to PubNub. The coordinates are also sent to the Flask server via a POST request. The Flask server takes the GPS coordinates and inserts them into the Mongo database. The webpage takes the coordinates that were sent to PubNub and, with help from a script, uses them to mark the real-time location on the map.

### 2. Flask Server:
   - **Purpose:**
      - The Flask server is an important part of the project but its functionality is very simple. It has routes for displaying various HTML templates and handling form submissions to update the MongoDB collection with GPS coordinates. The templates are rendered with data retrieved from the MongoDB collection. 

   - **Endpoints and Routes:**<br>
The Index Route handles POST requests and form submissions and extracts latitude and longitude from the form data. It inserts the data into MongoDB collection and then redirects to the same route to display the updated coordinates. The Show Map Route takes the user to the main page by rendering the 'map.html' template, the template for the main page (Fig 2).<br>
<figure>
  <img src = /media/Default_view.png width = 800 height = 400>
  <figcaption>Fig 2. The main page</figcaption>
</figure>
<br><br>The Show Share Route takes the user to the page where they can share the location of their device by rendering the 'share.html' template, the template for the "Share Location" page (Fig 3).<br><br>
<figure>
  <img src = /media/Share_Location_Page.png width = 800 height = 400>
  <figcaption>Fig 3. The Share Location page</figcaption>
</figure>
<br><br> The Show MissingItem Route renders the 'MissingItem.html' template, the template for the "Missing Item" page (Fig 4).<br><br>
<figure>
  <img src = /media/Missing_Item_Page.png width = 800 height = 400>
  <figcaption>Fig 4. The Missing Item Page</figcaption>
</figure>
<br><br> The Back-to-Map Route is for the "Back to Map" button that, when clicked, renders the 'map.html' template, taking the user back to the main page.

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
   - **MongoDB Integration:**<br>
MongoDB is integrated into the Flask server to store GPS coordinates. The server establishes a connection to MongoDB, and when new coordinates are received through the /update route, they are inserted into the "coords" collection. The stored coordinates can be retrieved and displayed on the webpage. This integration allows for persistent storage of GPS data, enabling historical tracking and analysis (Fig 5).<br>
<figure>
  <img src = /media/Database.png>
  <figcaption>Fig 5. The Mongo Database with GPS coordinates</figcaption>
</figure>
<br><br>

### 7. User Interaction:
   - **Client-Side Interaction:**<br>
Once the user is on the main page of the website, there are a few things that they are able to do. The first thing they can do is click the green button that says "Start Tracking" and track the position of their device. When that button is clicked, the map will shift to the location of the device (Fig 6).<br><br>
<figure>
  <img src = /media/Tracking_view.png width = 800 height = 400>
  <figcaption>Fig 6. The map focused on the marker after the "Start Tracking" button is clicked </figcaption>
</figure>
<br><br> If the device is moving, then on the map the red marker will also be moving followed by a blue trail marking the path the device took (Fig 7).<br><br>
<figure>
  <img src = /media/Active_tracking.png width = 800 height = 400>
  <figcaption>Fig 7. What the map looks like while tracking the device</figcaption>
</figure>
<br><br> If the user wants to increase the size of the map, then they can click the "Fullscreen" button in the top right corner of the map window to make the map larger (Fig 8).<br><br>
<figure>
  <img src = /media/Fullscreen_view.png width = 800 height = 400>
  <figcaption>Fig 8. The Map in fullscreen view</figcaption>
</figure>
<br><br> If the user needs to zoom in on the marker, they can click on the "Zoom in" button at the bottom right of the screen or map window (Fig 9). <br><br>
<figure>
  <img src = /media/Zoomed_in_view.png width = 800 height = 400>
  <figcaption>Fig 9. The map zoomed in on the marker</figcaption>
</figure>
<br><br>Likewise, if they are zoomed in too much they can click the "Zoom out" button located under the zoom in button (Fig 10). <br><br>
<figure>
  <img src = /media/Zoomed_out_view.png width = 800 height = 400>
  <figcaption>Fig 10. The map zoomed out away from the marker</figcaption>
</figure>
<br><br> While in the regular or fullscreen view, there are a few things the user can do. The first thing they can do is change between the Street Map view, which is the default, and the Satellite view (Fig 11). <br><br>
<figure>
  <img src = /media/Satellite_View.png width = 800 height = 400>
  <figcaption>Fig 11. The map in satellite view</figcaption>
</figure>
<br><br> In the Street Map view, if they hover over the "Map" button at the top right of the map window, they can select an option to show the terrain (Fig 12).<br><br>
<figure>
  <img src = /media/StreetMap_with_Terrain.png width = 800 height = 400>
  <figcaption>Fig 12. The Street Map with the Terrain option selected</figcaption>
</figure>
<br><br> In the Satellite view, if they hover over the "Satellite" button, they can select the option to turn on/off the labels (Fig 13). <br><br>
<figure>
  <img src = /media/Satellite_View_without_Labels.png width = 800 height = 400>
  <figcaption>Fig 13. The map in satellite view with labels turned off</figcaption>
</figure>
<br><br>The user is also able to go into Street View. All they have to do is drag the yellow figure onto the map (Fig 14).<br><br>
<figure>
  <img src = /media/Street_View.png width = 800 height = 400>
  <figcaption>Fig 14. The map when in street view</figcaption>
</figure>
<br><br> Under the "Start Tracking" button there are links that go to other pages. The first link takes the user to the "Share Location" page where the user can share the location of their device.  The user can return to the map by clicking "Back to Map". The other link will take the user to the "Missing Item" page where they can chat with other people about missing/stolen items. The user can return to the map by clicking "Back to Map".

### Link to Code
  - [Raspberry Pi Code](/src/raspberry_pi)
  - [Webpage Code](/src/webpage)

---------------------------------------
## Test Plan

Introduction
------------
- This test plan is for the testing of my senior project.
-	The goals for this test plan are to pass all of the tests that are listed below and to create more tests to test things with the project that I might have missed or forgot to include.

References 
-----------
-	Functional Requirements Document
-	Test Cases Document

Test Items 
----------
-	GPS prototype (hardware)
-	Webpage app (software)

Features to be Tested
---------------------
1.	ID #1: The prototype device’s location shall be displayed in the web app on a map.
2.	ID #2: The prototype device, once configured and powered on, should begin transmitting a signal.
3.	ID #3: The web app must display the map immediately when opened.
4.	ID #4: The web app must display any active device’s location on the map within 10 – 20 seconds after being powered on.
5.	ID #5: The web app must enlarge the map when the “Maximize” button is clicked.
6.	ID #6: The web app must minimize the map when the “Minimize” button is clicked.
7.	ID #7: The prototype device must connect to the web app.
8.	ID #8: The web app must open when it is run.
9.	ID #9: The web app must prompt the user to enter an email address for someone they would like to receive a link to the device’s location when the “Share Location” button is clicked.
10.	ID #10: The web app must go to the missing item page when the “Lost and Found” button is clicked.
11.	ID #11: The web app must return to the map when the “Back to Map” button is clicked.
12.	ID #12: The web app must show all active devices in drop-down menu format when the “Devices” button is clicked.
13.	ID #13: When the “Devices” button is clicked, the drop-down menu with all currently active devices appears, and a device is clicked, the web app will have a “Change Name” button which allows the user to change the name of the device.
14.	ID #14: When the device from the “Devices” drop-down menu is clicked, the web app will only display that device’s location.
15.	ID #15: When the “Devices” button is clicked, the drop-down menu with all currently active devices appears, and a device is clicked, the web app will have a “Change Color” button the allows the user to change the color of the device’s locator dot on the map.
16.	ID #16: The device’s location on the map in the web app will be accurate to 10-15 feet.
17.	ID #17: The map in the web app will zoom in when the user clicks the “Zoom In” button/icon.
18.	ID # 18: The map in the web app will zoom out when the user clicks the “Zoom Out” button/icon.
19.	ID #19: The web app will display a map key when the “Key” button is clicked.
20.	ID #20: The web app must ask the user for permission to access the user’s device’s location.

Approach
--------
- Manual Testing

Item Pass/Fail Criteria
-----------------------
1.	ID #1:
  - Pass: The device’s location will be displayed on the map once the device is powered on.
  - Fail: The device’s location will not be displayed on the map once the device is powered on.
2.	ID #2:
  - Pass: Will pass if the device transmits a signal to the web app when powered on.
  - Fail: The device does not transmit a signal.
3.	ID #3: 
  - Pass: Once the web app is opened, the map will be the first thing to pop up.
  - Fail: Does not display the map immediately when opened.
4.	ID #4: 
  - Pass: After the web app is opened, the locations of any active trackers will appear after 10-20 seconds.
  - Fail: Does not display the active device’s location after being open for 10-20 seconds.
5.	ID #5:
  - Pass: The map will become larger when the maximize button is pressed.
  - Fail: The map will not become larger.
6.	ID #6:
  - Pass: When the “Minimize” button is pressed, the map should return to its original size.
  - Fail: Map will not minimize to original size.
7.	ID #7:
  - Pass: The prototype GPS tracker will connect to the web app.
  - Fail: The prototype GPS tracker will not connect to the web app.
8.	ID #8: 
  - Pass: The application will open when it is run.
  - Fail: Will not open when run.
9.	ID #9: 
  - Pass: When the “Share Location” button is clicked, it should prompt the user the enter an email address.
  - Fail: Will not prompt the user when the button is clicked.
10.	ID #10:
  - Pass: When the “Lost and Found” button is clicked, the user should be taken to the correct page.
  - Fail: Will not go to the correct page when the button is clicked.
11.	ID #11: 
  - Pass: When the “Back to Map” button is clicked, the user should be taken back to the map.
  - Fail: The user is not taken back to the map.
12.	ID #12: 
  - Pass: When the “Devices” button is clicked, A drop-down menu of all the user’s devices should appear.
  - Fail: No menu will appear when the “Devices” button is clicked.
13.	ID #13: 
  - Pass: When the “Devices” button is clicked, there should be a “Change Name” button that appears that allows the user to change the name of the device.
  - Fail: There will be no “Change Name” button that appears or the user will not be able to change the name of the device.
14.	ID #14:
  - Pass: When a device from the Devices drop-down menu is clicked, all other devices on the map should disappear until the user closes the drop-down menu.
  - Fail: No dots will disappear from the map when a device is clicked on.
15.	ID #15:
  - Pass: When the “Devices” button is clicked, there should be a “Change Color” button that appears and allows the user to change the color of the locator dot.
  - Fail: The user will not be able to change the color of the locator dot or the “Change Color” button will not appear.
16.	ID #16:
  - Pass: The location of the device will be accurate between 10 to 15 feet from the location of the device on the map.
  - Fail: Location is not accurate within 10-15 feet.
17.	ID #17:
  - Pass: When the “Zoom In” button/icon is clicked, the map will zoom in closer to the device.
  - Fail: The map will not zoom in.
18.	ID #18:
  - Pass: When the “Zoom Out” button/icon is clicked, the map will zoom out away from the device.
  - Fail: The map will not zoom out.
19.	ID #19:
  - Pass: The application should display a map key when the “Key” button is clicked.
  - Fail: Will not display the map key.
20.	ID #20:
  - Pass: Will be prompted for access to their current location.
  - Fail: Will not be prompted for access to their current location.

Test Deliverables
-----------------
- Test Plan (This document)
- Test Cases Document

Testing Environment
-------------------
- Prototype GPS device
- The software application for the web app

Project Update
--------------
- The project is missing some of the requirements from the requirements document, but they are of a low priority. All of the higher-priority requirements have been fulfilled.

Approvals
---------
- Dr. Hayes

---------------------------------------------
## Test Results

|   |   |
| - | - |
| Test Case | 1 |
| Test Details | Check response on running the application. |
| Test Steps | 1. Launch application |
| Test Data | Once the application is run and accessed from a web browser, the home page appears with the map. |
| Expected Result | Default home page will be displayed with the map |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 2 |
| Test Details | Check the connection between hardware and software. |
| Test Steps | <ol><li>Power on GPS tracker hardware.</li><li>Launch application.</li></ol> |
| Test Data | The device’s location was displayed on the map. |
| Expected Result | The map will display the device’s location |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 3 |
| Test Details | Check that the map is displayed on start-up. |
| Test Steps | 1. Launch application. |
| Test Data | Map is displayed after the application is run and accessed from a web browser. |
| Expected Result | The map will be displayed on startup. |
| Test Result | Pass |


|   |   |
| - | - |
| Test Case | 4 |
| Test Details | Check that the GPS tracker is transmitting a signal. |
| Test Steps | <ol><li>Power on GPS device.</li><li>Run script.</li></ol> |
| Test Data | When the script is run, the GPS tracker transmits a signal. |
| Expected Result | The GPS tracker transmits a signal. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 5 |
| Test Details | Checks that the device’s location matches the location of the device on the map. |
| Test Steps | <ol><li>Power on GPS device.</li><li>Launch application.</li><li>Check the map.</li></ol> |
| Test Data | The location of the GPS tracker matches its location on the map. |
| Expected Result | The location of the tracker matches its location on the map. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 6 |
| Test Details | Checks the time that active devices appear on the map after startup. |
| Test Steps | <ol><li>Power on the GPS device.</li><li>Launch application.</li><li>3.	Check that all the active devices appear after 10-20 seconds.</li> |
| Test Data | Once both the tracker and the application are on and running, when the “Start Tracking” button is clicked on the Map page, all active devices are displayed in less than 5 seconds. |
| Expected Result | All active devices do appear after 10-20 seconds of application startup. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 7 |
| Test Details | Checks the response to clicking the “Back to Map” button. |
| Test Steps | <ol><li>Launch application.</li><li>Navigate to a different page.</li><li>Click the "Back to Map" button</li> |
| Test Data | After the application is launched and when another page is navigated and the “Back to Map” button is clicked, the user is returned to the map page. |
| Expected Result | Should return to the map page. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 8 |
| Test Details | Checks the accuracy of the device’s location on the map. |
| Test Steps | <ol><li>Launch application.</li><li>Navigate to the Map page.</li> |
| Test Data | The device’s location on the map starts off less than 5 feet from the actual location. When the device is stationary for a while, it will begin to slightly move away from its original location. |
| Expected Result | The device’s location on the map will be no more than 15 feet from where the device is located. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 9 |
| Test Details | Checks the functionality of the “Maximize” button.  |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Maximize" button.</li> |
| Test Data | When the “Maximize” button is clicked, the map blows up to the full screen. |
| Expected Result | The map should become full screen. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 10 |
| Test Details | Checks the functionality of the “Minimize” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Maximize" button.</li><li>Click the "Minimize" button.</li> |
| Test Data | When the “Minimize” button is clicked after the “Maximize” button is clicked, the map returns to its original size. |
| Expected Result | The map will return to its original size. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 11 |
| Test Details | Checks the functionality of the “Share Location” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Share Device's Location" button.</li> |
| Test Data | When the “Share Location” link is clicked, the user is taken to another page where they are then asked to enter in an email. |
| Expected Result | When clicked, the user should be prompted to enter an email address. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 12 |
| Test Details | Checks the functionality of the “Lost and Found” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Click the "Lost and Found" button.</li> |
| Test Data | When the “Lost and Found” link is clicked, the user is taken to the Missing Items page. |
| Expected Result | User should be taken to the Missing Items Page. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 13 |
| Test Details | Checks the functionality of the “Devices” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Click the "Devices" button</li> |
| Test Data | The application does not have a “Devices” button. |
| Expected Result | A drop-down of all active devices should appear. |
| Test Result | Fail |

|   |   |
| - | - |
| Test Case | 14 |
| Test Details | Checks the functionality of the “Zoom In” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Zoom In" button.</li> |
| Test Data | When the “Zoom In” button is clicked, the map zooms in on the device. |
| Expected Result | When clicked, the map will zoom in on the device. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 15 |
| Test Details | Checks the functionality of the “Zoom Out” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Zoom Out" button.</li> |
| Test Data | When the “Zoom Out” button is clicked, the map zooms out on the map. |
| Expected Result | When clicked, the map will zoom out on the device. |
| Test Result | Pass |

|   |   |
| - | - |
| Test Case | 16 |
| Test Details | Checks the functionality of the “Show My Location” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the “Show My Location” button.</li> |
| Test Data | The application does not have a “Show My Location” button. |
| Expected Result | The user will be prompted to give permission for the location of their device to be used and a dot will appear showing the user’s location. |
| Test Result | Fail |

|   |   |
| - | - |
| Test Case | 17 |
| Test Details | Checks the functionality of the “Change Name” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click on the "Devices" button.</li><li>Click on the device whose name is to be changed.</li> |
| Test Data | The application does not have this feature. |
| Expected Result | A text box will appear allowing the user to change the device’s name. |
| Test Result | Fail |

|   |   |
| - | - |
| Test Case | 18 |
| Test Details | Checks the response to clicking a device in the “Devices” drop-down menu. |
| Test Steps | <ol><li>Power on the GPS device.</li><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Devices" button.</li><li>Click on a device.</li> |
| Test Data | The application does not have this feature. |
| Expected Result | The device selected should be the only one displayed on the map. |
| Test Result | Fail |

|   |   |
| - | - |
| Test Case | 19 |
| Test Details | Checks the functionality of the “Change Color” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Devices button.</li><li> Right-click on the device whose color is to be changed.</li><li>Click the "Change Color" button.</li><li>Select a new color.</li> |
| Test Data | The application does not have this feature. |
| Expected Result | The color of the device's locator dot on the map will change to the selected color. |
| Test Result | Fail |

|   |   |
| - | - |
| Test Case | 20 |
| Test Details | Checks the functionality of the “Key” button. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Key" button.</li> |
| Test Data | The application does not have this feature. |
| Expected Result | A key with map icons should appear on the map. |
| Test Result | Fail |

|   |   |
| - | - |
| Test Case | 21 |
| Test Details | Checks if the program asks the user for permission to have access to the location of the user’s device. |
| Test Steps | <ol><li>Launch the application.</li><li>Navigate to the map.</li><li>Click the "Show My Location" button.</li> |
| Test Data | The application does not have this feature. |
| Expected Result | The map will focus in on the user’s location. |
| Test Result | Fail |

---------------------------
## Challenges Overcome 

&nbsp;&nbsp;&nbsp;&nbsp; This project is without a doubt the most challenging assignment I think I have done throughout my time at Charleston Southern. There were a lot of challenges that I had to overcome in order to get get project where it is today. The first challenge I had to overcome was soldering the pins into my GPS module. To do that I had to first buy a soldering kit off of Amazon. Once it arrived I had to figure out how to hold the pins into the GPS module without the help of a stand or helping hands. So, I carefully balanced the pins in their holes by leaning the module on top of the pins and using gravity to keep them in place. This was the best method I could think of at the time and it worked out pretty well. If you look at the pins, you can see a slight bend in them.
Another challenge that I had to overcome was setting up the GPS module to work with the Raspberry Pi. It took a good amount of time to set up, even with following along with the website. After following along with the website to the end, I went to run the program to see if it would give me GPS coordinates and when I ran it, it didn't give me any coordinates. So I went back through the steps that the website gave, thinking I missed something or made a typo. It turned out that the coordinates coming from the GPS were encoded and couldn't get read when ser.readline() was called. I found the answer to my problem in the comments at the bottom of the website. Someone was having the same problem as me and to fix it, I just had to add .decode('unicode_escape') to the end of ser.readline(). Since the coordinates were encoded, they would be decoded with .decode('unicode_escape') and could be read. I ran the program after adding that snippet of code and it started to work.
<br>
&nbsp;&nbsp;&nbsp;&nbsp; Another challenge I had to overcome was trying to get my Raspberry Pi to send a post request containing GPS coordinates to my flask server. This took several weeks of troubleshooting with Dr. Hayes. We tried a whole array of things that didn't work. I created firewall rules allowing connections to the port where the server was running thinking that my computer's firewall was the reason that it couldn't connect, turns out that wasn't the reason. I thought the problem was with my home network, so we used an old router to create a private network and it didn't change anything. I thought the problem was with the network or something else, but it turns out that the problem was with the Python version or versions. Dr. Hayes wanted me to try and run it using the most recent version of Python(v3.12) and when that didn't work, we uninstalled every installation of Python that I had on my computer and just installed one. After doing that I ran my server code and then ran the code on the pi and by the grace of God, I was getting POST requests on my server and 200 status codes on the pi.


---------------------------
## Future Enhancements 

&nbsp;&nbsp;&nbsp;&nbsp; My project is nowhere near where I envisioned it. When I came up with the idea of doing a GPS-tracking device for my senior project, I pictured the end product looking something like an Apple Air Tag. To get it to that state it needs to be scaled down by a significant amount. I know that I won't be able to get it to be as small as an Apple Air Tag but it can definitely be smaller than it is now. A couple of things I can do to scale it down is to use a smaller Raspberry Pi. Right now I am using the Raspberry Pi 4 Model B for my project but according the the site I used to set it up, I can also use the Raspberry Pi Zero which is significantly smaller than the Raspberry Pi 4. Another way I can scale it down is to use a smaller GPS module. The smallest GPS module on the market is the u-blox MIA-M10. Replacing the NEO 6M GPS Module that is currently being used in my project with the u-blox MIA-M10 will help with scaling down my project as a whole. Another way to enhance the project is to send additional data along with the coordinates, like the date and time, that way it is easier to pull the right coordinates from the database.
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp; There are a bunch of things that I need/can do in the future to make my project better. A couple of these enhancements are related to my requirements for the project. Some of the requirements I have listed failed during the testing phase of my project. I still need to add the "Devices" button, that displays all of the active devices and other features. I need to add the "Show My Location" button, the change name feature, the change color feature, and the "Key" button.  So, to enhance my project further, I will need to get those requirements working. Some of the requirements that passed during testing can be modified to further enhance the project. An example of this would be the "Share Location" page. Right now as it sits, when you type an email address in and hit submit, nothing happens. There is no backend code that does anything with the email address that is entered. It is the same for the "Lost and Found" page, once something is typed in the text box and is submitted nothing happens. 
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp; While testing my project, I came up with another way that I could enhance it further. One of these ways is to run all the code only on the Raspberry Pi. I found out that for the project to work properly both the device running the server code and the Raspberry Pi have to be on the same network. To fix this issue, I can use the Raspberry Pi Zero W instead of the Raspberry Pi 4. Doing this should allow me to run all of the code on the Raspberry Pi Zero W instead of on two separate devices. Right now for the project to work properly, I have to run the server code on my computer and then run the code on the Raspberry Pi while having both of them connect to the hotspot on my phone. Doing it this way isn't feasible for tracking stolen merchandise from a retail store. By putting all of the code on a single device, that device can be configured to run the code when the device is booted up. This would mean that the user wouldn't have to manually run the code.
<br><br>
Another way to enhance the project is to change what is going to be tracked. My entire project from the beginning has been focused on being able to track merchandise stolen from stores but what might be better is if I change the focus to tracking something bigger, like vehicles or larger packages that are being shipped. Doing it this way would allow me to keep my project close to how it is now with little that I would have to change.
<br> <br>
Another thing that needs to be done is to add more security to the project. One way to do that is to make sure that all communication between the Raspberry Pi and the Flask server, as well as any communication involving sensitive data, is secured using TLS. Another security feature that needs to be implemented is to use HTTPS to serve the Flask server. This ensures that data transmitted between the web browser and the server is encrypted. Another security feature that might need to be implemented is authentication mechanisms to verify the identity of users or devices interacting with the system. Multifactor authentication would also add additional security. Additionally, I could also implement authorization checks to ensure that users or devices only access the data they are permitted to. Another way to add security to the project is to ensure that the database is properly secured by using authentication, setting up access controls, and encrypting data at rest. Another important security measure that needs to be added is to ensure that user inputs are properly validated before being processed by the server to prevent SQL injection, XSS, or other injection vulnerabilities. Another way that could increase security is to secure the Raspberry Pi itself by changing default passwords, disabling unnecessary services, and keeping the operating system and software up to date with security patches.

[Back to Top](#pi-tag)
