Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

  (2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Python 2.7
Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

Python 2.7
your function would return:

  [(0, 1), (3, 8), (9, 12)]


def merge_ranges(meetings):

    sorted_array=sorted(meetings)
    merged_meetings=[sorted_array[0]]

    for start, end in sorted_array[1:]:
        last_start,last_end=merged_meetings[-1]


        if(start<=last_end):
            merged_meetings[-1]=(last_start,max(end,last_end))
        else:
            merged_meetings.append((start,end))


    return merged_meetings
