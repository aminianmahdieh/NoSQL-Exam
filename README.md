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
* Ubuntu interface
* Java with version higher than 8
* python
* Start Kafka Server and Zookeeper
* Docker engine and docker-compose
* clone a repository


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
  
## Install Java on Ubuntu:

In order to install java on your machine, go to the [Orcle Java Page](https://www.oracle.com/java/technologies/javase-downloads.html) and download the latest version of the linux debian package. Then go to the your download folder and extract the pakage by:
```
sudo dpkg -i jdk-15.0.1_linux-x64_bin.deb
```
Then:
```
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-15.0.1/bin/java 1

sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-15.0.1/bin/javac 1
```
To see if it's installed properly: 
```
java --version

javac --version
```
Now In order to add the Java path to the machine path so it be availabe to all other softwares:
First; we must find the Java pathe:
```
sudo update-alternatives --config java
```
copy the result path till the jdk address. Then add this address at the end of:
```
sudo gedit /etc/environment
```
Like:
```
JAVA_HOME="the copied path"
```
save and exit. Then in the terminal type:
```
source /etc/environment

echo $JAVA_HOME
```
## Python

python is for sure by default on the system. Here I just explain hoe to get an interpreter for it. I choose Pycharm but you can choose any other interpreter that you like.
Go to the [Pycharm download webpage](https://www.jetbrains.com/pycharm/download/#section=linux) and download the community version of pycharm.
Go to your download folder and manually unzip the downloaded package there.
Now open the terminal and go the extracted pycharm folde:
```
cd bin
./pycharm.sh
```
pycharm will start on the backgroung.
Now you have a python interpreter to work with.

## Kafka

In order to run kafka server we have 2 options:
1. Start kafka server and zookeeper manually from scratch 

or

2. clone a repository that already have all this planned in itself.


### First option:
First, Go to the [Apache kafka quickstart page](https://www.apache.org/dyn/closer.cgi?path=/kafka/2.7.0/kafka_2.13-2.7.0.tgz) and download and move the downloaded zip folder to the opt directory where you download all your softwares or you can do as follow:
```
cd /opt
wget https://downloads.apache.org/kafka/2.7.0/kafka_2.13-2.7.0.tgz 
```
Nowl unzip the file by:
```
tar -xvzf kafka_2.13-2.7.0.tgz

cd kafka_2.13-2.7.0
```
Now we must change the configuration setting of the kafka server and zookeeper. Thus:
```
cd config

sudo nano server.properties
```
find the following commands and change them as follow:
```
advertised.listeners = PLAINTEXT://localhost:9092

zookeeper.connect = localhost:2181
```
save it and exit. Now to run zookeeper first:
```
sudo bin/zookeeper-server-start.sh config/zookeeper.properties
```
And then open a new terminal go to the same folder and start kafka server:
```
sudo bin/kafka-server-start.sh config/server.properties
```

### Second Option:
In this Option; first we need to install docker-compose on our system. All the steps to install docker is explained by details in [docker engine page](https://docs.docker.com/engine/install/ubuntu/). ButI also brifely mention the steps here.

#### Install docker-compose
##### Set up the repository

Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```
sudo apt-get update
sudo apt-get install \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg-agent \
     software-properties-common
```
Then add Docker’s official GPG key:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
And verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint as follow:
```
sudo apt-key fingerprint 0EBFCD88
```
Now use the following command to set up the stable repository. 
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
##### Install Docker Engine
Update the apt package index, and install the latest version of Docker Engine and containerdL
```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Verify that Docker Engine is installed correctly by running the hello-world image.
```
sudo docker run hello-world
```
##### Install Docker compose
Run this command to download the current stable release of Docker Compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Then apply executable permissions to the binary:
```
sudo chmod +x /usr/local/bin/docker-compose
```
Now test the installation:
```
docker-compose --version
```

Now we have docker-compose on our system now we can clone the repository:
```
cd /opt

sudo git clone https://github.com/gboissinot/esilv-kafka.git

cd esilv-kafka/collection-tier.src.main

sudo docker-compose up
```
Then when it's run completely you should open [http://127.0.0.1:3030]. Which is the interface of your kafka.








