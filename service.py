import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import sys
import subprocess
import datetime
import schedule
import time
import traceback

def execute_script(script_path):
    try:
        script_output = subprocess.check_output(script_path, shell=True, text=True)
        log_execution(script_path, True)
        save_output_log(script_output)
    except subprocess.CalledProcessError:
        log_execution(script_path, False)
    except Exception as e:
        log_execution(script_path, False, str(e), traceback.format_exc())

def log_execution(script_path, success, error_message=None, traceback_info=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Sucesso" if success else "Falha"
    log_message = f"{timestamp} - Execução do arquivo {script_path}: {status}"
    if error_message:
        log_message += f"\nErro: {error_message}"
    if traceback_info:
        log_message += f"\nTraceback:\n{traceback_info}"
    log_file_path = r"C:\Users\Caioh\OneDrive\Documentos\Python\Scheduler\execution.log"  # Atualize com o caminho completo para o arquivo de log
    with open(log_file_path, "a") as log_file:
        log_file.write(log_message + "\n")

def save_output_log(script_output):
    logs_directory = r"C:\Users\Caioh\OneDrive\Documentos\Python\Scheduler"
    os.makedirs(logs_directory, exist_ok=True)
    log_file_path = os.path.join(logs_directory, f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    with open(log_file_path, "w") as output_file:
        output_file.write(script_output)

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'PythonSchedulerService'
    _svc_display_name_ = 'Python Scheduler Service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        script_path = r"C:\Users\Caioh\OneDrive\Documentos\Python\Scheduler\arquivo.bat"

        schedule.every(5).minutes.do(execute_script, script_path)

        while self.is_running:
            schedule.run_pending()
            time.sleep(1)

        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STOPPED,
                              (self._svc_name_, ''))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)
