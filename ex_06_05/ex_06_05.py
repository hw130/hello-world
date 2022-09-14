str = 'X-DSPM-Confidence: 0.8475'

ipos=str.find(':')
print(ipos)
piece=str[ipos+2:]
print(piece)
#print(piece+42.0) error: 문자열과 float를 더할 수 없음.
value=float(piece)
print(value)
