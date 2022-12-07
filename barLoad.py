import time

limit = 40

def ProgressBar(segment, total, length):
    porcent = segment / total
    completed = int (porcent * length)
    rest = length - completed
    bar = f"[{'#' * completed}{'^'*rest}{porcent: .2%}]"
    return bar

for i in range(limit+1):
    time.sleep(0.08)
    print(ProgressBar(i,limit,20),end = "\r")
