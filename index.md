# INTRODUCTION

### This project is done in collaboration with a group of NYP students as part of their effort to develope a prototype to demonstrate the efficiency brought about by digitisation.

# INTEGRATED PATIENT CENTRIC HEADBOARD DISPLAY

### The patient headboard contains information that are critical to responsive bedside care.  The information are contributed by various members of the healthcare team which keyed the information into the main system.  At the time of this project, a designated healthcare team member woould constantly check for updates and update the patient headboard for patients that are under his/her charge.  Besides being time consuming, this process also carries the risk of healthcare workers working with outdated data.  The digitisation of this process would save time and create capacity for more quality bedside care.

# MOTIVATION

### Information that are relevant to bedside care should be available whenever the data is updated and be automatically available at the place that it is required.

# ENVISAGED SYSTEM

### In the envisaged system (see Figure 1), the current infrastructure would remain and a typical ward would be equipped with server which would contain a subset of the patient related data to supply to the various patient headboard displays.

- the need for a separate server - a separate server is required to store the information as they are pushed from the main system.  This results in a one way traffic which reduces the cybersecurity risk,

- the server would keep the information and allow the displays to poll for the relevant information. This allows for flexibility in the usage of the headboard displays to cater for patient movements e.g. change of bed, ward, discharge, admitted. 

![image](https://user-images.githubusercontent.com/4100494/118666290-a2d37580-b825-11eb-836b-5feb54da50b5.png)
{{< caption >}}Figure 1 : Envisaged System{{< /caption >}}

#  REQUIREMENTS OF PROTOTYPE

### The project team would like to demonstrate the input of data by various healthcare workers and their update at the respective patiet headboards.  As higher management support and futher consultation with the IT Departments of the respective hospitals would need to be done before any connecto the the LIVE system, this portion would need to be simulated.  A pictorial view of the requirements is as shown in Figure 2. 

![image](https://user-images.githubusercontent.com/4100494/118668519-89332d80-b827-11eb-861d-b51f7c4f315d.png)
{{< caption >}}Figure 2 : Requirements of Prototype{{< /caption >}}

# HARDWARE AND SOFTWARE DEVELOPMENT ENVIRONMENT

### Hareware

- A raspberry pi 4B was configured to perform the role of the server to receive updated patient information from the various healthcare workers and supply these information when pulled by the respective patient headboards.  As it operates on the Linux version of Debian Operating System, it could also be hardened against security threats.

- A tablet was used to simulate the LCD display.  It gets the patient information by subscribing to a website with the browser refresh rate set through auto refresh plug-in.

- The raspberry pi also performed the role of simulating the main system by provide simulated web pages for the healthcare workers to key in the patient information. 

### Software

The flask framework was used to develope the application.  The required software were encapsulated in a Python virtual environment (See Figure 3). 

![image](https://user-images.githubusercontent.com/4100494/118671405-052e7500-b82a-11eb-99ae-4b1c584690a6.png)
{{< caption >}}Figure 3 : Software Development Environment {{< /caption >}}

### Code
An overview of the code files used in the project is as shown in Figure 4.

![image](https://user-images.githubusercontent.com/4100494/118674818-acaca700-b82c-11eb-81f2-cd7c56118234.png)
{{< caption >}}Figure 4 : Overview of Code Files used in the project{{< /caption >}}

### Value of Project
With the prototype, the team was able to produce a video clip to seek the comments of healthcare teams from the various hospitals.  These feedback enriches the team's final report to seek management's approval for more extensive implementation.

### Sample Patient Headboard Display page

![image](https://user-images.githubusercontent.com/4100494/118689116-4417f700-b839-11eb-8593-82ab0dabd511.png)

{{< caption >}}Figure 5 : Overview of Code Files used in the project{{< /caption >}}


### Sample Simulated Page to capture Healthcare Workers' Input 

![image](https://user-images.githubusercontent.com/4100494/118688901-0e730e00-b839-11eb-884a-7c47e24692f5.png)
{{< caption >}}Figure 6 : Simulated Screen for Health care worker's input of critical patient information{{< /caption >}}

![image](https://user-images.githubusercontent.com/4100494/118689387-84777500-b839-11eb-9e1b-9c656c64e265.png)
{{< caption >}}Figure 7 : Screen for overview of records in database{{< /caption >}}

