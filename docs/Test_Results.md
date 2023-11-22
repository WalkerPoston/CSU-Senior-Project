Senior Project Test Results
===========================

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
