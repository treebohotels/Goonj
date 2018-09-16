# Goonj  (WORK In Progress)
A python library to enable easy alerting services across multiple channels.

## Requirement

### What?
A library that can communicate with any alerting channel like Email, SMS, Slack etc..
A library that can generate reports by aggregating information and sending an alert when it crosses customizable thresholds.

### Why?
We often raise alerts from code. Sometimes these alerts require some processing themselves which litter the actual code.
Getting an aggregated alert allows us to determine if there are any major breakages in the product and act on them quickly. It also allows us to determine the severity of the alert in case we’re getting a lot of them through the day.

## Getting started

TBF

## Installation

Simply use the following command to install the latest released version:

    pip install goonj

## Configuration

Define channels needed for alerting
```
channels:
  email_channels:
    - name: email_channel1
      to: xyz@gmail.com,xyz@gmail.com
      subject:
      from_add: xyz@tech.com

    - name: aaaaa
      to:
      subject:
      from_add:
  slack_channels:
    - name: xyz_channel
      webhook: https://hooks.slack.com/services/T067891FY/B95PKS6TZ/WuDm9lYHF
    - name: abc_channel
      webhook: https://hooks.slack.com/services/T067891FY/B95PKS6TZ/WuDm9lYHF
  sms_channels:
    - name : sms1
      phone_numbers: 1234567890,1234567890
    - name : sms2
      phone_numbers: 1234567890
```

Specify settings for channels
```
email_settings:
  custom_notification_service: samples.module.CustomNotificationService  
sms_settings:
  custom_notification_service: samples.module.CustomNotificationService
  
#these are modules for custom notfication that will be called for sending email/sms which extends BaseCustomEmailNotificationService or BaseCustomSMSNotificationService
```
example for CustomNotificationService
```
class CustomNotificationService(BaseCustomEmailNotificationService,
                                BaseCustomSmsNotificationService):

    def send_email_notification(self, from_add, to, sev, message, subject,
                                error_id,
                                error,
                                tag_list):
        print('your logic to send email ')

    def send_sms_notification(self, phone_numbers, sev, message, subject,
                              error_id,
                              error,
                              tag_list):
        print('Your logic to send  sms here ')
```

You can define a source ,Each source can have different sevs ( high medium low)
and channels assocaited with it
```
  source_name1:
     sev:
      high:  
        email_channels:   Each sev will have diffrent channels associated with it 
        - sohit
        slack_channels:
        - xyz_channel
        sms_channels:
        - sms1

      low:
        email_channels:
        - sohit
```
## Key Usage points

Initialize the goonj  
```  
core.Goonj(config_file_path='/path/to/config/goonj.yaml')
```

Get alert source , you can inject logger as well and goonj will take care of logging
 ```
 smart_alert = get_smart_alert('source_name1', logger)
```

If you need only looging  
Use .format to pass string variable instead 
```
smart_alert.info("your genreral logging mesage {}".format("abc"))
smart_alert.error("")
smart_alert.warn()
smart_alert.exception()
smart_alert.error()
```
if you need alerting  along with  logging , pass the sev , it will send alert to channels associated with the given sev in config file 
```
smart_alert.info("your message ",sev=Sev.HIGH,subject="subject for alert")
smart_alert.error("your message",sev=Sev.HIGH,subject="subject for alert")
smart_alert.warn("your message",sev=Sev.HIGH,subject="subject for alert")
smart_alert.exception("your message",sev=Sev.HIGH,subject="subject for alert")
smart_alert.error("your message",sev=Sev.HIGH,subject="subject for alert")
```





## Limitations

Here are the basic limitations which need to be kept in mind while using the library:
1. TBF

## Roadmap

The current limitation of the library is planed to be addressed in the future releases.
also below are some of the key features which are planed for future releases:
1. TBF

## Project history

This project has been inspired to solve basic alerting service requirements.


[1]: TBF

