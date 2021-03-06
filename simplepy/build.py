""" Build HTML examples for the simple Python to WASM compiler.
"""

import os
import wasmfun as wf
from simplepy import simplepy2wasm


for fname in os.listdir('.'):
    if fname.startswith('example') and fname.endswith('.py'):
        
        code = open(fname, 'rb').read().decode()
        wasm = simplepy2wasm(code)
        
        print('%s nbytes: %i' %(fname, len(wasm.to_bytes())))
        wasm_name = fname.replace('example', 'simplepy').replace('.py', '.html')
        
        wf.run_wasm_in_node(wasm)
        wf.export_wasm_example(wasm_name, code, wasm)


##

ii = wasm.sections[-1].functiondefs[0].instructions

for i in ii:
    i.show()


py = """
if 4 > 5:
    print(0)
elif 4 > 5:
    print(1)
else:
    print(2)
"""

m = simplepy2wasm(py)

print('='*80)
for i in m.sections[-1].functiondefs[0].instructions:
    i.show()
