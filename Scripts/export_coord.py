import pandas as pd
df3 = pd.DataFrame( )
data = pd.read_csv('coord.txt', sep = '\t')
for index,row in data.iterrows():
    val = row['Address']
    var = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % val
    goapi = pd.read_json(var)
    data_map =(pd.DataFrame(goapi))
    loc = (data_map.results[0]['geometry']['location'])
    lat = (loc['lat'])
    lon = loc['lng']    
    s1 = pd.Series([lat,lon,val])
    i = index
    df = pd.DataFrame( [list(s1)], columns = ['Lat','Lon','Address'], index = [index] )
    df3 = pd.concat([df,df3])
merged_data = (pd.merge(data,df3,on = 'Address'))
print(merged_data)
merged_data.to_excel('coord_final.xls')
