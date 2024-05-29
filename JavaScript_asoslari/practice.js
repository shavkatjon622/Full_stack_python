// ip manzilni himoyalaydigan dastur

let ip = prompt("Iltiomos, Ip manzilkiriting!!!")

let natija  = ip.replaceAll(".", "[.]");

console.log(natija);
// dastur tugadi





// matndagi oxirgi so'zni harflari sonini aniqlab beruvchi dastur

function hisoblovchi(text) {
    
    let sozlar = text.trim().split(' ');
    
    let songgiSoz = sozlar[sozlar.length - 1];
    return songgiSoz.length;
}

let matn = prompt("Biror matn kiriting!");
console.log(hisoblovchi(matn));
//dastur tugadi
