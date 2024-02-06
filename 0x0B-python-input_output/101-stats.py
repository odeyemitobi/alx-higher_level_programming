#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C), prints the following statistics since the beginning:
- Total file size: File size: <total size>
- Number of lines by status code:
  - possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
  - format: <status code>: <number> (status codes in ascending order)
  - if a status code doesn’t appear, don’t print anything for this status code
"""

import sys
from collections import defaultdict


def print_metrics(total_size, status_codes):
    """
    Print the computed metrics.

    Args:
        total_size: The total file size.
        status_codes: A dictionary containing the count of lines for each status code.
    """
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            # Assuming the input lines are in the specified format
            _, _, _, status_code, file_size = line.split()[8:13]
            total_size += int(file_size)
            status_codes[status_code] += 1
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_metrics(total_size, status_codes)


if __name__ == "__main__":
    main()
