$(function(){
	$(".construction").typed({
		strings: ["Under Construction"],
		// Optionally use an HTML element to grab strings from (must wrap each string in a <p>)
		stringsElement: null,
		// typing speed
		typeSpeed: 0,
		// time before typing starts
		startDelay: 0,
		// backspacing speed
		backSpeed: 20,
		// time before backspacing
		backDelay: 500,
		// loop
		loop: false,
		// false = infinite
		loopCount: false,
		// show cursor
		showCursor: false,
		// character for cursor
		cursorChar: "|",
		// attribute to type (null == text)
		attr: null,
		// either html or text
		contentType: 'html',
		// call when done callback function
		callback: function() {},
		// starting callback function before each string
		preStringTyped: function() {},
		//callback for every typed string
		onStringTyped: function() {},
		// callback for reset
		resetCallback: function() {}
	});
});
$(function(){$(".flask").typed({strings: ["Full Stack Web Development"],stringsElement: null,typeSpeed: 0,startDelay: 0,backSpeed: 20,backDelay: 500,loop: false,loopCount: false,showCursor: false,cursorChar: "|",attr: null,contentType: 'html',callback: function() {},preStringTyped: function() {},onStringTyped: function() {},resetCallback: function() {}});});
$(function(){$(".text-based").typed({strings: ["Python Text Based Game"],stringsElement: null,typeSpeed: 0,startDelay: 0,backSpeed: 20,backDelay: 500,loop: false,loopCount: false,showCursor: false,cursorChar: "|",attr: null,contentType: 'html',callback: function() {},preStringTyped: function() {},onStringTyped: function() {},resetCallback: function() {}});});

/*
	This is the type script for the club description in the about page
*/

var i = 0;
var txt = "We are working on the workshop. Check out our github to take a peak at the source code or what this weeks workshop will be on here: https://github.com/lowell-dev-club";
var speed = 40;
var delayInMilliseconds = 1200
setTimeout(function() {
    if (i < txt.length) {
      document.getElementById("message").innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
}, delayInMilliseconds);

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("message").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
var i1 = 0;
var txt1 = "1. https://repl.it";
var delayInMilliseconds = 1200
setTimeout(function() {if (i1 < txt1.length) {document.getElementById("link1").innerHTML += txt1.charAt(i1);i1++;setTimeout(typeWriter1, speed);}}, delayInMilliseconds);
function typeWriter1() {if (i1 < txt1.length) {document.getElementById("link1").innerHTML += txt1.charAt(i1);i1++;setTimeout(typeWriter1, speed);}}
var i2 = 0;
var delayInMilliseconds2 = 3000
var txt2 = "2. https://lowelldev.club/workshop/hack1";
setTimeout(function() {if (i2 < txt2.length) {document.getElementById("link2").innerHTML += txt2.charAt(i2);i2++;setTimeout(typeWriter2, speed);}}, delayInMilliseconds2);
function typeWriter2() {if (i2 < txt2.length) {document.getElementById("link2").innerHTML += txt2.charAt(i2);i2++;setTimeout(typeWriter2, speed);}}
var i3 = 0;
var delayInMilliseconds3 = 5000
var txt3 = "3. https://lowelldev.club/workshop/hack2";
setTimeout(function() {if (i3 < txt3.length) {document.getElementById("link3").innerHTML += txt3.charAt(i3);i3++;setTimeout(typeWriter3, speed);}}, delayInMilliseconds3);
function typeWriter3() {if (i3 < txt3.length) {document.getElementById("link3").innerHTML += txt3.charAt(i3);i3++;setTimeout(typeWriter3, speed);}}
var i4 = 0;
var delayInMilliseconds4 = 3000
var txt4 = "2. https://lowelldev.club/workshop/hack3";
setTimeout(function() {if (i4 < txt4.length) {document.getElementById("link4").innerHTML += txt4.charAt(i4);i4++;setTimeout(typeWriter4, speed);}}, delayInMilliseconds4);
function typeWriter4() {if (i4 < txt4.length) {document.getElementById("link4").innerHTML += txt4.charAt(i4);i4++;setTimeout(typeWriter4, speed);}}