# FileScan

This simple application takes a file and an email address/phone number. It then scans the file and sends a summary of the meta data of the file and whether it is safe or not via email/phone to the user.

## Architecture

* Each microservice will be a Spring boot or Flask app
* There will be a *Serice Discovery* server. Each microservice registers itself to this service discovery. Any request from the client will be router through this service discovery
* A dedicated Redis server has been deployed and placed between the FileScanApp and StorageManager  

Microservices

1. *FileScanApp*: User facing main app that accepts email or phone and a file to scan
2. *StorageManager*: Accepts owner info and file. Uploads it to cloud and return public URL
3. *MessagePublisher*: Accpets owner info and file URL. Publishes it to the queue
4. *AntiVirusScanner*: Accpets owner info and file URL. Scans for virues. If virus is found, it directly forwards the result to the *Notifier*. In case the file is clean, it forwards the email, file URL and the result to the *MetaDataExtractor* service
5. *MetaDataExtractor*: Accpets owner info and file URL. Extracts data from file and publish result to queue
6. *Notifier*: Accepts owner info and the result and pass it on to the *EmailMessager* or *PhoneMessager*
7. *EmailMessager*: Accepts owner info and the result and sends out email to user
8. *PhoneMessager*: Accepts owner info and the result and sends out text message to user

## Topics of Interest

1. Docker
2. Message Queue
3. Service Discovery
4. Caching

## Tech Stack Used
  
1. Spring Boot (*StorageManager*, *MessagePublisher*, *MetaDataExtractor*, *AntiVirusScanner*, *Notifier*)
2. Flask (*FileScanApp*, *EmailMessager*, *PhoneMessager*)
3. RabbitMQ (MessageQueue)
4. Bucket4JS (Rate Limiter)
5. Redis (Caching)
6. Docker (Deploying Redis Server)
7. Netflix Eureka Service Discovery (Service Discovery)
8. AWS S3 (File Storage)

## Architecture Diagram

![architecture diagram](https://raw.githubusercontent.com/pkenil96/images/main/FileScanArchDiag.png)

## Other Requirements

1. Unit Test for each microservice
2. Dockerize each microservice

## Future Scope

1.Adding authentication
    - OAuth
    - SSO (3rd party login)
2.Adding multiple cloud providers
    - Google Cloud Storage
    - Azure Blob Storage
    - Google Drive
    - Dropbox
3.Deploy the app to GCP App Engine