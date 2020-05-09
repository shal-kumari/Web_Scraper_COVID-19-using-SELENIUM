from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
import datetime
import smtplib
import credentials                               #Defined in my local computer. Declare it in your own computer before execution.

driver=webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.covid19india.org/")              #Opens browser and navigates to url
sleep(2)

def extractor():
    
    #Extracts HTML elements using full xpath 
    TCases = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/h1")    #xpath corresponding to total cases
    TActive = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/h1")   #xpath corresponding to total active cases
    TRecov = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/h1")    #xpath corresponding to total recoveries
    TDeath = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/h1")    #xpath corresponding to total deaths
    New_Cases = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/h4") #xpath corresponding to new cases 
    New_Rcov = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/h4")  #xpath corresponding to new recoveries
    New_Death = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/h4") #xpath corresponding to new deaths 
    #Prints statistics on sender's console
    print("Total Cases:",TCases.text)
    print("Total Active Cases:",TActive.text)
    print("Total Recovered Cases:",TRecov.text)
    print("Total Deaths:",TDeath.text)
    print("New Cases:",New_Cases.text[1:len(New_Cases.text)-1])
    print("New Recovered Cases:",New_Rcov.text[1:len(New_Rcov.text)-1])
    print("Additional Deaths yet:",New_Death.text[1:len(New_Death.text)-1])
    
    list_of_emails=["sandip68544@gmail.com"]   #Recipients' email list. Can be updated as per need.
    sender = credentials.sender_mail          #Need to change credentials.py file for updating sender's email address
    password = credentials.password           #Need to change credentials.py file for updating sender's password  
    subject = 'COVID-19 STATISTICS( INDIA )'
    DT = datetime.datetime.now()              #Extracts date and time from local computer
    datetext='DATE:  %d / %d / %d\n'%((DT.day),(DT.month),(DT.year))
    timetext='TIME:  %d : %d : %d\n\n'%((DT.hour),(DT.minute),(DT.second))
    messagetext = ' 1. Total Cases-->                         %s\n 2. Total Active Cases-->              %s\n 3. Total Recovered Cases-->      %s\n 4. Total Deaths-->                        %s\n 5. New Positive Cases-->            %s\n 6. New Recovered Cases-->       %s\n 7. Additional deaths-->                %s\n' %(str(TCases.text),str(TActive.text),str(TRecov.text),str(TDeath.text),str(New_Cases.text[1:len(New_Cases.text)-1]),str(New_Rcov.text[1:len(New_Rcov.text)-1]),str(New_Death.text[1:len(New_Death.text)-1])) 
    messageHTML = '<p>***Please visit this <a href="https://www.covid19india.org/">link<a> for more information on COVID-19. STAY SAFE, STAY HEALTHY***<p><br><br>'
    id_personal = '                                                            ---Sandipan Das'
    #EMAIL SEGMENT BEGINS HERE
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)

    for i in list_of_emails:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = i
        msg['Subject'] = subject
        msg.attach(MIMEText(datetext,'plain'))
        msg.attach(MIMEText(timetext,'plain'))
        msg.attach(MIMEText(messagetext, 'plain'))
        msg.attach(MIMEText(messageHTML,'html'))
        msg.attach(MIMEText(id_personal,'plain'))
        text = msg.as_string()
        server.sendmail(sender, i, text)
        print("Email has been sent to",i)
    server.quit()
while(True):
    sleep(60*60)            # Loop executes on an hourly basis
    extractor()
