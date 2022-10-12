from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color
import csv, os

while True:
    print("Would you like to:\n1. Generate Certificates\n2. Email Certificates\n3. End Program")
    main_opt = int(input("Your Choice: "))
    if main_opt == 1:
        print("Great. And who are you generating Certificates for:\n1. A particular State/College\n2. Everyone in the imported CSV file.")
        sub_one = int(input("Your Choice: "))
        rakshins = []

        if sub_one == 1:
            id_code = input("Enter the 4-letter College Code/2-letter State Code: ")
            file = open("assets/rakshins.csv", "r", encoding = 'utf-8')
            data = csv.reader(file)

            for rakshin in data:
                r_id = rakshin[4].split("-")
                if len(id_code) == 4 and id_code == r_id[2]:
                    rakshins.append(rakshin)
                if len(id_code) == 2 and id_code == r_id[3]:
                    rakshins.append(rakshin)

        if sub_one == 2:
            file = open("assets/rakshins.csv", "r", encoding = 'utf-8')
            data = csv.reader(file)
            for rakshin in data:
                rakshins.append(rakshin)

        for i in rakshins:
            rname,rclg,rdate,rstate,rid,rmail = i[0],i[1],i[2],i[3],i[4],i[5]
            if not os.path.exists("output"):
                os.mkdir("output")
            if not os.path.exists("output/"+rstate):
                os.mkdir("output/"+rstate)
            if not os.path.exists("output/"+rstate+"/"+rclg):
                os.mkdir("output/"+rstate+"/"+rclg)
            if not os.path.exists("output/"+rstate+"/"+rclg+"/"+rname+".pdf"):
                pdfname = ("output/"+rstate+"/"+rclg+"/"+rname+".pdf")
                c = canvas.Canvas(pdfname, pagesize = (862.5,600))
                c.setTitle(rname+"'s Certificate One")
                c.drawImage("assets/cert-1.jpg", 0, 0, width = 862.5, height = 600)
                pdfmetrics.registerFont(TTFont('Allura', 'assets/allura.ttf'))

                c.setFillColor(Color(0, 0, 0, alpha = 1))

                c.scale(1, 1)
                c.setFont("Allura", 40)
                c.drawCentredString(431.25, 290, rname)

                c.setFont("Helvetica", 10)
                c.drawString(66, 95, rdate)
                c.drawString(70, 75, rstate)
                c.drawString(87.5, 53, rclg)
                c.drawString(102.5, 31, rid)

                c.showPage()
                c.save()

                print(rid)

    if main_opt == 2:
        import pickle, os, smtplib
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        from email.header import Header
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        SCOPES = ['https://www.googleapis.com/auth/drive.metadata','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file']

        def get_gdrive_service():
            creds = None
            if os.path.exists('assets/token.pickle'):
                with open('assets/token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'assets/credentials.json', SCOPES)
                    creds = flow.run_local_server(port = 0)
                with open('assets/token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            return build('drive', 'v3', credentials = creds)

        def connect_mail_server():
            global server
            server = smtplib.SMTP('REDACTED')
            server.connect('REDACTED', REDACTED)
            server.starttls()
            server.login("REDACTED","REDACTED")

        def py_mail(body, receiver_name, receiver_mail):
            message = MIMEMultipart('alternative')
            message['subject'] = ("Hey "+rname.split()[0]+", your TRP Certificate is here!")
            message['To'] = str(Header(receiver_name+" <"+receiver_mail+">"))
            message['From'] = str(Header('The Rakshin Project <certify@therakshinproject.org>'))
            html_body = MIMEText(body, 'html')
            message.attach(html_body)
            server.sendmail("certify@therakshinproject.org", [receiver_mail], message.as_string())
        
        def search(service, query):
            result = []
            page_token = None
            while True:
                response = service.files().list(q = query,
                                                spaces = "drive",
                                                corpora = "drive",
                                                driveId = "0AGLRKQVwlNfHUk9PVA",
                                                supportsAllDrives = True,
                                                includeItemsFromAllDrives = True,
                                                fields = "nextPageToken, files(id, name, mimeType)",
                                                pageToken = page_token).execute()
                for file in response.get("files", []):
                    result.append(file["id"])
                page_token = response.get('nextPageToken', None)
                if not page_token:
                    break
            return result

        def findcert(rakshin_id):
            service = get_gdrive_service()
            search_result = search(service, query = f"fullText contains '\"{rakshin_id}\"'")
            global search_error
            search_error = 0

            if len(search_result) == 1:
                global file_id
                file_id = (search_result[0])
                return file_id
            
            elif len(search_result)>1:
                search_error = 1
            
            elif len(search_result)<1:
                search_error = 2

        input("Click the enter key to initialize connection with Google Drive API.")
        get_gdrive_service()
        input("Click the enter key to initialize mail server connection.")
        connect_mail_server()

        print("Great. And who are you emailing Certificates to:\n1. A particular State/College\n2. Everyone in the imported CSV file.")
        sub_one = int(input("Your Choice: "))
        rakshins = []

        if sub_one == 1:
            id_code = input("Enter the 4-letter College Code/2-letter State Code: ")
            file = open("assets/rakshins.csv", "r", encoding = 'utf-8')
            data = csv.reader(file)

            for rakshin in data:
                r_id = rakshin[4].split("-")
                if len(id_code) == 4 and id_code == r_id[2]:
                    rakshins.append(rakshin)
                if len(id_code) == 2 and id_code == r_id[3]:
                    rakshins.append(rakshin)

        if sub_one == 2:
            file = open("assets/rakshins.csv", "r", encoding = 'utf-8')
            data = csv.reader(file)
            for rakshin in data:
                rakshins.append(rakshin)

        for i in rakshins:
            rname,rclg,rdate,rstate,rid,rmail = i[0],i[1],i[2],i[3],i[4],i[5]

            gdriveid = findcert(rid)

            if search_error == 0:
                content1="""<style>@media screen and (max-width:767px) {.w-row {margin-left: 0; margin-right: 0;}}@media screen and (max-width:991px) { .footer { padding-right: 20px; padding-left: 20px; } } @media screen and (max-width:767px) { .footer { padding: 40px 20px; } } @media screen and (max-width:479px) { .footer { padding-right: 20px; padding-left: 20px; text-align: left; } .footer-logo-link { height: 60px; } } </style><div class="email-wrapper" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; margin: 0; padding: 40px 20px; background-color: #fff; font-family: 'Trebuchet MS','Lucida Grande','Lucida Sans Unicode','Lucida Sans',Tahoma,sans-serif; color: #3b3f49; font-size: 16px; line-height: 1.4;"> <div class="email-content-wrapper" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; max-width: 700px; margin-right: auto; margin-left: auto; border-radius: 20px;"> <div class="forty-below center" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; text-align: center; margin-bottom: 40px;"> <div style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;"><a href="https://rakshinproject.org" class="brand-logo w-inline-block" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; background-color: transparent; color: #2B489F; text-decoration: none; display: inline-block; max-width: 100%;"><img src="https://rakshinproject.org/wp-content/uploads/2022/02/mass-logo.png" height="60" alt="" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; border: 0; max-width: 100%; vertical-align: middle; display: inline-block;"></a></div> </div> <div class="row-light" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; margin-bottom: 40px; padding: 50px; border-radius: 15px; background-color: #f5f5f5;"> <div class="row-content center row" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; text-align: center; display: block; max-width: 500px; margin-right: auto; margin-left: auto;"> <div class="label" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; margin-bottom: 5px; color: #2B489F; font-size: 12px; font-weight: 700; text-transform: uppercase;">Congratulations on your achievement!</div> <h2 style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; font-weight: 700; line-height: 36px; margin-top: 0; margin-bottom: 10px; color: #3b3f49; font-size: 28px;">Your Certificate is Here</h2> <p style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; margin-top: 0; margin-bottom: 20px; color: #656a77;">You truly are leading by example to make a difference and #EndChildSexualAbuse. You"ve worked hard and proved to yourself and everyone what you are capable of. But this is merely the beginning of your journey! We have many more certifications waiting for you. That"s right; The Rakshin Project is offering you the chance to become a Rakshin Fellow. Scroll down below and click on the <i style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;">Continue</i> button to keep your streak going!<br style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;"><br style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;">Check out <a href="https://rakshinproject.org">our website</a> now!</p> <a href=\""""
                gdrivelink=("https://drive.google.com/file/d/"+gdriveid+"/view")
                content2="""" class="button-large w-button" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; display: inline-block; border: 0; line-height: inherit; text-decoration: none; cursor: pointer; width: 100%; max-width: 320px; padding: 15px 30px; border-radius: 10px; background-color: #2B489F; color: #fff; font-size: 16px; font-weight: 700; text-align: center;">Download Certificate</a></div> </div> <div class="row-outline" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; margin-bottom: 40px; padding: 20px; border-style: solid; border-width: 2px; border-color: #f5f5f5; border-radius: 15px;"> <div class="row-content center" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; text-align: center; display: block; max-width: 500px; margin-right: auto; margin-left: auto;"> <div style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;"> <h3 style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; font-weight: 700; line-height: 30px; margin-top: 0; margin-bottom: 10px; color: #3b3f49; font-size: 24px;">Continue with TRP</h3> <p style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; margin-top: 0; margin-bottom: 20px; color: #656a77;">Click on the 'Continue' button to register for the next step in your journey as a Rakshin. If you face any problems or find errors on your certificate, just fill in the error form linked below and we"ll get it rectified ASAP.</p> <div class="button-group" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; display: inline-block; margin-right: 5px; margin-left: 5px;"><a href="https://forms.gle/k3AEZ3A75NnFi4eT7" class="button w-button" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; border: 0; line-height: inherit; text-decoration: none; cursor: pointer; display: inline-block; min-width: 100px; padding: 12px 25px; border-radius: 10px; background-color: #2B489F; color: #f5f5f5; font-size: 16px; font-weight: 700;">Continue as a Rakshin</a></div> <div class="button-group" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; display: inline-block; margin-right: 5px; margin-left: 5px;"><a href="https://forms.gle/WSvqDbH7ZjvQnS658" class="button-light w-button" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; border: 0; line-height: inherit; text-decoration: none; cursor: pointer; display: inline-block; min-width: 100px; padding: 12px 25px; border-radius: 10px; background-color: #f5f5f5; color: #3b3f49; font-size: 16px; font-weight: 700;">Report Error</a></div> </div> </div> </div> <div class="row" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;"> <div class="social-links center text-small" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; text-align: center; color: #656a77; margin-bottom: 20px; font-size: 0;"> <a href="https://www.facebook.com/therakshinproject" target="_blank" class="social-icon w-inline-block" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; color: #2B489F; text-decoration: none; max-width: 100%; display: inline-block; margin-right: 10px; margin-left: 10px; padding: 10px; border-radius: 20px; background-color: #f5f5f5;"><img src="https://rakshinproject.org/wp-content/uploads/2022/02/mass-fb.png" width="20" alt="" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; border: 0; max-width: 100%; vertical-align: middle; display: inline-block;"></a> <a href="https://www.instagram.com/therakshinproject/" class="social-icon w-inline-block" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; color: #2B489F; text-decoration: none; max-width: 100%; display: inline-block; margin-right: 10px; margin-left: 10px; padding: 10px; border-radius: 20px; background-color: #f5f5f5;"><img src="https://rakshinproject.org/wp-content/uploads/2022/02/mass-insta.png" width="20" alt="" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; border: 0; max-width: 100%; vertical-align: middle; display: inline-block;"></a> <a href="https://twitter.com/therakshinproj" class="social-icon w-inline-block" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; color: #2B489F; text-decoration: none; max-width: 100%; display: inline-block; margin-right: 10px; margin-left: 10px; padding: 10px; border-radius: 20px; background-color: #f5f5f5;"><img src="https://rakshinproject.org/wp-content/uploads/2022/02/mass-twt.png" width="20" alt="" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; border: 0; max-width: 100%; vertical-align: middle; display: inline-block;"></a> </div> <div class="center" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; text-align: center;"> <div class="text-light text-small" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; font-size: 14px; color: #969caa;">Crafted with ♥ by <strong style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; font-weight: 700;">TRP by Sakshi</strong></div><div class="text-small text-light" style="-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; font-size: 14px; color: #969caa;">665-666/2, Ghitorni Village, New Delhi – 110030, India</div></div></div></div></div>"""
                content=(content1+gdrivelink+content2)

                py_mail(content, rname, rmail)
                print(rid)
            
            elif search_error == 1:
                print("More than one result found for "+rid+".")
            
            elif search_error == 2:
                print("No results found for "+rid+".")

        server.quit()

    if main_opt == 3:
        print("Cool. See you later.")
        break
