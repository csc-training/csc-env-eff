---
theme: csc-2019
lang: en
---

# Font size and weight

- Lorem ipsum dolor sit amet, *consectetuer* adipiscing elit. Sed posuere
  ***interdum sem***.
- Quisque ligula eros ullamcorper quis,
  <small>lacinia quis ***facilisis*** sed sapien</small>.
- **Mauris varius** diam vitae arcu.


# Math formulas

- Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere
  interdum sem.
- Quisque ligula eros ullamcorper quis ($e = mc^2$), lacinia quis facilisis
  sed sapien.
- Mauris varius diam vitae arcu:
  $\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 v$
    - Sed arcu lectus auctor vitae, consectetuer et venenatis eget velit.

$$\oint_{\partial \Sigma} E \cdot dl
    = - \int_\Sigma \frac{\partial B}{\partial t} \cdot d A$$


# Nesting lists 1

- Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere
  interdum sem.
    - Quisque ligula eros ullamcorper quis, lacinia quis facilisis sed sapien.
      Mauris varius diam vitae arcu.
    - Sed arcu lectus auctor vitae, consectetuer et venenatis eget velit.
        - sed augue orci
        - lacinia eu tincidunt et eleifend nec lacus
- Donec ultricies nisl ut felis, suspendisse potenti.
    - Lorem ipsum ligula ut hendrerit mollis, ipsum erat vehicula risus, eu
      suscipit sem libero nec erat.


# Nesting lists 2

1. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere
   interdum sem.
    - Quisque ligula eros ullamcorper quis, lacinia quis facilisis sed sapien.
      Mauris varius diam vitae arcu.
    - Sed arcu lectus auctor vitae, consectetuer et venenatis eget velit.
        - sed augue orci
        - lacinia eu tincidunt et eleifend nec lacus
2. Donec ultricies nisl ut felis, suspendisse potenti.
    - Lorem ipsum ligula ut hendrerit mollis, ipsum erat vehicula risus, eu
      suscipit sem libero nec erat.


# Nesting lists 3

1. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere
   interdum sem.
    - Quisque ligula eros ullamcorper quis, lacinia quis facilisis sed sapien.
      Mauris varius diam vitae arcu.
    - Sed arcu lectus auctor vitae, consectetuer et venenatis eget velit.
        1. sed augue orci
        2. lacinia eu tincidunt et eleifend nec lacus
2. Donec ultricies nisl ut felis, suspendisse potenti.
    - Lorem ipsum ligula ut hendrerit mollis, ipsum erat vehicula risus, eu
      suscipit sem libero nec erat.


# Nesting lists 4

- Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere
  interdum sem.
    1. Quisque ligula eros ullamcorper quis, lacinia quis facilisis sed sapien.
       Mauris varius diam vitae arcu.
    2. Sed arcu lectus auctor vitae, consectetuer et venenatis eget velit.
        * sed augue orci
        * lacinia eu tincidunt et eleifend nec lacus
- Donec ultricies nisl ut felis, suspendisse potenti.
    - Lorem ipsum ligula ut hendrerit mollis, ipsum erat vehicula risus, eu
      suscipit sem libero nec erat.


# Nesting lists 5

- Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere
  interdum sem.
    1. Quisque ligula eros ullamcorper quis, lacinia quis facilisis sed sapien.
       Mauris varius diam vitae arcu.
    2. Sed arcu lectus auctor vitae, consectetuer et venenatis eget velit.
        1. sed augue orci
        2. lacinia eu tincidunt et eleifend nec lacus
- Donec ultricies nisl ut felis, suspendisse potenti.
    - Lorem ipsum ligula ut hendrerit mollis, ipsum erat vehicula risus, eu
      suscipit sem libero nec erat.


# Definition list

Lorem
  : ipsum dolor sit amet

Consectetuer adipiscing elit
  : Sed posuere interdum sem.
  : Quisque ligula eros ullamcorper quis, lacinia quis facilisis sed sapien.

Mauris
  : varius diam vitae arcu

    Sed arcu lectus auctor vitae, consectetuer et venenatis eget velit.


# Function definition

`Lorem(ipsum, dolor, sit, amet)`
  : `ipsum`{.input}
    : consectetuer adipiscing elit

    `dolor`{.input}
    : sed posuere interdum sem

    `sit`{.input}
    : quisque ligula eros

    `amet`{.output}
    : ullamcorper quis


# Images 1

!["Some water"](img/10km.jpg "10000 water molecules")

Remember to add both title AND alt-text for screen reader
and accessibility!

# Images 2

!["Some water"](img/10km.jpg "10000 water molecules"){width=30%}

Remember to add both title AND alt-text for screen reader
and accessibility!


# Columns 1

<div class="column">
- Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere
  interdum sem.
    - quisque ligula eros ullamcorper quis
    - lacinia quis facilisis sed sapien
- Mauris varius diam vitae arcu.
</div>

<div class="column">
- Sed arcu lectus auctor vitae, consectetuer et venenatis eget velit.
- Sed augue orci, lacinia eu tincidunt et eleifend nec lacus.
</div>


# Columns 2

<div class="column">
- Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere
  interdum sem.
    - quisque ligula eros ullamcorper quis
    - lacinia quis facilisis sed sapien
- Mauris varius diam vitae arcu.
</div>

<div class="column">
![Water](img/10km.jpg "10000 water molecules"){width=50%}
</div>


# Code high-lighting

```python
import os

if os.path.isfile('foobar'):
    with open('foobar') as fp:
        txt = fp.read()
    print('File contents:')
    print(txt)
```

```c
#include <stdio.h>

int square(x) {
    printf("Going to square value %d.", x);
    return x*x;
}
```

Lorem ipsum dolor sit amet, consectetuer adipiscing elit: ```count = x + y```.
Sed posuere interdum ```foobar(args, x)``` sem.

# Code high-lighting with emphasis

```{.python emphasize=1:8-1:10,3-3}
import os

if os.path.isfile('foobar'):
    with open('foobar') as fp:
        txt = fp.read()
    print('File contents:')
    print(txt)
```

- emphasize syntax:
  `line1[:col1]-line2[:col2],line3[:col3]-line4[:col4]`
- Note: syntax highlighting does not work with emphasize


# Tables 1 (default)

|            |             | 1     | 2     | 4     | 8     |
| ---------- | ----------- | ----: | ----: | ----: | ----: |
| **Case 1** | vanilla     | 0.757 | 0.719 | 0.574 | 0.547 |
|            | *optimised* | 0.899 | 0.838 | 0.658 | 0.607 |
| **Case 2** | vanilla     | 1.252 | 1.111 | 0.684 | 0.756 |
|            | *optimised* | 1.443 | 1.277 | 0.748 | 0.818 |

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere interdum
sem.


# Tables 2 (default + highlighted cells)

|            |             | 1     | 2           | 4           | 8     |
| ---------- | ----------- | ----: | ----------: | ----------: | ----: |
| **Case 1** | vanilla     | 0.757 | 0.719       | 0.574       | 0.547 |
|            | *optimised* | 0.899 | 0.838       | 0.658       | 0.607 |
| **Case 2** | vanilla     | 1.252 | ***1.111*** | 0.684       | 0.756 |
|            | *optimised* | 1.443 | 1.277       | ***0.748*** | 0.818 |

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere interdum
sem.


# Tables 3 (colour) {.table-colour}

|            |             | 1     | 2           | 4           | 8     |
| ---------- | ----------- | ----: | ----------: | ----------: | ----: |
| **Case 1** | vanilla     | 0.757 | 0.719       | 0.574       | 0.547 |
|            | *optimised* | 0.899 | 0.838       | 0.658       | 0.607 |
| **Case 2** | vanilla     | 1.252 | ***1.111*** | 0.684       | 0.756 |
|            | *optimised* | 1.443 | 1.277       | ***0.748*** | 0.818 |

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere interdum
sem.


# Tables 4 (grid) {.table-grid}

|            |             | 1     | 2           | 4           | 8     |
| ---------- | ----------- | ----: | ----------: | ----------: | ----: |
| **Case 1** | vanilla     | 0.757 | 0.719       | 0.574       | 0.547 |
|            | *optimised* | 0.899 | 0.838       | 0.658       | 0.607 |
| **Case 2** | vanilla     | 1.252 | ***1.111*** | 0.684       | 0.756 |
|            | *optimised* | 1.443 | 1.277       | ***0.748*** | 0.818 |

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere interdum
sem.


# Tables 5 (none) {.table-none}

|            |             | 1     | 2           | 4           | 8     |
| ---------- | ----------- | ----: | ----------: | ----------: | ----: |
| **Case 1** | vanilla     | 0.757 | 0.719       | 0.574       | 0.547 |
|            | *optimised* | 0.899 | 0.838       | 0.658       | 0.607 |
| **Case 2** | vanilla     | 1.252 | ***1.111*** | 0.684       | 0.756 |
|            | *optimised* | 1.443 | 1.277       | ***0.748*** | 0.818 |

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere interdum
sem.


# Section title 1 {.section}

Lorem ipsum dolor sit amet, consectetuer adipiscing elit.


# Section title 2 {.section}


# Section title 3: Lorem ipsum dolor sit amet, consectetuer adipiscing elit. {.section}


# Section title 4: Lorem ipsum dolor sit amet, consectetuer adipiscing elit. {.section}

Sed posuere interdum sem.

