import os
import sys
import subprocess
import shutil
import platform
import time
import psutil
import socket
import hashlib
import random
import datetime

def print_dynamic_info():
    blue = "\033[94m"
    light_green = "\033[92m"
    reset = "\033[0m"

    message = [
        f"{blue}PydroidHelper v1.24.seek{reset}",
        f"{light_green}SeekModule (GPT Base v1.20){reset}",
        f"{blue}22/02/2025{reset}"
    ]
    
    for line in message:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        time.sleep(0.5)

print_dynamic_info()

class PyDroidHelper:
    def __init__(self):
        self.commands = {
            "install": self._install_package,
            "check": self._check_module,
            "list": self._list_installed_packages,
            "clear": self._clear_cache,
            "run": self._run_command,
            "update": self._update_packages,
            "storage": self._check_storage,
            "system": self._system_info,
            "wait": self._wait,
            "mkdir": self._create_directory,
            "rmdir": self._delete_directory,
            "cpu": self._check_cpu_usage,
            "memory": self._check_memory_usage,
            "ip": self._get_ip_address,
            "hash": self._generate_hash,
            "random": self._generate_random_number,
            "time": self._get_current_time
        }

    def _install_package(self, package):
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', package], check=True)
            print(f'Package {package} installed successfully!')
        except subprocess.CalledProcessError:
            print(f'Error installing {package}.')

    def _check_module(self, module):
        try:
            __import__(module)
            print(f'Module {module} is available.')
        except ImportError:
            print(f'Module {module} is not installed.')

    def _list_installed_packages(self):
        packages = sorted([p.project_name for p in pkg_resources.working_set])
        print('\n'.join(packages))

    def _clear_cache(self):
        cache_dirs = [os.path.expanduser('~/.cache'), '/data/data/com.termux/cache']
        for cache_dir in cache_dirs:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
                print(f'Cache in {cache_dir} cleared!')
            else:
                print(f'No cache found in {cache_dir}.')

    def _run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout.strip() or result.stderr.strip()
            print(output)
        except Exception as e:
            print(f'Error running command: {e}')

    def _update_packages(self):
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
            subprocess.run([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=freeze'], capture_output=True, text=True)
            print('All packages updated.')
        except subprocess.CalledProcessError:
            print('Error updating packages.')

    def _check_storage(self):
        total, used, free = shutil.disk_usage("/")
        print(f'Total space: {total // (2**30)} GB')
        print(f'Used space: {used // (2**30)} GB')
        print(f'Free space: {free // (2**30)} GB')

    def _system_info(self):
        info = {
            "System": platform.system(),
            "Node Name": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Architecture": platform.architecture()[0]
        }
        for key, value in info.items():
            print(f'{key}: {value}')

    def _wait(self, seconds):
        time.sleep(seconds)
        print(f'Waited for {seconds} seconds.')

    def _create_directory(self, directory_name):
        try:
            os.makedirs(directory_name, exist_ok=True)
            print(f'Directory {directory_name} created.')
        except Exception as e:
            print(f'Error creating directory: {e}')

    def _delete_directory(self, directory_name):
        try:
            shutil.rmtree(directory_name)
            print(f'Directory {directory_name} deleted.')
        except Exception as e:
            print(f'Error deleting directory: {e}')

    def _check_cpu_usage(self):
        print(f'CPU Usage: {psutil.cpu_percent(interval=1)}%')

    def _check_memory_usage(self):
        mem = psutil.virtual_memory()
        print(f'Total Memory: {mem.total // (2**30)} GB')
        print(f'Available Memory: {mem.available // (2**30)} GB')
        print(f'Used Memory: {mem.used // (2**30)} GB')
        print(f'Memory Usage: {mem.percent}%')

    def _get_ip_address(self):
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f'IP Address: {ip_address}')
        except Exception as e:
            print(f'Error retrieving IP address: {e}')

    def _generate_hash(self, text):
        print(f'Hash: {hashlib.sha256(text.encode()).hexdigest()}')

    def _generate_random_number(self, start=1, end=100):
        print(f'Random Number: {random.randint(start, end)}')

    def _get_current_time(self):
        print(f'Current Time: {datetime.datetime.now()}')

    def execute(self, command, *args):
        if command in self.commands:
            self.commands[command](*args)
        else:
            print(f'Unknown command: {command}')

def export_to_other_codes():
    helper = PyDroidHelper()
    return helper.execute