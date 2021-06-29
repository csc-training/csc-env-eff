---
title: Using CSC HPC Environment Efficiently
author: CSC Training
---

# Material for Using CSC HPC Environment Efficiently -course

{% assign items = site.hands-on |  sort: "title" | reverse %}

## 1. Prerequisites (Accounts, Connecting, Basics of CLI)
### 1.1 [Slides: Connecting to CSC Computers](https://a3s.fi/CSC_training/02_logging_in.html)
### 1.2 Hands-on and tutorials
{% for hands-on in items %}
{% if hands-on.topic == 'connecting' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% if hands-on.topic == 'Linux Prerequisites' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
1. [Login Puhti with NoMachine](https://docs.csc.fi/support/tutorials/nomachine-usage/) (Advanced)
2. [Advanced tutorial - Run R studio/Jupyter Notebook on Puhti via ssh-tunnel and browser](https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/) This requires ssh-keys (see above) but is the recommended way to use these interactive tools.

## 2. Introduction to HPC environment
### 2.1 [Slides](https://a3s.fi/CSC_training/01_environment.html)
### 2.2 [Video: CSC Datacenter in Kajaani](https://www.youtube.com/watch?v=HeqN0h391wg)

## 3. Disk areas
{% for hands-on in items %}
{% if hands-on.topic == 'disk-areas' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 4. Modules
{% for hands-on in items %}
{% if hands-on.topic == 'modules' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 5. Batch Jobs
{% for hands-on in items %}
{% if hands-on.topic == 'Batch jobs' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
1. [Exercise - Serial, array and parallel jobs with R + contours calculation from DEM with raster package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/R/puhti)
1. [Exercise - Serial, array and parallel jobs with Python + NDVI calculation rasterio package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/python/puhti)

## 6. Batch job resource usage
{% for hands-on in items %}
{% if hands-on.topic == 'batch resources' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 7. Allas
{% for hands-on in items %}
{% if hands-on.topic == 'allas' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 8. Installing your own software
{% for hands-on in items %}
{% if hands-on.topic == 'installing' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 9. Containers (Singularity)
{% for hands-on in items %}
{% if hands-on.topic == 'singularity' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## Throughput
{% for hands-on in items %}
{% if hands-on.topic == 'throughput' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
<p>

<div style="float: left; width: 50%;">
<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" />
</div>
<div style="float: right; width: 50%;">
<p><small>
  All material (C) 2020-2021 by CSC -IT Center for Science Ltd. and the authors. <br>
  This work is licensed under a <strong>Creative Commons Attribution-NonCommercial-ShareAlike</strong> 3.0 <br>
  Unported License, <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/">http://creativecommons.org/licenses/by-nc-sa/3.0/</a>
 </small></p>
</div>
<p>
