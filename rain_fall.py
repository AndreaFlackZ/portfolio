

def fun():
    import urllib.request
    with urllib.request.urlopen('https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain') as rain_fall:
        lines = [byte_line.decode('utf-8') for byte_line in rain_fall]

    rain_dict = {}
    for line in lines[12:]:
        date = line[0:12].strip()
        rain = line[13:18].strip()
        if rain == "-":
            continue
        rain_dict[date] = int(rain)

    date = ""
    highest = 0
    for x in rain_dict:
        if rain_dict[x] > highest:
            highest = rain_dict[x]
            date = x
    print ("Day with highest rainfall", date, highest)


    year_dict = {}
    for entry in rain_dict:
        year = int(entry[7:11])
        year_dict[year] = year_dict.get(year, 0) + rain_dict[entry]
    #for testing
    #for year, rain in sorted(year_dict.items()):
        #print(year, rain)

    highest_year = ""
    high_num = 0
    for rain in year_dict:
        if year_dict[rain] > high_num:
            high_num = year_dict[rain]
            highest_year = rain
    print("Year with highest rainfall", highest_year, high_num)
fun()
