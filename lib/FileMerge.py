# -*- coding: utf-8 -*-
__author__ = 'blfeng'
import os
class FileMerge:
    def filemerge(self,fdir,outfile):
        file_list = os.listdir(fdir)
        file_to_write = file(outfile,'w')
        for f in file_list:
            file_to_read = file(fdir+str(f),'r')
            #file_to_write.write('\r\n')
            while True:
                line = file_to_read.readline()
                if len(line) == 0:
                    break
                else:
                    file_to_write.write(line)
            file_to_read.close()
        file_to_write.close()
