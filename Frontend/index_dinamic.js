
// FUNCIONES PARA HACER DINAMICA LA INTERFAZ

let grapharbol="";
let graphts="";
let graphtsmetodo="";
let grapherrorsint="";
let grapherrorlex="";
let graphgramar="";
let cadena="";


// Para el Navbar
let navLinks = document.querySelectorAll('.navbar-nav .nav-link'); // Seleccionar solo los elementos del navbar
navLinks[0].classList.add('active');

window.addEventListener('scroll', function () {
  var logo = document.querySelector('.logoapp img');
  var navbar = document.querySelector('.navbar');

  if (window.scrollY > 30) {
    logo.src = 'Img/logoicon.ico';
    navbar.classList.add('bg-dark');
  } else {
    logo.src = 'Img/logoicon.ico';
    navbar.classList.remove('bg-dark');
  }

 
  
});

// Posicionar las secciones antes de la sección al dar clic
var links = document.querySelectorAll('.navbar-nav .nav-link');
for (var i = 0; i < 3; i++) {
  links[i].addEventListener('click', function (event) {
    event.preventDefault();
    var targetId = this.getAttribute('href').slice(1);
    var target = document.querySelector('#' + targetId);
    if (target) {
      var targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
      window.scrollTo(0, targetPosition - 130);
    }
  });
}


// Cambio de manuales
function changePDF(file, link) {
  var pdfViewer = document.querySelector('#pdf-viewer');
  pdfViewer.src = '../../Manuales/' + file;

  var links = document.querySelectorAll('.manualstile');
  links.forEach(function(link) {
    link.classList.remove('active');
  });
  link.classList.add('active');
}


// funcio para ver el offcamvas
function showOffcanvas(event) {
  event.preventDefault();
  var offcanvasElement = document.getElementById('offcanvasRight');
  var offcanvas = new bootstrap.Offcanvas(offcanvasElement);
  offcanvas.show();
}
function showOffcanvas1(event) {
  event.preventDefault();
  var offcanvasElement = document.getElementById('menu1');
  var offcanvas = new bootstrap.Offcanvas(offcanvasElement);
  offcanvas.show();
}

// Cambiar imagen de reporte segun lo seleccionado
function changeImage(text) {

   if (text=="1"){ 
       cadena=grapherrorlex;
   }else if(text=="2"){
      cadena=grapherrorsint;
    }else if(text=="3"){
      cadena=graphts;
    }else if (text=="4"){
      cadena=graphtsmetodo;
    }else if (text=="5"){
      cadena=grapharbol;
   }else{
      cadena= graphgramar;
   }
  d3.select("#imagenrep").graphviz()
  .width("1000px")
  .height("500px")
  .renderDot(cadena);
  var offcanvasElement = document.getElementById('offcanvasRight');
  var offcanvas = bootstrap.Offcanvas.getInstance(offcanvasElement);
  offcanvas.hide();

}

// Funciones de Importar y Exportar
function exportar() {
  console.log("Haciendo clic en Exportar");
  // que pida al usuario que ingrese de que base de datos se va a importar y que con un fech lo mande al backend
  const fileName = prompt('Ingrese la base de datos a exportar:');
  if (!fileName) {
    // El usuario hizo clic en Cancelar o dejó el campo vacío
    return;
  }
  fetch('http://localhost:5000/exportar', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ entrada: fileName })
  })
  // que saque una alerta con el contenido que se mando del backend
  .then(response => response.json())
  .then(data => {
      // colocar el contenido en una alerta de bootstrap
      Swal.fire({
        title: 'Contenido del Dump',
        html: '<textarea style="width:100%; height:200px; overflow:auto">' + data['message'] + '</textarea>',
        icon: 'info',
        confirmButtonText: 'Ok'
      })
  })
}

document.getElementById('import').addEventListener('click', () => {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = '.sql';

  input.onchange = () => {
    const file = input.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        const contenido = reader.result;
        fetch('http://localhost:5000/a', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ entrada: contenido })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data['message']);
            console.log(data['imprimir']);
            // Puedes manejar la respuesta del backend aquí
        })
        .catch(error => {
            console.error('Error:', error);
        });
      };
      reader.readAsText(file);
    }
  };

  // Simula un clic en el elemento de entrada
  input.click();
});

function CrearDump(){
  console.log("Haciendo clic en Crear Dump"); 
  //lo mismo que exportar  pero no pide nombre de base de datos y se muestra mensaje en alerta de bootstrap
  fetch('http://localhost:5000/dump', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ entrada: "" })
  })
  .then(response => response.json())
  .then(data => {
      // colocar el contenido en una alerta de bootstrap pero que lo muestre en un textarea con un scroll
      Swal.fire({
        title: 'Contenido del Dump',
        html: '<textarea style="width:100%; height:200px; overflow:auto">' + data['message'] + '</textarea>',
        icon: 'info',
        confirmButtonText: 'Ok'
      })
  })

} 

function CrearBase(){
  console.log("Haciendo clic en Crear Base");
  const fileName = prompt('Ingrese el nombre de la base de datos:');
  if (!fileName) {
    // El usuario hizo clic en Cancelar o dejó el campo vacío
    return;
  }
  fetch('http://localhost:5000/crear', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ entrada: fileName })
  })
  .then(response => response.json())
  .then(data => {
      console.log(data['message']);
      // Puedes manejar la respuesta del backend aquí
  })
  .catch(error => {
      console.error('Error:', error);
  });
}

function EliminarBase(){
  console.log("Haciendo clic en Eliminar Base");
  // Obtener el nombre del archivo del usuario usando prompt
  const fileName = prompt('Ingrese el nombre de la base de datos a eliminar:');
  if (!fileName) {
    // El usuario hizo clic en Cancelar o dejó el campo vacío
    return;
  }
  fetch('http://localhost:5000/eliminar', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ entrada: fileName })
  })
  .then(response => response.json())
  .then(data => {
      console.log(data['message']);
      // Puedes manejar la respuesta del backend aquí
  })
  .catch(error => {
      console.error('Error:', error);
  });
}




document.addEventListener('DOMContentLoaded', function () {
  // Function to fetch data from the backend
  function fetchDataFromBackend() {
    return fetch('http://localhost:5000/get_data') // Assuming your Flask app is running on the same domain
      .then(response => response.json())
      .catch(error => console.error('Error fetching data:', error));
  }

  function buildDynamicMenu(data) {
    const databasesSubmenu = document.getElementById('databases-submenu');

    // Clear existing content
    databasesSubmenu.innerHTML = '';

    // Iterate over the data and build the menu dynamically
    data.forEach(database => {
      const databaseItem = document.createElement('li');
      databaseItem.className = 'menu-item';
      databaseItem.textContent = database.name;

      const databaseSubmenu = document.createElement('ul');
      databaseSubmenu.className = 'submenu';

      // Add tables
      appendSubMenu(database.tables, 'Tablas', databaseSubmenu);

      // Add procedures
      appendSubMenu(database.procedures, 'Procedimientos', databaseSubmenu);

      // Add functions
      appendSubMenu(database.functions, 'Funciones', databaseSubmenu);

      // Append the submenu to the database item
      databaseItem.appendChild(databaseSubmenu);

      // Append the database item to the main menu
      databasesSubmenu.appendChild(databaseItem);
    });
  }

  // Function to append a submenu to the parent
  function appendSubMenu(items, label, parent) {
    const submenuItem = document.createElement('li');
    submenuItem.className = 'menu-item';
    submenuItem.textContent = label;

    const submenuUl = document.createElement('ul');
    submenuUl.className = 'submenu';

    items.forEach(item => {
      const itemElement = document.createElement('li');
      itemElement.className = 'menu-item';
      itemElement.textContent = item;
      submenuUl.appendChild(itemElement);
    });

    // Append the submenu to the parent
    submenuItem.appendChild(submenuUl);
    parent.appendChild(submenuItem);
  }

  // Fetch data from the backend and build the menu on page load
  fetchDataFromBackend().then(buildDynamicMenu);
});

document.querySelectorAll('.menu-item').forEach(item => {
  item.addEventListener('click', event => {
    event.preventDefault(); // Esto evita el comportamiento predeterminado del clic

    const submenu = event.target.querySelector('.submenu');
    if (submenu) {
      submenu.style.display = submenu.style.display === 'none' ? 'block' : 'none';
    }
  });
});






// FUNCIONES PARA EL EDITOR

const tabsContainer = document.querySelector('.tabs-container');
const addTabBtn = document.querySelector('.add-tab');

// Añadir nuevo tab/pestaña a la seccion de editor
addTabBtn.addEventListener('click', () => {

  // Obtener el número máximo de pestaña existente
  const tabs = document.querySelectorAll('.tab');
  let maxTabNum = 0;
  tabs.forEach(tab => {
    const tabNum = parseInt(tab.getAttribute('data-tab'));
    if (tabNum > maxTabNum) {
      maxTabNum = tabNum;
    }
  });
  const newTabNum = maxTabNum + 1;
  
  // Crear la nueva pestaña
  const newTab = document.createElement('div');
  newTab.classList.add('tab');
  newTab.setAttribute('data-tab', newTabNum);
  newTab.innerHTML = `Query ${newTabNum} <span class="close">×</span>`;
  tabsContainer.insertBefore(newTab, addTabBtn);
  
  // Crear el contenido de la nueva pestaña
  const newTabContent = document.createElement('div');
  newTabContent.classList.add('tab-content','activetab');
  newTabContent.setAttribute('data-tab', newTabNum);

  newTabContent.innerHTML = `<button type="button" class="btn btn-info">Abrir</button>
    <button type="button" class="btn btn-info">Guardar</button>
    <button type="button" class="btn btn-info">Guardar como</button>
    <button type="button" class="btn btn-info">Ejecutar Query</button>
    <div class="contenedorgeneral">
      <div class="editorcontainer">
        <textarea id="myeditor${newTabNum}"></textarea>
      </div>
      <div class="containerconsola">
        <textarea id="myconsole${newTabNum}"></textarea>
      </div>
    </div>`;
 // Agregar el nuevo contenido al DOM
 const editorElement = document.querySelector('#editor');
 editorElement.appendChild(newTabContent);
 
 // convertir los textarea a editores
  const editor = CodeMirror.fromTextArea(document.getElementById(`myeditor${newTabNum}`), {
    lineNumbers: true,
    mode: "text/x-typewise",
    theme:"tomorrow-night-bright",
    hintOptions: {
      hint: myHint,
      completeSingle: false
    },
    linerWrapping: true,
    indentWithTabs: true
  });
  //controlador de eventos del editor
editor.on("keyup", function(editor, event) {
  const keyCode = event.keyCode;
  if (keyCode !== 38 && keyCode !== 40) {
    editor.showHint();
  }
  if (event.key === 'Enter' && editor.state.completionActive) {
    editor.state.completionActive.close();
  }
});
editor.on('keydown', function(cm, event) {
  if (event.key === '\"') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('\"\"', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '\'') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('\'\'', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '(') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('()', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '{') {
    event.preventDefault();
    var cursor = cm.getCursor();
    const line = cm.getLine(cursor.line);
    const indentation = line.match(/^\s*/)[0];
    cm.replaceRange(`{}`, cursor);
    cm.setCursor({ line: cursor.line , ch: cursor.ch +1});
} 
if (event.key === 'Enter') {
  event.preventDefault();
  var cursor = cm.getCursor();
  const line = cm.getLine(cursor.line);
  const indentation = line.match(/^\s*/)[0];

  const textBeforeCursor = cm.getRange({ line: 0, ch: 0 }, cursor);
  const match = textBeforeCursor.match(/[^{]*\{([^}]*)$/);
  if (match && !match[1].trim().endsWith(';')) {
    cm.replaceRange(`\n${indentation}\t\n${indentation}`, cursor);
    cm.setCursor({ line: cursor.line + 1, ch: indentation.length + 1 });
  } else {
    cm.execCommand('newlineAndIndent');
  }
}
});
  const consoleEditor = CodeMirror.fromTextArea(document.getElementById(`myconsole${newTabNum}`), {
    lineNumbers: true,
    mode: "text/plain",
    theme:"tomorrow-night-bright",
    readOnly: true
  });

  // Agregar acción al botón "Abrir"
 const openBtn = newTabContent.querySelector('.btn-info:nth-child(1)');
 openBtn.addEventListener('click', () => {
   const input = document.createElement('input');
   input.type = 'file';
   input.accept = '.sql';
   input.onchange = () => {
     const file = input.files[0];
     if (file) {
       const reader = new FileReader();
       reader.onload = () => {
         editor.setValue(reader.result);
       };
       reader.readAsText(file);
     }
   };
   input.click();
 });
 
 // Agregar acción al botón "Guardar"
 const saveBtn = newTabContent.querySelector('.btn-info:nth-child(2)');
saveBtn.addEventListener('click', () => {
  const text = editor.getValue();
  if (!text) {
    Swal.fire(
      'No hay contenido para guardar',
      'Click en ok para salir',
      'info'
    )
    return;
  }
  // convirtiendo a archivo
  const blob = new Blob([text], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `Query${newTabNum}.sql`;
  a.click();
});
const saveAsBtn = newTabContent.querySelector('.btn-info:nth-child(3)');
saveAsBtn.addEventListener('click', () => {
  const text = editor.getValue();
  if (!text) {
    Swal.fire(
      'No hay contenido para guardar',
      'Click en ok para salir',
      'info'
    );
    return;
  }

  // Obtener el nombre del archivo del usuario usando prompt
  const fileName = prompt('Ingrese el nombre del archivo:');
  if (!fileName) {
    // El usuario hizo clic en Cancelar o dejó el campo vacío
    return;
  }

  const blob = new Blob([text], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${fileName}.sql`;
  a.click();
});
  // Agregar acción al botón "Ejecutar"
  const executeBtn = newTabContent.querySelector('.btn-info:nth-child(4)');
  executeBtn.addEventListener('click', () => {
    const editorContent = editor.getValue();
    ejecutaranalizador(editorContent,consoleEditor);
  });

  // Agregar event listeners a las nuevas pestañas y contenido
  newTab.addEventListener('click', () => {
    const tabNum = newTab.dataset.tab;
    selectTab(tabNum);
  });

  // agregando accion para cerrar pestaña
  const newCloseBtn = newTab.querySelector('.close');
  newCloseBtn.addEventListener('click', e => {
    e.stopPropagation();
    const tabNum = parseInt(e.target.parentNode.dataset.tab);
    // condicionando para que no se elimine la primera pestaña
    if (tabNum !== 1) {
      const isCurrentTab = e.target.parentNode.classList.contains('active');
      e.target.parentNode.remove();
      document.querySelector(`.tab-content[data-tab="${tabNum}"]`).remove();
      if (isCurrentTab) {
        const tabs = document.querySelectorAll('.tab');
        let prevTabNum = 0;
        tabs.forEach(tab => {
          const currentTabNum = parseInt(tab.dataset.tab);
          // condicion para seleccionar la pestaña anterior al eliminar pestaña activa
          if (currentTabNum < tabNum && currentTabNum > prevTabNum) {
            prevTabNum = currentTabNum;
          }
        });
        selectTab(prevTabNum);
      }
    }
  });
  selectTab(newTabNum);
});

// funcion para activar/seleccionar pestañas
function selectTab(tabNum) {
  const tabs = document.querySelectorAll('.tab');
  const tabContents = document.querySelectorAll('.tab-content');
  tabs.forEach(tab => {

    if (tab.dataset.tab == tabNum) {
      tab.classList.add('active');
    } else {
      tab.classList.remove('active');
    }
  });
  tabContents.forEach(content => {
    if (content.dataset.tab == tabNum) {
      content.classList.add('active');
    } else {
      content.classList.remove('active');
    }
  });
}

// Crear la primera pestaña y su contenido
const firstTab = document.createElement('div');
firstTab.classList.add('tab', 'active');
firstTab.setAttribute('data-tab', '1');
firstTab.innerHTML = `Query 1 <span class="close">×</span>`;
tabsContainer.insertBefore(firstTab, addTabBtn);

const firstTabContent = document.createElement('div');
firstTabContent.classList.add('tab-content', 'active','activetab');
firstTabContent.setAttribute('data-tab', '1');
firstTabContent.innerHTML = `<button type="button" class="btn btn-info">Abrir</button>
<button type="button" class="btn btn-info">Guardar</button>
<button type="button" class="btn btn-info">Guardar como</button>
<button type="button" class="btn btn-info">Ejecutar Query</button>
<div class="contenedorgeneral">
  <div class="editorcontainer">
    <textarea id="myeditor1"></textarea>
  </div>
  <div class="containerconsola">
    <textarea id="myconsole1"></textarea>
  </div>
</div>`;
// esta funcion obliga a que la pagina termine de cargar para realizar las acciones
window.onload = function() {

  // convierte el textarea en editor
  const editor = CodeMirror.fromTextArea(document.getElementById(`myeditor1`), {
    lineNumbers: true,
    mode: "text/x-typewise",
    theme:"tomorrow-night-bright",
    hintOptions: {
      hint: myHint,
      completeSingle: false
    },
    linerWrapping: true,
    indentWithTabs: true
  });
  //controlador de eventos del editor
editor.on("keyup", function(editor, event) {
  const keyCode = event.keyCode;
  if (keyCode !== 38 && keyCode !== 40) {
    editor.showHint();
  }
  if (event.key === 'Enter' && editor.state.completionActive) {
    editor.state.completionActive.close();
  }
});
editor.on('keydown', function(cm, event) {
  if (event.key === '\"') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('\"\"', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '\'') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('\'\'', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '(') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('()', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '{') {
    event.preventDefault();
    var cursor = cm.getCursor();
    const line = cm.getLine(cursor.line);
    const indentation = line.match(/^\s*/)[0];
    cm.replaceRange(`{}`, cursor);
    cm.setCursor({ line: cursor.line , ch: cursor.ch +1});
} 
if (event.key === 'Enter') {
  event.preventDefault();
  var cursor = cm.getCursor();
  const line = cm.getLine(cursor.line);
  const indentation = line.match(/^\s*/)[0];

  const textBeforeCursor = cm.getRange({ line: 0, ch: 0 }, cursor);
  const match = textBeforeCursor.match(/[^{]*\{([^}]*)$/);
  if (match && !match[1].trim().endsWith(';')) {
    cm.replaceRange(`\n${indentation}\t\n${indentation}`, cursor);
    cm.setCursor({ line: cursor.line + 1, ch: indentation.length + 1 });
  } else {
    cm.execCommand('newlineAndIndent');
  }
}
});
  const consoleEditor = CodeMirror.fromTextArea(document.getElementById('myconsole1'), {
    lineNumbers: true,
    mode: "text/plain",
    theme:"tomorrow-night-bright",
    readOnly: true
  });

    // Agregar acción al botón "Abrir"
    const openBtn = firstTabContent.querySelector('.btn-info:nth-child(1)');
    openBtn.addEventListener('click', () => {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.sql';
      input.onchange = () => {
        const file = input.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = () => {
            editor.setValue(reader.result);
          };
          reader.readAsText(file);
        }
      };
      input.click();
    });
    
    // Agregar acción al botón "Guardar"
    const saveBtn = firstTabContent.querySelector('.btn-info:nth-child(2)');
    saveBtn.addEventListener('click', () => {
      const text = editor.getValue();
      if (!text) {
        Swal.fire(
          'No hay contenido para guardar',
          'Click en ok para salir',
          'info'
        )
        return;
      }
      const blob = new Blob([text], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'Query1.sql';
      a.click();
    });
    const saveAsBtn = firstTabContent.querySelector('.btn-info:nth-child(3)');
    console.log(saveAsBtn);
    saveAsBtn.addEventListener('click', () => {
      const text = editor.getValue();
      if (!text) {
        Swal.fire(
          'No hay contenido para guardar',
          'Click en ok para salir',
          'info'
        );
        return;
      }

      // Obtener el nombre del archivo del usuario usando prompt
      const fileName = prompt('Ingrese el nombre del archivo:');
      if (!fileName) {
        // El usuario hizo clic en Cancelar o dejó el campo vacío
        return;
      }

      const blob = new Blob([text], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${fileName}.sql`;
      a.click();
    });
    // Agregar acción al botón "Ejecutar"
    const executeBtn = firstTabContent.querySelector('.btn-info:nth-child(4)');
    console.log(executeBtn)
    executeBtn.addEventListener('click', () => {
      const editorContent = editor.getValue();
      ejecutaranalizador(editorContent,consoleEditor);
     
     
    });
  
}

const editorElement = document.querySelector('#editor');
editorElement.appendChild(firstTabContent);
// seleccionar primera pestaña
firstTab.addEventListener('click', () => {
  const tabNum = firstTab.dataset.tab;
  selectTab(tabNum);
});

const firstCloseBtn = firstTab.querySelector('.close');
firstCloseBtn.addEventListener('click', e => {
  e.stopPropagation();
  const tabNum = parseInt(e.target.parentNode.dataset.tab);
  if (tabNum === 1) {
    const firstTabContent = document.querySelector(`.tab-content[data-tab="${tabNum}"]`);

    firstTabContent.innerHTML = `<button type="button" class="btn btn-info">Abrir</button>
    <button type="button" class="btn btn-info">Guardar</button>
    <button type="button" class="btn btn-info">Guardar como</button>
    <button type="button" class="btn btn-info">Ejecutar Query</button>
    <div class="contenedorgeneral">
      <div class="editorcontainer">
        <textarea id="myeditor${tabNum}"></textarea>
      </div>
      <div class="containerconsola">
        <textarea id="myconsole${tabNum}"></textarea>
      </div>
    </div>`;

    // crea los editores y consola
    const editor = CodeMirror.fromTextArea(document.getElementById(`myeditor${tabNum}`), {
      lineNumbers: true,
      mode: "text/x-typewise",
      theme:"tomorrow-night-bright",
      hintOptions: {
        hint: myHint,
        completeSingle: false,
          closeOnUnfocus: true
      },
      linerWrapping: true,
      indentWithTabs: true
    });
  //controlador de eventos del editor
editor.on("keyup", function(editor, event) {
  const keyCode = event.keyCode;
  if (keyCode !== 38 && keyCode !== 40) {
    editor.showHint();
  }
  if (event.key === 'Enter' && editor.state.completionActive) {
    editor.state.completionActive.close();
  }
});
editor.on('keydown', function(cm, event) {
  if (event.key === '\"') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('\"\"', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '\'') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('\'\'', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '(') {
    event.preventDefault();
    var cursor = cm.getCursor();
    cm.replaceRange('()', cursor);
    cm.setCursor({line: cursor.line, ch: cursor.ch + 1});
  }
  if (event.key === '{') {
    event.preventDefault();
    var cursor = cm.getCursor();
    const line = cm.getLine(cursor.line);
    const indentation = line.match(/^\s*/)[0];
    cm.replaceRange(`{}`, cursor);
    cm.setCursor({ line: cursor.line , ch: cursor.ch +1});
} 
if (event.key === 'Enter') {
  event.preventDefault();
  var cursor = cm.getCursor();
  const line = cm.getLine(cursor.line);
  const indentation = line.match(/^\s*/)[0];

  const textBeforeCursor = cm.getRange({ line: 0, ch: 0 }, cursor);
  const match = textBeforeCursor.match(/[^{]*\{([^}]*)$/);
  if (match && !match[1].trim().endsWith(';')) {
    cm.replaceRange(`\n${indentation}\t\n${indentation}`, cursor);
    cm.setCursor({ line: cursor.line + 1, ch: indentation.length + 1 });
  } else {
    cm.execCommand('newlineAndIndent');
  }
}
});
  const consoleEditor = CodeMirror.fromTextArea(document.getElementById(`myconsole${tabNum}`), {
    lineNumbers: true,
    mode: "text/plain",
    theme:"tomorrow-night-bright",
    readOnly: true
  });
    // Agregar acción al botón "Abrir"
    const openBtn = firstTabContent.querySelector('.btn-info:nth-child(1)');
    openBtn.addEventListener('click', () => {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.sql';
      input.onchange = () => {
        const file = input.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = () => {
            editor.setValue(reader.result);
          };
          reader.readAsText(file);
        }
      };
      input.click();
    });
    
    // Agregar acción al botón "Guardar"
    const saveBtn = firstTabContent.querySelector('.btn-info:nth-child(2)');
    console.log(saveBtn)
    saveBtn.addEventListener('click', () => {
      const text = editor.getValue();
      if (!text) {
        Swal.fire(
          'No hay contenido para guardar',
          'Click en ok para salir',
          'info'
        )
        return;
      }
      const blob = new Blob([text], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Query${tabNum}.sql`;
      a.click();
    });
    const saveAsBtn = firstTabContent.querySelector('.btn-info:nth-child(3)');
    console.log(saveAsBtn);
    saveAsBtn.addEventListener('click', () => {
      const text = editor.getValue();
      if (!text) {
        Swal.fire(
          'No hay contenido para guardar',
          'Click en ok para salir',
          'info'
        );
        return;
      }

      // Obtener el nombre del archivo del usuario usando prompt
      const fileName = prompt('Ingrese el nombre del archivo:');
      if (!fileName) {
        // El usuario hizo clic en Cancelar o dejó el campo vacío
        return;
      }

      const blob = new Blob([text], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${fileName}.sql`;
      a.click();
    });

    // Agregar acción al botón "Ejecutar"
    const executeBtn = firstTabContent.querySelector('.btn-info:nth-child(4)');
    console.log(executeBtn)
    executeBtn.addEventListener('click', () => {
      const editorContent = editor.getValue();
      ejecutaranalizador(editorContent,consoleEditor);
    });
  
    tabCounter = 1;
  } else {
    const isCurrentTab = e.target.parentNode.classList.contains('active');
    e.target.parentNode.remove();
    document.querySelector(`.tab-content[data-tab="${tabNum}"]`).remove();
    if (isCurrentTab) {
      selectTab(tabNum - 1);
    }
  }
});






// FUNCIONES PARA EL ANALIZADOR
function ejecutaranalizador (entrada,consoleEditor){
  // limpiando consola
  consoleEditor.setValue("");
  // limpiando variables globales
  grapharbol="";
  graphts="";
  graphtsmetodo="";
  grapherrorsint="";
  grapherrorlex="";
  graphgramar="";
  cadena="";
  // limpiando variables de tabla de simbolos
  tablaSimbolos=[];

  fetch('http://localhost:5000/a', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ entrada: entrada })
  })
  .then(response => response.json())
  .then(data => {
      console.log(data['message']);
      console.log(data['imprimir']);
      // {'message': 'Procesado con éxito','lista':lista1,'imprimir':imprimir,'Errorlexico':Errorlexico,'ErrorSintactico':ErrorSintactico,'Gramatical':Gramatical,'tablasim':tablasimbolo,'tablamet':tablametodo,'arbol':arbol}
      grapherrorlex=data['Errorlexico'];
      graphgramar=data['Gramatical'];
      grapherrorsint=data['ErrorSintactico'];
      graphts=data['tablasim'];
      graphtsmetodo=data['tablamet'];
      grapharbol=data['arbol'];
      consoleEditor.setValue(data['imprimir']);
  })
  .catch(error => {
      console.error('Error:', error);
  });

}

