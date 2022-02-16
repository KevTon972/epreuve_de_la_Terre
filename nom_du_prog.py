#!/usr/bin/env python3
#OU
#!/usr/bin/python3
 
#-*- coding:utf-8 -*-
import os

def chemin_du_prog():
    
    chemin = os.path.basename('/root/dir/sub/file.ext')

    print(chemin) 

chemin_du_prog()