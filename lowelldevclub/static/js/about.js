// var typed = new Typed('#typed',{
//     stringsElement: '#typed-strings',
//     backSpeed: 40,
//     typeSpeed: 40
//   });

$(function(){
	$(".about_us").typed({
		strings: ["About Us"],
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

/*
	This is the type script for the club description in the about page
*/
var i = 0;
var txt = "Meet the leaders:";
var speed = 40;
var delayInMilliseconds = 1200
setTimeout(function() {
    if (i < txt.length) {
      document.getElementById("meet_leaders").innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
}, delayInMilliseconds);

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("meet_leaders").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
