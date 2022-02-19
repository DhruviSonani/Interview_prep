import sys
def currency(fx_rate_l, original_currency, target_currency):  
    fx_rate_l = [str(i) for i in fx_rate_l.split(";")]  
    fx_rate_l = fx_rate_l[:-1]
    fx_rate = []
    
    for i in range(len(fx_rate_l)):
        l = []
        for j in (fx_rate_l[i]).split(","):
            l.append(j)                 
    fx_rate.append(l)
    max_list = [-1.0]
    temp_list = []
    Temp = ''
    mult = None
    for val in fx_rate:
        if val[0] == original_currency and val[1] == target_currency:
            max_list.append(float(val[-1]))
        elif val[0] == original_currency:
            Temp = val[1]
            temp_list.append(float(val[-1]))
        elif val[1] == target_currency and Temp == val[0]:
            temp_list.append(float(val[-1]))
    
    for i in temp_list:
            mult+=i
            max_list.append(mult)     
    return max(max_list)             
    
param  = [];    
for line in sys.stdin:
    param.append(line)
    
print(currency(param[0], param[1], param[2])   )


#java


String line;
    while ((line = in.readLine()) != null) {
      System.out.println(line);
    }
