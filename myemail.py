from urllib.request import Request, urlopen

req = Request('https://quest.squadcast.tech/api/RA1911031010011/emails',
              headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
finalstr = str(webpage)
print(finalstr.count('detulbbpsd.edu'))
