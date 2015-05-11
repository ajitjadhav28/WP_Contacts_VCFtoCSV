# Author : Ajit Jadhav
# E-mail : mr.ajitjadhav@live.com
# Descriptio : This program is written to create csv file from vcf backup file. 
# Program is specifically written to convert Windows phone contacts backup in vcf format
# to csv format so that it can be used anywhere. I have used google csv format.
# Date : 11/05/2015 

import sys

if(len(sys.argv)<2):
	print("\nError : Enter vcf or csv as argument..\n ex. Python3 contacts.vcf vcf")
	exit(0)
elif ((sys.argv[1]!="csv")and(sys.argv[1]!="vcf")):
	print("Wrong argumet entered Enter vcf or csv as argument..\n ex. Python3 contacts.vcf vcf")
	exit(0)
cn=open(input("Enter the backup file path with file extention .vcf to extract contacts: "),"r+")
p_list=["N:","FN:","BDAY;VALUE=DATE:","ADR;TYPE=HOME:","TEL;TYPE=CELL,VOICE:","TEL;TYPE=WORK,VOICE:","TEL;TYPE=HOME,VOICE:","URL:","EMAIL;TYPE=INTERNET:","EMAIL;TYPE=HOME","EMAIL;TYPE=WORK"]
csv_format="Name,Given Name,Additional Name,Family Name,Birthday,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 -Type,E-mail 2 - Value,E-mail 3 -Type,E-mail 3 - Value,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value,Phone 3 - Type,Phone 3 - Value,Address 1 - Type,Address 1 - Formatted"

con=""
a=0
b=0
for line in cn:
	if line[0:3]=="END":
		a+=1
print("Total contacts :"+str(a))
if sys.argv[1]=="vcf":
	cn.seek(0)
	path=str(input("Enter path to extract contacts(enter name & press enter for current directory) :"))
	for line in cn:
		con+=line
		if line[0:2]=="FN":
			name=line[3:].replace("\n","")
		if line[0:3]=="END":
			ncn=open(path+name+".vcf","w+")
			ncn.write(con)
			ncn.close()
			con=""
			b+=1
	cn.close()
	print("Total Contacts extracted from file "+str(b))
if sys.argv[1]=="csv":
	cn.seek(0)
	data=sn=fn=mn=bday=addr=p_home=p_cell=p_work=addr_type=p_ct=p_wt=p_ht=url=mail_work=mail_intr=mail_home=mail_it=mail_ht=mail_wt=""
	path=str(input("Enter full path to extract contacts with file name without extention(press enter for current directory) :"))
	ncn=open(path+".csv","w+")	
	for line in cn:
		for para in p_list:
			if line[:len(para)]==para:
				if(para==p_list[0]):
					name=line[2:].replace("\n","")
					sn=name[:name.find(";")]
					name=name[len(sn)+1:]
					fn=name[:name.find(";")]
					name=name[len(fn)+1:]
					mn=name[:name.find(";")]
				elif para==p_list[1]:
					Name=sn+" "+fn
				elif para==p_list[2]:
					bday=line[len(para):].replace("\n","")
				elif para==p_list[3]:
					addr="\""+line[len(para):]+"\"".replace("\n","")
					addr_type="Home"
				elif para==p_list[4]:
					p_cell=line[len(para):].replace("\n","")
					p_ct="Mobile"
				elif para==p_list[5]:
					p_work=line[len(para):].replace("\n","")
					p_wt="Work"
				elif para==p_list[6]:
					p_home=line[len(para):].replace("\n","")
					p_ht="Home"
				elif para==p_list[7]:
					url=line[len(para):].replace("\n","")
				elif para==p_list[8]:
					mail_intr=line[line.find(":")+1:].replace("\n","")
					mail_it="Other"
				elif para==p_list[9]:
					mail_home=line[line.find(":")+1:].replace("\n","")
					mail_ht="Home"
				elif para==p_list[10]:
					mail_work=line[line.find(":")+1:].replace("\n","")
					mail_wt="Work"
				else:
					pass
		if line.replace("\n","") =="END:VCARD":
			data += (Name+","+fn+","+mn+","+sn+","+bday+","+mail_ht+","+mail_home+","+mail_wt+","+mail_work+","+mail_it+","+mail_intr+","+p_ct+","+p_cell+","+p_wt+","+p_work+","+p_ht+","+p_home+","+addr_type+","+addr+"\n")
			sn=fn=mn=bday=addr=p_home=p_cell=p_work=addr_type=p_ct=p_wt=p_ht=url=mail_work=mail_intr=mail_home=mail_it=mail_ht=mail_wt=""

	ncn.write(csv_format+"\n"+data)
	print(str(a)+" contacts written in "+path+".csv")
	ncn.close()
	cn.close()
