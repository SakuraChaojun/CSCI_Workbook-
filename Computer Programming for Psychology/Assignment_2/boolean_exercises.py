#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: chaojunma
"""

number_1 = 1
float_1 = 1.0

string_1 = '1'
string_float = '1.0'

number_5 = 5
equation = 3+2 


#Are 1 and 1.0 equivalent

result_1 = number_1 == float_1

#Are "1" and "1.0" equivalent?

result_2 = string_1 == string_float

#Are 5 and (3+2) equivalent

result_3 = number_5 == equation


and_statements = result_1 and result_2 and result_3

or_statements =  result_1 or result_2 or result_3

andnot_statements = result_1 and not result_2 and not result_3 

ornot_statements = result_1 or not result_2 or not result_3

# List 5 ways to get True as your output.

or_and_statements = (result_1 or result_2) and result_3

notand_and_statements = (not(result_1 and result_2))and result_3

and_or_statements = (result_1 and result_3) or result_2

not_andand_statements = not (result_1 and result_2 and result_3)
 
and_not_and_statements = result_1 and not result_2 and result_3



