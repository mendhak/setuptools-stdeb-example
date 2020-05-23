
## Notes


Create a build using:  

```
rm -rf deb_dist dist *.tar.gz *.egg* build tmp
python3 setup.py --command-packages=stdeb.command bdist_deb
```

A .deb is produced inside ./deb_dist

Examine it using 

```
lintian example-pkg_0.0.2-1_all.deb
dpkg -I example-pkg_0.0.2-1_all.deb
```


Install it using

```
sudo apt install ./example-pkg_0.0.2-1_all.deb
```

Run the 'command' using

```
example_pkg
```

Uninstall it using

```
sudo apt purge example-pkg
```

