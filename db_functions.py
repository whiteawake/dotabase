def print_Records(records, fields = None, id = None):
    if id == None:
	style = 'style="border: 1px solid black; border-collapse: collapse;"'
    else:
	style = 'id=' + id
    if len(records) > 0:
	print '<table ' + style + '>'
	if fields != None:
	    print '<tr>'
	    for field in fields:
	        print'<th style="border: 1px solid black;">' + str(field) + '</th>'
	    print '</tr>'
	    
	for record in records:
	    print '<tr>'
	    for field in record:
	        print'<td style="border: 1px solid black;">' + str(field) + '</td>'
	    print '</tr>'
	print '</table>'                         
    else:
	print('[No records found]')