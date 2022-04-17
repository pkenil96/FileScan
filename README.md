# FileScan
This simple application takes a file and an email address/phone number. It then scans the file and sends a summary of the meta data of the file and whether it is safe or not via email/phone to the user.

## Architecture

Microservices - Each microservice will be a spring boot application.  

1. FileScanApp: User facing main app that accepts email or phone and a file to scan
2. StorageManager: Accepts owner info and file. Uploads it to cloud and return public URL
3. MessagePublisher: Accpets owner info and file URL. Publishes it to the queue
4. AntiVirusScanner: Accpets owner info and file URL. Scans for virues and publish result to queue
5. MetaDataExtractor: Accpets owner info and file URL. Extracts metadata from file and publish result to queue
6. Notifier: Accepts owner info and the result and pass it on to the EmailMessager or PhoneMessager
7. EmailMessager: Accepts owner info and the result and sends out email to user
8. PhoneMessager: Accepts owner info and the result and sends out text message to user

## Tech Stack Used
  
1. Spring Boot (StorageManager, MessagePublisher, MetaDataExtractor, AntiVirusScanner, Notifier)
2. Flask (FileScanApp, EmailMessager, PhoneMessager)
3. RabbitMQ (MessageQueue)
4. Bucket4JS (Rate Limiter)
5. Redis (Caching)
6. Docker (Deploying Redis Server)
7. Netflix Eureka Service Discovery (Service Discovery)


## Architecture Diagram
