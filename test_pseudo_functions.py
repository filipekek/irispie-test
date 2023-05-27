import sys
sys.path.append('..')
from irispie.parsers import pseudofunctions as pf
import re

def test(variable, manual, func, num=None):
    if num:
        resolved = pf.resolve_pseudofunctions(func+"("+variable+","+num+")")
    if not num:
        resolved = pf.resolve_pseudofunctions(func+"("+variable+")")
    assert resolved == manual

variable_list = ['x', 'log(x)+3*y']
func_list = ['diff', 'difflog', 'movavg', 'movsum', 'movprod', 'pct', 'roc']
manual_list = ['((x)-(x[-1]))',
               '((log(x)+3*y)-(log(x[-1])+3*y[-1]))',
               '(log(x)-log(x[-1]))',
               '(log(log(x)+3*y)-log(log(x[-1])+3*y[-1]))',
               '(((x)+(x[-1])+(x[-2])+(x[-3]))/4)',
               '(((log(x)+3*y)+(log(x[-1])+3*y[-1])+(log(x[-2])+3*y[-2])+(log(x[-3])+3*y[-3]))/4)',
               '((x)+(x[-1])+(x[-2])+(x[-3]))',
               '((log(x)+3*y)+(log(x[-1])+3*y[-1])+(log(x[-2])+3*y[-2])+(log(x[-3])+3*y[-3]))',
               '((x)*(x[-1])*(x[-2])*(x[-3]))',
               '((log(x)+3*y)*(log(x[-1])+3*y[-1])*(log(x[-2])+3*y[-2])*(log(x[-3])+3*y[-3]))',
               '(100*(x)/(x[-1])-100)',
               '(100*(log(x)+3*y)/(log(x[-1])+3*y[-1])-100)',
               '((x)/(x[-1]))',
               '((log(x)+3*y)/(log(x[-1])+3*y[-1]))'
]
manual_list_nums = ['((x)-(x[-2]))',
                    '(log(x)-log(x[-2]))',
                    '(((x)+(x[-1])+(x[-2])+(x[-3])+(x[-4]))/5)',
                    '((x)+(x[-1])+(x[-2])+(x[-3])+(x[-4]))',
                    '((x)*(x[-1])*(x[-2])*(x[-3])*(x[-4]))',
                    '(100*(x)/(x[-2])-100)',
                    '((x)/(x[-2]))'
]

x = -1
for i in func_list:
    x += 1
    test(variable_list[0], manual_list[x], i)
    x += 1
    test(variable_list[1], manual_list[x], i)

for i in func_list:
    if re.search('mov', i):
        test(variable_list[0], manual_list_nums[func_list.index(i)], i, '-5')
    else:
        test(variable_list[0], manual_list_nums[func_list.index(i)], i, '-2')

