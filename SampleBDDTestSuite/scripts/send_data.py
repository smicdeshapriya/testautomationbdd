#!/usr/bin/python

import subprocess
import paramiko
import os
import smtplib


def sendEmail():
    
    sender = 'indikade@millenniumit.com'
    receivers = ['haaziqh@millenniumit.com']
    
    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test
    
    This is a test e-mail message.
    """
    
    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receivers, message)         
       print "Successfully sent email"
    except SMTPException:
       print "Error: unable to send email"

def fileTransfer(localpath,remotepath):
    envDetails=setEnvDetailsBGTest()
#     
#     host='172.25.72.115'
#     username='s5surv23'
#     password='mit123'
#     
    host=str(envDetails[0])
    username=str(envDetails[2])
    #password=str(envDetails[3])
    password='mit_0987'
    
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(host, username=str(username), password=str(password))
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath)
    sftp.close()
    ssh.close()

def fileTransfer2Surv4(localpath,file):
    #envDetails=setEnvDetailsBGTest()
    surv4remotepath='/x01/fe1surv4/data/NewsData/'+file
    host='172.25.93.154'
    username='fe1surv4'
    #password=str(envDetails[3])
    password='mit123'
    
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(host, username=str(username), password=str(password))
    sftp = ssh.open_sftp()
    sftp.put(localpath, surv4remotepath)
    sftp.close()
    ssh.close()

def remoteRunner(host,username,password,cmd,file):
    host=host
    username=username
    password=password
     
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(cmd)
    
    if file == '' :
         for line in stdout:
             print '... ' + line.strip('\n')
         client.close()
    
    else:
         for line in stdout:
             file = file
             log = open(file, "a")
             print >>log, '... ' + line.strip('\n')
         client.close()    
         
        
    
def printLogToFile():
    #file should be given within " "
    file = "haaziqLog.txt"
    log = open(file, "w")
    print "creating log files"
    print >>log, "test"
    print "File created"

def runSikuliScript(path):
    filepath = path
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print "Done Running Sikuli"
    
    
def rumBat():
    filepath="D:/TestDIR/myCMD.bat"
    #"D:/path/to/batch/myBatch.bat"
    #"D:/TestDIR/myCMD.bat"
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    
    stdout, stderr = p.communicate()
    print p.returncode # is 0 if success
    

 
def os_capture(args, cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    proc = subprocess.Popen(
        args=args,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    stdout = proc.communicate()[0]
  
    return stdout, proc.returncode
    
    
def main():
    print "send Data Main runner..."
    remoteRunner('172.25.72.115','s5surv23',"mit123",'pwd','')
    
    file='C:\\Users\\indikade\\Desktop\\git_product\\src\\Product\\suite_Surveillance\\shared\\testdata\\NewsData\\28_01_01_both.xml'
    fileTransfer(file,"/x01/s5surv23/data/NewsData/28_01_01_both.xml")
    fileTransfer2Surv4
#winRemote()
    #remoteRunner('SSI 5 "SurvCommon:1:1:SurveillanceManager:1" GENERAL WINDOW_MODE TABBED')
    #sendEmail()
    #remoteRunner('172.25.72.112','s5surv22','mit123','SurveillanceManager -v','abccc.txt')
    #sshOut()
    
#     stdout, exit_code = os_capture("mycommand")
#     test.compare(exit_code, 0, "Expected exit code: 0")
#     test.verify(stdout.find("some expected substring") != -1, "Expected to find: 'some expected substring'")
#     
    
    #setDateTime()
    #pids = get_pids_for_title("Internet Explorer")
    #runSikuliScript("echo 'Hello'")
    #runSikuliScript("runsikulix.cmd -r D:\TestDIR\sikulix_scrpts\one.sikuli")
    #sshOut()
    #rumBat()
     
if __name__ == "__main__": main()       