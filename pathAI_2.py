#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'find_meeting_slots' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER num_slots
#  2. 2D_STRING_ARRAY employee_schedules
#

def find_meeting_slots(num_slots, employee_schedules):
    # Write your code here
    if(len(employee_schedules)) == 0:
        return []
    if num_slots == 0:
        return []
    all_interval = [0]*100
    for emp in employee_schedules:
        for meetings_list in emp:
            time = meetings_list.split("-")
            s_time, e_time = time[0], time[1]
            s_time_list = s_time.split(":")
            s_time_hour, s_time_minute = int(s_time_list[0]), int(s_time_list[1])
            e_time_list = e_time.split(":")
            e_time_hour, e_time_minute = int(e_time_list[0]), int(e_time_list[1])
            l, r = s_time_hour * 4 + int(s_time_minute/15), e_time_hour * 4 + int(e_time_minute/15)
            # Meeting time isn't valid
            if s_time_minute % 3 != 0 or e_time_minute % 3 != 0 or s_time == e_time:
                continue
                # break
            while l < r:
                all_interval[l] += 1
                l += 1

    min_heap = []
    index_of_heap = -1
    prev_meetings = -1
    s_time = None
    i = 0

    while i < len(all_interval):
        curr_meetings = all_interval[i]
        if prev_meetings != curr_meetings:
            time_hour, time_min = int(i/4), (i % 4)*15
            if time_hour < 10:
                time_hour = "0"+str(time_hour)
            else:
                time_hour = str(time_hour)

            if time_min == 0:
                time_min = "00"
            else:
                time_min = str(time_min)

            curr_time = time_hour + ":"+time_min

            if index_of_heap != -1:
                min_heap.append((prev_meetings,
                                s_time + "-"+curr_time))
            index_of_heap += 1
            s_time = curr_time
            prev_meetings = curr_meetings
        i += 1
    if s_time != "24:00":
        time_hour, time_min = "24", "00"
        curr_time = time_hour + ":" + time_min
        min_heap.append((prev_meetings, s_time+"-"+curr_time))
    min_heap = sorted(min_heap, key=lambda x: (x[0]))

    ans = []
    if len(min_heap) < num_slots:
        return sorted(ans)

    i = 0
    while i < num_slots and i < len(min_heap):
        if int(min_heap[i][0]) < len(employee_schedules) - 1:
            ans.append(min_heap[i][1])
        i += 1

    if (len(ans) != num_slots or len(ans) < num_slots):
        return []

    ans.sort()
    # print(ans)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_slots = int(input().strip())

    employee_schedules_rows = int(input().strip())
    employee_schedules_columns = int(input().strip())

    employee_schedules = []

    for _ in range(employee_schedules_rows):
        employee_schedules.append(input().rstrip().split())

    result = find_meeting_slots(num_slots, employee_schedules)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
