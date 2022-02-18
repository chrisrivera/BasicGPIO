# BasicGPIO
This is a quick sample Python application to demonstrate GPIO usage with various switches.

### To get GPIO working
```
   sudo apt update
   sudo apt upgrade
   sudo apt install rpi.gpio
```
##### Enable Interfaces
 Enable I2C and SPI in raspi-config
```
sudo raspi-config
```

## Example usage
With the following 3 switches 
 [0] - can be UP or DOWN
 [1] - can be UP or DOWN
 [2] - can be UP or DOWN

Logic is checking that all 3 switches are UP beofre LED is enabled.

### Value of (1, -1, 1) 
LED is disabled when button is pressed
![LED OFF](20220217_203041.jpg)

### Value of (1, 1, 1) 
LED is enabled when button is pressed
![LED ON](20220217_203014.jpg)

## GPIO Diagram
![GPIO](GPIO.png)

```
//TODO add wireling diagram
```

![GPIO_BB](20220217_203025.jpg)
