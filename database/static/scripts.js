function stats_table() {
  var tableDiv = document.createElement("stats_table_div");
  var table = document.createElement("stats_table");

  
  tableDiv.appendChild(table);
}

var number_of_blocks = 0;
var img_id = 0;

function add_item(path, item_id) {
  var table = document.getElementById("blocks_table-" + number_of_blocks.toString());
  var img = document.createElement('img');
  img.src = path;
  img.id = img_id.toString();
  img.alt = item_id;
  img_id++;
  img.addEventListener('click', function() { remove_item(img.id) });
  cell = table.rows[0].insertCell(-1);
  table.rows[0].appendChild(img);
}

function remove_item(img_id) {
  var table = document.getElementById("blocks_table-" + number_of_blocks.toString());
  var item = document.getElementById(img_id);
  table.rows[0].removeChild(item);
}

function new_block() {
  if (number_of_blocks >= 10) {
    return;
  }

  number_of_blocks++;
  var tableDiv = document.getElementById("blocks");
  var table = document.createElement('table');
  table.id = "blocks_table-" + number_of_blocks.toString();
  var tr = document.createElement('tr');
  table.appendChild(tr);
  tableDiv.appendChild(table)
}

function remove_block() {
  if (number_of_blocks == 0) {
    return;
  }
  var tableDiv = document.getElementById("blocks");
  var table = document.getElementById("blocks_table-" + number_of_blocks.toString());
  tableDiv.removeChild(table);
  number_of_blocks--;
}

function build_item_set() {
  for (i = 0; i <= number_of_blocks; i++) {
    var table = document.getElementById("blocks_table-" + i.toString());
    console.log(table.childNodes);

  }
}

/*
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
*/
