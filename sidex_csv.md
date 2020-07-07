### Example SIDEX data file:
*First 3 lines ONLY*
```
Latitude Longitude Altitude GPSTime Satellites Quality HDOP geoid BoardTime Gain NumChannels Frequency DAQStatus
0 0 0 0 0 0 0 0 20200127T235718p525826 0 16 1000.000000 1
0.000026,-0.000024,0.000013,-0.000007,-0.000015,-0.000008,0.000008,-0.000017,0.000034,-0.000014,0.000017,0.000040,0.000045,0.000389,-0.000181,-0.000007
```

### Header Breakdown
*I suspect that the GPS was off or not recording position because of the lat/lon vals and the number of satellites in view*
```
Latitude = 0
Longitude = 0
Altitude = 0
GPSTime = 0
Satellites = 0
Quality = 0
HDOP = 0
geoid = 0
BoardTime = 20200127T235718p525826
Gain = 0
NumChannels = 16
Frequency = 1000.000000
DAQStatus = 1
```
#### If you're more visual:
```
Latitude Longitude Altitude GPSTime Satellites Quality HDOP geoid BoardTime Gain NumChannels Frequency DAQStatus
    |        |        |        |         |        |     |     |       |      |        |          |         |
    |        |        |        |         |        |     |     |       |      |        |          |         ---------> 1
    |        |        |        |         |        |     |     |       |      |        |          -------------------> 1000.000000
    |        |        |        |         |        |     |     |       |      |        ------------------------------> 16
    |        |        |        |         |        |     |     |       |      ---------------------------------------> 0
    |        |        |        |         |        |     |     |       ----------------------------------------------> 20200127T235718p525826
    |        |        |        |         |        |     |     ------------------------------------------------------> 0
    |        |        |        |         |        |     ------------------------------------------------------------> 0
    |        |        |        |         |        ------------------------------------------------------------------> 0
    |        |        |        |         ---------------------------------------------------------------------------> 0
    |        |        |        -------------------------------------------------------------------------------------> 0
    |        |        ----------------------------------------------------------------------------------------------> 0
    |        -------------------------------------------------------------------------------------------------------> 0
    ----------------------------------------------------------------------------------------------------------------> 0
```

### Breaking down the data
##### First 'Data' line
Each value represents a reading from a channel.
The values column tells you which channel the reading is from.
Since there is only one line at the top that gives you pose data, the Lat/Lon etc... are the same for all readings.
*There are situations where you may want pose data for every reading*
*ex: a fast moving vehicle where the lat/lon or pose would be different by the time a second has passed*
Since these geophones are on the ground someone decided that pose updates at the begining of the file were accurate enough for the whole file
```
# This row represents all the samples taken from the array in this iteraction
# If the sample rate is 1000Hz, you should have 1000 rows of data (not including the header) for a file length of 1 second

0.000026,-0.000024,0.000013,-0.000007,-0.000015,-0.000008,0.000008,-0.000017,0.000034,-0.000014,0.000017,0.000040,0.000045,0.000389,-0.000181,-0.000007
    |        |        |        |         |          |          |         |       |         |        |        |         |       |         |         |
    |        |        |        |         |          |          |         |       |         |        |        |         |       |         |         ---------> Channel 16
    |        |        |        |         |          |          |         |       |         |        |        |         |       |         -------------------> Channel 15
    |        |        |        |         |          |          |         |       |         |        |        |         |       -----------------------------> Channel 14
    |        |        |        |         |          |          |         |       |         |        |        |         -------------------------------------> Channel 13
    |        |        |        |         |          |          |         |       |         |        |        -----------------------------------------------> Channel 12
    |        |        |        |         |          |          |         |       |         |        --------------------------------------------------------> Channel 11
    |        |        |        |         |          |          |         |       |         -----------------------------------------------------------------> Channel 10
    |        |        |        |         |          |          |         |       ---------------------------------------------------------------------------> Channel 9
    |        |        |        |         |          |          |         -----------------------------------------------------------------------------------> Channel 8
    |        |        |        |         |          |          ---------------------------------------------------------------------------------------------> Channel 7
    |        |        |        |         |          --------------------------------------------------------------------------------------------------------> Channel 6
    |        |        |        |         -------------------------------------------------------------------------------------------------------------------> Channel 5
    |        |        |        -----------------------------------------------------------------------------------------------------------------------------> Channel 4
    |        |        --------------------------------------------------------------------------------------------------------------------------------------> Channel 3
    |        -----------------------------------------------------------------------------------------------------------------------------------------------> Channel 2
    --------------------------------------------------------------------------------------------------------------------------------------------------------> Channel 1
```

### For spectrograms:
AFAIK, you can only do one channel at a time. That means you'll pull all the data from say, column 1, 
then use those values to create the spectrogram for that channel during the time that file was created.

The data file you shared has 60,003 lines total. It has 60,000 lines of data.
That tells me that if the sample rate is 1,000 Hz and there are 60,000 lines of data, the file represents 60 seconds worth of data

### To run the specgram.py
```
pip install -r requirements.txt
python specgram.py
```