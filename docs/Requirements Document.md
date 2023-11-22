### Senior Project Requirements ###

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
