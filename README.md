# AQMS - Air Quality Monitoring System

AQMS is my bechelor's degree final project.

Due to my absent class activities,
I develop my final project all by myself with 
Asst.Prof.Dr.Visit Hirankitti as my project advisor. 

It is a Python web application develop with Django Webframework.

It is also my first Django project that I learn and develop along the way.

# Description

AQMS Stands for Air Quality Monitoring System.
In this project, I aim to develop a weather monitoring system based on LoRa 
and MQTT technology. We develop a weather monitoring station using LoPy 
microcontroller equipped with sensors to measure weather properties such as 
temperature, relative humidity, PM10 concentration, and PM2.5 concentration. Besides 
of these capabilities. 
By creating our own local LoRa network, we use LoPy microcontroller as the main 
device both end node and gateway of LoRa system. At the gateway, the received data 
is sent to a cloud server via MQTT messaging protocol. Then, MQTT cloud server 
will further send the data to our web application running on a server to log the data on 
our database server. We represent the data through a web-based application that we 
develop with Django framework and use Grafana which is visualization tool to
perform advanced data visualization and transmission in our front-end website.

P.S. I intend to present only the web server part of the project(Django) because the hardware part is not my strong suit.
