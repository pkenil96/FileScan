# Learning Path and Notes

## Independent Components

1. Docker
2. Message Queue
3. Spring Boot
4. Flask
5. Service Discovery


---

## Docker

1. Difference between VM and containers
2. Need for VM
3. Need for containers
4. What problem does docker solves?
5. chroot
6. namespaces


chroot - Used for file-level isolation. (Jailing)
This command changes the apparent root directory for the currently running process. When this command is executed in a directory, that directory becomes the root directory for that process and it cannot see anything beyond that directoy without root priveleges. 

**Similarly, there are tools to provide resource level isolation which if used in conjugation with one another maybe used to create altogether a different machine (like VM) within the same machine**

namespaces - Used for resource-level isolation.
It partitions resources such that one set of processes sees one set of resources while another set of process sees different set of resources.

cgroup - Used for setting resource consumption limit.
It is used to limit the amount of resources used per process.

https://www.youtube.com/watch?v=FzwIs2jMESM
---

## Messaging Queue

### Synchronous messaging

A system sends some message/request to the other system and blocks itself till it receives a response from the other message (e.g. HTTP GET request)

### Asynchronous messaging

A system sends some message/request to the other system and does not block itself and continues to perform its task. Once the other system is done processing the request, it sends the response and the initial sender receives it (e.g. Producer/Consumer communication using message queue)

### Message Broker

The intermiediate system that handles the receiving and delivering of messages. Need for message broker? - Why not just keep peer to peer connections? A system can send some message to another and keep doing its work. Once the other system finishes processing, it sends it back to the  original sender.  This is a good way to achieve the purpose, however, whenever a new machines comes up, it needs to directly connect itself to all the machines. Thus, if there are n machines, there has to be n*n-1 connections. So, a message broker is used. Now, each newly added machine needs to connect only to the mesage broker.

---

## Spring Boot

**@Component vs @Bean**
@Component is used for component scanning and automatic wiring. For example, if there is a class that needs to be made available for injection, then we annotate it with @Component. What happens then is, whenever the spring application is initialized, all the classes are scanned (@ComponentScan) and the classes with @Component tags are instantiated and stored in the IoC containers for future use. So, in future whenever we declare a class and annotate it with @Autowired, spring will look for the instance of that class in its IoC container and thereby eliminating the need to explicitly instantiate it.

@Bean annotation above a method tells spring that this method produces a bean to be managed by the spring container. This is a method level annotation. @Bean is used over @Component in situations wherein automatic configuration is not an option. Lets imagine that you want to wire components from a 3rd party library for which you don't have source code so you cannot annotate its classes with @Component. In such a case, we create a method and annotate it with @Bean. This method then returns an object required by the application. The body of the method bears the logic responsible for creating the instance.

---