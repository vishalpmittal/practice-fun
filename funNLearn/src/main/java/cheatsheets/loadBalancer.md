
* A load balancer is a device that acts as a reverse proxy and distributes 
  network or application traffic across a number of servers. 
 
* Load balancers are used to increase capacity (concurrent users) and reliability 
  of applications.

  They improve the overall performance of applications by decreasing the burden 
  on servers associated with managing and maintaining application and network sessions, 
  as well as by performing application-specific tasks.

## Categories
-------------
* Layer 4 : Layer 4 load balancers act upon data found in network and transport 
  layer protocols (IP, TCP, FTP, UDP). 

* Layer 7 load balancers distribute requests based upon data found in application 
  layer protocols such as HTTP.

  Layer 7 load balancers can further distribute requests based on application specific 
  data such as HTTP headers, cookies, or data within the application message itself, 
  such as the value of a specific parameter.

## Algorithms
--------------
* Round robin

* Weighted round robin

* Least connections

* Least response time / latency

* IP Hash – The IP address of the client is used to determine which server 
  receives the request.

* URL hash. Much like source IP hash, except hashing is done on the URL of the request. 
  Useful when load balancing in front of proxy caches, as requests for a given object 
  will always go to just one backend cache.

* Client ID key hashing