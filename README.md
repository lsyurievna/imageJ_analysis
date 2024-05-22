The project I did while working for Dr. Erika Merschrod who is an expert in Surface Science. 
The idea behind the project was to process a batch Scanning Electron Microscope (SEM) images of 
cobal ferrite nanoparticles and determine their approximate cross-sectional areas.

Below is what an SEM image typically looks like. You can see a few nanoparticles 
in their beautiful trigonal bipyramidal form.

<img  style = "width: 400px;" src="https://user-images.githubusercontent.com/61998449/180675091-cdb57007-4404-45bd-974e-b946819e54da.jpg">

We then take that SEM image and - with the magic of coding -  try to isolate all individual nanoparticles. This gives us an image below where the black spots are the nanoparticles the script identified.


<img  style = "width: 400px;" src="https://user-images.githubusercontent.com/61998449/180675654-d605a96e-eba4-4a7b-9346-cadf4265b9a8.jpg">

Afterwards, tge area of the black shapes is calculated in pixels and further converted to nanometers based on how many pixels fit
into the black rectangular scale in the original image. 

With these scripts, I analyzed dozens of SEM images and was able to give an approximate size distribution of the cobalt ferrite nanoparticles in a given sample. 
