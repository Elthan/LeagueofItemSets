
document.getElementById("stat_table").innerHTML = "JAVASCRIPT TABLE HERE"

var number_of_blocks = 0;

function new_block() {
  number_of_blocks++;

  if (number_of_blocks > 10) {
    return
  }

  var tableDiv = document.getElementById("blocks");
  var table = document.createElement('table');
  table.id = "block_table";
  var tr = document.createElement('tr');
  tr.appendChild( document.createTextNode('Drag items here') );
  table.appendChild(tr);
  tableDiv.appendChild(table)
}

function block_drop(ev) {
  ev.preventDefault();
  if (dragSrcEl != this) {
    var table = document.getElementById('block_table');
    if (table.innerHTML == "Drag items here") {
      table.innerHTML = "";
    } else {
      table.innerHTML += " + ";
    }
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
  }
}

var cols = document.querySelectorAll('#items');
[].forEach.call(cols, function(col) {
  col.addEventListener('dragstart', handleDragStart, false);
  col.addEventListener('dragenter', handleDragEnter, false);
  col.addEventListener('dragover', handleDragOver, false);
  col.addEventListener('dragleave', handleDragLeave, false);
  col.addEventListener('drop', handleDrop, false);
  col.addEventListener('dragend', handleDragEnd, false);
});

var dragSrcEl = null;

function handleDragOver(ev) {
  ev.preventDefault();
  ev.dataTransfer.dropEffect = 'move';
  return false;
}

function handleDragStart(ev) {
  this.style.opacity = "0.7";
  dragSrcEl = this;

  ev.dataTransfer.effectAllowed = 'move';
  ev.dataTransfer.setData("text/html", this.innerHTML);
}

function handleDragEnter(ev) {
  this.classList.add('over');
  /*
  if (ev.stopPropagation) {
    ev.stopPropagation();
  }
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
  */
}

function handleDragLeave(ev) {
  this.classList.remove('over');
}

function handleDragEnd(ev) {
  [].forEach.call(cols, function (col) {
      col.classList.remove('over');
  });
}

function handleDrop(ev) {
  if (ev.stopPropagation) {
    ev.stopPropagation();
  }

  if (dragSrcEl != this) {
    dragSrcEl.innerHTML = this.innerHTML;
    this.innerHTML = ev.dataTransfer.getData("text/html");
  }

  return false;
}
