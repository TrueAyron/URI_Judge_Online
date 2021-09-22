days = int(input())
years = days // 365
months = (days - years*365) // 30
days = (days - years*365 - months*30)

print("{} ano(s)".format(years))

print("{} mes(es)".format(months))

print("{} dia(s)".format(days))