start = '1b1b1b1b01010101'
stop = '1b1b1b1b1a'
data = ''
runs = 0
result = ''

while runs <1:
    char = open("smart_meter.log", "r")
    data = data + char.read().encode('HEX')
    offset = data.find(start)
    if (offset <> -1):
        data = data[offset:len(data)]
    offset = data.find(stop)
    if (offset <> -1):
        
        search = '070100010800ff'
        offset = data.find(search)
        if (offset <> -1):
            offset = offset + len(search) + 22
            hex_value = data[offset:offset + 16]
            dec_value = int(hex_value, 16) / 10000
            print 'Active energy: ' + str(dec_value) + ' kWh'
            result = result + ';' +  str(dec_value)

        search = '070100010801ff'
        offset = data.find(search)
        if (offset <> -1):
            offset = offset + len(search) + 14
            hex_value = data[offset:offset + 16]
            dec_value = int(hex_value, 16) / 10000
            print 'Active energy - Pricing 1: ' + str(dec_value) + ' kWh'
            result = result + ';' +  str(dec_value)

        search = '070100010802ff'
        offset = data.find(search)
        if (offset <> -1):
            offset = offset + len(search) + 14
            hex_value = data[offset:offset + 16]
            dec_value = int(hex_value, 16) / 10000
            print 'Active energy - Pricing 2: ' + str(dec_value) + ' kWh'
            result = result + ';' +  str(dec_value)

        search = '0701000f0700ff'
        offset = data.find(search)
        if (offset <> -1):
            offset = offset + len(search) + 14
            hex_value = data[offset:offset + 8]
            dec_value = int(hex_value, 16)
            print 'Active power: ' + str(dec_value) + ' W'
            result = result + ';' +  str(dec_value)

        search = '070100150700ff'
        offset = data.find(search)
        if (offset <> -1):
            offset = offset + len(search) + 14
            hex_value = data[offset:offset + 8]
            dec_value = int(hex_value, 16)
            print 'Active power - L1: ' + str(dec_value) + ' W'
            result = result + ';' +  str(dec_value)

        search = '070100290700ff'
        offset = data.find(search)
        if (offset <> -1):
            offset = offset + len(search) + 14
            hex_value = data[offset:offset + 8]
            dec_value = int(hex_value, 16)
            print 'Active power - L2: ' + str(dec_value) + ' W'
            result = result + ';' +  str(dec_value)

        search = '0701003d0700ff'
        offset = data.find(search)
        if (offset <> -1):
            offset = offset + len(search) + 14
            hex_value = data[offset:offset + 8]
            dec_value = int(hex_value, 16)
            print 'Active power - L3: ' + str(dec_value) + ' W'
            result = result + ';' +  str(dec_value)

        search = '070100000009ff'
        offset = data.find(search)
        if (offset <> -1):
            offset = offset + len(search) + 20
            hex_value = data[offset:offset + 6]
            dec_value = int(hex_value, 16)
            print 'Smart-Meter-ID: ' + str(dec_value)
            result = result + ';' +  str(dec_value)
    data = ''
    runs = 1
