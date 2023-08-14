import Vue from 'vue';

new Vue({
  el: '#app',
});
var tl = gsap.timeline();

tl.from(".nav>i, .nav>div, .head, .content, .img1",{
    y:-200,
    duration:1,
    delay:0,
    opacity:0,
    stagger:0.2
})
signBtn=document.querySelector(".sign_in")
signBtn.addEventListener("click", () => {
    location.assign("/sign-in");
  });
Btn=document.querySelector(".button")
Btn.addEventListener("click", () => {
    location.assign("/certificate-us");
  });
