import re, subprocess
 
 
def check_CPU_temp():
    temp = None
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)   # a solution with a  regex 
        try:
            temp = float(m.group())
        except:
            pass
    return temp, msg
 
temp, msg = check_CPU_temp()
 
print( "temperature (" + u'\xb0' + "C): ", temp)
print( "full message:    ", msg)
 #which returns uns a floating point value  and furtermore additionally the original message in which it is contained.