# iometerTools
Store the iomerter tools and some useful script or python file

# wafmio.cmd
Nand Flash Write amplification Factor Measurement using iometer
WorkFlow: 

       Secure erase Nand Flash => Precondition => 
       Write amplification Factor Measurement ==> 
       Get smart data using CrystalDiskInfo app

Tool Requirement:
* CrystalDiskinfo 
* Iometer 
* se (3rd security erase tools)

# iometer_result_parser.py
Parsing the iometer logging file to csv format

Usage

     iometer_result_parser.py [folder path]
