__author__ = 'shengwen'
import openpyxl
# 1604
def loadCaptainID(cap_id_dict, src = "captid_career_voy_link"):
    wb = openpyxl.load_workbook(filename=src + ".xlsx", read_only= True)
    ws = wb.get_sheet_by_name(src)
    rowN = ws.max_row
    colN = 4
    # for r_index in range(2, 100):
    for r_index in range(2, rowN + 1):
        print "row:", r_index
        try:
            val= ws.cell(row = r_index, column = 1).value
            val = val.replace(", ", " ")
            id_cap_dict[ int(ws.cell(row = r_index, column = 2).value)] =  val
            id_cap_dict[ int(ws.cell(row = r_index, column = 4).value)] =  ws.cell(row = r_index, column = 3).value
        except:
            print "row", r_index, "has error, skipped!"
    # for row in ws.rows:
    #     for cell in row:
    #         print cell.value
    # 1295
def loadCapInfo(cap_info_dict, src="careers_clean"):
    wb = openpyxl.load_workbook(filename=src + ".xlsx", read_only= True)
    ws = wb.get_sheet_by_name(src)
    rowN = ws.max_row
    print rowN
    #birthloc_capt1	POCC_capt1	marriage_capt2 lastname_capt2
    colIndices = [4, 6, 9] # left for last name
    for r_index in range(3, rowN + 1):
    # for r_index in range(3, 100):
        try:
            name = ws.cell(row = r_index, column = 2).value
            name = name.replace("=", " ")
            name = name.replace("  ", " ")
            if name not in cap_info_dict:
                cap_info_dict[name] = ["", "", "", ""]
            print "row:", r_index
            cap_info_dict[name][3] = name.split()[1]
            for index in range(3):
                c_index = colIndices[index]
                val = ws.cell(row = r_index, column = c_index).value
                if val is not None:
                    cap_info_dict[name][index] = val
        except:
            print "row", r_index, "has error, skipped!"
        # for c_index in colIndices:
        #     val = ws.cell(row = r_index, column = c_index).value
        #     if val is None:
        #         cap_info_dict[name].append("")
        #     else:
        #         cap_info_dict[name].append(val)

def fillCaptainNetwork(id_cap_dict, cap_info_dict, src="captain_captain_network"):
    wb = openpyxl.load_workbook(filename=src + ".xlsx")
    cap_id_indices = [3, 4]
    col_indices = [i for i in range(11, 19)]
    ws = wb.get_sheet_by_name(src)
    rowN = ws.max_row
    print rowN
    for r_index in range(3, 10):
        print r_index
        for col_index in col_indices:
            ws.cell(row=r_index, column=col_index).value = "test"
    wb.save(src + ".xlsx")

def store_table(id_cap_dict, cap_info_dict):
    id_cap_src = "./id_cap_table"
    cap_info_src = "./cap_info_dict"
    res = []
    for key in id_cap_dict:
        try:
            name = id_cap_dict[key]
            if name in cap_info_dict:
                res.append(",".join([str(key)] + [name] + cap_info_dict[name]) + "\n")
        except:
            print "key", key, " has error, skipped!"
    with open("link_table.csv","w+") as fout:
        fout.writelines(res)
def get_table(link_table):
    with open("link_table.csv") as fin:
        lines = fin.read().splitlines()
    for line in lines:
        try:
            data = line.split(",")
            link_table[data[0]] = [i for i in data[1:]]
        except:
            print "key", line, " has error, skipped!"
id_cap_dict = {}
cap_info_dict = {}
link_table = {}
loadCaptainID(id_cap_dict)
print "loadCaptainID done"
loadCapInfo(cap_info_dict)
print "loadCaptainInfo Done"
store_table(id_cap_dict, cap_info_dict)
print "store_link_table"
get_table(link_table)
print "link_table done"
print link_table
# print cap_info_dict
# fillCaptainNetwork(id_cap_dict, cap_info_dict)


