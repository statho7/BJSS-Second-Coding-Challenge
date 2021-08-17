def LBBT_tax(property_value):
    '''
    Up to £145,000          0%

    £145,001 to £250,000    2%

    £250,001 to £325,000    5%

    £325,001 to £750,000    10%

    Over £750,000           12%
    '''
    # '''
    taxes = {   '1st band':{'lower':0,'upper':145000,'rate':0},
                '2nd band':{'lower':145000,'upper':250000,'rate':2},
                '3rd band':{'lower':250000,'upper':325000,'rate':5},
                '4th band':{'lower':325000,'upper':750000,'rate':10},
                '5th band':{'lower':750000,'upper':1000000000,'rate':12}
            }
    # '''
    # print(taxes['2nd band']['lower'], taxes['2nd band']['upper'], taxes['2nd band']['rate'])
    try:
        if property_value:
            if property_value <= 145000:
                return 0
            else:
                tax = 0

                if property_value > 250000:
                    tax += (250000 - 145000) * 0.02
                else:
                    return (property_value - 145000) * 0.02

                if property_value > 325000:
                    tax += (325000 - 250000) * 0.05
                else:
                    return tax + (property_value - 250000) * 0.05

                if property_value > 750000:
                    tax += (750000 - 325000) * 0.10 + (property_value - 750000) * 0.12
                else:
                    return tax + (property_value - 325000) * 0.10
                    
                return tax
        else:
            return 'please enter number'
    except TypeError as err:
        return err

if __name__ == '__main__':
    LBBT_tax()