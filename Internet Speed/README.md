## Overview
This is a graphical user interface (GUI) application built using Python's `customtkinter` library, which allows users to measure their internet speed, including download speed, upload speed, and ping. The app runs speed tests using the `speedtest` module, provides real-time updates on progress, and displays the results in a clean, easy-to-read interface.

## Features
- **Download Speed**: Measures the download speed in Mbps.
- **Upload Speed**: Measures the upload speed in Mbps.
- **Ping**: Measures the network latency in milliseconds (ms).
- **Real-Time Progress Bar**: Visual feedback during the speed test process.
- **Last Test Time**: Displays the timestamp of the last completed speed test.
- **Error Handling**: Provides clear error messages in case of internet connection issues or test failures.

## Requirements
To run the application, you need the following Python libraries:
- `customtkinter`: For creating the application's GUI.
- `speedtest-cli`: For measuring internet speed.
- `threading`: To run speed tests in the background without freezing the UI.
- `datetime`, `socket`: Used for checking internet connection and managing time stamps.

You can install the required packages using pip:

```bash
pip install customtkinter speedtest-cli
```

## How to Run
1. Clone the repository or download the Python script.
2. Install the required dependencies.
3. Run the script using Python:

```bash
python speedtest_app.py
```

## Application Usage
1. Upon launching, the app will display a "Start Test" button.
2. Click the **Start Test** button to begin the internet speed test.
3. The app will update the progress bar as it performs:
   - Download speed test
   - Upload speed test
   - Ping test
4. Once completed, the results will be displayed on the interface.
5. The **Last tested** timestamp will also update, showing when the last test was completed.

## Error Handling
- **No Internet Connection**: If no internet connection is detected, the app will show an error message and stop the test.
- **Speed Test Failures**: If the speedtest configuration cannot be retrieved, or no matching servers are found, an error message will be displayed.

## Code Structure
- **`SpeedTestApp` Class**: The main class that manages the GUI, handles button clicks, and runs the speed test.
- **`start_speed_test`**: Triggered when the "Start Test" button is clicked. It resets the display and starts the speed test in a separate thread.
- **`run_speed_test`**: Handles the actual speed test operations, including download, upload, and ping measurements.
- **`update_progress`**: Updates the progress bar and status messages during the test.
- **`check_internet_connection`**: Verifies if there is an active internet connection before running the speed test.

## Happy coding
