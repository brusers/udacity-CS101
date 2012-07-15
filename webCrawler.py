import urllib


def get_page(url):
    try:
        return  urllib.urlopen(url).read()
	except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)



def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed,max_depth):	# max_depth not in udacities final code
	tocrawl=[seed]
	crawled=[]
	next_depth =[]		# not in udacities final code
	index={}
	depth = 0
	while tocrawl and depth <= max_depth:
		page=tocrawl.pop()
		if page not in crawled:
			content=get_page(page)
			add_page_to_index(index,page,content)
			union(next_depth, get_all_links(content))
			crawled.append(page)
		if not tocrawl:		# whole if statement not in udacities final code
			tocrawl, next_depth = next_depth, []
			depth+=1
	return index

def record_user_click(index,keyword,url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1]+=1

def add_to_index(index, keyword, url):
    if keyword in index:
		index[keyword].append(url)
	else:
		index[keyword]=[url]

	
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None
    

def add_page_to_index(index,url,content):
    myList = split_string(content," !,.)
    for i in range(len(myList)):
        add_to_index(index,myList[i],url)
		
def split_string(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit=False
            else:output[-1] = output[-1]+char
    return output
	
	
def bucket_find(bucket, key):
	for entry in bucket:
		if entry[0] == key:
			return entry
	return None
	
def hashtable_update(htable,key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket,key)
    if entry:
        entry[1]=value
    else:
        bucket.append([key,value])
			
def hashtable_lookup(htable,key):
    entry = bucket_find(hashtable_get_bucket(htable, key), key)
    if entry:
        return entry[1]
    else:
        return None
	
def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
