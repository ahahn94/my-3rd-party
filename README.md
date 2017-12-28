# About
This Repo offers some packages that did not make it into the 3rd party repo of Solus.  
As with the normal 3rd party repo, packages need to be build on your system.

# Install Instructions:  
## GoLand  
```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ahahn94/my-3rd-party/master/programming/goland/pspec.xml
sudo eopkg it goland*.eopkg;sudo rm goland*.eopkg
```

## Modelio  
```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ahahn94/my-3rd-party/master/programming/modelio/pspec.xml
sudo eopkg it modelio*.eopkg;sudo rm modelio*.eopkg
```

## Synology Cloud Station Backup  
```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ahahn94/my-3rd-party/master/network/download/synology-cloud-station-backup/pspec.xml
sudo eopkg it synology-cloud-station-backup*.eopkg;sudo rm synology-cloud-station-backup*.eopkg
```
