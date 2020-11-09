import subprocess as sp
import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as py
import platform
my_system = platform.uname()

print("\t\t WELCOME TO THE HOME MENU ")
print("\t\t ******************************** ")

print('''\n\n
1.  start AWS menu
2.  start webserver 
3.  start lvm menu
4.  start hadoop menu
5.  start docker menu''')

rcz=sr.recognizer()
with sr.Microphone() as source:
	py.speak("I have created a home menu for your help.Say it loud, what do you want to start? ")
	audio=rcz.listen(source)
	py.speak("i got it, please wait...")
main=rcz.recognize_google(audio)


def aws():
   if my_system.system == 'Windows' :
        os.system('cls')
    elif my_system.system == 'Linux' :
        os.system('clear')
    else :
        print("We are Sorry but the program is not meant for your OS")
        exit()
  print("\t\t Welcome to AWS Menu")
  print("\t\t *************************** ")
  print('''\n\n
  1. open ec2 services
  2. open s3
  3. create cloudfront destribution
  4. exit to home menu''')
  
  rcz=sr.recognizer()
  with sr.Microphone() as source:
	  py.speak("here is your aws menu, tell you request now ")
	  audio=rcz.listen(source)
	  py.speak("i got it, please wait...")
  main=rcz.recognize_google(audio)
  aws=main.lower()
  if 'open ec2 services' in ws:
    ec2()
  elif 'open s3' in ws:
    s3()
  elif 'open cloudfront services' in ws:
    cf()
  elif 'exit to home menu' in ws:
    break
  else :
    print("Doesn't support")
    py.speak("please select from menu")

    
def ec2():
  if my_system.system == 'Windows' :
        os.system('cls')
    elif my_system.system == 'Linux' :
        os.system('clear')
    else :
        print("We are Sorry but the program is not meant for your OS")
        exit()
  print('''\n\n
  1. create key pair
  2. create security group
  3. create  volume
  4. lauch instance
  5. attach volume
  6. go back to aws menu''')
  rcz=sr.recognizer()
  with sr.Microphone() as source:
    print("\t\t start saying")
	  py.speak("tell your ec2 request ")
	  audio=rcz.listen(source)
	  py.speak("i got it, please wait...")
  main=rcz.recognize_google(audio)
  ec=main.lower
  if 'create key pair' in ec:
		key=input("Enter the key name: ")
		sp.getoutput('aws ec2 create-key-pair --key-name {0} --query "KeyMaterial" --output text > {1}.pem'.format(key,key))
		print(f"\n\t\t key {key} is created ")
    input("Press enter to continue....")
  elif 'create security group' in ec:
    sg=input("Enter the security group name: ")
		des=input("Enter the description: ")
		sp.getoutput('aws ec2 create-security-group --group-name "{0}" --description "{1}" '.format(sg,des))
		print(f"\n\t\t Security Group {sg} is created \n")
		inp=input('For adding inbound rules press "y" ')
		if (inp=='y'):
			gid=input("Enter the group id :")
			while (1):
				pr=input("Enter the protocol port: ")
				cidr=input("Enter the range of IPv4 address in format of 0.0.0.0/0 for VPC: ")
				sp.getoutput("aws ec2 authorize-security-group-ingress --group-id {0} --protocol tcp --port {1}  --cidr {2}".format(gid,pr,cidr))
				print(f"\n\t\t rule added to the security group {sg}  ")
				in1=input('For adding more inbound rules press "y" ')
				if in1!='y':
					break
    input("Press enter to continue....")
  elif "create a volume" in ec:
		az=input("Enter the availability zone: ")
		sz=int(input("Enter the size of volume: ")
		p=sp.getoutput("aws ec2 create-volume --availability-zone {0} --size {1} ".format(az,sz))
		print(f"\n\t\t volume has been created with size {sz} in availabilty zone {az} ")
    
    
  



