def LBBT_tax(property_value):
    '''
    This function calculates tax based on the value of the property.
    
    Args:
        property_value: The value of the property we want to calculate the LBBT tax.

    Returns: The calculated tax based on the value of the property.
    '''

    # Up to £145,000          0%

    # £145,001 to £250,000    2%

    # £250,001 to £325,000    5%

    # £325,001 to £750,000    10%

    # Over £750,000           12%

    taxes = {   '1st band':{'lower':0,'upper':145000,'rate':0},
                '2nd band':{'lower':145000,'upper':250000,'rate':2},
                '3rd band':{'lower':250000,'upper':325000,'rate':5},
                '4th band':{'lower':325000,'upper':750000,'rate':10},
                '5th band':{'lower':750000,'upper':10000000000,'rate':12}
            }
            
    try:
        if property_value:
            tax = 0
            for key, value in taxes.items():
                if property_value > value['upper']:
                    tax += (value['upper'] - value['lower']) * value['rate'] / 100
                else:
                    tax += (property_value - value['lower']) * value['rate'] / 100
                    break
            return tax
        else:
            return 'please enter number'
    except TypeError as err:
        return err

if __name__ == '__main__':
    LBBT_tax()