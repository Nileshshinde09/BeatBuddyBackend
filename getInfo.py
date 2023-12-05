from imports import *

df=pd.read_csv('data/cleaned_dataset.csv')
df.drop_duplicates(inplace=True)
Artist=pd.DataFrame(df['Artist'].unique(),columns=["Artist"])

def getAbout(name):
    link_dict={
        'spotify':[],
        'youtube music':[],
        'apple music':[],
        'youtube':[],
        'jiosaavn':[]
    }
    static_dict={
        'spotify':['https://open.spotify.com'],
        'youtube music':['https://music.youtube.com'],
        'apple music':['https://music.apple.com'],
        'youtube':['https://www.youtube.com'],
        'jiosaavn':['https://www.jiosaavn.com']
    }
    name=name.strip()
    name=name.replace(" ","+")
    try:
        url = f"https://www.google.com/search?q={name}&oq={name}&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDsyBggCEEUYOzIGCAMQRRg7MgkIBBBFGDsYjwIyBwgFEAAYjwIyBwgGEAAYjwIyBggHEEUYPdIBBzk2N2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8#wptab=si:ALGXSlYkc89PD3mXGxDFzFzv8DyVhrRIzb63ypGSGQTHQytMBlpPsgNLzeozXkC14yU6393fb5OL0uSj-8kSrH2Vw6gK9lyZeSTPGtdzsi6xv3KgBfdkQ_kLmhpK5VU4cPRBzUJUpzwW"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        response = requests.get(url,headers=headers)
        html = response.text
    
        soup = BeautifulSoup(html, 'html.parser')
        plat_link = soup.find('div', class_="r0VsPb").prettify()
        links=BeautifulSoup(plat_link, 'html.parser')
        links=soup.find_all('a',class_='JkUS4b',href=True)
        for i in links:
            if 'spotify' in i['href']:
                link_dict['spotify']=i['href']
            elif 'music.youtube' in i['href']:
                link_dict['youtube music']=i['href']
            elif 'apple' in i['href']:
                link_dict['apple music']=i['href']
            elif 'www.youtube' in i['href']:
                link_dict['youtube']=i['href']
            elif 'jiosaavn' in i['href']:
                link_dict['jiosaavn']=i['href']
        return link_dict
    except Exception:
        return static_dict
    
def getUrl(name):
    link_dict={
        'spotify':[],
        'youtube music':[],
        'apple music':[],
        'youtube':[],
        'jiosaavn':[]
    }
    static_dict={
        'spotify':[f'https://open.spotify.com/{name}'],
        'youtube music':[f'https://music.youtube.com/{name}'],
        'apple music':[f'https://music.apple.com/{name}'],
        'youtube':[f'https://www.youtube.com/{name}'],
        'jiosaavn':[f'https://www.jiosaavn.com/{name}']
    }
    name=name.strip()
    name=name.replace(" ","+")
    try:
        url = f"https://www.google.com/search?q={name}&oq={name}&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDsyBggCEEUYOzIGCAMQRRg7MgkIBBBFGDsYjwIyBwgFEAAYjwIyBwgGEAAYjwIyBggHEEUYPdIBBzk2N2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8#wptab=si:ALGXSlYkc89PD3mXGxDFzFzv8DyVhrRIzb63ypGSGQTHQytMBlpPsgNLzeozXkC14yU6393fb5OL0uSj-8kSrH2Vw6gK9lyZeSTPGtdzsi6xv3KgBfdkQ_kLmhpK5VU4cPRBzUJUpzwW"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        response = requests.get(url,headers=headers)
        html = response.text
    
        soup = BeautifulSoup(html, 'html.parser')
        plat_link = soup.find('div', class_="r0VsPb").prettify()
        links=BeautifulSoup(plat_link, 'html.parser')
        links=soup.find_all('a',class_='JkUS4b',href=True)
        for i in links:
            if 'spotify' in i['href']:
                link_dict['spotify']=i['href']
            elif 'music.youtube' in i['href']:
                link_dict['youtube music']=i['href']
            elif 'apple' in i['href']:
                link_dict['apple music']=i['href']
            elif 'www.youtube' in i['href']:
                link_dict['youtube']=i['href']
            elif 'jiosaavn' in i['href']:
                link_dict['jiosaavn']=i['href']
        return link_dict
    except Exception as e:
        return static_dict
    
def getDesc(name):
    try:
        url = f"https://www.google.com/search?q={name}&sca_esv=582945116&sxsrf=AM9HkKk3fZdl2ufp7ILUGf3ndzArszfq0w%3A1700146386967&ei=0ixWZaTQOreMseMPv7qQgAw&ved=0ahUKEwikgdjr4siCAxU3RmwGHT8dBMAQ4dUDCBA&uact=5&oq=Gorillaz&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgBIghHb3JpbGxhejIHECMYsAMYJzIHECMYsAMYJzIHECMYsAMYJzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYigUYsAMYQzIOEAAY5AIY1gQYsAPYAQEyDhAAGOQCGNYEGLAD2AEBMg4QABjkAhjWBBiwA9gBATIQEC4YigUYyAMYsAMYQ9gBAjIQEC4YigUYyAMYsAMYQ9gBAjIZEC4YigUYyAMYsAMYQxiLAxiYAxioA9gBAjIQEC4YigUYyAMYsAMYQ9gBAkjJCFAAWABwAXgBkAEAmAEAoAEAqgEAuAEDyAEA-AEC-AEB4gMEGAAgQYgGAZAGE7oGBggBEAEYCboGBggCEAEYCA&sclient=gws-wiz-serp"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        response = requests.get(url,headers=headers)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        soup = BeautifulSoup(soup.find('div', jsname="g7W7Ed").prettify(), 'html.parser')
        soup = soup.find_all('span')[0]
        return soup.text.strip()
    except Exception:
        return ""
    
def getSocialMedia(name):
    social_dict={
        
        'Instagram':[],
        'YouTube':[],
        'Facebook':[],
        'Twitter':[]
    }
    static_dict={
        'Instagram':[f'https://www.instagram.com/{name}'],
        'YouTube':[f'https://www.youtube.com/{name}'],
        'Facebook':[f'https://www.facebook.com/{name}'],
        'Twitter':[f'https://twitter.com/{name}']
    }
    try:
        url = f"https://www.google.com/search?q={name}&sca_esv=582945116&sxsrf=AM9HkKk3fZdl2ufp7ILUGf3ndzArszfq0w%3A1700146386967&ei=0ixWZaTQOreMseMPv7qQgAw&ved=0ahUKEwikgdjr4siCAxU3RmwGHT8dBMAQ4dUDCBA&uact=5&oq=Gorillaz&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgBIghHb3JpbGxhejIHECMYsAMYJzIHECMYsAMYJzIHECMYsAMYJzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYigUYsAMYQzIOEAAY5AIY1gQYsAPYAQEyDhAAGOQCGNYEGLAD2AEBMg4QABjkAhjWBBiwA9gBATIQEC4YigUYyAMYsAMYQ9gBAjIQEC4YigUYyAMYsAMYQ9gBAjIZEC4YigUYyAMYsAMYQxiLAxiYAxioA9gBAjIQEC4YigUYyAMYsAMYQ9gBAkjJCFAAWABwAXgBkAEAmAEAoAEAqgEAuAEDyAEA-AEC-AEB4gMEGAAgQYgGAZAGE7oGBggBEAEYCboGBggCEAEYCA&sclient=gws-wiz-serp"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        response = requests.get(url,headers=headers)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        soup = BeautifulSoup(soup.find('div', class_="OOijTb P6Tjc gDQYEd").prettify(), 'html.parser')
        soup = soup.find_all('a')
        for i in soup:
            if 'instagram' in i['href']:
                social_dict['Instagram']=i['href']
            elif 'youtube' in i['href']:
                social_dict['YouTube']=i['href']
            elif 'facebook' in i['href']:
                social_dict['Facebook']=i['href']
            elif 'twitter' in i['href']:
                social_dict['Twitter']=i['href']
        return social_dict
    except Exception:
        return static_dict
    
if __name__=="__main__":
    getDesc()
    getSocialMedia()
    getUrl()
    