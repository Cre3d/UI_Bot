def praisal(id, choice):
    from lxml import html
    import requests

    source = 'https://evepraisal.com/item/'
    source += str(id)
    if choice == 1:  # sell order min
        xpath_minerals = '//*[@id="jita"]/div/div[1]/table/tbody/tr[1]/td'
    elif choice == 2:  # sell order median
        xpath_minerals = '//*[@id="jita"]/div/div[1]/table/tbody/tr[2]/td'
    elif choice == 3:  # sell order average
        xpath_minerals = '//*[@id="jita"]/div/div[1]/table/tbody/tr[3]/td'
    elif choice == 4:  # buy order max
        xpath_minerals = '//*[@id="jita"]/div/div[2]/table/tbody/tr[1]/td'
    elif choice == 5:  # buy order median
        xpath_minerals = '//*[@id="jita"]/div/div[2]/table/tbody/tr[2]/td'
    elif choice == 6:  # buy order average
        xpath_minerals = '//*[@id="jita"]/div/div[2]/table/tbody/tr[3]/td'
    else:
        print("Choice Value Error")

    pagesource = requests.get(source)
    parsing = html.fromstring(pagesource.text)
    textvalue = parsing.xpath(xpath_minerals)
    try:
        return float(textvalue[0].text.replace('ISK', '').replace(',', ''))
    except IndexError:
        return 0
