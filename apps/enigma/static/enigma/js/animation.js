const tl = new TimelineLite({ paused: false });

tl.fromTo('.graber-left', 1, {
    opacity: 0,
    x: -1000,
    ease: Power2.easeout
},{
    opacity: 1,
    x: 0
})
// .fromTo('.graber-right', 0.8, {
//     opacity: 0,
//     x: 1500,
//     ease: Power2.easeout
// },{
//     opacity: 1,
//     x: 0
// })
