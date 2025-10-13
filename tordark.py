from colorama import Fore, Style, init
import shutil
import time

init(autoreset=True)

logo1 = r"""
▄▄▄█████▓ ▒█████   ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░      ░ ░ ░ ▒    ░░   ░ 
             ░ ░     ░     
                           
""".splitlines()

logo2 = r"""
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ 
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░ 
   ░          ░  ░   ░     ░  ░   
 ░                                
""".splitlines()

def print_side_by_side(l1, l2, color1=Fore.MAGENTA, color2=Fore.WHITE):
    cols = shutil.get_terminal_size().columns
    max_len = max(len(l) for l in l1)
    for left, right in zip(l1, l2):
        line = color1 + left.ljust(max_len, " ") + color2 + right
        print(line.center(cols) + Style.RESET_ALL)

def print_header():
    print_side_by_side(logo1, logo2)
    time.sleep(0.5)
    info()
 
    print()  
    
def info():
    cols = shutil.get_terminal_size().columns
    block = (
        Fore.MAGENTA + Style.BRIGHT + "[ INFO ]" + Style.RESET_ALL + "\n"
        + Fore.MAGENTA + '-' + Fore.WHITE   + " Name     :                     " + Fore.MAGENTA + "TorDark\n"
        + Fore.MAGENTA + '-' + Fore.WHITE   + " Version  :                         " + Fore.MAGENTA + "0.2\n"
        + Fore.MAGENTA + '-' + Fore.WHITE   + " Author   :                      " + Fore.MAGENTA + "Orbitz\n"
        + Fore.MAGENTA + '-'    + Fore.WHITE   + " GitHub   : " + Fore.MAGENTA + "https://github.com/Orbitz11\n"
        + Fore.MAGENTA + '-'    + Fore.WHITE   + " Email    : " + Fore.MAGENTA + "orbitz.business11@gmail.com\n"
    )

    for line in block.splitlines():
        print(line.center(cols))


if __name__ == "__main__":
    print_header()








def menu():
    while True:
        def ask_return_or_exit():
            while True:
                print("\n")
                print(Fore.GREEN + '[1] Back to main ')
                print(Fore.RED + '[2] Exit' )
                choice = input('Choose : ').strip()

                if choice == "1":
                    return  
                elif choice == "2":
                    print(Fore.RED + "")
                    time.sleep(2)
                    exit()
                else:
                    print(Fore.YELLOW + "Choose 1 or 2" + Style.RESET_ALL)
        print(Fore.MAGENTA + Style.BRIGHT + '----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(Fore.WHITE + 'Choose One Of This Choices')
        print(Fore.MAGENTA + '----------------------------')
        print('\n')
        print('\n')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '00' + Fore.WHITE + ']' + Fore.MAGENTA + ' Exit')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '01' + Fore.WHITE + ']' + Fore.MAGENTA + ' All')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '02' + Fore.WHITE + ']' + Fore.MAGENTA + ' Search Engine')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '03' + Fore.WHITE + ']' + Fore.MAGENTA + ' Chatrooms')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '04' + Fore.WHITE + ']' + Fore.MAGENTA + ' Financial Services    ' + Fore.WHITE + '[' + Fore.MAGENTA + 'Markets' + Fore.WHITE + ']')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '05' + Fore.WHITE + ']' + Fore.MAGENTA + ' Commercial Services   ' + Fore.WHITE + '[' + Fore.MAGENTA + 'Markets' + Fore.WHITE + ']')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '06' + Fore.WHITE + ']' + Fore.MAGENTA + ' Drugs                 ' + Fore.WHITE + '[' + Fore.MAGENTA + 'Markets' + Fore.WHITE + ']')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '07' + Fore.WHITE + ']' + Fore.MAGENTA + ' Other')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '08' + Fore.WHITE + ']' + Fore.MAGENTA + ' File sharing          ' + Fore.WHITE + '[' + Fore.MAGENTA + 'Hosting Services' + Fore.WHITE + ']')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '09' + Fore.WHITE + ']' + Fore.MAGENTA + ' Web Hosting           ' + Fore.WHITE + '[' + Fore.MAGENTA + 'Hosting Services' + Fore.WHITE + ']')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '10' + Fore.WHITE + ']' + Fore.MAGENTA + ' Paste Bin             ' + Fore.WHITE + '[' + Fore.MAGENTA + 'Hosting Services' + Fore.WHITE + ']')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '11' + Fore.WHITE + ']' + Fore.MAGENTA + ' Blogs / Essays / Personal Pages / News')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '12' + Fore.WHITE + ']' + Fore.MAGENTA + ' Email / Messaging')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '13' + Fore.WHITE + ']' + Fore.MAGENTA + ' Social Networks')
        print(Fore.WHITE + '[' + Fore.MAGENTA + '14' + Fore.WHITE + ']' + Fore.MAGENTA + ' wiki')
        print('\n')
        print('\n')


        choice = int(input('choose : '))

        if choice == 0:
            print('Exit Program, Good Bye\n' )
            time.sleep(3)
            break

        elif choice == 1:
            all =r'''
            search engine


            -http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/
            -https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/
            -http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/
            
            
            chatrooms


            -http://blkhatjxlrvc5aevqzz5t6kxldayog6jlx5h7glnu44euzongl4fh5ad.onion/
            -http://enxx3byspwsdo446jujc52ucy2pf5urdbhqw3kbsfhlfjwmbpj5smdad.onion/
            
            
            markets


            Financial Services
            
                -http://xqxe7spwdgnz4a3mjmf4r4wixcqjwgw6ufasl3p3lthkyhrvg7y4ryyd.onion/
                -http://torbuyxpe6auueywlctu4wz6ur3o5n2meybt6tyi4rmeudtjsysayqyd.onion/ 
                -http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/
                -http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/
                -http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/
                
            Commercial Services
            
                -http://blackops3zlgfuq4dg4yrtxoe57u3sxfa34kqzbooqbovutleqhf3zqd.onion/
                -http://hn2paw7zaahbikbejiv6h22zwtijlam65y2c77xj2ypbilm2xs4bnbid.onion/
                -http://deep6xcucd2o3ubqmuhwxiq37yw3fkroiwt74icyindute5znr2zpuad.onion/
                -http://j2dbibq43m4fdyry2pltez346mwneqfl7a5dzr2mgsouhp7lox2eu2qd.onion/
                -http://kw4zlnfhxje7top26u57iosg55i7dzuljjcyswo2clgc3mdliviswwyd.onion/
                
            drugs
            
                -http://bazaarboom567hsuxjspmwurpl7lyx23p7r2byg22vwfhv5yubvvezid.onion/
                -http://waa2dbeditmgttutm4m64jvwirmwtirhbuupngbhheddadyojgjsttid.onion/
                -https://h3h66vqwmmxxheeuwi4hhk52ic5svhnb73xdnxnzaj6vrnk742ntnhyd.onion/
                -http://4pt4axjgzmm4ibmxplfiuvopxzf775e5bqseyllafcecryfthdupjwyd.onion/
                -http://pt2mftbxeczbzufi2v7b3ekmsun4khq6hi7bdjo7w23fsx3easvr73ad.onion/
                -http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/
                -http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/
                -http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/
                
            other
            
                    -http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/   [  mining  ]
                    -http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/   [guns store]
                    -http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/   [ bitcoins ]
                    
                    
                    
            Hosting Services


            File sharing
                
                -http://oju4yn237c6hjh42qothvpreqecnqjhtvh4sgn3fqmsdvhu5d5tyspid.onion/
                -http://uoxqi4lrfqztugili7zzgygibs4xstehf5hohtkpyqcoyryweypzkwid.onion/

            Web Hosting
            
                -http://hzwjmjimhr7bdmfv2doll4upibt5ojjmpo3pbp5ctwcg37n3hyk7qzid.onion/
                -http://fhostingineiwjg6cppciac2bemu42nwsupvvisihnczinok362qfrqd.onion/
                -https://njallalafimoej5i4eg7vlnqjvmb6zhdh27qxcatdn647jtwwwui3nad.onion/
                -http://spore64i5sofqlfz5gq2ju4msgzojjwifls7rok2cti624zyq3fcelad.onion/
                
            Paste Bin
                
                -http://zerobinftagjpeeebbvyzjcqyjpmjvynj5qlexwyxe7l3vqejxnqv5qd.onion/
                
                
            Blogs / Essays / Personal Pages / News
            
            
                -http://ovgl57qc3a5abwqgdhdtssvmydr6f6mjz6ey23thwy63pmbxqmi45iid.onion/
                -http://bible4u2lvhacg4b3to2e2veqpwmrc2c3tjf2wuuqiz332vlwmr4xbad.onion/
                -http://potatoynwcg34xyodol6p6hvi5e4xelxdeowsl5t2daxywepub32y7yd.onion/
                -https://www.bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion/

            
            Email / Messaging	   	
                
                
                -http://mail.danielas3rtn54uwmofdo3x2bsdifr47huasnmbgqzfrec5ubupvtpid.onion/
                -http://pissmaiamldg5ciulncthgzudvh5d55dismyqf6qdkx372n2b5osefid.onion/
                -http://mail2torjgmxgexntbrmhvgluavhj7ouul5yar6ylbvjkxwqf6ixkwyd.onion/
                -http://6n5nbusxgyw46juqo3nt5v4zuivdbc7mzm74wlhg7arggetaui4yp4id.onion/
                -https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion/
                -http://asapmsp2nsqiyufpnw5bziguahdpxbpyc6jbiss35wgca6ka434w27ad.onion/
                -http://hxuzjtocnzvv5g2rtg2bhwkcbupmk7rclb6lly3fo4tvqkk5oyrv3nid.onion/
                -http://tp7mtouwvggdlm73vimqkuq7727a4ebrv4vf4cnk6lfg4fatxa6p2ryd.onion/
                
                
            Social Networks


                -https://pitchprash4aqilfr7sbmuwve3pnkpylqwxjbj2q5o4szcfeea6d27yd.onion/
                -https://www.reddittorjg6rue252oqsxryoxengawnmo46qy4kyii5wtqnwfj4ooad.onion/
                -https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion
                -https://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/
                
                
            wiki


                -https://thehiddenwiki.ws/index.php/Main_Page
                -http://darkfailenbsdla5mal2mxn2uz66od5vtzd5qozslagrfzachha3f3id.onion/

            '''

            print(all)
            ask_return_or_exit()

        elif choice == 2:
            SearchEngine =r'''
    search engine


                -http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/
                -https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/
                -http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/
    '''
            print(SearchEngine)
            ask_return_or_exit()

        elif choice == 3:
            chatrooms =r'''
    chatrooms


                -http://blkhatjxlrvc5aevqzz5t6kxldayog6jlx5h7glnu44euzongl4fh5ad.onion/
                -http://enxx3byspwsdo446jujc52ucy2pf5urdbhqw3kbsfhlfjwmbpj5smdad.onion/
    '''
            print(chatrooms)
            ask_return_or_exit()

        elif choice == 4:

            FinancialServices =r'''
    Financial Services
   
                -http://xqxe7spwdgnz4a3mjmf4r4wixcqjwgw6ufasl3p3lthkyhrvg7y4ryyd.onion/
                -http://torbuyxpe6auueywlctu4wz6ur3o5n2meybt6tyi4rmeudtjsysayqyd.onion/ 
                -http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/
                -http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/
                -http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/
'''

            print(FinancialServices)
            ask_return_or_exit()

        elif choice == 5:

            CommercialServices =r'''
    Commercial Services
   
                -http://blackops3zlgfuq4dg4yrtxoe57u3sxfa34kqzbooqbovutleqhf3zqd.onion/
                -http://hn2paw7zaahbikbejiv6h22zwtijlam65y2c77xj2ypbilm2xs4bnbid.onion/
                -http://deep6xcucd2o3ubqmuhwxiq37yw3fkroiwt74icyindute5znr2zpuad.onion/
                -http://j2dbibq43m4fdyry2pltez346mwneqfl7a5dzr2mgsouhp7lox2eu2qd.onion/
                -http://kw4zlnfhxje7top26u57iosg55i7dzuljjcyswo2clgc3mdliviswwyd.onion/
'''

            print(CommercialServices)
            ask_return_or_exit()


        elif choice == 6:

                    drugs =r'''
        drugs
            
                -http://bazaarboom567hsuxjspmwurpl7lyx23p7r2byg22vwfhv5yubvvezid.onion/
                -http://waa2dbeditmgttutm4m64jvwirmwtirhbuupngbhheddadyojgjsttid.onion/
                -https://h3h66vqwmmxxheeuwi4hhk52ic5svhnb73xdnxnzaj6vrnk742ntnhyd.onion/
                -http://4pt4axjgzmm4ibmxplfiuvopxzf775e5bqseyllafcecryfthdupjwyd.onion/
                -http://pt2mftbxeczbzufi2v7b3ekmsun4khq6hi7bdjo7w23fsx3easvr73ad.onion/
                -http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/
                -http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/
                -http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/
        '''

                    print(drugs)
                    ask_return_or_exit()
                    
                    
                    
        elif choice == 7:

                    other =r'''
        other
            
                -http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/   [  mining  ]
                -http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/   [guns store]
                -http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/   [ bitcoins ]
        '''

                    print(other)
                    ask_return_or_exit()
                    
                    
        elif choice == 8:

                    Filesharing =r'''
        File sharing
                
                -http://oju4yn237c6hjh42qothvpreqecnqjhtvh4sgn3fqmsdvhu5d5tyspid.onion/
                -http://uoxqi4lrfqztugili7zzgygibs4xstehf5hohtkpyqcoyryweypzkwid.onion/
        '''

                    print(Filesharing)
                    ask_return_or_exit()                   
                    
                    
        elif choice == 9:

                    WebHosting =r'''
        Web Hosting
            
                -http://hzwjmjimhr7bdmfv2doll4upibt5ojjmpo3pbp5ctwcg37n3hyk7qzid.onion/
                -http://fhostingineiwjg6cppciac2bemu42nwsupvvisihnczinok362qfrqd.onion/
                -https://njallalafimoej5i4eg7vlnqjvmb6zhdh27qxcatdn647jtwwwui3nad.onion/
                -http://spore64i5sofqlfz5gq2ju4msgzojjwifls7rok2cti624zyq3fcelad.onion/
        '''

                    print(WebHosting)
                    ask_return_or_exit()                   
                    
        elif choice == 10:

                    PasteBin =r'''
       Paste Bin
                
                -http://zerobinftagjpeeebbvyzjcqyjpmjvynj5qlexwyxe7l3vqejxnqv5qd.onion/
        '''

                    print(PasteBin)
                    ask_return_or_exit()                   
                    
        elif choice == 11:

                    news =r'''
        Blogs / Essays / Personal Pages / News
            
            
                -http://ovgl57qc3a5abwqgdhdtssvmydr6f6mjz6ey23thwy63pmbxqmi45iid.onion/
                -http://bible4u2lvhacg4b3to2e2veqpwmrc2c3tjf2wuuqiz332vlwmr4xbad.onion/
                -http://potatoynwcg34xyodol6p6hvi5e4xelxdeowsl5t2daxywepub32y7yd.onion/
                -https://www.bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion/
        '''

                    print(news)
                    ask_return_or_exit()                               
                    
                    
        elif choice == 12:

                    email =r'''
        Email / Messaging	   	
                
                
                -http://mail.danielas3rtn54uwmofdo3x2bsdifr47huasnmbgqzfrec5ubupvtpid.onion/
                -http://pissmaiamldg5ciulncthgzudvh5d55dismyqf6qdkx372n2b5osefid.onion/
                -http://mail2torjgmxgexntbrmhvgluavhj7ouul5yar6ylbvjkxwqf6ixkwyd.onion/
                -http://6n5nbusxgyw46juqo3nt5v4zuivdbc7mzm74wlhg7arggetaui4yp4id.onion/
                -https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion/
                -http://asapmsp2nsqiyufpnw5bziguahdpxbpyc6jbiss35wgca6ka434w27ad.onion/
                -http://hxuzjtocnzvv5g2rtg2bhwkcbupmk7rclb6lly3fo4tvqkk5oyrv3nid.onion/
                -http://tp7mtouwvggdlm73vimqkuq7727a4ebrv4vf4cnk6lfg4fatxa6p2ryd.onion/
        '''

                    print(email)
                    ask_return_or_exit()                        
                    
        elif choice == 13:

                    social =r'''
        Social Networks


                -https://pitchprash4aqilfr7sbmuwve3pnkpylqwxjbj2q5o4szcfeea6d27yd.onion/
                -https://www.reddittorjg6rue252oqsxryoxengawnmo46qy4kyii5wtqnwfj4ooad.onion/
                -https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion
                -https://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/
        '''

                    print(social)
                    ask_return_or_exit()                                            
                    
        elif choice == 14:

                    wiki =r'''
            wiki


                -https://thehiddenwiki.ws/index.php/Main_Page
                -http://darkfailenbsdla5mal2mxn2uz66od5vtzd5qozslagrfzachha3f3id.onion/
        '''

                    print(wiki)
                    ask_return_or_exit()                                                               
                   
                    
        else:
            print('Wrong Choice')

menu()





