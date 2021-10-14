import numpy as np

# Gerador de Estimação de vídeos do DVR

# quantidade de vídeos por câmeras
videos  = [
1539,
1552,
588,
1536,
1513,
1523,
1533,
1531,
555,
1418,
1526
]


tempo_por_video = 30 # minutos
total_days = 0
total_hours = 0
total_minutes = 0
total_seconds = 0


for video in videos:
    days = ((video*(tempo_por_video/60))/24)
    hours = (days - int(days))*24
    minutes = (hours - int(hours))*60
    seconds = (minutes - int(minutes))*60

    total_days = int(total_days + days)
    total_hours = int(total_hours + hours)
    total_minutes = int(total_minutes + minutes)
    total_seconds = (total_seconds + seconds)

    if days > 1:
        print('{} days, {}:{}:{}'.format(int(days),int(hours),int(minutes),int(seconds)))
    else:
        print('para {} videos, {} day, {}:{}:{}'.format(videos[video],int(days), int(hours), int(minutes), int(seconds)))


final_seconds = int((total_seconds/60 - int(total_seconds/60))*60)
total_minutes = total_minutes+int(total_seconds/60)
final_minutes = int((total_minutes/60 - int(total_minutes/60))*60)
total_hours = total_hours+int(total_minutes/60)
final_hours = int((total_hours/24 - int(total_hours/24))*24)
total_days = np.ceil(total_days+int(total_hours/24))



print('Total: {} days, {}:{}:{}'.format(int(total_days), int(final_hours), int(final_minutes), int(final_seconds)))