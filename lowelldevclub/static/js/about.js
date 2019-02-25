/* ---- js for the particles ---- */
particlesJS("particles-js", {"particles":{"number":{"value":100,"density":{"enable":true,"value_area":800}},"color":{"value":"#EFEFEF"},"shape":{"type":"circle","stroke":{"width":0,"color":"#000000"},"polygon":{"nb_sides":5},"image":{"src":"img/github.svg","width":100,"height":100}},"opacity":{"value":0.5,"random":false,"anim":{"enable":false,"speed":0.5,"opacity_min":0.1,"sync":false}},"size":{"value":3,"random":true,"anim":{"enable":false,"speed":7,"size_min":0.1,"sync":false}},"line_linked":{"enable":true,"distance":150,"color":"#EFEFEF","opacity":0.4,"width":1},"move":{"enable":true,"speed":3,"direction":"bottom","random":false,"straight":false,"out_mode":"out","bounce":false,"attract":{"enable":false,"rotateX":600,"rotateY":1200}}},"interactivity":{"detect_on":"canvas","events":{"onhover":{"enable":true,"mode":"grab"},"onclick":{"enable":true,"mode":"push"},"resize":true},"modes":{"grab":{"distance":140,"line_linked":{"opacity":1}},"bubble":{"distance":400,"size":40,"duration":2,"opacity":8,"speed":3},"repulse":{"distance":200,"duration":0.4},"push":{"particles_nb":4},"remove":{"particles_nb":2}}},"retina_detect":true});

var typed = new Typed("#typed", {
  stringsElement: '#typed-strings',
  typeSpeed: 0,
  backSpeed: 0,
  backDelay: 500,
  startDelay: 1000,
  loop: false,
  onComplete: function(self) { prettyLog('onCmplete ' + self) },
  preStringTyped: function(pos, self) { prettyLog('preStringTyped ' + pos + ' ' + self); },
  onStringTyped: function(pos, self) { prettyLog('onStringTyped ' + pos + ' ' + self) },
  onLastStringBackspaced: function(self) { prettyLog('onLastStringBackspaced ' + self) },
  onTypingPaused: function(pos, self) { prettyLog('onTypingPaused ' + pos + ' ' + self) },
  onTypingResumed: function(pos, self) { prettyLog('onTypingResumed ' + pos + ' ' + self) },
  onReset: function(self) { prettyLog('onReset ' + self) },
  onStop: function(pos, self) { prettyLog('onStop ' + pos + ' ' + self) },
  onStart: function(pos, self) { prettyLog('onStart ' + pos + ' ' + self) },
  onDestroy: function(self) { prettyLog('onDestroy ' + self) }
});