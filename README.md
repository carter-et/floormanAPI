# floormanAPI 
## Version 1.0 (1.1 Coming with POST abilities)
## Description
This is a really basic flask server that holds on to data, ~~and if you ask nicely~~, gives it to you. 

## Constraints
- I would not consider this a REST API since it's **read only**. There is no editing or pushing new data to it. At the moment, those kind of functions would be a bit dangerous to implement without having a layer of some sort of checking. At the very least, it needs to make sure that the only thing sending data is poker-floorman.
