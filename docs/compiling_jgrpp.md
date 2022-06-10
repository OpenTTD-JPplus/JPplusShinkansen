# **Compiling JGRPP**
  
**Note: this seems to be broken now**


## First Time Compile Commands
```
sudo apt install build-essential cmake git
sudo apt build-dep openttd
```
  ## Commands
  ```
  git clone https://github.com/JGRennison/OpenTTD-patches.git Applications/jgrpp-latest
  ```
Then
  ```
  cd Applications/jgrpp-latest
  git checkout jgrpp-x.xx.x
  mkdir build
  cd build
  cmake ..
  make
  ./openttd
  ```
## Notes
* I compile in a folder called **'Applications'** and put the latest version into a subfolder called **'jgrpp-latest'**
* If downloading a new version, rename the current jgrpp-latest folder to the version number (or delete it)
* Replace x.xx.x in git checkout jgrpp-x.xx.x above with the latest version on GitHub
  