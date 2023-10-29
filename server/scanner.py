import os
import psutil


class Scanner():
    def get_processes(self):
        process_list = []
    
        for process in psutil.process_iter(['pid', 'name', 'username']):
            if process.info['username'] == 'root': continue # likewise dont want users messing with systems processes
            process_list.append(f'PID {process.info["pid"]} NAME {process.info["name"]}')
        
        return process_list
    

    def terminate_ps(self, pid):
        target_process = psutil.Process(pid)
        target_process.kill()

