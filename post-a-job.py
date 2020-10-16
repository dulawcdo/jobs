#!/bin/python

import time
from selenium import webdriver
import urllib
from selenium.webdriver.support.ui import Select
import subprocess

def screenclear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

class bcol:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

screenclear()

driver = webdriver.Firefox()
driver.get("https://law-denver-csm.symplicity.com/manager/")

managerun = driver.find_element_by_name('username')
managerun.clear()
managerun.send_keys("careers@law.du.edu")

managerpass = driver.find_element_by_name('password')
managerpass.clear()
managerpass.send_keys("careers@law.du.edu")

signinbutton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div/div[3]/input')
signinbutton.click()

# It works! Now embed the following within a while loop: with an if statement for each kind of job.

x = 1

while x == 1:
    screenclear()
    print(bcol.HEADER+'What kind of job are you posting Indeed[i], Government[g], or Other[o]?'+bcol.ENDC)
    jobtype = raw_input()
    if jobtype == 'i':
        screenclear()
        print(bcol.HEADER+'INDEED JOB'+bcol.ENDC)
        print("Enter Indeed URL")
        joburl = raw_input()

        driver.get(joburl)

        employername = driver.find_element_by_css_selector('div.icl-u-lg-mr--sm.icl-u-xs-mr--xs')
        employername_text = employername.text

        jobdescription = driver.find_element_by_id('jobDescriptionText')
 
        jobdescription_text = jobdescription.text

        jobtitle = driver.find_element_by_class_name('jobsearch-JobInfoHeader-title-container')

        jobtitle_text = jobtitle.text

        sector_text = "Private Sector"

        screenclear()

    elif jobtype == 'g':
        screenclear()
        print(bcol.HEADER+'GOVERNMENT JOBS'+bcol.ENDC)

        print("Enter CO GovernmentJobs URL")
        joburl = raw_input()
        
        driver.get(joburl)
        time.sleep(1)

        try:
            employername = driver.find_element_by_css_selector('.department-name')
        except:
            employername = driver.find_element_by_class_name('term-value department-name')
            
        employername_text = employername.text

        jobdescription = driver.find_element_by_css_selector('#details-info')
 
        jobdescription_text = jobdescription.text

        jobtitle = driver.find_element_by_css_selector('.summary > h1:nth-child(1)')

        jobtitle_text = jobtitle.text

        sector_text = "Public Sector"

        screenclear()

    elif jobtype == 'o':
        screenclear()
        print(bcol.HEADER+'OTHER / MANUAL POSTING'+bcol.ENDC)
        
        print("Enter Employer Name")
        employername_text = raw_input()

        print("Enter Job Title")
        jobtitle_text = raw_input()

        print("Enter Job Description")
        jobdescription_text = open('/home/zeeshanr/Documents/python/jobs/jobdescription.txt').read().decode('utf-8', 'ignore')
        
        joburl = "See description"
        
        print('Sector: Private[1] or Public[2]?')
        sectoption = raw_input()
        if sectoption == '1':
            sector_text = "Private Sector"
        elif sectoption == '2':
            sector_text = "Public Sector"
        else:
            print('Description Error: Returning to start.')
            continue
            screenclear()


    else:
        print(bcol.HEADER+'OTHER / MANUAL POSTING'+bcol.ENDC)
        
        print("Enter Employer Name")
        employername_text = raw_input()

        print("Enter Job Title")
        jobtitle_text = raw_input()

        print("Enter Job Description")

    #   jobdescription_text = sys.stdin.read() 
        jobdescription_text = open('home/zeeshanr/Documents/python/jobs/jobdescription.txt').read().decode('utf-8', 'ignore')
        
        joburl = "See description"

        print('Sector: Private[1] or Public[2]?')
        sectoption = raw_input()
        if sectoption == '1':
            sector_text = "Private Sector"
        elif sectoption == '2':
            sector_text = "Public Sector"
        else:
            print('Description Error: Returning to start.')
            screenclear()
            continue
# FOR TESTING ONLY
#    print(jobdescription_text)
#    exit()
###################
    
    driver.get("https://law-denver-csm.symplicity.com/manager/")
    employers = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/ul/li[5]/a/span[2]')
    employers.click()


    employerssub = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/ul/li[5]/ul/li[2]/a/span[2]')

    try:
        employerssub.click()
    except:
        time.sleep(1)
        employers.click()
        employerssub.click()

    try:
        employersearchbar = driver.find_element_by_xpath('//*[@id="employerfilters_keywords_"]')
        employersearchbar.clear()
        employersearchbar.send_keys(employername_text)
    except:
        driver.find_element_by_class_name('back').click()
        employersearchbar = driver.find_element_by_xpath('//*[@id="employerfilters_keywords_"]')
        employersearchbar.clear()
        employersearchbar.send_keys(employername_text)
   

    employersearchbutton = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[1]/form/div[3]/input[1]')
    employersearchbutton.click()

    w3 = raw_input("Prepare posting page. Then enter y to proceed. . .\n")

    if w3 == 'y':
        sector = Select(driver.find_element_by_xpath('//*[@id="dnf_class_values_job__cdo_highlight_job___"]'))
        sector.select_by_visible_text(sector_text)

        driver.find_element_by_xpath('//*[@id="dnf_class_values_job__job_type___1_check"]').click()

        driver.find_element_by_xpath('//*[@id="dnf_class_values_job__job_type___21_check"]').click()

        jobcontact = Select(driver.find_element_by_xpath('//*[@id="dnf_class_values_job__job_contact_"]'))
        jobcontact.select_by_visible_text("Jobs Contact")

        posting_jobtitle = driver.find_element_by_xpath('//*[@id="dnf_class_values_job__job_title_"]')
        posting_jobtitle.send_keys(jobtitle_text)

        driver.find_element_by_xpath('//*[@id="dnf_class_values_job__resume_mode___other_check"]').click()

        driver.find_element_by_xpath('//*[@id="dnf_class_values_job__contact_blurb_"]').send_keys(joburl)
    
        posting_job_description = driver.find_element_by_xpath('//*[@id="dnf_class_values_job__job_desc__ifr"]')
        posting_job_description.click()
        posting_job_description.send_keys(jobdescription_text)

        driver.find_element_by_name('dnf_class_values[job][approved]').click()

        p = subprocess.Popen(["date", "+%Y-%m-%d", "-d", "+30 days"], stdout=subprocess.PIPE)
        out, err = p.communicate()
        expirydate_input = out.strip()

        expiry_date = driver.find_element_by_id('dnf_class_values_job__job_end_')
        expiry_date.click()
        expiry_date.clear()
        expiry_date.send_keys(expirydate_input)
       
        print(bcol.HEADER+"Now set up remaining parameters and finalize post"+bcol.ENDC)
        print(bcol.HEADER+"Check the date---arbitrary date applied."+bcol.ENDC)
        
        w33 = raw_input("Submit and post another job? [y/n] \n")
        if w33 == 'y':
            try:
                screenclear()
                driver.find_element_by_name('dnf_opt_submit').click()
            except:
                # driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/ul/li[1]/a/span[2]').click()
                driver.find_element_by_link_text('Home').click()
            time.sleep(2)
            # driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/ul/li[1]/a/span[2]').click()
            driver.find_element_by_link_text('Home').click()
            continue
        else:
            print("Submit & Quit")
            try:
                driver.find_element_by_name('dnf_opt_submit').click()
            except:
                # driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[1]/ul/li[1]/a/span[2]').click()
                driver.find_element_by_link_text('Home').click()
            driver.find_element_by_class_name('icn-chevron_down').click()
            driver.find_element_by_css_selector('li.options-list-items:nth-child(4) > a:nth-child(1)').click()
            driver.quit()
            x = 0
         

