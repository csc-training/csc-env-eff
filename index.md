---
title: CSC Computing Environment
author: CSC Training
---

# Material for _CSC Computing Environment_ -course

{% assign items = site.hands-on |  sort: "title" | reverse %}

<blockquote style="color: #0f0f0f; border: 2px solid #002f5f; padding: 10px; background-color: #d0dced;">
<ul>
<li>The material is organized by topics in increasing complexity<ul>
<li>Feel free to jump if you know the basics already</li>
</ul>
</li>
<li>In each topic read the slides / watch the video first</li>
<li>Complete tutorial(s) to make sure you’ve got the steps right</li>
<li>Try out the exercises to verify your new skill</li>
<li>If you get stuck, consult <a href="https://docs.csc.fi">Docs CSC</a> linked in the slides and the tutorials</li>
<li>If the documentation does not provide sufficient answer, please contact support by email <a href="mailto:servicedesk@csc.fi">servicedesk@csc.fi</a> or by submitting (a question and feedback form) <a href="https://research.csc.fi/support">https://research.csc.fi/support</a></li>
<li>Press <code>ctrl/cmd</code> with click to open links to a new window or tab</li>
<li>Left-click on slides and you can then navigate them with arrow-keys<ul>
<li>Use the browser back-button or external link to return to main menu</li>
</ul>
</li>
<li><a href="https://video.csc.fi/media/t/0_d7trmsru">A video about study tips</a></li>
</ul>
</blockquote>

## 1. Prerequisites (Accounts, Connecting, Basics of CLI)
### 1.1 [Slides: Accounts and Projects](https://a3s.fi/CSC_training/00_account_and_project.html)
### 1.2 [Video: Accounts and Projects](https://video.csc.fi/media/t/0_j5ezfw80)
### 1.3 [Slides: Connecting to CSC Computers](https://a3s.fi/CSC_training/01_logging_in.html)
### 1.4 [Video: Connecting to CSC Computers](https://video.csc.fi/media/t/0_8fdqjuf9)
### 1.5 [Video tutorial: Connecting to Puhti](https://video.csc.fi/media/t/0_d0i4dk2j)
### 1.6 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'connecting' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% if hands-on.topic == 'Linux Prerequisites' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
2. [Advanced tutorial - Run R studio/Jupyter Notebook on Puhti via ssh-tunnel and browser](https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/) This requires ssh-keys (see above) but is the recommended way to use these interactive tools.

## 2. Introduction to HPC environment
### 2.1 [Slides](https://a3s.fi/CSC_training/02_environment.html)
### 2.2 [Video: HPC Environment](https://video.csc.fi/media/t/0_u1tvtzga)
### 2.3 [Video: CSC Datacenter in Kajaani](https://www.youtube.com/watch?v=HeqN0h391wg)

## 3. Disk areas
### 3.1 [Slides](https://a3s.fi/CSC_training/03_disk_areas.html)
### 3.2 [Video: Disk Areas](https://video.csc.fi/media/t/0_99zrt6or)
### 3.3 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'disk-areas' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 4. Module system
### 4.1 [Slides](https://a3s.fi/CSC_training/04_modules.html)
### 4.2 [Video: Modules and preinstalled software](https://video.csc.fi/media/t/0_y57f260c)
### 4.5 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'modules' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 5. Batch queue system and interactive use
### 5.1 [Slides](https://a3s.fi/CSC_training/05_batch_jobs.html)
### 5.2 [Video: Batch jobs](https://video.csc.fi/media/t/0_fagcet5x)
### 5.3 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'Batch jobs' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}
1. [Exercise - Serial, array and parallel jobs with R + contours calculation from DEM with raster package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/R/puhti)
1. [Exercise - Serial, array and parallel jobs with Python + NDVI calculation rasterio package (GIS) ](https://github.com/csc-training/geocomputing/tree/master/python/puhti)

## 6. Batch job resource usage
### 6.1 [Slides](https://a3s.fi/CSC_training/06_understanding_usage.html)
### 6.2 [Video: Resources usage](https://video.csc.fi/media/t/0_bfbgk9zf)
### 6.3 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'batch resources' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 7. Allas and where to keep your data
### 7.1 [Slides](https://a3s.fi/CSC_training/07_allas.html)
### 7.2 [Video: Allas Object Storage](https://video.csc.fi/media/t/0_fvn4jbh1)
### 7.3 [Video: Using Allas](https://video.csc.fi/media/t/0_q04hc35j)
### 7.4 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'allas' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 8. Installing your own software
### 8.1 [Slides](https://a3s.fi/CSC_training/08_installing.html)
### 8.2 [Video: Installing own software](https://video.csc.fi/media/t/0_anzwy1es)
### 8.3 Tutorials and exercises
{% for hands-on in items %}
{% if hands-on.topic == 'installing' %}
1. [{{ hands-on.title }}]({{ hands-on.url | relative_url }})
{% endif %}
{% endfor %}

## 9. Containers and Singularity
### 9.1 [Slides](https://a3s.fi/CSC_training/09_singularity.html)
### 9.2 [Video: Containers](https://video.csc.fi/media/t/0_0ws9ei53)
### 9.3 Tutorials and exercises
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
    <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png" width=180>
    <p><small>
  All material (C) 2020-2021 by CSC -IT Center for Science Ltd.  <br />
  This work is licensed under a <strong>Creative Commons Attribution-ShareAlike</strong> 3.0 <br />
  Unported License, <a href="http://creativecommons.org/licenses/by-sa/4.0/">http://creativecommons.org/licenses/by-sa/4.0/</a>
      </small>
    </p>
  </div>
</p>
<p>&nbsp;</p>
   
