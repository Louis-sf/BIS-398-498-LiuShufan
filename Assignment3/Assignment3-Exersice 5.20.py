# 5.20 (Display a Two-Dimensional List in Tabular Format) Define a
#function named display_table that receives a two-dimensional list
#and displays its contents in tabular format. List the column indices as
#headings across the top, and list the row indices at the left of each row

def display_table(List):
    length = 0
    for item in List:
        if len(item)>length:
            length = len(item)
    print('\t', end ='')
    for j in range(length):
        print( j+1, end ='\t')
    print()
    i=1
    for row in List:
        print(i, end='\t')
        i = i+1
        for item in row:
            print(item,end ='\t' )
        print()

#test for result:
a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81,]]
display_table(a)