import re
import pandas as pd
with open('DJI_0002.srt', 'r') as h:
    sub = h.readlines()

re_pattern = r'[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} -->'
regex = re.compile(re_pattern)
# Get start times
start_times = list(filter(regex.search, sub))
start_times = [time.split(' ')[0] for time in start_times]
# Get lines
lines = [[]]
for sentence in sub:
    if re.match(re_pattern, sentence):
        lines[-1].pop()
        lines.append([])
    else:
        lines[-1].append(sentence)
lines = lines[1:]         
lon_lat = []
j=0
for i in lines:
    lon = float(i[1].split(',')[0][4:])
    lat = float(i[1].split(',')[1])
    lon_lat.append([start_times[j][:8],lon,lat])
    j+=1



df = pd.DataFrame(lon_lat,columns=['time','lon','lat'])
df.to_csv('out.csv', index=False)  
