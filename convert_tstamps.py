import time
from datetime import datetime
import pathlib
import glob
import os

def get_sidex_tstamp_from_filename(filename):
    # Sidex_20200127T235718p525826.txt
    time_str = filename[filename.find('_')+1:filename.rfind('.')]
    dt = datetime.strptime(time_str, '%Y%m%dT%H%M%Sp%f')
    #
    # Returns a list of tuples where tuple[0] = filename 
    #                                tuple[1] = timestamp (datetime object) 
    return(filename, dt)

def main(filenames):
    timestamps = []
    for f in filenames:
        timestamps.append(get_sidex_tstamp_from_filename(filename=f.name))

    print('=============================================')
    for val in timestamps:
        # print the file name and corresponding timestamp
        print(' Filename:  {}'.format(val[0]))
        print(' Timestamp: {}'.format(val[1]))
        print('=============================================')

if __name__ == '__main__':
    filenames = sorted(pathlib.Path('./').glob('Sidex_*.txt'))
    main(filenames)