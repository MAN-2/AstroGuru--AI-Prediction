window.history.scrollRestoration = "manual";

window.onload = () => {
  window.scrollTo(0, 0);
};

const btn = document.getElementById("startReadingBtn");

gsap.registerPlugin(ScrollTrigger);

// Initial states
gsap.set(".container", {
  top: "50%",
  left: "50%",
  rotationX: 0,
  xPercent: -50,
  yPercent: -50,
});

gsap.set("#appTitle", {
  top: "10%",
  left: "50%",
  scale: 0,
  opacity: 0,
  xPercent: -50,
  yPercent: -50,
  position: "fixed",
  visibility: "hidden",
});

gsap.set(btn, {
  opacity: 0,
  display: "none",
  visibility: "hidden",
  position: "fixed",
  top: "70%",
  left: "70%",
  xPercent: -50,
  yPercent: -50,
  cursor: "pointer",
  zIndex: 170,
});

const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".spacer",
    start: "top top",
    end: "bottom bottom",
    scrub: 1,
    onEnter: () => gsap.set("#appTitle", {visibility: "visible"}),
    onLeaveBack: () => gsap.set("#appTitle", {visibility: "hidden"}),
  }
});

// Animate wheel down and rotate to pedestal
tl.to(".container", {
  duration: 1,
  top: "85%",
  rotationX: 90,
  ease: "power1.inOut",
});

// Animate app title fading and scaling in
tl.to("#appTitle", {
  duration: 1,
  top: "40%",
  scale: 4,
  opacity: 1,
  ease: "power1.inOut",
}, "<"); // start simultaneously with previous

// Animate wheel back to upright, move to right side
tl.to(".container", {
  duration: 1,
  top: "60%",
  left: "10%",
  rotationX: 0,
  xPercent: -50,
  yPercent: -50,
  ease: "power1.inOut",
  delay: 0.2,
});

// Animate app title scaling down and moving above button
tl.to("#appTitle", {
  duration: 0.8,
  top: "35%",
  left: "70%",
  scale: 3,
  ease: "power1.inOut",
}, "<");

// Reveal button with fade in and display
tl.to(btn, {
  duration: 0.8,
  opacity: 1,
  display: "block",
  visibility: "visible",
  ease: "power1.inOut",
  top: "64%",
  left: "86%",
}, "-=0.4");

// Button click navigates to /form
btn.addEventListener("click", () => {
  window.location.href = "/form";
});
