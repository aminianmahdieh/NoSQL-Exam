# NoSQL-Exam


## MAIN CONCEPTS

* Choose a continuous data source (available in API)
* Collect the data in a Kafka topic
* Query the API at a given interval
* Produce a Kafka message for each data capture
* Continuous data processing with Kafka Stream & KSQL
* Aggregated data production
* Writing in new topics
* Ingest denormalized data into MongoDB
* Connectivity with a geoloc system.
* Students are in charge of finding the use case regarding its data source

## Prequesitions
* Java with version higher than 8
* Start Kafka Server and Zookeeper
* Docker engine and docker-compose
* clone a repository
* python

## Ubuntu Interface
Since my own pc system is windows10 pro; I needed the ubuntu system to be able to run this program so I designed a ubuntu virtual machine as follow:

### RUN Ubuntu in a VM in Hyper_V

1. Enable Hyper_V:
  To enable hyper_v; open powershell with admin rights and write:
  ```
  Enable-WindowsOptionalFeature -Online -Feature Microsoft-Hyper-V -All
  ```
  Then it prompts you to a restart which you should confirm.
  
2. Run Hyper_V manager:
  Now that Hyper_v is enabled; write in the search box Hyper and click on the Hyper-V manager.
  
3. Choose quick create:
  Inside the Hyper-V manager, choose quick create which is on the left column on the top.
 
4. Choose Ubuntu:
  Choose the version of Ubuntu that you like.
  After the download is completed, clicl on connect and then start. 
  Thus Ubuntu starts. on the first run; you must choose basic parameters based on your needs. Continue the initial setup by creating a user and password.
  After the initial configuration finishes, the ubuntu reboot itself.
  
5. Make Ubuntu full screen:
  Inside your Ubuntu system, open the terminal, and type:
  ```
  sudo nano /etc/default/grub
  ```
  And change the following lines:
  ```
  GRUB_CMDLINE_LINUX_DEFAULT=video=hyperv_fb:1920x1080
  GRUB_CMDLINE_LINUX=video=hyperv_fb:1920x1080
  ```
  save it and exit; then:
  ```
  sudo update-grub
  sudo reboot
  ```  
  Now you have a full screean ubuntu in a VM in Hyper-V.
  
  
  

