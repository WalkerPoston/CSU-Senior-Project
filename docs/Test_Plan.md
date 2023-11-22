[Back to Documentation](/Documentation.md)

Test Plan
=========

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

[Back to Documentation](/Documentation.md)
