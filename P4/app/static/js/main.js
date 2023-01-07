//______________________________________________
//----------------MODO OSCURO-------------------
//______________________________________________

document.getElementById("moon").addEventListener('click', function(){
    let val = document.body.classList.toggle("dark")
    localStorage.setItem("moon", val)
})

let valor = localStorage.getItem("moon")

if (valor==true){
    document.body.classList.add("dark")
}
else{
    document.body.classList.remove("dark")

}



//______________________________________________
//----------------TAMAÑO LETRA------------------
//______________________________________________

document.getElementById("text").addEventListener('click', function(){
    let val = document.body.classList.toggle("size")
    localStorage.setItem("text", val)
})

let valorl = localStorage.getItem("text")

if (valorl==true){
    document.body.classList.add("size")
}
else{
    document.body.classList.remove("size")

}



//______________________________________________
//------------------- TABLA----------------------
//______________________________________________
const recetas = []              // declaraciones   
let html_str  = ''              // de variables
let i         = 0               //
let i_eliminar = 0
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
                        <button onclick="detalle('${i-1}')" type="button" class="btn btn-outline btn-sm" data-bs-toggle="modal" data-bs-target="#detailModal" id="nombreFila"> ${fila.name}</button>
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
                        <button onclick="editarReceta('${i-1}')" 
                        type="button" class="btn btn-warning btn-sm"
                        data-bs-toggle="modal" data-bs-target="#editModal" id="editButton">
                        Edit
                        </button>
                        <div class="modal" tabindex="-1" role="dialog" id="editModal">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="titleEditModal"></h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body" id="bodyEditModal">
                                        
                                    </div>
                                </div>
                            </div>
                        </div>

                        <button type="button" onclick="asegurar_i('${i}')" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" id="deleteButton">Delete</button>
                        <div class="modal" tabindex="-1" role="dialog" id="deleteModal">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="staticBackdropLabel">Confirmación</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        ¿Estás seguro de que quieres eliminar la receta?
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" onclick="eliminarReceta()">Eliminar</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>`         // ES6 templates
    });
    document.getElementById('tbody').innerHTML=html_str  // se pone el html en su sitio
})



//______________________________________________
//------------FUNCIONES ELIMINAR----------------
//______________________________________________


function asegurar_i(identifi){
    i_eliminar = identifi-1
}


function eliminarReceta(){
    fetch('/api/recipes/' + recetas[i_eliminar]._id.$oid, {
        method: 'DELETE'
    });
    location.reload();
}




//______________________________________________
//------------FUNCIONES EDITAR----------------
//______________________________________________

function editarReceta(ide){

    var nombre = recetas[ide].name;


    html_str_formulario_titulo = `      
        <p>${nombre}</p>
    `


    var instrucciones_html = ''
    recetas[ide].instructions.forEach(inst =>{
        instrucciones_html += `${inst}
`
    })

    var ingredientes_html = ''
    recetas[ide].ingredients.forEach(ing =>{
        ingredientes_html += `${ing.name}
`
    })


    html_str_formulario_body= `
        <!--Donde se mete la info-->
        <form action="/api/recipes/" method="put" enctype="multipart/form-data" id="recipe-form-edit"> 
            <!--Nombre-->
            <div class="md-form mb-4">
                <label for="nameRecipe" class="letter-name">Name</label>
                <input type="text" class="form-control" id="nameRecipe" name="nameInputEdit" value="${nombre}">
                <label data-error="wrong" data-success="right" for="form8" class="letter-bottom">A name for the recipe</label>
            </div>

            <!--Ingredientes-->
            <div class="md-form mb-4">
                <label data-error="wrong" data-success="right" for="form8" class="letter-name">Components</label>
                <textarea type="text" id="form8" class="md-textarea form-control" rows="4" name="componentsInputEdit">${ingredientes_html}</textarea>
                <label data-error="wrong" data-success="right" for="form8" class="letter-bottom">The components recipe, in lines</label>
            </div>

            <!--Instrucciones-->
            <div class="md-form mb-4">
                <label data-error="wrong" data-success="right" for="form8" class="letter-name">Instructions</label>
                <textarea type="text" id="form8" class="md-textarea form-control" rows="4" name="instructionsInputEdit">${instrucciones_html}</textarea>
                <label data-error="wrong" data-success="right" for="form8" class="letter-bottom">The instructions, in lines</label>
            </div>

            <!--Botones de guardar y salir-->
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button onclick="anadirRecetaEditada(${ide})" type="button" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
            </div>
        </form>  
    `

    document.getElementById('titleEditModal').innerHTML=html_str_formulario_titulo
    document.getElementById('bodyEditModal').innerHTML=html_str_formulario_body

}



function anadirRecetaEditada(identif){
    
    //Creamos el object que vamos a guardar en nuestra BBDD
    var total = {};

    
    //Obtenemos el formulario del html
    var formData = new FormData(document.getElementById("recipe-form-edit"));

    //Obtenemos el name que viene en el formulario, comprobando si existe


    var name = formData.get("nameInputEdit");

    //Y lo guardamos en el object final
    total["name"] = name;

    //Obtenemos las instrucciones de la receta, que vienen en filas distintas
    var instrucciones = [];
    var cadena = formData.get("instructionsInputEdit");
    var array = cadena.split("\n");
    
    array.forEach(function(instr){
        instrucciones.push(instr);
    })
    
    total["instructions"] = instrucciones;

    //Obtenemos los componentes, los separamos
    var componentes = [];
    var cadena = formData.get("componentsInputEdit");
    var array = cadena.split("\n");
    
    array.forEach(function(comp, index){
        //Y los guardamos en el formato necesario
        componentes[index] = {"name": comp};
    })

    total["ingredients"] = componentes;


    fetch('/api/recipes/' + recetas[identif]._id.$oid, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(total)
    });
    location.reload();

}




//______________________________________________
//------------FUNCION DETALLE----------------
//______________________________________________


function detalle(ident) {  // saca un modal con la información de cada coctel
    // saca un modal con receta[i]
  
      var nombre = recetas[ident].name;
  
      let html_str_title  = `
          <p id="name-detail">${nombre}</p>
      `
  
      html_str_body = `
          <p class="letter-name">Ingredients</p>
          <div class="ing-div">
      `
      recetas[ident].ingredients.forEach(ing =>{
          html_str_body += `
          <li>${ing.name}</li>
          `
      })
  
      html_str_body +=`
          </div>
      `
  
      html_str_body += `<div id="margin-top"></div>`
      recetas[ident].instructions.forEach(inst =>{
          html_str_body += `
          <p>-${inst}</p>
          `
      })
  
      document.getElementById('titleModal').innerHTML=html_str_title  
      document.getElementById('bodyModal').innerHTML=html_str_body  
  
  }
    



//___________________________________________________
//------------ FUNCION BUSCAR RECETA ----------------
//___________________________________________________

function buscarReceta(){
    var formData = new FormData(document.getElementById("searchForm"));
    var busqueda = formData.get("searchInput");

}




//___________________________________________________
//------------ FUNCION AÑADIR RECETA ----------------
//___________________________________________________



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
        var componentes = [];
        var cadena = formData.get("componentsInput");
        var array = cadena.split("\n");
        
        array.forEach(function(comp, index){
            //Y los guardamos en el formato necesario
            componentes[index] = {"name": comp};
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
    location.reload();

}

