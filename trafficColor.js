function red(){
    console.log("red")

}

function green(){
    console.log("green")
}

function yellow(){
    console.log("yellow")
}


const tic = function(delay,fn){
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            fn()
            resolve()
        },delay)
    })
}


async function steps(){
    while(true){
        await tic(2000,red)
        await tic(2000,yellow)
        await tic(2000,green)
    }
} 

steps()
// setTimeout(()=>{},10000)