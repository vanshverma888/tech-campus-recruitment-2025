📜 Log Extraction Script Discussion

🌟 Solutions Considered

🟢 1. Sequential Log Search

🔍 Approach: Read the log file line by line and extract relevant logs based on the date.

✅ Pros: Simple to implement and requires no pre-processing.

❌ Cons: Inefficient for large log files as it requires scanning the entire file each time.

🚀 2. Index-Based Log Retrieval (Final Solution)

🔍 Approach: Create an index file mapping dates to byte positions in the log file. Use binary search for efficient retrieval.

✅ Pros:

⚡ Fast lookup using binary search.

📂 Efficient for large log files.

🚀 Avoids reading unnecessary data.

❌ Cons: Requires an additional step to maintain an index file.

🏆 Final Solution Summary

We chose the Index-Based Log Retrieval approach because it provides significant performance improvements for large log files. By maintaining an index, we can quickly locate and extract logs for a specific date without scanning the entire file. This solution balances efficiency and maintainability.

🛠 Steps to Run

📌 1. Prepare Log File

Ensure you have a log file named test_logs.log in the script directory. The logs should be formatted with a date at the beginning of each line, e.g.,:

2025-01-30 Error: Something went wrong
2025-01-30 Warning: High memory usage
2025-01-31 Info: Process started

▶️ 2. Run the Script

Execute the script using the command:

python extract_logs.py YYYY-MM-DD

Replace YYYY-MM-DD with the desired date (e.g., 2025-01-30).

🔄 3. Index Creation (If Not Exists)

If an index file (log_index.txt) is missing, the script will automatically create one by scanning the log file.

📂 4. Log Extraction

The script will extract logs for the specified date and save them in the output directory as output_YYYY-MM-DD.txt.

✅ 5. Output Verification

Check the extracted logs in the output folder:

cat output/output_YYYY-MM-DD.txt

🔧 6. Rebuilding the Index (Optional)

If logs are updated frequently, delete log_index.txt and re-run the script to regenerate the index:

rm log_index.txt
python extract_logs.py YYYY-MM-DD

🚀 Happy Logging! 🎯

