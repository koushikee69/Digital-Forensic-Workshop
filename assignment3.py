import os
import argparse
import subprocess
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="input file")
parser.add_argument("output", type=str, help='output directory')
parser.add_argument("file", type=str, help='file type')
args = parser.parse_args()
file_names = os.listdir(args.input)
file_names=[file for file in file_names if os.path.isfile(os.path.join(args.input,file))]
print(file_names)
f=''
print(args.input)
print(args.output)
for i in range (0, len(file_names)):
    if file_names[i].endswith(".dd"):
        f=file_names[i]
        command=f"foremost -i {args.input}/{f} -o {args.output} -t {args.file}"#,stdout=subprocess.PIPE,shell=True, text=True
        print(command)
        r=subprocess.run(command,stdout=subprocess.PIPE,shell=True, text=True)
