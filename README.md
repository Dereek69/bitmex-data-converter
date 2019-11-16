# Bitmex-data-converter

Converts the candles from CryptoBigBro's bitmex data (https://github.com/cryptobigbro/bitmex-XBTUSD/blob/master/bitmex-XBTUSD-1m.csv) from 1m to whatever you need and changes the time from unix to data to make it compatible with matlab's timetable

Sometimes the candle's high is lower or the candle's low is higher than the open. The Fix option adapts the highs and lows to avoid that

ITS IMPORTANT TO DELETE THE FIRST LINE OF DATA FROM CryptoBigBro's FILE SINCE ITS 1M off
