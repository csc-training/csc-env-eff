---
topic: installing
title: Tutorial - Installing Java applictions
---

# Installing Java applications

Java applications do not typically require special installation. You just need
to download the distribution package.

If you get an error message about java version, try loading a suitable java 
module. You can check the available modules with command:
```text
module spider java
```
Despite their name, modules named `biojava` are just normal java installations,
and can be used with any software, not just bio applications.

Some java applications fail to run on the login nodes. Try running them using
`sinteractive` instead. 

Naturally no compute heavy tasks should be run on the login nodes.