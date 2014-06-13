time = None
while not time:
    try:
        time = int(raw_input('Time in seconds: '))
    except ValueError:
        print 'Invalid Number'
hundredths = float (time)/60
minutes = time/60
while hundredths > 1:
    hundredths -= 1
hundredths *= 60
print str(minutes) + ':' + str(hundredths)