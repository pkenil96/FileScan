# High Level Design

1. *FileScanApp* - Flask App
    - **Input**: User facing interface that accepts user details and the file to be scanned
    - **Cache Lookup**: Makes call to redis server using file hash:
        * CACHE HIT: Returns the cached value to the Notifier
        * CACHE MISS: Forwards user email and the file to the *StorageManager*
2. *StorageManager* - Spring Boot App
    - **Upload to cloud**:
        * Uploads the file to cloud storage and returns public URL
        * Forwards the user email and file URL to the *MessagePublisher*
3. *MessagePublisher* - Spring Boot App
    - **Publish message on the queue**: Publishes user email and file URL to RabbitMQ
4. *MessageQueue* - RabbiMQ
    - **Notifies the subscriber**: Whenever any producer (here *MessagePublisher*) publishes anything on the queue, it notifies all its subscribers (here *AntiVirusScanner*)
5. *AntiVirusScanner* - Spring Boot App
    - **Scans for virus**: This service scans the file for virus
        * VIRUS FOUND: Returns the result to the Notifier
        * VIRUS NOT FOUND: Forwards the user email, file and the result to the MetaDataExtractor service
6. *MetaDataExtractor* - Spring Boot App
    - **Extracts metadata**: Extracts information about the file and append it to the result from the *AntiViruScanner* service and forwards it to the *Notifier*
7. *Notifier* - Spring Boot App
    - **Initiate notification**: Forwards the result using appropriate messaging channel. If the user provided email, *Notifier* invokes *EmailMessager* else *PhoneMessager*
8. *EmailMessager* - Flask App
    - **Sends result via email**
9. *PhoneMessager* - Flask App
    - **Sends result via SMS**
