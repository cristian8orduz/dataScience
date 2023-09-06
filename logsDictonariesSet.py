import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logReg=[]
        logdata = file.read()
        log_set=logdata.split("\n")
        pattern = r'^(?P<host>[\d.]+) - (?P<user_name>\w+) \[(?P<request_time>[^\]]+)\] "(?P<request>[^"]+)"'
    for log in log_set:
        match = re.match(pattern, log)
        if match:
            dictionary = match.groupdict()
            logReg.append(dictionary)
    return logReg
    raise NotImplementedError()
print(len(logs())) #501 logs, why?
