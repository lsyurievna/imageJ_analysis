//Selects a rectangular section of the picture that only contains the particles, and
//applies a number of filters to it. Once the picture is converted to binary,
//measures the areas of the particles and saves file as a .scv document
//
function action(input, filename, pic_output, data_output)
{
	run("Size...", "width=300 height=240 depth=1 constrain average  interpolation=Bilinear");
	makeRectangle(0, 0, 298, 224);
	run("Duplicate...", " ");
	run("Smooth");
	run("Subtract Background...", "rolling=5 create");
	setOption("BlackBackground", false);
	run("Convert to Mask");
	run("Watershed");
	saveAs("Jpeg", pic_output + filename);
	name = filename + ".scv";

	
	run("Analyze Particles...", "clear");
	Table.sort("Area");
	saveAs("Results", data_output + name);
	close();	
}

//The heart of this automatization. 

function getParticleAreas(input, filename)
{
	open(input + filename);

	stringArray = split(filename, "-");
	name = stringArray[0];
	pxls = stringArray[1];
	number= stringArray[2];
	
	lastString = split(stringArray[3],".");
	units = lastString[0];
	

	fpxls = parseFloat(pxls);
	fnumber = parseFloat(number);

	scaleSetter(units);
	action(input, name, pic_output, data_output);	
}

//Takes string of units as a parameter, and sets the scale appropriately.
function scaleSetter(units)
{
	if (units == "nm")
	{
		run("Set Scale...", "distance=fpxls known=fnumber unit=nm");
	}
	else
	{
		run("Set Scale...", "distance=fpxls known=1000 unit=nm");
	}
	
}

input = "C:/Users/test/Desktop/Job/Cobalt Ferrites/12_ Trial 3 (S) copy/";
pic_output = "C:/Users/test/Desktop/Job/Cobalt Ferrites/12_ Trial 3 (S) bw/";
data_output = "C:/Users/test/Desktop/Job/Cobalt Ferrites/12_ Trial 3 (S) areas/";


setBatchMode(true); 
list = getFileList(input);
for (i = 0; i < list.length; i++){
        getParticleAreas(input, list[i]);
}
setBatchMode(false);
