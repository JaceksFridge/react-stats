

## react-stats

<code>react-stats</code> is a Python package offering a collection of utilities for React.js developers. With just three commands, manage your assets and get statistics on your codebase.

### 🪄 How to Install


install: 
```
pip install react-stats
```


to update:
```
pip install react-stats --upgrade
```



### 😁 What you can do

<code>* fun statistics about your project</code>

<code>* instant asset structure</code>

<code>* automatic asset manager </code>


### ⌨ 1 of 3 Get-Stats


You'll get a stats.txt file with statstics about your project such as:

* language usage chart
* file overview table
* hook overview table


run command:
```
get-stats
```

language usage:
```
Python   | 83.47% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░
Markdown |  8.67% ▓▓░░░░░░░░░░░░░░░░░░
Text     |  7.86% ▓▓░░░░░░░░░░░░░░░░░░
                                  100%
```

file usage:
```
====================  =======  ==========
files                   lines  language
====================  =======  ==========
get_stats.py              167  Python
auto_assets.py             43  Python
make_assets.py             42  Python
README.md                  37  Markdown
setup.py                   27  Python
exts.py                    20  Python
SOURCES.txt                17  Text
ahoy.py                    10  Python
printr.py                   8  Python
entry_points.txt            6  Text
requires.txt                5  Text
top_level.txt               1  Text
__init__.py                 0  Python
dependency_links.txt        0  Text
====================  =======  ==========
```

hook usage:
```
 file               |   all hooks |   useState |   useEffect |   useContext |   otherHooks |   customHooks
--------------------+-------------+------------+-------------+--------------+--------------+---------------
 Home.js            |          10 |          6 |           0 |            2 |            0 |             2
 Forms.js           |           5 |          2 |           0 |            1 |            0 |             2
 Register.js        |           4 |          3 |           0 |            1 |            0 |             0
 Login.js           |           4 |          3 |           0 |            1 |            0 |             0
 useLocalStorage.js |           2 |          1 |           0 |            0 |            0 |             1
 FormSlider.js      |           2 |          1 |           0 |            0 |            0 |             1
 NodoForm.js        |           1 |          0 |           0 |            0 |            0 |             1
 FormChecks.js      |           1 |          0 |           0 |            0 |            0 |             1
 useCurrentDate.js  |           1 |          1 |           0 |            0 |            0 |             0
 userContext.js     |           1 |          1 |           0 |            0 |            0 |             0
 HappinessForm.js   |           1 |          0 |           0 |            0 |            0 |             1
 WealthForm.js      |           1 |          0 |           0 |            0 |            0 |             1
 HealthForm.js      |           1 |          0 |           0 |            0 |            0 |             1
 FormCounters.js    |           1 |          0 |           0 |            0 |            0 |             1
 IntroPage.js       |           1 |          0 |           0 |            0 |            0 |             1
 Scores.js          |           1 |          1 |           0 |            0 |            0 |             0
 LogReg2.js         |           1 |          1 |           0 |            0 |            0 |             0
```

### ⌨ 2 of 3 Make-Assets

Run the following command to get a asset folder structure specified for dealing with assets.

command:

```
make-assets
```

folder structure:


```
├── assets
│   ├── audio
│   ├── data
│   ├── docs
│   ├── fonts
│   ├── icons
│   ├── images
│   └── video
```



### ⌨ 3 of 3 Auto-Assets

For automatically organizing your assets including docs, images, videos, data...

run command:
```
auto-assets
```

Now, when you create a file in the root directory it will be automatically moved to the correct
subfolder in the assets folder.

If you haven't run <code>make-assets</code>, than a subfolder will still be automatically created. 

This command will keep running in the background. You can stop it anytime with `Ctrl+C`.



### Contributing

If you encounter any issues or have suggestions for improvements, please open an issue or a pull request.


### License

This project is licensed under the MIT License.
