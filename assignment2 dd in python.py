import os
import sys
import subprocess
directory=sys.argv[1]
output=sys.argv[2]
d=sys.argv[3]
z=None
if len(sys.argv)>4:
	z=sys.argv[4]
file_names = os.listdir(directory)
file_names=[file for file in file_names if os.path.isfile(os.path.join(directory,file))]
print(file_names)
for i in range(0,len(file_names)):
	if z=="zip":
		r=subprocess.run(f"{d} if={file_names[i]} | gzip > ./{output}/image{i}.dd.gz",stdout=subprocess.PIPE,shell=True, text=True)
	else:
		r=subprocess.run([d,f"if={file_names[i]}",f"of=./{output}/image{i}.dd"],stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
