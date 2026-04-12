# Preparations  for bot deployment

## purpose of this program
* program measures Internet connection speed of your Internet Service Provider
* and make tweet on Twitter when your connection speed isn't satisfying terms of contract which you signed

### on Windows OS
* install chrome browser (minimal version 147.0)
* create new folder, steps: 1) w+r,2) cmd + Enter, 3) `mkdir c:\profiles\twitter`
* start chrome using this command from cmd `"C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir="C:\profiles\twitter"`
* warm up your new profile few days or use old warmed before profile you don't use anymore
* it's recommended to use `import undetected_chromedriver as uc` instead of ordinary chromedriver
* `C:\Users\BadUser\AppData\Roaming\undetected_chromedriver` remove this binary files if this error occurred `SessionNotCreatedException` (https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/#sessionnotcreatedexception)