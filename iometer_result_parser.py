# coding: utf-8

# In[1]:

# iometer result parser
#/usr/bin/python

# In[2]:

import os,sys,csv,glob,argparse
ver = 1.51


# In[11]:

if len(sys.argv) < 2:
    print "Usage: %s [folder path]" %(sys.argv[0])
    sys.exit()


print "\n\t***** Iometer csv log file transfer tool: %s *****\n" %(ver)

csvfile = []
try:
    for csvfiles in glob.glob(sys.argv[1] + '\\*.csv'):
        csvfile.append(csvfiles)

    for j,fileitem in enumerate(csvfile):
        fheader = fileitem.split(sys.argv[1] + "\\")[1].split('.')[0]

        logftp = open(sys.argv[1] + '\\' + fheader + "_p.csv","a+")
        n = 0
        print "\t\t-----Round %s/%s -----" %(j+1,len(csvfile))
        print "PHASE 1: Read %s ... " %(fileitem)
        with open(fileitem,"r") as f:
			# Write Title
            logftp.write("Target Type,Target Name,Access Specification Name,# Managers,# Workers,# Disks,IOps,Read IOps,Write IOps,MBps (Binary),Read MBps (Binary),Write MBps (Binary),MBps (Decimal),Read MBps (Decimal),Write MBps (Decimal),Transactions per Second,Connections per Second,Average Response Time,Average Read Response Time,Average Write Response Time,Average Transaction Time,Average Connection Time,Maximum Response Time,Maximum Read Response Time,Maximum Write Response Time,Maximum Transaction Time,Maximum Connection Time,Errors,Read Errors,Write Errors,Bytes Read,Bytes Written,Read I/Os,Write I/Os,Connections,Transactions per Connection,Total Raw Read Response Time,Total Raw Write Response Time,Total Raw Transaction Time,Total Raw Connection Time,Maximum Raw Read Response Time,Maximum Raw Write Response Time,Maximum Raw Transaction Time,Maximum Raw Connection Time,Total Raw Run Time,Starting Sector,Maximum Size,Queue Depth,% CPU Utilization,% User Time,% Privileged Time,% DPC Time,% Interrupt Time,Processor Speed,Interrupts per Second,CPU Effectiveness,Packets/Second,Packet Errors,Segments Retransmitted/Second\n")
            for line in f:
                if "ALL,All," in line:
                    logftp.write(line)
                    os.fsync(logftp)
        logftp.close()
    print "Done"
except Exception:
    print Exception.message
    print "Error Processing ... "

