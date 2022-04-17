# FileScan
This simple application takes a file and his/her email address/phone number. It then scans the file and sends a summary of the file and whether it is safe or not via email/phone to the user.

## Architecture

Microservices - Each microservice will be a spring boot application.  

* FileScanApp: User facing main app that accepts email or phone and a file to scan
* StorageManager: Accepts owner info and file. Uploads it to cloud and return public URL
* MessagePublisher: Accpets owner info and file URL. Publishes it to the queue
* AntiVirusScanner: Accpets owner info and file URL. Scans for virues and publish result to queue
* MetaDataExtractor: Accpets owner info and file URL. Extracts metadata from file and publish result to queue
* Notifier: Accepts owner info and the result and pass it on to the EmailMessager or PhoneMessager
* EmailMessager: Accepts owner info and the result and sends out email to user
* PhoneMessager: Accepts owner info and the result and sends out text message to user

## Tech Stack Used
  
* Spring Boot (StorageManager, MessagePublisher, MetaDataExtractor, AntiVirusScanner, Notifier)
* Flask (FileScanApp, EmailMessager, PhoneMessager)
* RabbitMQ (MessageQueue)
* Bucket4JS (Rate Limiter)
* Redis (Caching)
* Docker (Deploying Redis Server)
* Spring Cloud: Eureka Netflix (Service Discovery)


## Architecture Diagram