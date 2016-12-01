rem Nand Flash Write amplification Factor Measurement using iometer
rem WorkFlow: 
rem Secure erase Nand Flash => Precondition => Write amplification Factor Measurement ==> Get smart data using CrystalDiskInfo app
rem Tool nees:
rem 1. CrystalDiskinfo 2. Iometer

cls
@echo off

echo **  Nand flash Write amplification Factor Measurement using iometer
echo **  Version 1.3
echo **
IF [%1] EQU [] GOTO END
echo **  Test using DriveNum=%1
echo **
echo on
@echo off

REM ==================================================
REM Profile 
REM ==================================================
set DriveNum=%1%
set config_zero=4KRW_32_6.icf
set config_one=4KRW_32_2.icf
set result_zero=Pre_4KRW_32_6
set result_one=Run_4KRW_32_2
set smart_zero=PreSMT_4KRW_32_6
set smart_one=RunSMT_4KRW_32_2

REM ==================================================
REM MAIN PROG. 
REM ==================================================

pause 

echo STEP0: * Secure Erase Disk %DriveNum%
echo.
se -n %DriveNum%
pause

echo STEP1: * Precondition - 4K_RW x 6 hr - iometer /c %config_zero%
echo.
iometer /c %config_zero% /r %result_zero%.txt

echo STEP2: * Precondition - Gather SMART value in %smart_zero% file
.\CrystalDiskInfoPortable\App\CrystalDiskInfo\DiskInfo.exe /CopyExit 
move .\CrystalDiskInfoPortable\App\CrystalDiskInfo\diskinfo.txt %smart_zero%
echo.
echo STEP3: * Run - 4KRW_2hr - iometer /c %config_one%
iometer /c %config_one% /r %result_one%.txt
echo.
echo STEP4: * Precondition - Gather SMART value in %smart_one% file
.\CrystalDiskInfoPortable\App\CrystalDiskInfo\DiskInfo.exe /CopyExit 
move .\CrystalDiskInfoPortable\App\CrystalDiskInfo\diskinfo.txt %smart_one%
echo.
pause

GOTO EXIT

:END
echo ** usage:
echo **
echo ** wafmio [DiskPhysicalNum]
echo **
echo ** wafmio 1
echo **
echo.
wmic diskdrive get deviceID,model
exit /b 5


:EXIT
echo !!! Finished !!!
