# WP_Contacts_VCFtoCSV and VCFtoVCF
Converts contacts from windows phone contacts backup which is in vcf to csv

Few days ago Windows Phone got an update to create contacts backup on sd card. 
It creates backup in vcf format. It is single vcf file that contains all your contacts.
If you want to use this backup on other platforms (phones,Computers, google contacts, android..) you need to conver it in csv format.
You can also convert the file in multiple vcf files. So each file contains single contact. Some older phones
requires this types of contacts to import.
      You can also create csv file from directory that contain multiple vcfs.

-------------------------------------------------------------------------------------------------------------------------
## Requirements:
      The only requirement is [Python3] should be installed.
-------------------------------------------------------------------------------------------------------------------------

# How to use
## 1. Convert from vcf to csv -
      Give csv as argument as following-
      python3 wp_vcf2csv.py csv
## 2. Convert from vcf to vcfs -
      Give vcf as argument as following-
      python3 wp_vcf2csv.py vcf
## 3. Convert from multiple vcfs from directory to csv
      argument - mvcf2csv -
      python3 wp_vcf2csv.py mvcf2csv
 @ Note - Always use full paths while giving file path
 
-------------------------------------------------------------------------------------------------------------------------
[Python3]:https://www.python.org/downloads/
