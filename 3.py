import os
root_path = os.getcwd()
#print(root_path)
offset = len(root_path.split("\\"))
for root,files,dirs in os.walk(root_path):
	current_dir = root
	path_list = current_dir.split("\\")
	indent_level = len(path_list) - offset 
	print("\t"*indent_level,"\\",path_list[-1])
	#print(files)
	#print(dirs)
	# for f in files:
	# 	print(f)
	for d in dirs:
	 	#print(d)
	 	dirs_name = os.path.splitext(d)[0]
	 	print("\t"*(indent_level+1),dirs_name)
		
		
		
import os
root_path=os.getcwd()
offset = len(root_path.split("\\"))

for root,dirs,files in os.walk(root_path):
	current_dir = root.split("\\")
	indent=len(current_dir)-offset
	print("\t"*indent,"\\"+current_dir[-1])
	for f in files:
		print("\t"*(indent+1),f)
  
