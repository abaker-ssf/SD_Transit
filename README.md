#San Deigo Transit Analysis
Author: Alexander Baker

Overview:
This is an Attempt to understand the San Diego County public mass transit situation. Is the MTS SD efficient or on time?
If not how off schedule are they? What potential reasons may this be happening? I aim to achieve this understanding 
through conducting a statical and data analysis of the situation with local government provided data. From these analysis
I am hoping to learn more about data science and the public transit situation of my home city. Finally, once enough 
research was conduct I hope to begin predicting when buses and trams will arrive and whether their on time or not.

MTS San Diego API KEY: d6d8bc59-5bd6-4160-acea-2965f2cb48b0

URLs (API KEY included): (change .pb to .pbtext for human readable format.)
https://realtime.sdmts.com/api/api/gtfs_realtime/trip-updates-for-agency/MTS.pb?key=d6d8bc59-5bd6-4160-acea-2965f2cb48b0
https://realtime.sdmts.com/api/api/gtfs_realtime/vehicle-positions-for-agency/MTS.pb?key=d6d8bc59-5bd6-4160-acea-2965f2cb48b0
https://realtime.sdmts.com/api/api/gtfs_realtime/alerts-for-agency/MTS.pb?key=d6d8bc59-5bd6-4160-acea-2965f2cb48b0


Todo list:
1. Conduct initial data exploration/analysis of MTS SD static GTFS data
2. Conduct Exploration and analysis of real-time GTFS data
3. Figure out how I want to store the data into a MongoDB 


