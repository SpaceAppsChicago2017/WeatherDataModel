import pandas as pd

data_2013 = pd.read_csv('StormEvents_2013.csv')
data_2014 = pd.read_csv('StormEvents_2014.csv')
orig_data = pd.concat([data_2013, data_2014])

min_lat = 39.66
max_lat = 45.41
min_lng = -93.64
max_lng = -86.00
start_mon = 201311
end_mon = 201404

out_data = pd.DataFrame(columns=['date', 'type', 'lat', 'lng'])

for row in orig_data.iterrows():
    entry = row[1]
    if ((not pd.isnull(entry.BEGIN_YEARMONTH) and start_mon <= int(entry.BEGIN_YEARMONTH) <= end_mon) and
        (not pd.isnull(entry.BEGIN_LAT) and min_lat < entry.BEGIN_LAT < max_lat) and
        (not pd.isnull(entry.BEGIN_LON) and min_lng < entry.BEGIN_LON < max_lng) ):
        new_record = pd.DataFrame([[str(int(entry.BEGIN_YEARMONTH)) + str(int(entry.BEGIN_DAY)), 
                entry.EVENT_TYPE, entry.BEGIN_LAT, entry.BEGIN_LON,
                ]],
                columns=['date', 'type', 'lat', 'lng'])
        # print new_record
        out_data = out_data.append(new_record, ignore_index=True)
        
out_data.to_csv('selected.csv')
