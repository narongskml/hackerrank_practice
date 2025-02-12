function gridChallenge(grid) {
    // Write your code here
    let n= grid.length;
    let result="";
    if (n==1){
        return "YES"
    }
    for (let i=0; i<n-1 ; i++){
        let v1 =grid[i].split('').sort().join();
        let v2 =grid[i+1].split('').sort().join();
        console.log(`${i} : v1 = ${ v1 }, v2= ${ v2}`)
        for(let j=0; j< v1.length;j++)
        {
            if (v1.charAt(j)<=v2.charAt(j))
            {
                result="YES";
            }
            else{
                result = "NO";
                return result;
            }
        }
    }
    return result;
}
let  grid1 = ['hcd', 'awc', 'shm'];
console.log(gridChallenge(grid1));

let  grid2 = ['sur', 'eyy', 'gxy'];
console.log(gridChallenge(grid2));

let  grid3 = ['nyx', 'ynx', 'xyt'];
console.log(gridChallenge(grid3));

let  grid4 = ['vpvv', 'pvvv', 'vzzp','zzyy'];
console.log(gridChallenge(grid4));
/*

4
3
hcd
awc
shm
3
sur
eyy
gxy
3
nyx
ynx
xyt
4
vpvv
pvvv
vzzp
zzyy

Expect output

NO
NO
YES
YES
*/