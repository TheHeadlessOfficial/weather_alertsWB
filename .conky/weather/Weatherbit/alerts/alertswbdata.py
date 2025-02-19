import os, sys
import requests
import textwrap
# Lock file to tell conky that the script is running
lock_file = "/tmp/script_wbalerts.lock"
# Check lock file
try:
    open(lock_file, 'w').close()
    ################################ get your HOME automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set your latitude, longitude and APPID between apostrophes
    mylat = 45.40713
    mylon = 11.87680
    myAPPID = ''
    ################################ pattern url alerts
    urlA = 'https://api.weatherbit.io/v2.0/alerts?lat=' + str(mylat) + '&lon=' + str(mylon) + '&key=' + myAPPID
    resA = requests.get(urlA).json()
    dataA = resA
    ################################ set variables
    tdeg = 0
    winddeg = 0
    vtext = 'n/a'
    ################################ set the paths for the API files
    home = '/home/'
    conky = '/.conky/'
    ptemp = conky + 'weather/Weatherbit/alerts/'
    #                   set the path for the weatherbit logo
    pwblogo = home + homename + ptemp + 'wblogo.txt'
    #                   set the path for the ALERTS raw section
    pathalertsraw = home + homename + ptemp + '-alertsraw.txt'
    #                   set the path for the ALERTS clean section
    pathalerts = home + homename + ptemp + '-alerts.txt'
    #                   set the path for the ALERTS conky section
    pathalertsc = home + homename + ptemp + 'alerts.txt'
    ################################ create the path for weatherbit logo
    pi = "${image " + home
    pi2 = homename
    pi3 = conky + 'weather/Weatherbit/wblogo2'
    est = '.png -p '
    x = 250
    virg = ','
    y = 0
    pf = ' -s 15x15}'
    fo = open(pwblogo, 'w')
    tot = pi + pi2 + pi3 + est + str(x) + virg + str(y) + pf
    fo.write('{}\n'.format(tot))
    fo.close()
    ################################ create ALERTS section
    #                 set variables and array
    anum = 2 # set number of alerts to show in conky
    titlea = []
    descriptiona = []
    description2a = []
    severitya = []
    effective_utca = []
    effective_locala = []
    expires_utca = []
    expires_locala = []
    onset_utca = []
    onset_locala = []
    ends_utca = []
    ends_locala = []
    uria = []
    regionsa = []
    ################################ choose how many rows to write for some alerts variable
    def writedata(var, counter):
        text2 = '-'
        y = 0
        nchars = 100
        myrowsad = 3 # number of rows
        strlenght = len(var)
        if strlenght == 0:
            var = text2
        wrapper = textwrap.TextWrapper(width=nchars, max_lines=(myrowsad))
        word_list = wrapper.wrap(text=var)
        for element in word_list:
            fo.write('{}\n'.format(element))
            y = y + 1
            if (strlenght <= nchars) and (y == 1):
                fo.write('{}\n'.format(text2))
                y = y + 1
            if (strlenght <= nchars*2) and (y == 2):
                fo.write('{}\n'.format(text2))
                y = y + 1
            # if (strlenght <= nchars*3) and (y == 3):
            #     fo.write('{}\n'.format(text2))
            #     y = y + 1
            # if (strlenght <= nchars*4) and (y == 4):
            #     fo.write('{}\n'.format(text2))
            #     y = y + 1
            # if (strlenght <= nchars*5) and (y == 5):
            #     fo.write('{}\n'.format(text2))
            #     y = y + 1
            # if (strlenght <= nchars*6) and (y == 6):
            #     fo.write('{}\n'.format(text2))
            #     y = y + 1
            # if (strlenght <= nchars*7) and (y == 7):
            #     fo.write('{}\n'.format(text2))
            #     y = y + 1
            if y == 3:
                y = 0
    #                 get data for alerts
    city_namea = dataA['city_name']
    country_codea = dataA['country_code']
    lata = dataA['lat']
    lona = dataA['lon']
    state_codea = dataA['state_code']
    timezonea = dataA['timezone']
    for i in range(0, anum):
        try:
            descriptiona.append(dataA['alerts'][i]['description'])
        except:
            descriptiona.append(vtext)
        try:
            description2a.append(dataA['alerts'][i]['description'])
        except:
            description2a.append(vtext)
        try:
            effective_locala.append(dataA['alerts'][i]['effective_local'])
        except:
            effective_locala.append(vtext)
        try:
            effective_utca.append(dataA['alerts'][i]['effective_utc'])
        except:
            effective_utca.append(vtext)
        try:
            ends_locala.append(dataA['alerts'][i]['ends_local'])
        except:
            ends_locala.append(vtext)
        try:
            ends_utca.append(dataA['alerts'][i]['ends_utc'])
        except:
            ends_utca.append(vtext)    
        try:
            expires_locala.append(dataA['alerts'][i]['expires_local'])
        except:
            expires_locala.append(vtext)    
        try:
            expires_utca.append(dataA['alerts'][i]['expires_utc'])
        except:
            expires_utca.append(vtext)    
        try:
            onset_locala.append(dataA['alerts'][i]['onset_local'])
        except:
            onset_locala.append(vtext)
        try:
            onset_utca.append(dataA['alerts'][i]['onset_utc'])
        except:
            onset_utca.append(vtext)    
        try:
            regionsa.append(dataA['alerts'][i]['regions'])
        except:
            regionsa.append(vtext)
        try:
            severitya.append(dataA['alerts'][i]['severity'])
        except:
            severitya.append(vtext)    
        try:
            titlea.append(dataA['alerts'][i]['title'])
        except:
            titlea.append(vtext)
        try:
            uria.append(dataA['alerts'][i]['uri'])
        except:
            uria.append(vtext)
    #                 write raw data for alerts
    fo = open(pathalertsraw, 'w')
    # general data
    fo.write('lat: {}\n'.format(lata))
    fo.write('lon: {}\n'.format(lona))
    fo.write('tz: {}\n'.format(timezonea))
    fo.write('city: {}\n'.format(city_namea))
    fo.write('state: {}\n'.format(state_codea))
    fo.write('country: {}\n'.format(country_codea))
    # alerts data
    divisor = "Italian(it-IT): " # set your language here if different from english
    for i in range(0, anum):
        fo.write('title: {}\n'.format(titlea[i]))
        # write your language
        if descriptiona[i] != vtext:
            temp = descriptiona[i]
            temp = temp.split(divisor)
            temp = temp[1]
            descriptiona[i] = temp
            writedata(descriptiona[i], i)
        else:
            fo.write('desc: {}\n'.format(descriptiona[i]))
        # write the default language (english)
        if description2a != vtext:
            temp = description2a[i]
            temp = temp.split(divisor)
            temp = temp[0]
            description2a[i] = temp
            writedata(description2a[i], i)
        else:
            fo.write('desc: {}\n'.format(description2a[i]))
        #fo.write('desc: {}\n'.format(descriptiona[i]))
        fo.write('sev: {}\n'.format(severitya[i]))
        fo.write('effUTC: {}\n'.format(effective_utca[i]))
        fo.write('effLOC: {}\n'.format(effective_locala[i]))
        fo.write('exUTC: {}\n'.format(expires_utca[i]))
        fo.write('exLOC: {}\n'.format(expires_locala[i]))
        fo.write('startUTC: {}\n'.format(onset_utca[i]))
        fo.write('startLOC: {}\n'.format(onset_locala[i]))
        fo.write('endUTC: {}\n'.format(ends_utca[i]))
        fo.write('endLOC: {}\n'.format(ends_locala[i]))
        fo.write('url: {}\n'.format(uria[i]))
        fo.write('regions: {}\n'.format(regionsa[i]))
    fo.close()
    #                 write clean data for alerts
    fo = open(pathalerts, 'w')
    # general data
    fo.write('{}\n'.format(lata))
    fo.write('{}\n'.format(lona))
    fo.write('{}\n'.format(timezonea))
    fo.write('{}\n'.format(city_namea))
    fo.write('{}\n'.format(state_codea))
    fo.write('{}\n'.format(country_codea))
    # alerts data
    for i in range(0, anum):
        fo.write('{}\n'.format(titlea[i]))
        writedata(descriptiona[i], i)
        writedata(description2a[i], i)
        #fo.write('{}\n'.format(descriptiona[i]))
        fo.write('{}\n'.format(severitya[i]))
        fo.write('{}\n'.format(effective_utca[i]))
        fo.write('{}\n'.format(effective_locala[i]))
        fo.write('{}\n'.format(expires_utca[i]))
        fo.write('{}\n'.format(expires_locala[i]))
        fo.write('{}\n'.format(onset_utca[i]))
        fo.write('{}\n'.format(onset_locala[i]))
        fo.write('{}\n'.format(ends_utca[i]))
        fo.write('{}\n'.format(ends_locala[i]))
        fo.write('{}\n'.format(uria[i]))
        fo.write('{}\n'.format(regionsa[i]))
    fo.close()
    #                 create conky statements for ALERTS
    rowtitlea = []
    rowseva = []
    rowstarta = []
    rowenda = []
    startenda = []
    rowexa = []
    rowrega = []
    rowdesca = []
    rowdesca1 = []
    rowdesca2 = []
    rowdesca3 = []
    rowdesca4 = []
    rowcount = 0
    alertsblock = 18
    rowcolor = '${color}'
    rowcolor1 = '${color1}'
    rowcolor2 = '${color2}'
    rowcolor3 = '${color3}'
    rowcolor4 = '${color4}'
    rowcolor5 = '${color5}'
    rowcolor6 = '${color6}'
    rowcolor9 = '${color9}'
    rowfont6 = '${font URW Gothic L:size=6}'
    rowfont7 = '${font URW Gothic L:size=7}'
    rowfont8 = '${font URW Gothic L:size=8}'
    rowheadinga = rowcolor3 + '${alignc}----------------- WEATHERBIT ALERTS -----------------'
    for i in range(0, anum):
            # block control
        rowcount = 7 + alertsblock * i
        rowtitlea.append(rowcolor2 + rowfont7 + "Title: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + "}")
        rowcount = rowcount + 7
        rowseva.append(rowcolor2 + "Sev: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + "}")
        rowcount = rowcount + 6
        rowstarta.append(rowcolor2 + "Start: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + "}")
        rowcount = rowcount + 2
        rowenda.append(rowcolor2 + "${goto 200}end: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + "}")
        startenda.append(rowstarta[i] + rowenda[i])
        rowcount = rowcount - 4
        rowexa.append(rowcolor2 + "Expires: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + "}")
        rowcount = rowcount + 6
        rowrega.append(rowcolor2 + "Reg: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + "}")
        rowcount = rowcount - 16
        rowdesca.append(rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + '}' + rowcolor)
        rowcount = rowcount + 1
        rowdesca1.append(rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + '}' + rowcolor)
        rowcount = rowcount +1
        rowdesca2.append(rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + '}' + rowcolor)
        rowcount = rowcount +1
        rowdesca3.append(rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + '}' + rowcolor)
        rowcount = rowcount +1
        rowdesca4.append(rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pathalerts + '}' + rowfont7 + rowcolor)
    #                 write conky syntax in alerts.txt
    fo = open(pathalertsc, 'w')
    fo.write('{}\n'.format(rowheadinga))
    for i in range(0, anum):
        fo.write('{}\n'.format(rowtitlea[i]))
        fo.write('{}\n'.format(rowseva[i]))
        fo.write('{}\n'.format(startenda[i]))
        fo.write('{}\n'.format(rowexa[i]))
        fo.write('{}\n'.format(rowrega[i]))
        fo.write('{}\n'.format(rowdesca[i]))
        fo.write('{}\n'.format(rowdesca1[i]))
        fo.write('{}\n'.format(rowdesca2[i]))
        fo.write('{}\n'.format(rowdesca3[i]))
        fo.write('{}\n'.format(rowdesca4[i]))
    fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed