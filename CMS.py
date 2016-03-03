__author__ = 'osboxes'
import urllib2,re, MySQLdb


def gethtml(address):
    try:
        website = urllib2.urlopen(address)
        return website.read()
    except urllib2.URLError, e:
       print 'Cannot retrieve URL :' + e.reason

request = urllib2.Request('https://freelancehunt.com/freelancers?q=CMS&country=1&city=', headers={'User-Agent': 'Mozilla/5.0'})
fl = gethtml(request)


#fetch freelancers personal pages
freelancers= re.findall('<a.*href="?(/freelancer/.+html)"..>', fl)

# get top 10 freelancers

top10fl = freelancers[:10]

# get full personal webpage address

top10fl = ['https://freelancehunt.com' + f for f in top10fl]

# get project web page from portfolio data
total_list=[]
for page in top10fl:
    request = urllib2.Request(page, headers={'User-Agent': 'Mozilla/5.0'})
    fl = gethtml(request)
    sites = re.findall(' <a.*rel="nofollow".*target="_blank".+href="(.*)">', fl)
    total_list+=sites
print total_list

'''
    db_id = 5
for s in total_list:
        try:
            db = MySQLdb.connect('localhost', 'root', '1111', 'CMS')
            cursor = db.cursor()
            query = 'INSERT INTO Names (ID,ADDRESS,CMS) VALUES("%d", "%s","UNKNOWN")' % (db_id,s)
            cursor.execute(query)
            db.commit()
        except MySQLdb.Error, e :
            print 'DataBase Error :'+ e.args[1]
        db_id += 1

show_all ='SELECT * FROM Names'
cursor.execute(show_all)
data = cursor.fetchall()
print data
'''
# encode addresses with cyrillic script



#vacs=re.findall('<a.*href="?(.*open-vacancies/.*-.*/)?"',gethtml(vac))

