<div id="top"></div>
<div align="center">
  <a href="https://github.com/sakshiorg/trp-certificate-generator">
    <img src="https://rakshinproject.org/wp-content/uploads/2021/01/Untitled-1.png" alt="TRP Logo" width="80" height="80">
  </a>

  <h3 align="center">TRP Certificate Generator</h3>

  <p align="center">
    The simple code solution developed to automatically generate Rakshin Certificates at a large scale.
    <br>
    <a href="https://github.com/sakshiorg/trp-certificate-generator/blob/master/README.md"><strong>Explore the docs »</strong></a>
    <br>
    <br>
    <a href="https://github.com/sakshiorg/trp-certificate-generator">View Demo</a>
    ·
    <a href="https://github.com/sakshiorg/trp-certificate-generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/sakshiorg/trp-certificate-generator/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#how-to-use">How to Use</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributions</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This auto-generator is a code-editor based program that was designed to generate TRP certificates at a large scale and sort them based on geolocation and the receiver's university. The code pumps out the certificates in PDF format. If these are uploaded to a Google Drive folder, you may also email the certificates to the student! This was made possible due to the extensive flexibility of Google's Drive API v3. Using the same and a proprietary SMTP relay, we have created a system that looks for the certificate and emails it to the receiver via SMTP. We have replaced the standard plain-text email format with a heavily-optimized HTML mail format.

Here's why this project was made:
* You shouldn't be doing the same tasks over and over.
* Your time should be focused on building something amazing.
* You shouldn't have to repeat DRY processes in your workplace :smile:

Use the `main.py` to get started.

<p align="right">(<a href="#top">Back to Top</a>)</p>

## Built With

Here is a list of the frameworks, libraries and modules we have used to bootstrap this project.

* [Python](https://www.python.org/)
* [SMTPLib](https://docs.python.org/3/library/smtplib.html)
* [ReportLab](https://pypi.org/project/reportlab/)
* [Google Drive API](https://developers.google.com/drive/api)

<p align="right">(<a href="#top">Back to Top</a>)</p>

## Getting Started

Follow the instructions below to set up the generator locally. To get a local copy up and running, simply follow the steps below. Make sure all prerequistes are present.

### Prerequisites
The following list of prerequisites assumes that you have Python installed and added to PATH. If not, follow [this guide](https://realpython.com/installing-python/) to download Python and [this guide](https://www.geeksforgeeks.org/how-to-add-python-to-windows-path/) to add Python to PATH. Also, make sure you use an appropriate code-editor. I'm partial to VS Code but to each person their own.

* ReportLab

  ```sh
  python -m pip install reportlab
  ```

* Google Drive API

  ```sh
  python -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib tabulate requests tqdm
  ```

* Certificate Recipients CSV
  Prepare a list of recipients. Make sure that it follows [this template](). Straying away from the template's formatting would create breaks and errors in the code. Be sure to remove the table header before beginning the import process.
  
<p align="right">(<a href="#top">Back to Top</a>)</p>

## How to Use

Place the prepared CSV file with list of certificate recipients into the assets folder (where the template sits). Begin running the `main.py` file. Select the options from the menu as necessary. If you select generation of certificates, a new folder with certificates will be generated. A pre-requisite for mailing certificates is that the generated certificates must be uploaded to a Google Drive, set to view with link, and a user with editor access to those files must authenticate the connection. You can then wait as the files are automatically sent via a Google Drive link (to reduce overhead in mail weight).

<p align="right">(<a href="#top">Back to Top</a>)</p>

## Roadmap

- [x] Add mailing capabilities
- [x] Add specific generation options
- [ ] Add option to generate and mail certificates w/o upload
- [ ] Multi-language Support
    - [ ] Hindi
    - [ ] Other regional languages

See the [open issues](https://github.com/sakshiorg/trp-certificate-generator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">Back to Top</a>)</p>

## Contributions

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star. Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">Back to Top</a>)</p>

## License

Distributed under the MIT License. See the `LICENSE` file for more information.

<p align="right">(<a href="#top">Back to Top</a>)</p>

## Contact

Name: Akshit Anchan
<br>
Website: [akshitanchan.com](https://akshitanchan.com)
<br>
E-mail: akshit@sakshi.org.in

<p align="right">(<a href="#top">Back to Top</a>)</p>
