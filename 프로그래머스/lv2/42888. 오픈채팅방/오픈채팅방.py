from collections import deque

def solution(record):
    answer = []
    temp_message = deque()
    user = {}
    for str in record:
        temp = str.split()
        cmd, user_id = temp[0], temp[1]

        if cmd == "Enter":
            temp_message.append(user_id + "님이 들어왔습니다.")
            user[user_id] = temp[2]
        elif cmd == "Leave":
            temp_message.append(user_id + "님이 나갔습니다.")
        else: # Change
            user[user_id] = temp[2]

    while temp_message:
        message = temp_message.popleft()
        user_id = message.split("님이")[0]
        answer.append(message.replace(user_id, user[user_id]))

    return answer
