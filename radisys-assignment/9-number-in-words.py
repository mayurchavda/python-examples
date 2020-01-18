numdict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: 'Zero'}
def get_str_digit(n):
    try:
        print(numdict[n])
    except KeyError:
        try:
            print(numdict[n - n % 10] + " " + numdict[n % 10])
        except KeyError:
            print('Number out of range')

get_str_digit(9)
get_str_digit(87)
get_str_digit(100)
