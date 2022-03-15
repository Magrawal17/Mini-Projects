import time, random, datetime, smtplib, getpass

thedate = datetime.date.today()

#-- adds employee into list if they are not in the list --#
emplist=[]

#-- fuction for shiftwork --#
def shiftwork():
    employee=input('What is your name?\n')

    while (employee.isdigit()) or (employee==''):
        print('Please try again.\n')
        employee=input('What is your name?\n')

    if employee in emplist:
        pass
    else:
        emplist.append(employee)

    coolphrase=['Hi this is','Whats up it\'s','Hello it\'s me again','Hey stranger! it\'s me again','Long time no see, it\'s']

    emplname=(random.choice(coolphrase))+' %s'%(employee.title())+'. \n'
    worklog=open('worklog.txt','w')
    worklog.write('Todays date: '+str(thedate)+'\n')
    worklog.write(emplname)
    worklog.close()
    print(('Greetings %s,')%(employee.title())+'\n')

    time.sleep(0.5)



    print('What shift did you work?')
    day=input('Morning (m), Afternoon (a),Evening (e) \n')
    if (day== 'm') or (day =='M'):
        day=['I worked the morning shift today\n','Well I worked the morning shift.\n','I did the morning shift today.\n','I was on the morning shift.\n']
        worklog=open('worklog.txt','a')
        worklog.write(random.choice(day))
        worklog.close()
        print ('Morning')
        #print ('Morning')

    elif (day== 'a') or (day =='A'):
        day=['Once again I worked the afternoon shift\n','Well I worked the afternoon shift.\n','I did the afternoon shift today.\n','I was on the afternoon shift.\n']
        worklog=open('worklog.txt','a')
        worklog.write(random.choice(day))
        worklog.close()
        print ('Afternoon')
    elif (day== 'e') or (day =='E'):
        day=['Hey buddy I worked the evening.\n','Well I worked the evening shift.\n','I did the evening shift today.\n','I was on the evening shift.\n']
        worklog=open('worklog.txt','a')
        worklog.write(random.choice(day))
        worklog.close()
        print ('Evening')
    else:
        time.sleep(0.5)
        print(day)

    call=0
    while call<3:
        calllist=['Today I took ','Well on my shift I took ','Well until now I took ','It was a easy ','Honestly I only took a total of ']
        calls=input('how many hours did you work?\n')
        if (calls.isdigit()):
            worklog=open('worklog.txt','a')
            worklog.write(random.choice(calllist)+calls+' calls today.\n')
            worklog.close()
            break
        else:
            time.sleep(0.5)
            print('Not a number.')
            time.sleep(0.5)
            print(calls)
             
        call+=1

    chars=0
    while chars<300:
        final=input('Any comments? Yes(y),No(n)\n')
        if (final=='y') or (final=='Y'):
            final=input('Type additional comments: \n')
            worklog=open('worklog.txt','a')
            if chars%16==0:
                worklog.write(final+'\n')
            else:
                worklog.write(final)
            worklog.close()
        elif (final=='n') or (final=='N'):
            worklog.close()
            print('Done see you tomorrow.')
            break
        else:
            break
        chars+=len(final)
        print(chars)

    print('\nFile was auto-saved as worklog.txt on your drive for refrence')
    print('Take care folks!')
    print('Current date is: '+str(thedate))

#-- Initial question to begain workflow --
q=0
while q<1:
    print('Welcome to my Python Program to enter your shiftwork details')
    print('Are you ready to submit log for today?')
    question=input('Type: yes(y),no(n)\n')
    if (question=='y') or (question=='Y'):
        shiftwork()
    elif (question=='n') or (question=='N') or (question==''):
        break
    else:
        print('please try again..\n')
    q+=1

#-- gathers information to log into gmail account --#
email=input('\nEnter your Gmail email to login\n')
print('\nEnter your Gmail passowrd to complete login\n')
print('Plese note that nothing you type shows for security reasons')
password = getpass.getpass()
#print(password)
to=input('\nEnter email address of recipent\n')
subject=input('Subject:\n')
emailbody=input('Type Your email body here (example: here is the report from our work day. Check it out!)\n')
subject_emailbody='Subject:{}\n\n{}'.format(subject,emailbody)


#-- log into email with infomation provided --#
netconnect = smtplib.SMTP('smtp.gmail.com',587)
netconnect.starttls()
netconnect.login(email,password)
print(netconnect.sendmail(email,to,subject_emailbody))
netconnect.quit()
