import sys
import os
import bisect

INDEX_FILE = 'log_index.txt'
LOG_FILE = 'test_logs.log'
OUTPUT_DIR = 'output'

def create_index(log_file, index_file):
    """Creates an index file mapping dates to byte positions in the log file."""
    if not os.path.exists(log_file):
        print(f"Error: Log file '{log_file}' not found.")
        sys.exit(1)

    with open(log_file, 'r', buffering=10**7) as f, open(index_file, 'w') as index_f:
        prev_date = None
        while True:
            pos = f.tell()
            line = f.readline()
            if not line:
                break

            parts = line.split(maxsplit=1)
            if not parts:
                continue
            
            date = parts[0]
            if date != prev_date:
                index_f.write(f"{date} {pos}\n")
                prev_date = date

    print(f"Index file '{index_file}' created successfully.")

def load_index(index_file):
    """Loads index file into memory as a sorted list of (date, position)."""
    index = []
    if not os.path.exists(index_file):
        print(f"Error: Index file '{index_file}' not found. Creating a new index.")
        return index

    with open(index_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                date, pos = parts
                index.append((date, int(pos)))

    return index

def find_position(index, date):
    """Finds the byte position of logs for a given date using binary search."""
    dates = [entry[0] for entry in index]
    pos = bisect.bisect_left(dates, date)
    
    if pos < len(index) and index[pos][0] == date:
        return index[pos][1]
    return None

def extract_logs(log_file, index, date):
    """Extracts logs for a given date using the precomputed index."""
    position = find_position(index, date)
    if position is None:
        print(f"No logs found for date: {date}")
        return []

    logs = []
    with open(log_file, 'r', buffering=10**7) as f:
        f.seek(position)
        while True:
            line = f.readline()
            if not line or not line.startswith(date):
                break
            logs.append(line.strip())

    return logs

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]

    if not os.path.exists(INDEX_FILE):
        print("Creating index...")
        create_index(LOG_FILE, INDEX_FILE)

    index = load_index(INDEX_FILE)
    logs = extract_logs(LOG_FILE, index, date)

    if logs:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_file = os.path.join(OUTPUT_DIR, f'output_{date}.txt')

        with open(output_file, 'w') as f:
            f.write("\n".join(logs) + "\n")

        print(f"Logs for {date} have been saved to {output_file}")
    else:
        print(f"No logs found for {date}.")

if name == "main":
    main()
