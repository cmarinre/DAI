document.getElementById("switch").addEventListener('click', function(){
    let val=document.body.classList.toggle("dark")
    localStorage.setItem("switch", val)
})

let valor = localStorage.getItem("switch")

if(valor=="true"){
    document.body.classList.add("dark")
}
else{
    document.body.classList.remove("dark")
}