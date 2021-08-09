
from bs4 import BeautifulSoup
import requests
import time
# print(html_text)
def find_jobs():
     print('put some skills you wanna filter out')
     filter_out = input('-->')
     print('Filter out the skills ',filter_out  ,'...')
     html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

     soup= BeautifulSoup(html_text, 'lxml')
     jobs= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

     for index , job in enumerate(jobs):
          published_date= job.find('span', class_ ='sim-posted').span.text
          if 'few' in published_date:
               company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ','')
               skills = job.find('span', class_='srp-skills').text.replace(' ','')
               more_info= job.header.h2.a['href']
               if filter_out not in skills:
                    with open(f'jobs/{index}.txt','w') as f:
                         f.write(f"company : {company_name.strip()}\n")
                         f.write(f"Required Skills : {skills.strip()}\n")
                         f.write(f'More info:{more_info}\n')

                    print(f" File Saved as :{index}.txt\n")     

              



if __name__ =='__main__':
        while True:
              find_jobs()
              time_to_wait= 15
              print('Proccessing', time_to_wait, 'minute ...')
              time.sleep(60*time_to_wait)
              
       
           
        




 
           

        

             

    


