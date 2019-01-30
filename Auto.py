import os
import webbrowser
import shutil

print('_'.center(80, '_'))
print('\n', 'AUTOCODE WEB-DESIGN AUTOMATOR'.center(80))
print('\n', 'FULL VERSION 1.0'.center(80))
print('\nCopyright (c) 2017 kelvinGichunge Softwares')
print('\n', '_'.center(79, '_'))
AC = True
while AC:
    lev1_input = (input('\n$AutoCode >>> ')).upper()
    header = ''
    navigation = ''
    script = ''
    if lev1_input == 'CODE-CREATE-HTML':
        proj_name = input('NAME OF YOUR PROJECT : ')
        # Creates both the software and project directories on drive C
        os.chdir('C:\\')
        try:
            os.mkdir('Autocode Web Automator')
            os.chdir('Autocode Web Automator')
        except Exception:
            os.chdir('Autocode Web Automator')
        os.mkdir(proj_name)
        os.chdir('../')
        # Copies both bootstrap and jquery sourcecode directories from Autocode program folder to the project
        try:
            shutil.copytree('/Program Files (x86)/Autocoder/bootstrap',
                            'C:/Autocode Web Automator/' + proj_name + '/bootstrap')
            shutil.copytree('/Program Files (x86)/Autocoder/jquery',
                            'C:/Autocode Web Automator/' + proj_name + '/jquery')
        except Exception:
            shutil.copytree('/Program Files/Autocoder/bootstrap',
                            'C:/Autocode Web Automator/' + proj_name + '/bootstrap')
            shutil.copytree('/Program Files/Autocoder/jquery',
                            'C:/Autocode Web Automator/' + proj_name + '/jquery')
        os.chdir('C:\\Autocode Web Automator\\' + proj_name)
        os.mkdir('Source Code')
        os.mkdir('Stylesheets')
        os.mkdir('Scripts')
        os.mkdir('Javascript')
        os.mkdir('Images')
        # Prompting whether the top header is required in the project file
        top_header = (str(input('\tInclude Top Header Layer?(YES/NO) : '))).upper()
        if top_header == 'YES':
            header = "<div id = 'top_header' class='container-fluid'><h4><b>" \
                     "\nYour Logo/Name</b><a name='top_home'></a></h4><br>" \
                     "\n<h6><b>SHORT DESCRIPTION OF YOUR WEBSITE TO THE CUSTOMERS/PEOPLE</b></h6><br>" \
                     "\n</div>"
            # Writing header styles to styles.css file
            os.chdir('Stylesheets')
            of_css_file = open('styles.css', 'w')
            # Writes to CSS Styles file
            of_css_file.write('#top_header{background-color:#666666}'
                              '\nh4{color:red}'
                              '\nh6{color:#66ff66}'
                              )
            of_css_file.close()
            os.chdir('../')
        elif top_header == 'NO':
            header = ''
        # Prompting for what type of navigation bar is to be used on the page
        nav_bar = (str(input("\n\tNavigation Bar:CUSTOM/BOOTSTRAP?(CUST/BTSP): "))).upper()
        if nav_bar == "BTSP":
            navigation = "<nav class = 'nav navbar-inverse'>" \
                         "\n\t<div class = 'container-fluid'>" \
                         "\n\t\t<ul class='nav navbar-nav'>" \
                         "\n\t\t\t<li class='active'><a href=''><b>Home</b></a></li>" \
                         "\n\t\t\t<li><a href=''><b>Page 1</b></a></li>" \
                         "\n\t\t\t<li><a href=''><b>Page 2</b></a></li>" \
                         "\n\t\t\t<li><a href=''><b>Page 3</b></a></li>" \
                         "\n\t\t\t<li><a href=''><b>Page 4</b></a></li>" \
                         "\n\t\t\t<li><a href=''><b>Page 5</b></a></li>" \
                         "\n\t\t\t<li><a href=''><b>Page 6</b></a></li>" \
                         "\n\t\t\t<li><a href=''><b>Page 7</b></a></li>" \
                         "\n\t\t\t<li><a href=''><b>Page 8</b></a></li>" \
                         "\n\t\t<ul>" \
                         "\n\t</div>" \
                         "\n</nav>"
        elif nav_bar == 'CUST':
            script = "<!--CSS Styles used on Jquery-->" \
                     "\n<style>" \
                     "\n\t.activated_link{ color: #000000; background: #ff3333; }" \
                     "\n</style>" \
                     "\n<!--Jquery Scripts-->" \
                     "\n<script>" \
                     "\n\t$(document).ready(function(){" \
                     "\n\t\t$('#home_link').addClass('activated_link');" \
                     "\n\t})" \
                     "\n</script>"
            navigation = "<div class='container-fluid' >" \
                         "\n<div  class='menu'>" \
                         "\n\t<ul>" \
                         "\n\t\t<li><a href='home.html#top_home' id='home_link'>Home</a></li>" \
                         "\n\t\t<li><a href='page_1.html' id='Links'>Page 1</a></li>" \
                         "\n\t\t<li><a href='Page_2.html' id='Links'>Page 2</a></li>" \
                         "\n\t\t<li><a href='Page_3.html' id='Links'>Page 3</a></li>" \
                         "\n\t\t<li><a href='Page_4.html' id='Links'>Page 4</a></li>" \
                         "\n\t\t<li><a href='Page_5.html' id='Links'>Page 5</a></li>" \
                         "\n\t\t<li><a href='Page_6.html' id='Links'>Page 6</a></li>" \
                         "\n\t\t<li><a href='Page_7.html' id='Links'>Page 7</a></li>" \
                         "\n\t\t<li><a href='Page_8.html' id='Links'>Page 8</a></li>" \
                         "\n\t</ul>" \
                         "\n</div>"
            # Writing the styles of the navigation bar to styles.css
            os.chdir('Stylesheets')
            css_file = open('styles.css', 'a')
            css_file.write("/* Custom Menu Styles */"
                           "\n.menu{ width:1360px, auto; background: #66ff66;}"
                           "\n.menu ul{ padding:5px; width:1000px, auto; margin:0 auto; text-align: center;}"
                           "\n.menu ul li{ display:inline;  color:#fff;border-left: 1px solid #6f6767; padding: 20px "
                           "10px;} "
                           "\n.menu ul li a{ color: #000000;text-decoration: none;display: inline-block;padding: 16px "
                           "15px;} "
                           "\n.menu ul li a#Links:hover{ color: #000000; background: #5c5cd6; }")
            css_file.close()
            os.chdir('../')
        of_file = open('index.html', 'w')
        if of_file:
            os.chdir('Stylesheets')
            # Writes the Style of the Footer
            of_css_file = open('styles.css', 'a')
            of_css_file.write('\n/* footer styles */'
                              '\n#footer{background-color:black;color:#ffffff;text-align:center;padding:5px;clear:both}'
                              )
            of_css_file.close()
        os.chdir('../Source Code')
        # Writing visible web design code to projectcode.txt text file
        of_code = open('projectcode.txt', 'w')
        of_code.write('<!DOCTYPE html>'
                      '\n<!--This SourceCode is Generated Automatically by AutoCode Web-Design Automator Software ('
                      'gichungeservices@gmail.com/ https://www.gichungekelvin.herokuapp.com )--> '
                      '\n<html>'
                      '\n<head>'
                      '\n   <meta name="author" content="AutoCode Web-Design Automator">'
                      '\n   <meta charset="utf-8">'
                      "\n   <meta name='viewport' content='width=device-width, initial-scale=1'>"
                      "\n   <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
                      "'></script>"
                      "\n   <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
                      "'></script>"
                      "\n   <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"
                      "'></script>"
                      "\n   <link rel='stylesheet' href='bootstrap/css/bootstrap.min.css'>"
                      "\n   <script src='jquery/jquery.min.js'></script>"
                      "\n   <script src='bootstrap/js/bootstrap.min.js'></script>"
                      "\n   <script src='Javascript/sample.js'></script>"
                      "\n   <link rel='stylesheet' href = 'Stylesheets/styles.css'>"
                      '\n' + script +
                      '\n</head>'
                      "\n<body>"
                      '\n' + header +
                      '\n' + navigation +
                      "\n   <div class='container' style='background-color:#d9d9d9'>"
                      "\n      <h1 style='color:#5c5cd6'><b>Top Content</b></h1><br><br><br>"
                      "\n      <h1 style='color:#5c5cd6'><b>Middle Content</b></h1><br><br><br><br><br><br>"
                      "\n      <h1 style='color:#5c5cd6'><b>Footer Content</b></h1><br><br><br>"
                      "\n   </div>"
                      "\n   <div id='footer'>"
                      "\n       <h5>Copyright (c)yourCompany 2017/Year</h5><br>"
                      "\n       <h6>Autocode WebDesign Automator</h6>"
                      "\n       <h6>gichungeservices@gmail.com</h6>"
                      "\n   </div>"
                      '\n</body>'
                      '\n</html>')
        of_code.close()
        # Writes the code to index.html
        os.chdir('../')
        # Writing  the web design code to index.html
        of_file.write('<!DOCTYPE html>'
                      '\n<!--This SourceCode is Generated Automatically by AutoCode Web-Design Automator Software ('
                      'gichungeservices@gmail.com/ https://www.gichungekelvin.herokuapp.com )--> '
                      '\n<html>'
                      '\n<head>'
                      '\n   <meta name="author" content="AutoCode Web-Design Automator">'
                      '\n   <meta charset="utf-8">'
                      "\n   <meta name='viewport' content='width=device-width, initial-scale=1'>"
                      "\n   <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
                      "'></script>"
                      "\n   <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
                      "'></script>"
                      "\n   <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"
                      "'></script>"
                      "\n   <link rel='stylesheet' href='bootstrap/css/bootstrap.min.css'>"
                      "\n   <script src='jquery/jquery.min.js'></script>"
                      "\n   <script src='bootstrap/js/bootstrap.min.js'></script>"
                      "\n   <script src='Javascript/sample.js'></script>"
                      "\n   <link rel='stylesheet' href = 'Stylesheets/styles.css'>"
                      '\n' + script +
                      '\n</head>'
                      '\n<body>'
                      '\n' + header +
                      '\n' + navigation +
                      "\n   <div class='container' style='background-color:#d9d9d9'>"
                      "\n      <h1 style='color:#5c5cd6'><b>Top Content</b></h1><br><br><br>"
                      "\n      <h1 style='color:#5c5cd6'><b>Middle Content</b></h1><br><br><br><br><br><br>"
                      "\n      <h1 style='color:#5c5cd6'><b>Footer Content</b></h1><br><br><br>"
                      "\n   </div>"
                      "\n   <div id='footer'>"
                      "\n       <h5>Copyright (c)yourCompany 2017/Year</h5><br>"
                      "\n       <h6>Autocode WebDesign Automator</h6>"
                      "\n       <h6>gichungeservices@gmail.com</h6>"
                      "\n   </div>"
                      '\n</body>'
                      '\n</html>')
        of_file.close()
        run_html = (str(input("\n\tOpen Your Project? (YES/NO) :"))).upper()
        if run_html == 'YES':
            # Opening the web project on the browser
            print("\n", "OPENING YOUR PROJECT ON THE BROWSER,PLEASE WAIT".center(80))
            # Opens the Project on the Browser
            webbrowser.open('index.html')
            print('\n' + 'GET YOUR READY MADE PROJECT ON C://Autocode Web Automator'.center(80))
            print('\n\n\a' + 'THANK YOU FOR USING AUTOCODE AUTOMATOR,GROWING A NEW WORLD OF '
                             'AUTO-CODING'.center(80))
            os.chdir('../')
        elif run_html == 'NO':
            print('\n' + 'GET YOUR READY MADE PROJECT ON C://Autocode Web Automator'.center(80))
            print('\n\n\a' + 'THANK YOU FOR USING AUTOCODE AUTOMATOR,GROWING A NEW WORLD OF '
                             'AUTO-CODING'.center(80))
            os.chdir('../')
    # Displays the Help Menu
    elif lev1_input == 'CODE-HELP':
        print('\n\tcode-help :  Command to ask for assistance from AutoCode'
              '\n\n\tcode-create-html :  Command to Create a HTML FILE')
input()

# THIS AUTOMATION SOFTWARE IS DESIGNED BY KELVIN GICHUNGE KIMATHI
# Last Review of the Source-Code: APRIL-7-2017 BY:GICHUNGE KELVIN
