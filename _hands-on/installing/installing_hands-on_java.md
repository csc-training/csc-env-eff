---
topic: installing
title: Tutorial - Installing Java applictions
---

# Installing Java applications

💬 Java applications do not typically require special installation. 
- You just need to download the distribution package, typically a .jar file.

💡 Compute nodes do not have default java installation, so you need to load a suitable java module. 
- You can check the available modules with command:
```bash
module spider java
```

💬 Despite their name, modules named `biojava` are just normal java installations, and can be used with any software, not just bio applications.

☝🏻 Some java applications fail to run on the login nodes. Try running them using `sinteractive` instead. 

‼️ Naturally no compute heavy tasks should be run on the login nodes.

## Example: Installing ABRA2

💬 In this example we install and run java application ABRA2.

1. Download the software
```bash
wget https://github.com/mozack/abra2/releases/download/v2.23/abra2-2.23.jar
```
2. Load java module
```bash
module load biojava
```
 💡 If you get error messages or warnings about java version, try loading another java module.

 3. Run the application
 ```bash
 java -jar abra2-2.23.jar
 ```
 If you are not in the same directory as the .jar file, you need to include the path to the file, e.g.
  ```bash
 java -jar /projappl/project_12345/abra2/abra2-2.23.jar
 ```

 ## Example 2: Java application with shell wrapper script

 💬 Some java applications come with shell scripts that are used to launch them instead of calling java directly. You should see the documentation for each softaware for details.

 One example of such application:
  ```bash
 module load beast
 beast --help
 ```
 ☝🏻 BEAST will fail to run on the login nodes. Try running it using `sinteractive` instead.