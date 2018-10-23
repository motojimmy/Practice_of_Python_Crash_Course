print("\n******************************************************")
print("< 8-15 >\n")
from Module_8 import printing_functions as pf, printing_functions

pf.list_print('fang_jian', 'motojimmy',
              'jay_zhou', 'zhou jie lun')


print("\n******************************************************")
print("< 8-16 >\n")

printing_functions.list_print('1', 'fang_jian', 'motojimmy',
              'jay_zhou', 'zhou jie lun')


from Module_8.printing_functions import list_print

list_print('2', 'fang_jian', 'motojimmy',
            'jay_zhou', 'zhou_jie_lun')

from Module_8.printing_functions import list_print as lp

lp('3', 'fang_jian', 'motojimmy',
   'jay_zhou', 'zhou jie lun')

import Module_8.printing_functions as pf

pf.list_print('4', 'fang_jian', 'motojimmy',
              'jay_zhou', 'zhou jie lun')

from Module_8.printing_functions import *

list_print('5', 'fang_jian', 'motojimmy',
            'jay_zhou', 'zhou_jie_lun')


print("\n******************************************************")
print("< 8-17 >\n")

print('Done!')



