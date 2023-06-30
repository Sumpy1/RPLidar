#Written by Gopal(sumiran) Pokharel for collection of dataset from RPLidar
#Gives data set in quality, angle and distance(polar co-ordinates) which can be converted into cartesian co-ordnates for better 3d modelling
#You can export time-stamps as z to form a better visualization
import time
from datetime import datetime
from rplidar import RPLidar

# Set the path where you want to save the data file
desktop_folder = "/home/pokharelg1/Desktop/"
data_file = desktop_folder + "lidar_data.txt"

# Initialize the RPLidar scanner
lidar = RPLidar('/dev/ttyUSB0')  # Update the port if necessary

# Set the duration in seconds
duration = 10

try:
    # Open the data file for writing
    with open(data_file, 'w') as file:
        # Get the start time
        start_time = time.time()

        # Collect data for the specified duration
        while (time.time() - start_time) < duration:
            # Iterate over each measurement and timestamp
            for scan in lidar.iter_measurments():
                # Get the current timestamp
                timestamp = datetime.now().strftime("%H:%M:%S.%f")

                # Extract the measurement data
                _, quality, angle, distance = scan

                # Write the data and timestamp to the file
                file.write(f"{timestamp}, {quality}, {angle}, {distance}\n")

                # Print the data to the console (optional)
                print(f"{timestamp}, {quality}, {angle}, {distance}")

                # Break the loop if the duration has elapsed
                if (time.time() - start_time) >= duration:
                    break

except KeyboardInterrupt:
    print("Program interrupted by the user")

finally:
    # Close the lidar connection
    lidar.stop()
    lidar.disconnect()

