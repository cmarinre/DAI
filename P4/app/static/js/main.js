

const recetas = []              // declaraciones   
let html_str  = ''              // de variables
let i         = 0               //
// fetch devuelve una promise
fetch('/api/recipes/')           // GET por defecto,
.then(res => res.json())        // respuesta en json, otra promise
.then(filas => { // arrow function

    
    filas.forEach(fila => {     // bucle ES6, arrow function
        i++
        recetas.push(fila)      // se guardan para después sacar cada una             
        // ES6 templates
        html_str += `
                <tr>
                    <td>${i}</td>
                    <td>
                        <button onclick="detalle('${i-1}')" 
                            type="button" class="btn btn-outline btn-sm"
                            data-bs-toggle="modal" data-bs-target="#detailModal">
                        ${fila.name}
                        </button>
                        <div class="modal" tabindex="-1" role="dialog" id="detailModal">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="titleModal"></h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body" id="bodyModal">
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                    </td>
                    <td>
                        <button type="button" class="btn btn-warning btn-sm">Edit</button>
                        <button type="button" class="btn btn-danger btn-sm">Delete</button>
                    </td>
                </tr>`         // ES6 templates
    });
    document.getElementById('tbody').innerHTML=html_str  // se pone el html en su sitio
})




function detalle(i) {  // saca un modal con la información de cada coctel
  // saca un modal con receta[i]

    var nombre = recetas[i].name;


    let html_str_title  = `
        <p id="name-detail">${nombre}</p>
    `

    html_str_body = `
        <p class="letter-name">Ingredients</p>
        <div class="ing-div">
    `
    recetas[i].ingredients.forEach(ing =>{
        html_str_body += `
        <li>${ing.name}</li>
        `
    })

    html_str_body +=`
        </div>
    `

    html_str_body += `<div id="margin-top"></div>`
    recetas[i].instructions.forEach(inst =>{
        html_str_body += `
        <p>-${inst}</p>
        `
    })

    document.getElementById('titleModal').innerHTML=html_str_title  
    document.getElementById('bodyModal').innerHTML=html_str_body  

}
  

function anadirReceta(){


    //Creamos el object que vamos a guardar en nuestra BBDD
    var total = {};
    
    //Obtenemos el formulario del html
    var formData = new FormData(document.getElementById("recipe-form"));

    //Obtenemos el name que viene en el formulario, comprobando si existe
    if(formData.has("nameInput")){

        var name = formData.get("nameInput");

        //Y lo guardamos en el object final
        total["name"] = name;

        //Obtenemos las instrucciones de la receta, que vienen en filas distintas
        var instrucciones = [];
        var cadena = formData.get("instructionsInput");
        var array = cadena.split("\n");
        
        array.forEach(function(instr){
            instrucciones.push(instr);
        })
        
        total["instructions"] = instrucciones;

        //Obtenemos los componentes, los separamos
        var componentes = [{'hola': "e"}];
        var cadena = formData.get("componentsInput");
        var array = cadena.split("\n");         //No me coge bien el primero
        
        array.forEach(function(comp, index){
            //Y los guardamos en el formato necesario
                componentes.push({"name": comp});
        })

        total["ingredients"] = componentes;

        fetch('/api/recipes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(total)
        });
    }



    
}