from pick import pick
import os
import sys
import utils


R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow


def Malicious_url():
    os.system(
        "konsole --profile='fsociety' --geometry 1000x700+0+0 -e python /home/fsociety/Desktop/Project/CyberTraq/CyberTraq.py & konsole --profile='fsociety' --geometry 800x400+80+0 -e ngrok http 8080 &")
    os.system("konsole -e clear")


def url_detect():
    os.system(
        "konsole --profile='fsociety' --geometry 800x400+80+0 -e python /home/fsociety/Desktop/Project/CyberTraq/heart_turtle.py")
    os.system("konsole -e clear")


def quit():
    sys.exit()


def Selections():
    title = r'''

                                                                                                                                          
 @@@@@@@   @@@@@@   @@@@@@@   @@@@@@@   @@@  @@@  @@@@@@@   @@@@@@@      @@@@@@   @@@@@@@   @@@@@@@@@@   @@@ @@@  
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@ @@@  
!@@       @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@    @@!       @@!  @@@  @@!  @@@  @@! @@! @@!  @@! !@@  
!@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@    !@!       !@!  @!@  !@!  @!@  !@! !@! !@!  !@! @!!  
!@!       @!@  !@!  @!@!!@!   @!@!!@!   @!@  !@!  @!@@!@!     @!!       @!@!@!@!  @!@!!@!   @!! !!@ @!@   !@!@!   
!!!       !@!  !!!  !!@!@!    !!@!@!    !@!  !!!  !!@!!!      !!!       !!!@!!!!  !!@!@!    !@!   ! !@!    @!!!   
:!!       !!:  !!!  !!: :!!   !!: :!!   !!:  !!!  !!:         !!:       !!:  !!!  !!: :!!   !!:     !!:    !!:         
:!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:         :!:       :!:  !:!  :!:  !:!  :!:     :!:    :!:    
 ::: :::  ::::: ::  ::   :::  ::   :::  ::::: ::   ::          ::       ::   :::  ::   :::  :::     ::      ::   
 :: :: :   : :  :    :   : :   :   : :   : :  :    :           :         :   : :   :   : :   :      :       :    |ＵＭＥＳＨ | ＮＩＲＡＪ|
                                                                                                                 | --------- + --------- |
                                                                                                                 |ＰＩＮＫＵ | ＳＵＮＮＹ|
                                                                                                                      
                                                                                                                  
    
                                                                 
    Please Select one the following:'''
    options = ['[>]Generate Malicious URL',
               '[>]Detect Malicious URL', '[!]Quit']

    option, index = pick(options, title, indicator='=>', default_index=0)

    return option


def run(option):
    if option == '[>]Generate Malicious URL':
        Malicious_url()

    if option == '[>]Detect Malicious URL':
        url_detect()

    if option == '[!]Quit':
        quit()
