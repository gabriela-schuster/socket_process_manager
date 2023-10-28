import os
import re


class Scanner():
    def get_processes(self):
        pss_out = os.popen('ps aux').read().split('\n')
        processes = []

        for line in pss_out[1:]: # skip header line
            columns = line.split(' ')  # Split the line into columns using whitespace
            if len(columns) < 11: continue
            if columns[0] == 'root': continue
            pid = ''
            for column in columns[1:]: # skip user
                if column != '': # check for the next thing that isn't a blank space
                    pid = column
                    break
            command = ' '.join(columns[-2:])
            processes.append(f'PID {pid} COMMAND {command}')

        return processes

