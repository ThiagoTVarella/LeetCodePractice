class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        output = [0]*n
        
        function,key,prev_time = logs[0].split(":")
        function = int(function)
        prev_time = int(prev_time)

        call_stack = [function]

        for log in logs[1:]:
            function,key,time = log.split(":")
            function = int(function)
            time = int(time)

            if key == 'end':
                output[function] += time-prev_time+1
                call_stack.pop()
                prev_time = time+1
            else:
                if call_stack:
                    output[call_stack[-1]] += time-prev_time
                call_stack.append(function)
                prev_time = time

        return output


#         times = [0]*n
#         stack = []
#         prev_time = 0

#         for log in logs:
#             f_id,type_call,timestamp = log.split(":")
#             f_id,timestamp = int(f_id),int(timestamp)

#             if type_call == "start":
#                 if stack:
#                     times[stack[-1]] += timestamp-prev_time
#                 stack.append(f_id)
#                 prev_time = timestamp

#             if type_call == "end":
#                 prev_f = stack.pop()
#                 times[prev_f] += (timestamp+1)-prev_time
#                 prev_time = timestamp+1

#         return times

# # ["0:start:0","1:start:2","1:end:5","0:end:6"]
# # 0,s,0
# # prev = 0, prev_f = 0
# # 1,s,2
# # times[0] = 2-0, prev = 2, prev_f = 1
# # 1,e,5
# # times[1] = 6-2 = 4, prev = 5, prev_f = 1
# # 0,e,6
# # times[0] = 2 + (7-5)