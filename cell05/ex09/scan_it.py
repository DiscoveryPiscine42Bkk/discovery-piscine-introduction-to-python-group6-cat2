import sys
import re

def scan_it():
    
    if len(sys.argv) != 3:
    
        print("none")
        return

    keyword = sys.argv[1]
    
    text_to_scan = sys.argv[2]
    
    matches = re.findall(re.escape(keyword), text_to_scan)
    
    count = len(matches)
    
    if count == 0:
    
        print("none")
    else:
    
        print(count)

if __name__ == "__main__":
    scan_it()