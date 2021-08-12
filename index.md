---
title: Using CSC HPC Environment Efficiently
author: CSC Training
---

# Material for Using CSC HPC Environment Efficiently -course

{% assign items = site.hands-on |  sort: "title" | reverse %}

* The material is organized by topics in increasing complexity
    * Feel free to jump if you know the basics already
* In each topic read the slides / watch the video first
* Complete the tutorial to make sure you’ve got the steps right
* Try out the exercises to verify your new skill
* If you get stuck, consult [the docs](https://docs.csc.fi) linked to the topic slides
* Press `ctrl/cmd` to open links to a new window or tab
* Left-click on slides and you can then navigate them with arrow-keys

## 1. Prerequisites (Accounts, Connecting, Basics of CLI)
### 1.1 [Slides: Connecting to CSC Computers](https://a3s.fi/CSC_training/01_logging_in.html)
### 1.2 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'connecting' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% if hands-on.topic == 'Linux Prerequisites' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
1. [Advanced tutorial - Login Puhti with NoMachine](https://docs.csc.fi/support/tutorials/nomachine-usage/)
2. [Advanced tutorial - Run R studio/Jupyter Notebook on Puhti via ssh-tunnel and browser](https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/) This requires ssh-keys (see above) but is the recommended way to use these interactive tools.

## 2. Introduction to HPC environment
### 2.1 [Slides](https://a3s.fi/CSC_training/02_environment.html)
### 2.2 [Video: CSC Datacenter in Kajaani](https://www.youtube.com/watch?v=HeqN0h391wg)

## 3. Disk areas
### 3.1 [Slides](https://a3s.fi/CSC_training/03_disk_areas.html)
### 3.2 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'disk-areas' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 4. Module system
### 4.1 [Slides](https://a3s.fi/CSC_training/04_modules.html)
### 4.2 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'modules' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 5. Batch queue system and interactive use
### 5.1 [Slides](https://a3s.fi/CSC_training/05_batch_jobs.html)
### 5.2 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'Batch jobs' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
1. [Exercise - Serial, array and parallel jobs with R + contours calculation from DEM with raster package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/R/puhti)
1. [Exercise - Serial, array and parallel jobs with Python + NDVI calculation rasterio package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/python/puhti)

## 6. Batch job resource usage
### 6.1 [Slides](https://a3s.fi/CSC_training/06_understanding_usage.html)
### 6.2 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'batch resources' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 7. Allas and where to keep your data
### 7.1 [Slides](https://a3s.fi/CSC_training/07_allas.html)
### 7.2 [Video: Using Allas](https://a3s.fi/CSC_training/Allas-video.mp4)
### 7.3 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'allas' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 8. Installing your own software
### 8.1 [Slides](https://a3s.fi/CSC_training/08_installing.html)
### 8.2 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'installing' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 9. Containers and Singularity
### 9.1 [Slides](https://a3s.fi/CSC_training/09_singularity.html)
### 9.2 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'singularity' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 10. How to speed up jobs
### 10.1 [Slides](https://a3s.fi/CSC_training/10_speed_up_jobs.html)
### 10.2 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'throughput' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## Information
<p></p>

<p>
  <div style="float: left; width: 50%;">
   <img src="./slides/img/EuroCC_Logo_invert.png" width=110 align=middle/>
   <p><small>
     This project has received funding from the European High-Performance Computing Joint Undertaking (JU) under grant agreement No 951732.
      </small>
    </p>
  </div>
  <div style="float: right; width: 50%;">
    <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" width=200>
    <p><small>
  All material (C) 2020-2021 by CSC -IT Center for Science Ltd. and the authors. <br />
  This work is licensed under a <strong>Creative Commons Attribution-NonCommercial-ShareAlike</strong> 3.0 <br />
  Unported License, <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/">http://creativecommons.org/licenses/by-nc-sa/3.0/</a>
      </small>
    </p>
  </div>
</p>
<p>&nbsp;</p>
   
