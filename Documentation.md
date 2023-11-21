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


-------------------------------
### Research and Background ###


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

----------------------------
### Project Requirements ###

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

----------------------------------------------------------
### Project Implementation Description and Explanation ###

-----------------
### Test Plan ###

--------------------
### Test Results ###

---------------------------
### Challenges Overcome ###

---------------------------
### Future Enhancements ###


[Back to Top](#pi-tag)
