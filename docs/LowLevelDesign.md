# Microservices

* Any microservce that sends object to Notifier service must have at least two keys: 'destination' and 'messageBody'. Failing to do so will break the flow of the Notifier service.

1. FileScanApp

  POST ```/hash```

  GET ```/cache/lookup```

  POST ```/cache/update```

2.StorageManager

3.MessagePublisher

4.AntiVirusScanner

5.MetaDataExtractor

6.Notifier

7.EmailMessager

8.PhoneMessager

  POST ```/send/sms```
