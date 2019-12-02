# https://www.codewars.com/kata/5d4c6809089c6e5031f189ed/train/python

# Computer problem series #2: Torrent download

# Your task is to determine how much time will take to download all the files in your Torrent and the order of completion. All downloads are started and done in parallel like in real life. In the event of a tie you should list alphabeticaly.

# Help:
# GB: Giga Byte
# Mbps: Mega bits per second
# G = 1000 M
# Byte = 8 bits
# https://en.wikipedia.org/wiki/Byte
# https://en.wikipedia.org/wiki/Bandwidth_(computing)
# Input:
# Array of files
# File example: {"name": "alien", "size_GB": 38.0, "speed_Mbps": 38}
# Output:
# List of files in the order of completed download
# Time in seconds to download last file
# Examples:
# Basic
# file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}
# file_2 = {"name": "predator", "size_GB": 38, "speed_Mbps": 2}
# file_3 = {"name": "terminator", "size_GB": 5, "speed_Mbps": 25}

# torrent([file_1, file_2, file_3]) -> ["terminator", "alien", "predator"], 152000
# Order by name in case of a tie.
# file_4 = {"name": "zombieland", "size_GB": 38, "speed_Mbps": 38}
# file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}

# torrent([file_1, file_4]) -> ["alien", "zombieland"], 8000

# test.describe("Computer problem series #2: uTorrent download")

# file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}
# file_2 = {"name": "predator", "size_GB": 38, "speed_Mbps": 2}
# file_3 = {"name": "terminator", "size_GB": 5, "speed_Mbps": 25}
# file_4 = {"name": "zombieland", "size_GB": 38, "speed_Mbps": 38}

# # Basic
# test.it("Basic tests")
# files = [file_1, file_2, file_3]
# test.assert_equals(torrent(files), (["terminator", "alien", "predator"], 152000))

# # Order by name in case of a tie
# test.it("Tie tests")

# files = [file_1, file_4]
# test.assert_equals(torrent(files), (["alien", "zombieland"], 8000))

# files = [file_4, file_1]
# test.assert_equals(torrent(files), (["alien", "zombieland"], 8000))

# my solution
def torrent(files):
    # helper function to calculate time in seconds to download last file
    def remaining_time(size, speed):
        return size * 1000 * 8 / speed

    new_files = []        # [time, name]
    for f in files:
        time = remaining_time(f['size_GB'], f['speed_Mbps'])
        new_files.append([time, f['name']])
    new_files.sort()      # sort ascending by amount of time

    # if same amount of time, sort alphabeticaly
    for i in range (len(new_files)-1):
        if new_files[i][0] == new_files[i+1][0]:
            if new_files[i][1][0] > new_files[i+1][1][0]:
                new_files[i], new_files[i+1] = new_files[i+1], new_files[i]

    result = []
    # create list with names only
    for j in range(len(new_files)):
        result.append(new_files[j][1])
    return result, new_files[-1][0]    # return sorted list and amount of time for last file

# other solution
def torrent(files):
    files = sorted(files, key=lambda f: (f['size_GB'] / f['speed_Mbps'], f['name']))
    last = files[-1]
    return [f['name'] for f in files], 8000 * last['size_GB'] / last['speed_Mbps']
