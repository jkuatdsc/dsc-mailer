# dsc-mailer

A simple mailing library for python powered applications using Sendgrid.

<img src="https://github.com/jkuatdsc/dsc-mailer/blob/master/assets/dsc_mailer.png?raw=true" width="1000">


## Installation

To install the library using pip, run;

  

``pip install dsc-mailer``

  

## Required parameters

The library has one module for sending emails `mailer`

  

> the mailer module contains a send_mail function that expects five parameters

  

* Sender

* Receiver

* Email Subject

* Html Content

* Sendgrid Api_key



## Example Usage

  

```python
from dscmailer import mailer
my_email = mailer.send_mail(sender, receiver, subject, html_content, api_key)

```


