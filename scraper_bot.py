from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
import datetime
import smtplib
import credentials

driver=webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.covid19india.org/")
sleep(2)

def extractor():
    TCases = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/h1")
    TActive = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/h1")
    TRecov = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/h1")
    TDeath = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/h1")
    New_Cases = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/h4")
    New_Rcov = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/h4")
    New_Death = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/h4")

    print("Total Cases:",TCases.text)
    print("Total Active Cases:",TActive.text)
    print("Total Recovered Cases:",TRecov.text)
    print("Total Deaths:",TDeath.text)
    print("New Cases:",New_Cases.text[1:len(New_Cases.text)-1])
    print("New Recovered Cases:",New_Rcov.text[1:len(New_Rcov.text)-1])
    print("Additional Deaths yet:",New_Death.text[1:len(New_Death.text)-1])

    list_of_emails=["soumyadeep.dbsslg@gmail.com"]
    sender = credentials.sender_mail 
    password = credentials.password
    subject = 'COVID-19 STATISTICS( INDIA )'
    DT = datetime.datetime.now()
    datetext='DATE:  %d / %d / %d\n'%((DT.day),(DT.month),(DT.year))
    timetext='TIME:  %d : %d : %d\n\n'%((DT.hour),(DT.minute),(DT.second))
    messagetext = ' 1. Total Cases-->                         %s\n 2. Total Active Cases-->              %s\n 3. Total Recovered Cases-->      %s\n 4. Total Deaths-->                        %s\n 5. New Positive Cases-->            %s\n 6. New Recovered Cases-->       %s\n 7. Additional deaths-->                %s\n' %(str(TCases.text),str(TActive.text),str(TRecov.text),str(TDeath.text),str(New_Cases.text[1:len(New_Cases.text)-1]),str(New_Rcov.text[1:len(New_Rcov.text)-1]),str(New_Death.text[1:len(New_Death.text)-1])) 
    messageHTML = '<p>***Please visit this <a href="https://www.covid19india.org/">link<a> for more information on COVID-19. STAY SAFE, STAY HEALTHY***<p><br><br>'
    id_personal = '                                                            ---Sandipan Das'

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
extractor()