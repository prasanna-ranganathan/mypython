
import re,sys

with open(sys.argv[1],'r') as f1:
    data = f1.readlines()

txt=''

with open(sys.argv[1],'r') as f3:
    severity=True
    default=4
    vmowner=True
    default_VM = "Prasanna Ranganathan"

    for line in f3:
        if line.strip().startswith('_SEV'):
            severity=False

        if line.strip().startswith('_VMOWNER'):
            vmowner=False

    if severity:
        txt = txt + "_SEV\t\t\t\t" + str(default) + "\n"

    if vmowner:
        txt = txt + "\t_VMOWNER\t\t\t" + str(default_VM) + "\n"
    txt = txt + "_SEVOWNER\t\t\tSRINIVAS,AVIREDDY\n"
    txt = txt + "}\n"

with open(sys.argv[1],'r+') as f2:
    for line in data:
        if line.strip().startswith('}'):
            line = line.replace('}',txt)
#        f2.write(line)
        print line,
