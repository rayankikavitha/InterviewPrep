calculate_average_mean_time_by_step.py
I got asked the same question. this is how I solved it.
This solves it for a static stream but we can modify the strategy to compute the running new average time spent on each step for every new stream of data coming into the system.

import datetime
streams = [
             [1000, 123, 1, datetime.datetime(2014, 4, 11, 8, 0)]
            ,[1000, 123, 2, datetime.datetime(2014, 4, 11, 8, 10)]
            ,[1000, 123, 3, datetime.datetime(2014, 4, 11, 8, 20)]
            ,[1000, 123, 4, datetime.datetime(2014, 4, 11, 8, 30)]
            ,[1000, 123, 5, datetime.datetime(2014, 4, 11, 8, 31)]
            ,[1001, 125, 1, datetime.datetime(2014, 4, 11, 9, 10)]
            ,[1001, 125, 2, datetime.datetime(2014, 4, 11, 9, 30)]
            ,[1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 50)]
            ,[1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 51)]
            ,[1001, 125, 4, datetime.datetime(2014, 4, 11, 9, 52)]
            ,[1005, 129, 1, datetime.datetime(2014, 4, 11, 9, 8)]
            ,[1005, 129, 2, datetime.datetime(2014, 4, 11, 9, 10)]
            ,[1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 12)]
            ,[1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 13)]
            ,[1005, 129, 4, datetime.datetime(2014, 4, 11, 9, 14)]
            ,[1005, 129, 5, datetime.datetime(2014, 4, 11, 9, 18)]
          ]

Python Code:

from collections import defaultdict
def avg_time(streams):
    result_dict = {}
    time_spent = {}
    users_on_steps = {1:0, 2:0, 3:0, 4:0}
    for i in range(len(streams)):
        stream = streams[i]
        session_id, user_id, step_id, current_step_start_time = stream
        if ((session_id, user_id, step_id) not in result_dict):
            result_dict[(session_id, user_id, step_id)] = current_step_start_time

            if step_id &gt; 1 and (session_id, user_id, step_id-1) in result_dict:
                users_on_steps[step_id-1] +=1
                previous_step_start_time = result_dict[(session_id, user_id, step_id-1)]
                if (step_id-1) not in time_spent:
                    time_spent[step_id-1] = (current_step_start_time - previous_step_start_time).total_seconds()
                else:
                    time_spent[step_id-1] += (current_step_start_time - previous_step_start_time).total_seconds()

    print(result_dict)

    print("Users in each step", users_on_steps)

    print("Time spent in each step", time_spent)

    for step in time_spent:
        avg_time = time_spent[step]/users_on_steps[step]
        print("Avg. time spent on step {} is {} seconds".format(step, avg_time))

avg_time(streams)

O/p:

Users in each step {1: 3, 2: 3, 3: 3, 4: 2}
Time spent in each step {1: 1920.0, 2: 1920.0, 3: 840.0, 4: 300.0}
Avg. time spent on step 1 is 640.0 seconds
Avg. time spent on step 2 is 640.0 seconds
Avg. time spent on step 3 is 280.0 seconds
Avg. time spent on step 4 is 150.0 seconds

Mitesh on Jun 20, 2018	
