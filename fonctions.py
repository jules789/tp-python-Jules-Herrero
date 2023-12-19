#Fonction 1

def produce_default_dict():
    default_dict = {'root': 'password'}
    return default_dict

print(produce_default_dict())




#Fonction 2

def salutation(nom, age):
    print(f"Bonjour '{nom}', vous avez actuellement {age} ans.")

salutation("Jules", 21)


#Fonction 3

def power_2(limit):
    result = []
    for i in range(0, limit):
        valeur = 2 ** i
        if valeur < limit:
            result.append(str(valeur))
        else:
            break
    print(','.join(result))

power_2(10)


#Fonction 4

def check_ip_format(ip):
    ip_split = ip.split('.')
    if len(ip_split) != 4:
        return False
    for i in ip_split:
        if not i.isdigit():
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True
    

print(check_ip_format('10.0.0.0'))  
print(check_ip_format('192.12.'))   
    
    






