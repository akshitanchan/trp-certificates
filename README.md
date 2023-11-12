## About The Project
This code is designed to generate TRP certificates at a large scale. Made possible due to the extensive flexibility of Google's Drive API v3. Using the same and a proprietary SMTP relay, we have created a system that looks for the certificate and emails it to the receiver via SMTP. We have replaced the standard plain-text email format with a heavily-optimized HTML mail format.

Use the `main.py` to get started.

## Built With
Here is a list of the frameworks, libraries and modules we have used to bootstrap this project.
* [Python](https://www.python.org/)
* [SMTPLib](https://docs.python.org/3/library/smtplib.html)
* [ReportLab](https://pypi.org/project/reportlab/)
* [Google Drive API](https://developers.google.com/drive/api)

## Getting Started
Follow the instructions below to set up the service locally. To get a local copy up and running, simply follow the steps below. Make sure all prerequisites are accounted for.

## Prerequisites
The following list of prerequisites assumes that you have Python installed and added to PATH. If not, follow [this guide](https://realpython.com/installing-python/) to download Python and [this guide](https://www.geeksforgeeks.org/how-to-add-python-to-windows-path/) to add Python to PATH.

* ReportLab
  ```sh
  python -m pip install reportlab
  ```

* Google Drive API
  ```sh
  python -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib tabulate requests tqdm
  ```

* Certificate Recipients CSV
  Prepare a list of recipients. Make sure that it follows given template. Straying away from the template's formatting would create breaks and errors in the code. Be sure to remove the table header before beginning the import process.

## How to Use
Click [here](https://github.com/sakshiorg/trp-certificate-generator/archive/refs/heads/main.zip) to download the entire code as a zipped folder. Unzip the folder where appropriate. Place the prepared CSV file with list of certificate recipients into the assets folder (where the template.csv sits). Rename every occurence of `template.csv` in `main.py` to your CSV file's name. Begin running the `main.py` file. Select the options from the menu as necessary. If you select generation of certificates, a new folder with certificates will be generated. A pre-requisite for mailing certificates is that the generated certificates must be uploaded to a Google Drive, set to view with link, and a user with editor access to those files must authenticate the connection. You can then wait as the files are automatically sent via a Google Drive link (to reduce overhead in mail weight).

## Roadmap
- [x] Add mailing capabilities
- [x] Add specific generation options
- [x] Add option to generate and mail certificates w/o upload
- [ ] Multi-language Support
    - [x] Hindi
    - [ ] Other regional languages

See the [open issues](https://github.com/sakshiorg/trp-certificate-generator/issues) for a full list of proposed features (and known issues).

## License
Distributed under the MIT License. See the `LICENSE` file for more information.
