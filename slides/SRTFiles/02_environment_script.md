---
theme: csc-2019
lang: en
---

# Brief introduction to HPC environments {.title}

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All material (C) 2020-2021 by CSC -IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

:::info (speech)
This lecture is about High Performance Computing environments
:::

# Notes on vocabulary

<div class="column">
Roughly you can think of

- computer ~= node
- processor ~= socket
- core~= CPU
</div>
<div class="column">
![](./img/node.svg){width=60%} 
</div>

:::info (speech)
We assume that a laptop computer is a familiar thing to you, so this comparison shows how the components of a laptop, and a supercomputer roughly relate to each other. 
So your laptop would be something similar to a one node in a cluster. 
A cluster is a collection of nodes, that are linked together with fast connections.
That collection of nodes is what makes a supercomputer so super – in terms of computing power.
Your laptop has a processor, and the equivalent of that in a supercomputer is called a socket. 
A socket or a processor has CPU's or cores.
Terms CPU and core are used interchangeably. 
Very often it's just "core". 
Sometimes it's "CPU core" and so on. 
Simply put you can think a supercomputer as a set of computers, that are connected together. 
Each of the nodes have their own memory.
Some nodes have also local storage, which is useful in certain workflows. 
:::

# Cluster systems

<div class="column">
- Login nodes are used to set up jobs (and to launch them)
- Jobs are run in the compute nodes
- A batch job system (aka scheduler) is used to run and manage the jobs
  - On CSC machines we use Slurm
  - Other common systems include SGE and Torque/PBS
  - Syntax is different, but basic operation is similar
</div>
<div class="column">
![](./img/cluster.svg){width=80%} 
</div>

:::info (speech)
Typically a computing cluster contains a storage system, login nodes and compute nodes. 
The supercomputer uses the login nodes for connecting with the outside world.
They are like fat laptops, that enable users for example to browse their files in the supercomputer.
Running heavy computations on login nodes is against the CSC usage policy.
Then there is a central storage system, where users can have their codes and relevant files.
The essence of the supercomputer are of course the compute nodes.
You are not supposed to log in in those, but they are dedicated for actually running the jobs, and doing the heavy computing.
Accessing the compute nodes is done through a batch job system.
On CSC machines we use batch job scheduler called Slurm. 
There are other schedulers for example SGE, Torque or PBS, and they all do the same function. 
The syntax between those is a little bit different
If you copy-paste a batch script from the internet, you have to adapt it to the supercomputer that you are using.
Also a different Slurm cluster may use a little bit different syntax than ours. 
:::

# Available HPC resources

- [Puhti](https://docs.csc.fi/computing/systems-puhti/) is the general purpose supercomputer ☑️
- [Mahti](https://docs.csc.fi/computing/systems-mahti/) is the massively parallel flagship supercomputer
- [Pouta](https://docs.csc.fi/cloud/pouta/pouta-what-is/) provides cloud resources via OpenStack (Iaas)
- [Rahti](https://docs.csc.fi/cloud/rahti/rahti-what-is/) provides containers via okd (Paas)
- [Allas](https://docs.csc.fi/data/Allas/) provides object storage for all services

:::info (speech)
CSC provides these HPC resources for customers. 
Try the links in the slides to open corresponding documentation. 
Puhti is the general purpose supercomputer.
It has the most pre-installed applications, and it can run both serial and parallel jobs. 
Mahti is a massively parallel supercomputer. 
Then Lumi will have even more resources for parallel computation. 
Pouta is a cloud resource infrastructure-as-a-service.
There you set up and operate virtual machines, so you can have a root access for your system. 
Rahti is a little bit similar system, but everything you run there should be deployed as containers.
Allas is for storing data. 
It is managed by CSC, and designed for large amounts of data. 
One of the reasons for using HPC is that you may have so much data, that you cannot keep it in your own laptop.
:::

# Which supercomputer to use? 

- What kind of recources can _your application_ use?
  - Can it use more than one core?
  - How much memory it will need?
  - Can it use GPU or NVMe?
  - What takes long (is the time limiting part) in your job?
- See what kind of resources are _available_
  - Is my code already installed?
  - Max. runtime, partitions (queues), provisioning policy (Per core/per node/other)
  - Each system is different, so check the documentation

:::info (speech)
This is really an open-ended question, and the answer depends on your needs.
You should figure out what kind of resources your application can use. 
Some software can use only one core, which makes them serial programs. 
They should run in Puhti.
Parallel programs can use more than one core, which is what Mahti and Lumi are designed for. 
Other factors to consider are the memory requirement, and if the application can benefit from GPU's, or fast local disk. 
Every job has a limiting stage in the workflow.
Identifying which it is may give insight to choosing a suitable supercomputer.
We recommend you to find out answers to these questions by investigating your application. 
Then you should check, which resources are available in the different supercomputers. 
If the code that you want to use is already installed, then probably there are also instructions on usage. 
Then you can get started immediately with running the code, rather than installing and learning how it works. 
Different machines, or different partitions, have different maximum run times, or provisioning policies.
Some let you apply for a single core or full nodes and so on.
We recommend always to check the documentation. 
Feel free to contact us, if the documentation does not provide you with answers. 
:::

# Quick and dirty comparison of Puhti and Mahti

|                             | Puhti  | Mahti    |
| --------------------------- |------- | ----     | 
| Number of preinstalled applications   | [123+](https://docs.csc.fi/apps/by_system/#puhti)   | [16+](https://docs.csc.fi/apps/by_system/#mahti)       | 
| Cores per node              | 40     | 128       |
| Job size (min-max) cores    | 1-1040 | 128-25600 |
| Memory per node (GiB)       | 192-1536 | 256     |
| GPU cards (NVIDIA)          | 120 x V100 | 96 x A100|
| Fast node local disk (NVMe) | 120   | (24 GPU nodes)  |

In short: Mahti is for much larger parallel jobs, prepare to install and optimize your code.
(Still, a Puhti *node* is > 10x your laptop.)

:::info (speech)
Together Puhti and Mahti provide users with extensive HPC resources. 
This comparison gives a quick overview, that helps to decide which one to use.
Puhti is more general use supercomputer, and it also has a lot more applications preinstalled than Mahti.
The links in the slides take you to the lists of the installed applications. 
Of course, you can also install your own applications if you want. 
The sizes of the nodes are quite different.
In Puhti the each node has 40 cores – or CPU's – and in Mahti it has 128. 
The job size - so how many CPU cores one job can use - starts from one in Puhti.
That means you can run both serial or parallel jobs there. 
In Mahti the resources are allocated by nodes, so the minimum number of requested cores is one full node. 
That means your job should be able to use at least 128 cores in parallel.
This is what Mahti is really meant for - to run these massively parallel jobs. 
If your job needs a lot of memory, then we have these huge memory nodes in Puhti. 
Certain kind of applications will run a lot faster with a lot of memory. 
In Mahti, there's a lot less memory per core available, but that is enough for most applications. 
In comparison your laptop has propably 8 or 16 gigs of RAM.
Both machines have Nvidia GPU cards. 
These are extremely good for a certain machine learning jobs. 
Later we will cover whether it makes sense to use GPUs, or should you use CPUs instead. 
In Puhti we have 120 nodes with fast local disk, and in Mahti only the GPU nodes have this local disk. 
To summarize: Puhti is a general purpose supercomputer.
One node in Puhti is around 10 times faster than your laptop, and there are many of those nodes.
Mahti is for large parallel jobs. 
But if you want to use that, then be prepared to install and optimize your code. 
:::
