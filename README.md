# dsc-mailer

A simple mailing library for python powered applications using Sendgrid.

<img src="" width="1000">

## Installation

To use the library using pip, run;

  

``pip install dsc-mailer``

  

## Usage

The library has one module for sending emails `mailer`

  

> the mailer module contains a sendmail function that expects five parameters

  

* Sender

* Receiver

* Email Subject

* Html Content

* Sendgrid Api_key

  
  

## Example Usage

  

```python
from dsc-mailer import mailer
my_email = mailer.send_mail(sender, receiver, subject, html_content, api_key)

```