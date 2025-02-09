import subprocess

def run_applescript(cmd, has_text=False):
    if has_text:
        result = subprocess.run(['osascript', '-e', cmd], capture_output=True, text=True)
    
    else:
        result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
    
    return result

