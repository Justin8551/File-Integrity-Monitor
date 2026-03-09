import hashlib
import os
import json
import time

def calculate_hash(path):
    sha256 = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return None
    
def get_current_status(directory, exclude_file):
    status = {}
    for file in os.listdir(directory):
        if os.path.isfile(file) and file != exclude_file and file != "fim.py" and file != "security_log.txt":
            f_hash = calculate_hash(file)
            if f_hash:
                status[file] = f_hash
    return status

def log_alert(message):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}\n"
    with open("security_log.txt", "a") as f:
        f.write(log_entry)
    print(log_entry.strip())
    
def monitor_realtime():
    directory = "."
    baseline_file = "baseline.json"
    
    print("Real-Time Monitor is running...")
    baseline = get_current_status(directory, baseline_file)
    
    with open(baseline_file, "w") as f:
        json.dump(baseline, f, indent=4)
        
    print(f"Baseline created for {len(baseline)}.")
    print("Press Ctrl+C to stop.")
    print("-"*20)
    
    try:
        while True:
            time.sleep(3)
            current_status = get_current_status(directory, baseline_file)
            
            for file in list(baseline.keys()):
                if file not in current_status:
                    log_alert(f"[{time.strftime('%H:%M:%S')}] DETECT DELETED FILE!: {file}")
                    del baseline[file]
                elif baseline[file] != current_status[file]:
                    log_alert(f"[{time.strftime('%H:%M:%S')}] DETECTED MODIFY FILE!: {file}")
                    baseline[file] = current_status[file]
            
            for file in current_status:
                if file not in baseline:
                    log_alert(f"[{time.strftime('%H:%M:%S')}] DETECTED NEW FILE!: {file}")
                    baseline[file] = current_status[file]
    except KeyboardInterrupt:
        log_alert("\nMonitoring stopped by user.")
        
if __name__ == "__main__":
    monitor_realtime()
    