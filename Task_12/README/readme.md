## RQT Graph
![graph](Screenshot%20from%202026-06-30%2023-08-11.png)

## Terminal output
![output](Screenshot%20from%202026-06-30%2023-17-11.png)

## Notes
To handle the synchronization between the 2 incoming data streams:
- Used a shared class dictionary (self.robots_incoming_data) to store the latest asynchronous updates for all robots. 
- Added a safety check inside the 10Hz control timer loop to ensure that distance math and priority checks are skipped    
  for any robot until both its position and priority data are completely populated. This prevents runtime errors and guarantees synchronization.
- Used lambda functions in subscribers to identify and route data to the correct robot slot dynamically.{}

