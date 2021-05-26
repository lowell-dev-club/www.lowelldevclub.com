particlesJS('particles-js', {
  particles: {
    number: { value: 180, density: { enable: !0, value_area: 800 } },
    color: { value: 'random' },
    shape: {
      type: 'circle',
      stroke: { width: 0, color: '#edfedf' },
      polygon: { nb_sides: 0 },
      image: { src: 'img/github.svg', width: 100, height: 100 },
    },
    opacity: {
      value: 0.9,
      random: !0,
      anim: { enable: !1, speed: 1, opacity_min: 0.1, sync: !1 },
    },
    size: {
      value: 3,
      random: !0,
      anim: { enable: !1, speed: 40, size_min: 0.1, sync: !1 },
    },
    line_linked: {
      enable: !1,
      distance: 150,
      color: '#ffffff',
      opacity: 0.4,
      width: 1,
    },
    move: {
      enable: !0,
      speed: 10,
      direction: 'none',
      random: !1,
      straight: !1,
      out_mode: 'out',
      bounce: !1,
      attract: { enable: !0, rotateX: 600, rotateY: 1200 },
    },
  },
  interactivity: {
    detect_on: 'canvas',
    events: {
      onhover: { enable: !0, mode: 'grab' },
      onclick: { enable: !0, mode: 'bubble' },
      resize: !0,
    },
    modes: {
      grab: { distance: 140, line_linked: { opacity: 0 } },
      bubble: { distance: 200, size: 12, duration: 0.5, opacity: 1, speed: 10 },
      repulse: { distance: 200, duration: 0.4 },
      push: { particles_nb: 4 },
      remove: { particles_nb: 2 },
    },
  },
  retina_detect: !0,
});
