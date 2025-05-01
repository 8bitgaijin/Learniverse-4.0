# -*- coding: utf-8 -*-
"""
Created on Thu May  1 11:49:27 2025

@author: Shane
"""

import platform
from pathlib import Path

def detect_os_name():
    """Return the current operating system name."""
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "macOS"
    elif system == "Linux":
        return "Linux"
    return "Unknown OS"

def get_local_path(os_name):
    """Dispatch to OS-specific function to resolve script directory."""
    try:
        if os_name == "Windows":
            return get_windows_path()
        elif os_name == "macOS":
            return get_mac_path()
        elif os_name == "Linux":
            return get_linux_path()
        else:
            raise ValueError(f"Unsupported OS: {os_name}")
    except Exception as error:
        print(f"[WARN] Path resolution failed: {error}")
        return Path.cwd()

def get_windows_path():
    return Path(__file__).resolve().parent.parent

def get_mac_path():
    return Path(__file__).resolve().parent.parent

def get_linux_path():
    return Path(__file__).resolve().parent.parent
