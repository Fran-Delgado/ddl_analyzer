import re

filein  = r"ddl_analyzer\DDL_PREUSA_.D220120.txt"
filein_red = "DDL_PREUSA_.D220120.txt"

def init_count():
    count_out_create_table     = 0
    count_out_create_view      = 0
    count_out_create_index     = 0
    count_out_create_uindex    = 0
    count_out_create_grant     = 0
    count_out_create_comment   = 0
    count_out_create_synonym   = 0
    count_out_create_alias     = 0
    count_out_create_sequence  = 0
    count_out_create_resto     = 0
    return count_out_create_table,     \
           count_out_create_view,      \
           count_out_create_index,     \
           count_out_create_uindex,    \
           count_out_create_grant,     \
           count_out_create_comment,   \
           count_out_create_synonym,   \
           count_out_create_alias,     \
           count_out_create_sequence,  \
           count_out_create_resto  

def files_out(filein_red):
    out_create_table    = filein_red + "_" + "create_table.txt"
    out_create_view     = filein_red + "_" + "create_view.txt"
    out_create_index    = filein_red + "_" + "create_index.txt"
    out_create_uindex   = filein_red + "_" + "create_uindex.txt"
    out_create_grant    = filein_red + "_" + "create_grant.txt"
    out_create_synonym  = filein_red + "_" + "create_synonym.txt"
    out_create_alias    = filein_red + "_" + "create_alias.txt"
    out_create_comment  = filein_red + "_" + "create_comment.txt"
    out_create_sequence = filein_red + "_" + "create_sequence.txt"
    out_create_resto    = filein_red + "_" + "create_resto.txt"
    return out_create_table,    \
           out_create_view,     \
           out_create_index,    \
           out_create_uindex,   \
           out_create_grant,    \
           out_create_synonym,  \
           out_create_alias,    \
           out_create_comment,  \
           out_create_sequence, \
           out_create_resto   

def print_totals(count_out_create_table, count_out_create_view, count_out_create_index, count_out_create_uindex, count_out_create_grant, count_out_create_comment, count_out_create_synonym, count_out_create_alias, count_out_create_sequence, count_out_create_resto):
    print(f"Create table        = {count_out_create_table}")    
    print(f"Create view         = {count_out_create_view}")     
    print(f"Create index        = {count_out_create_index}")    
    print(f"Create unique index = {count_out_create_uindex}")   
    print(f"Grant               = {count_out_create_grant}")    
    print(f"Create comment      = {count_out_create_comment}")  
    print(f"Create Synonym      = {count_out_create_synonym}")  
    print(f"Create alias        = {count_out_create_alias}")    
    print(f"Create sequence     = {count_out_create_sequence}") 
    print(f"Resto               = {count_out_create_resto}")


out_create_table,          \
out_create_view,           \
out_create_index,          \
out_create_uindex,         \
out_create_grant,          \
out_create_synonym,        \
out_create_alias,          \
out_create_comment,        \
out_create_sequence,       \
out_create_resto = files_out(filein_red)

count_out_create_table,    \
count_out_create_view,     \
count_out_create_index,    \
count_out_create_uindex,   \
count_out_create_grant,    \
count_out_create_comment,  \
count_out_create_synonym,  \
count_out_create_alias,    \
count_out_create_sequence, \
count_out_create_resto = init_count()

with open(filein,'r') as filein  ,                                   \
     open(out_create_table       ,'w') as file_out_create_table,     \
     open(out_create_view        ,'w') as file_out_create_view,      \
     open(out_create_index       ,'w') as file_out_create_index,     \
     open(out_create_uindex      ,'w') as file_out_create_uindex,    \
     open(out_create_grant       ,'w') as file_out_create_grant,     \
     open(out_create_comment     ,'w') as file_out_create_comment,   \
     open(out_create_synonym     ,'w') as file_out_create_synonym,   \
     open(out_create_alias       ,'w') as file_out_create_alias,     \
     open(out_create_sequence    ,'w') as file_out_create_sequence,  \
     open(out_create_resto       ,'w') as file_out_create_resto:
     content_filein = filein.readlines() 
     for count,line in enumerate(content_filein):
        if line.find(" TABLE ") != -1:
            if line.find(" GRANT ") != -1:
                count_out_create_grant +=1
                file_out_create_grant.write(line)    
            elif line.find(" COMMENT ") != -1:
                count_out_create_comment +=1
                file_out_create_comment.write(line)    
            else:
                count_out_create_table +=1
                file_out_create_table.write(line)
        elif line.find(" VIEW ") != -1:
            count_out_create_view +=1
            file_out_create_view.write(line)
        elif line.find(" INDEX ") != -1:
            if line.find(" UNIQUE INDEX ") != -1:
                count_out_create_uindex +=1   
                file_out_create_uindex.write(line)   
            else:
                count_out_create_index +=1
                file_out_create_index.write(line)
        elif line.find(" GRANT ") != -1:
            count_out_create_grant +=1
            file_out_create_grant.write(line)
        elif line.find(" ALIAS ") != -1:
            count_out_create_alias +=1
            file_out_create_alias.write(line)
        elif line.find(" SYNONYM ") != -1:
            count_out_create_synonym +=1
            file_out_create_synonym.write(line)
        elif line.find(" SEQUENCE ") != -1:
                out_create_sequence +=1 
                file_out_create_sequence.write(line)
        else:
            count_out_create_resto +=1
            file_out_create_resto.write(line)


print_totals(count_out_create_table, 
             count_out_create_view, 
             count_out_create_index, 
             count_out_create_uindex, 
             count_out_create_grant, 
             count_out_create_comment, 
             count_out_create_synonym, 
             count_out_create_alias, 
             count_out_create_sequence, 
             count_out_create_resto)    
