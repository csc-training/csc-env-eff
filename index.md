---
title: Using CSC HPC Environment Efficiently
author: CSC Training
---

# Hands-on

{% assign items = site.hands-on |  sort: "title" | reverse %}

## 1. Prerequirements (accounts and projects, Linux 101)
* [Tutorial - Login Puhti with ssh](hands-on/connecting/ssh-puhti.html)
{% for hands-on in items %}
{% if hands-on.topic == 'Linux Prerequisites' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 2. Connecting
{% for hands-on in items %}
{% if hands-on.topic == 'connecting' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
* [Advanced tutorial - Run R studio/Jupyter Notebook on Puhti via ssh-tunnel and browser](https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/) This requires ssh-keys (see above) but is the recommended way to use these interactive tools.

## 3. Disk areas
{% for hands-on in items %}
{% if hands-on.topic == 'disk-areas' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 4. Modules
{% for hands-on in items %}
{% if hands-on.topic == 'modules' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 5. Batch Jobs
{% for hands-on in items %}
{% if hands-on.topic == 'Batch jobs' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
* [Exercise - Serial, array and parallel jobs with R + contours calculation from DEM with raster package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/R/puhti)
* [Exercise - Serial, array and parallel jobs with Python + NDVI calculation rasterio package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/python/puhti)

## 6. Batch job resource usage
{% for hands-on in items %}
{% if hands-on.topic == 'batch resources' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 7. Allas
{% for hands-on in items %}
{% if hands-on.topic == 'allas' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 8. Installing your own software
{% for hands-on in items %}
{% if hands-on.topic == 'installing' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 9. Containers (Singularity)
{% for hands-on in items %}
{% if hands-on.topic == 'singularity' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## Throughput
{% for hands-on in items %}
{% if hands-on.topic == 'throughput' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}



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
<br>
<br>
