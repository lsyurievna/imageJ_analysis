//The script runs through all the images in a specified folder,
//captures the scales and saves the results in a separate .txt file with 
//the same name, in the specified folder. 

//Opens a specified file from the specified folder
//extracts the part with the scale bar and 
//returns the area and parameter of the scale bar in a text document 
//to the folder of interest. 
function captureScaleBar(input, filename, output)
{
	filename = substring(filename, 0, filename.length-4);

	open(input+filename+".jpg" );
	makeRectangle(0, 1924, 1696, 60);
	run("Duplicate...", " ");
	setOption("BlackBackground", false);
	run("Convert to Mask");
	run("Set Measurements...", "area perimeter redirect=None decimal=3");
	run("Analyze Particles...", "clear");
	run("Input/Output...", "jpeg=85 gif=-1 file=.txt use use_file");
	saveAs("Results", output + filename + ".txt");
	close();
}



input = "C:/Users/test/Desktop/Job/Cobalt Ferrites/12_ Trial 3 (S) copy/";
output = "C:/Users/test/Desktop/Job/Cobalt Ferrites/12_ Trial 3 (S) txt_results/";


setBatchMode(true); 
list = getFileList(input);
for (i = 0; i < list.length; i++){
        captureScaleBar(input, list[i], output);
}
setBatchMode(false);
