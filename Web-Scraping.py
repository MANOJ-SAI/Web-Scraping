# we import bs4 package for using BeautifulSoup function
#For opening the url we can import the urllib.request package
import bs4 
import urllib.request as ur   


#we can assign url  to the url variable
#open the url using urlopen from urllib.request package
url="https://www.indiatoday.in/science"
uc=ur.urlopen(url) 


#read the content in the url using read()
#close the read() function using the close()
ph=uc.read()
uc.close()


#Apply BeautifulSoup() using readed content in ph variable
#find the requeried content tags using the find_all()
pg=bs4.BeautifulSoup(ph,"html.parser")
cl=pg.find_all("div",{"class":"catagory-listing"})


#create an empty list for storing the image urls
#iterate the cl list which store data in the form of list from find_all()
img_url=[]
for i in cl:
    #get images tag from the each list in cl using the finall("img")
    im=i.find_all("img")
    #iterate the stored img tag in im variable
    for j in im:
        #from the img tag we get the url of the image by using get('src')
        img_url.append(j.get('src'))

        
#iterate the imgs_url list
for i in img_url:
    #give the folder location to store the images
    #using the urlretrieve function we get image from url then store into given file path
    
    fullpath="C:\\Users\\MS\\Desktop\\web-scarp\\"+"image"+str(img_url.index(i))+'.jpg' 
    ur.urlretrieve(i,fullpath)
    
print("images-downloaded successfully")

