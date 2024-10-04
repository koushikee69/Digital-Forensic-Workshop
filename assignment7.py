def extract_pids_from_file(filename, column_no):
    pids = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                columns = line.split()  
                if len(columns) >= 1:  
                    pid = columns[column_no]  
                    pids.append(pid)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return pids

def compare_pids(pslist_pids, psxview_pids):
    hidden_pids = []
    for pid in psxview_pids:
        if pid not in pslist_pids:
            hidden_pids.append(pid)
    return hidden_pids

def merge(list1, list2):
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

pslist_pids = extract_pids_from_file('pslist1', 0)
pslist_ppids = extract_pids_from_file('pslist1', 1) 
common = merge(pslist_pids, pslist_ppids)
psxview_pids = extract_pids_from_file('psxview1', 2)

hidden_pids = compare_pids(common, psxview_pids)

print("Hidden PIDs:")
for pid in hidden_pids:
    print(pid)
