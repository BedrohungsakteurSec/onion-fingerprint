#!/bin/python3
import mmh3
import requests
import codecs
from bs4 import BeautifulSoup

path_to_favicon = "favicon.ico"

# Array of onion links to fingerprint

domain_list = ["http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/",
               "http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/",
               "http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/",
               "http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/",
               "http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/",
               "http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/",
               "http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/",
               "http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/",
               "http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/",
               "http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion/",
               "http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion/",
               "http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/",
               "http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/",
               "http://2ln3x7ru6psileh7il7jot2ufhol4o7nd54z663xonnnmmku4dgkx3ad.onion/",
               "http://usmost4cbpesx552s2s4ti3c4nk2xgiu763vhcs3b4uc4ppp3zwnscyd.onion/",
               "http://xf2gry25d3tyxkiu2xlvczd3q7jl6yyhtpodevjugnxia2u665asozad.onion/",
               "http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/",
               "http://prjd5pmbug2cnfs67s3y65ods27vamswdaw2lnwf45ys3pjl55h2gwqd.onion/",
               "http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/",
               "http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/",
               "http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/",
               "http://jhi4v5rjly75ggha26cu2eeyfhwvgbde4w6d75vepwxt2zht5sqfhuqd.onion/",
               "http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/",
               "http://vhlehwexxmbnvecbmsk4ormttdvhlhbnyabai4cithvizzaduf3gmayd.onion/",
               "http://ymvhtqya23wqpez63gyc3ke4svju3mqsby2awnhd3bk2e65izt7baqad.onion/",
               "http://k6m3fagp4w4wspmdt23fldnwrmknse74gmxosswvaxf3ciasficpenad.onion/",
               "http://lqcjo7esbfog5t4r4gyy7jurpzf6cavpfmc4vkal4k2g4ie66ao5mryd.onion/",
               "http://qazkxav4zzmt5xwfw6my362jdwhzrcafz7qpd5kugfgx7z7il5lyb6ad.onion/",
               "http://gd5x24pjoan2pddc2fs6jlmnqbawq562d2qyk6ym4peu5ihzy6gd4jad.onion/",
               "http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/",
               "http://okayd5ljzdv4gzrtiqlhtzjbflymfny2bxc2eacej3tamu2nyka7bxad.onion/",
               "http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/",
               "http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/",
               "http://kq4okz5kf4xosbsnvdr45uukjhbm4oameb6k6agjjsydycvflcewl4qd.onion/",
               "http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/",
               "http://odahix2ysdtqp4lgak4h2rsnd35dmkdx3ndzjbdhk3jiviqkljfjmnqd.onion/"
               ]

# Create a TOR session

def get_tor_session():
    tor_session = requests.session()
    tor_session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                           'https': 'socks5h://127.0.0.1:9050'}
    return tor_session

tor_session = get_tor_session()

# Itterate through onion-link-array 

for domain in domain_list:
    # Make a request and get the favicon
    response_ico = tor_session.get(f"{domain}{path_to_favicon}")
    # Make a request a request and get the title
    response_title = tor_session.get(f"{domain}")

    # Encode the favicon with base64
    favicon = codecs.encode(response_ico.content,"base64")
    # Hash the base64 output with MurmurHash3 (you can search for this Hash on Shodan) >  https://pypi.org/project/mmh3/
    hash = mmh3.hash(favicon)
    # Parse the response to BeautifulSoup
    soup = BeautifulSoup(response_title.text, 'html.parser')
        
    # Print the onion-link, the murmur-favicon-hash and page title
    print(f"http.title:\"{soup.find('title').text}\"\n{domain}\nhttp.favicon.hash:{hash}\n")