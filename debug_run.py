import sys
import traceback

try:
    sys.path.append('Python scripts')
    import app
except Exception as e:
    with open('error_full.txt', 'w', encoding='utf-8') as f:
        traceback.print_exc(file=f)
