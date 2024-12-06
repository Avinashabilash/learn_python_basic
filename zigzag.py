alphabets="abcdxyz"
n=len(alphabets)
if n%2==0:
    med_value=(alphabets[(n//2)-1]+alphabets[(n//2)])/2
    taken=alphabets[0]+med_value+alphabets[-1]
    between_values = alphabets[1:(n // 2) - 1] + alphabets[(n // 2) + 1:-1]
    #print(between_values)
else:
    med_value=alphabets[n//2]
    taken=alphabets[0]+med_value+alphabets[-1]
    between_values = alphabets[1:(n // 2)] + alphabets[(n // 2) + 1:-1]
    print(taken)
    print(between_values)
zigzag_out=""
taken_index=0
between_index=0
while taken_index<len(taken)or between_index<len(between_values):
    if taken_index<len(taken):
        zigzag_out+=taken[taken_index]
        taken_index+=1
        print(taken_index)
    if between_index<len(between_values):
        zigzag_out+=between_values[between_index]
        between_index+=1
        print(between_index)
        
print(zigzag_out)
