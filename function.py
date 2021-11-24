import requests,json,os,random
from bs4 import BeautifulSoup as bs
from fake_headers import Headers

'''
get_image_page принимает параметры:

текст(по которому будет идти поиск)
количество нужных картинок(число)
выбрать одно фото из полученного списка(любой параметр, кроме 0 - включит эту функцию, если count > 1)
mask - не советую трогать, это сам массив, в который наполняются url

возвращает либо ссылку (str)
либо массив ссылок (list)

download_image принимает параметры:
data - либо list(список url) , либо str(1 url)
path - куда будут скачиваться фото (TEXT)
'''

url = 'https://yandex.ru/images/search?text={}'

def get_image_page(zapros,count=5,rand=0,mask=[]):
    soup = bs(requests.get(url.format(str(zapros)),headers=Headers().generate()).content,'html.parser')
    items = soup.select('.serp-item.serp-item_type_search')

    for item in items:
        try:
            if len(mask) < count:
                data = str(json.loads(item.attrs['data-bem'])['serp-item']['preview'][0]['origin']['url'])
                
                try:
                    requests.get(data,headers=Headers().generate())
                    mask.append(data)
                
                except:
                    pass
                    #print(f'{data} --fail')
        except Exception as e:
            print(e)
    
    if rand != 0 and len(mask) >= 2:
        return random.choice(mask) #(STRING)
    else:
        return mask #(LEN) 

def download_image(data,path='yandex_image'):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        
        if str(data) == data:
            with open(f"{path}/{data.replace('/','').replace(':large','').strip()}",'wb') as file:
                file.write(requests.get(data).content)
        else:
            for image in data:
                with open(f"{path}/{image.replace('/','').replace(':large','').strip()}",'wb') as file:
                    file.write(requests.get(image).content)
        return True
    except Exception as error:
        print(f'ERROR in download_image!!!\n{str(error)}')

if __name__ == '__main__':
    print(download_image(
        get_image_page('anime лоля',rand=0,count=2)
    ))