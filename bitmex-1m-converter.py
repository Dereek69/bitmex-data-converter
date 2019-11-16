import csv
from datetime import datetime

with open('bitmex-XBTUSD-1m.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter = ',')
    
    resolution = int(input("Enter the resolution (in minutes): "))
    fix = bool(input("Fix open/close? (No = 0, Yes = 1)"))
    x = 0
    f = open(f"bitmex-XBTUSD-{resolution}m-date.csv", "w")
    
    time = [0] * resolution
    p_open = [0.0] * resolution
    p_high = [0.0] * resolution
    p_low = [0.0] * resolution
    p_close = [0.0] * resolution
    volume = [0.0] * resolution
    f_time = 0
    f_high = 0.0
    f_close = 0.0
    f_volume = 0.0

    for row in spamreader:
        print(row)
        time[x] = int(row["open_timestamp_utc"])
        p_open[x] = float(row["open"])
        p_high[x] = float(row["high"])
        p_low[x] = float(row["low"])
        p_close[x] = float(row["close"])
        volume[x] = float(row["volume"])

        if x == 0:

            #convert unix time to data
            #and insert open
            f_time = datetime.utcfromtimestamp(time[x]).strftime('%Y-%m-%d %H:%M:%S')
            f.write(f'{f_time},')
            
            #If fix is true check when the candle high is lower than candle open
            #and that the candle low is higher than candle open
            if p_open[x] > p_high[x] and fix == True:
                p_high[x] = p_open[x]
            if p_open[x] < p_low[x] and fix == True:
                p_low[x] = p_open[x]

            f.write(f'{p_open[x]},')

        if x == resolution-1:
            #find highs and lows for the last x entries
            #and insert close and newline
            f_high = p_high[x]
            f_low = p_low[x]
            
            for y in range(0,resolution):
                if f_high < p_high[y]:
                    f_high = p_high[y]
                if f_low > p_low[y]:
                    f_low = p_low[y]
                f_volume = f_volume + volume[y]

            f.write(f'{f_high},{f_low},{p_close[x]},{f_volume}\n')

            f_volume = 0

        x = x + 1
        if x > resolution-1:
            x = 0
    
    f.close()
    print("Task completed")
