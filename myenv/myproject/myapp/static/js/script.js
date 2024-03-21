'use strict';


/*event listener on mul element*/

const addEventOnElements = function(element, eventType, callback){
    for(let i =0,len =element.length; i< len; i++){
        element[i].addEventListener(eventType, callback);
    }
}

/**PRELOADER */

/**preloader will be vissible until document load */

const preloader = document.querySelector("[data-preloader]");

window.addEventListener("load",function(){
 preloader.classList.add("loaded");
 document.body.classList.add("loaded");
});

/**mobile navbar */

const navbar= document.querySelector("[data-navbar]");
const navTogglers=document.querySelectorAll("[data-nav-toggler]");
const overlay=document.querySelector("[data-overlay]");

const toggleNav =function(){
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
    document.body.classList.toggle("nav-active");
}
addEventOnElements(navTogglers, "click", toggleNav);

/**header */
const header=document.querySelector("[data-header]");
const activeElementOnScroll = function (){
    if(window.scrolly > 100){
        header.classList.add("active");
    }else{
        header.classList.remove("active");
    }
}
window.addEventListener("scroll",activeElementOnScroll);
