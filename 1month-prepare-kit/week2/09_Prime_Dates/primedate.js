function findPrimeDate(input){
    let prim=0; let curdate=new Date(input.split(' ')[0].split('-')[2],input.split(' ')[0].split('-')[1]-1, input.split(' ')[0].split('-')[0]);  let enddate=new Date(input.split(' ')[1].split('-')[2],input.split(' ')[1].split('-')[1]-1, input.split(' ')[1].split('-')[0]); 
    for(let d=curdate; d<=enddate ;d.setDate(d.getDate()+1) ){ if (d.toJSON().slice(0,10).split('-').reverse().join('')%4==0|| d.toJSON().slice(0,10).split('-').reverse().join('')%7==0){ prim++;}    }
    return prim;
}
function processData(input) {
    console.log(findPrimeDate(input));
} 

/*
process.stdin.resume();
process.stdin.setEncoding("ascii");
let _input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
*/
let _input="02-08-2025 04-09-2025";
processData(_input);