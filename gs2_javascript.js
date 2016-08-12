var name=["Sam", "Gale", "Riley", "Jordan", "Cam", "Dani", "Charlie", "Dakota", "Skylar", "Frankie", "Jessie", "Sage", "Quinn", "Peyton", "Avery", "Reese", "Taylor", "Morgan", "Ryan", "Carter"];
var gender=["Female", "Male", "Other"];
var age=[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99];
var bloodtype=["A+", "A-", "B+", "B-", "AB+", "AB-"," O"];
var meds=["Adderal", "Amoxicillin",  "Coumadin"];

function Patient(){
	this.Name= name[Math.floor(Math.random()*name.length)];
	this.Gender= gender[Math.floor(Math.random()*gender.length)];
	this.Bloodtype= bloodtype[Math.floor(Math.random()*bloodtype.length)];
	this.Meds= meds[Math.floor(Math.random()*meds.length)];
	this.Age= age[Math.floor(Math.random()*age.length)];
	this.Stats= "Name: {} "+"\n"+"Age: {} "+"\n"+"Gender: {} "+"\n"+"Bloodtype: {} "+"\n"+"Medication: {} ";
}

function Neo_natal(){
	Patient.call(this);
	this.premature=[0,0,0,0,0,0,0,0,0,1];
	this.breech=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
	this.Premature=Neo_natal.premature[Math.floor(Math.random()*10)];
	this.Age_range;
}
// Neo_natal.prototype = Object.create(Patient.prototype);
var Jane=new Neo_natal();
