function stats_table() {
  var tableDiv = document.createElement("stats_table_div");
  var table = document.createElement("stats_table");

  tableDiv.appendChild(table);
}

var number_of_blocks = -1;
var img_id = 0;

// Add an item to the selected block
function add_item(path, item_id) {
  var selected = document.getElementById("block-selector").selectedIndex;
  var table = document.getElementById("blocks-table-" + selected.toString());
  var img = document.createElement('img');
  img.src = path;
  img.id = img_id.toString();
  img.alt = item_id;
  img_id++;
  img.addEventListener('click', function() { remove_item(img) });
  table.rows[0].appendChild(img);
}

function remove_item(item) {
  var table = item.parentNode;
  table.removeChild(item);
}

// Makes captions editable and updates selection.
var caption_edit = {
  bindEvents: function(table) {
    table.caption.addEventListener('click', this.editCaption);
    table.caption.children[1].addEventListener('blur', this.updateCaption);
    table.caption.children[1].addEventListener('keypress', this.keypressCaption);
  },
  editCaption: function() {
    var input = this.children[1];
    this.className = "edit";
    input.focus;
    input.setSelectionRange(0, input.value.length);
  },
  updateCaption: function() {
    if (this.value != "") {
      this.previousElementSibling.innerHTML = this.value;
      var selector = document.getElementById("block-selector");
      var option = selector.children[id=this.parentNode.id];
      option.innerHTML = this.value;
    }
    this.parentNode.className = "";
  },
  keypressCaption: function(event) {
    if (event.which === 13) {
      caption_edit.updateCaption.call(this);
    }
  }
}

// Create a new block with an editable caption and a td tag inside.
function new_block() {
  if (number_of_blocks >= 10) {
    return;
  }
  number_of_blocks++;
  var tableDiv = document.getElementById("blocks");
  var table = document.createElement('table');
  table.id = "blocks-table-" + number_of_blocks.toString();

  var tr = document.createElement('tr');
  tr.appendChild(document.createElement('td'));
  table.appendChild(tr);

  var caption = table.createCaption();
  caption.id = "block-caption-" + number_of_blocks.toString();
  caption.innerHTML = "<span>Block</span> <input value='Block' />";
  caption_edit.bindEvents(table);

  var selector = document.getElementById("block-selector");
  var option = document.createElement("option")
  option.id = "block-caption-" + number_of_blocks.toString();
  option.value = number_of_blocks;
  option.innerHTML = caption.innerHTML;
  selector.appendChild( option );
  selector.selectedIndex = number_of_blocks;

  tableDiv.appendChild(table)
}

// Create the first block
new_block();

// Remove a block. If it's the last one create a new one.
function remove_block() {
  var tableDiv = document.getElementById("blocks");
  var table = document.getElementById("blocks-table-" + number_of_blocks.toString());
  tableDiv.removeChild(table);
  number_of_blocks--;
  if (number_of_blocks  < 0) {
    new_block();
  }
}

function build_item_set() {
  for (i = 0; i <= number_of_blocks; i++) {
    var table = document.getElementById("blocks-table-" + i.toString());
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
