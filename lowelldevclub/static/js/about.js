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
	$(".meet_leaders").typed({
		strings: ["Meet the leaders:"],
		// Optionally use an HTML element to grab strings from (must wrap each string in a <p>)
		stringsElement: null,
		// typing speed
		typeSpeed: 0,
		// time before typing starts
		startDelay: 1850,
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
var txt = 'Lowell Dev Club is a place where anyone can be engaged in the world of \
			computer science. Our club is focuses on enchancing your programming skills or \
			helping you learn new ones. Don\'t worry if you\'re a beginner because at our \
			club you\'ll have expert peer instructors who have tons of computer science experience and completed projects.';
var speed = 10;
var delayInMilliseconds = 800
setTimeout(function() {
    if (i < txt.length) {
      document.getElementById("about_paragraph").innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
}, delayInMilliseconds);

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("about_paragraph").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
