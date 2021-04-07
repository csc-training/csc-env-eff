---
title: Using CSC HPC Environment Efficiently
author: CSC Training
---

# Hands-on

{% assign items = site.hands-on |  sort: "title" | reverse %}

## Prerequirements
* [Tutorial - Login Puhti with ssh](hands-on/connecting/ssh-puhti.html)
{% for hands-on in items %}
{% if hands-on.topic == 'Linux Prerequisites' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## Connecting
{% for hands-on in items %}
{% if hands-on.topic == 'connecting' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## Disk-areas
{% for hands-on in items %}
{% if hands-on.topic == 'disk-areas' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## Modules
{% for hands-on in items %}
{% if hands-on.topic == 'modules' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## Batch Jobs
{% for hands-on in items %}
{% if hands-on.topic == 'Batch jobs' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
* [Exercise - Serial, array and parallel jobs with R + contours calculation from DEM with raster package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/R/puhti)
* [Exercise - Serial, array and parallel jobs with Python + NDVI calculation rasterio package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/python/puhti)

## Batch job resource usage
{% for hands-on in items %}
{% if hands-on.topic == 'batch resources' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## Allas
{% for hands-on in items %}
{% if hands-on.topic == 'allas' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}


## Singularity
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

## Installing
{% for hands-on in items %}
{% if hands-on.topic == 'installing' %}
- [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
