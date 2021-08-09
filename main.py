from bs4 import BeautifulSoup


with open('home.html','r') as html_file:
       content= html_file.read()
       course_card = BeautifulSoup(content , 'lxml')
    #    print(course_card.prettify())
       tags= course_card.find_all('div' , class_='card')
       for tag in tags :
           print(tag.h5.text, "||" , tag.p.text ,"||" , tag.a.text )
    #    print(content)

    #    soup= BeautifulSoup(content, 'lxml')
    #    print(soup.prettify())

    #    tags = soup.find_all('div')

    #    for tag in tags:

    #      print(tag.text)
   

    
