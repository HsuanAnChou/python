import sys
import io

def setutf8():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
