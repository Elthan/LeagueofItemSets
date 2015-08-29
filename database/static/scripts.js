/***********
*
* Disclaimer: this is messy.
*
***********/

var stats_table = {

  // Convert db names to more human friendly names.
  stats_names: {
    "MPRegen": "Mana Regen",
    "SpellBlock": "Magic Resist",
    "Crit": "Critical Chance",
    "AttackDamage": "Attack Damage",
    "MP": "Mana",
    "HPRegen": "Health Regen",
    "HP": "Health",
    "Armor": "Armor",
    "MoveSpeed": "Move Speed"
  },

  champ_stats: "",
  stats_table: "",

  createTable: function() {
    var tableDiv = document.getElementById("stats-table-div");
    var table = document.createElement("table");
    table.id = "stats-table";

    // Make an object out of the stats
    var champ_stats = tableDiv.dataset.stats;
    champ_stats = champ_stats.replace(/'/g, '\"');
    champ_stats = champ_stats.replace(/Decimal\(\"([\d\.]+)\"\)/g, '$1');
    champ_stats = JSON.parse(champ_stats)[0];

    delete champ_stats["ChampID"];
    delete champ_stats["AttackRange"];
    delete champ_stats["AttackSpeedOffset"];

    var count = 0;
    var tr = document.createElement('tr');
    for (stat in champ_stats) {
      if (!~stat.indexOf("PerLevel") && stat != "ChampID") {
        var th = document.createElement('th');
        var td = document.createElement('td');

        th.className = "stats-header";
        td.className = "stats-cell";

        th.id = stat;

        th.appendChild( document.createTextNode(this.stats_names[stat]) );
        td.appendChild( document.createTextNode(champ_stats[stat]) );

        th.appendChild(td);
        tr.appendChild(th);

        count++;
      }
      if (count >= 3) {
        table.appendChild(tr);
        tr = document.createElement('tr');
        count = 0;
      }
    }

    table.appendChild(tr);
    tableDiv.appendChild(table);

    this.champ_stats = champ_stats;
    this.stats_table = table;
  },

  updateStats: function(item_stats) {
    
  }
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

// Remove item
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
function add_block() {
  if (number_of_blocks >= 10) {
    return;
  }
  number_of_blocks++;
  var tableDiv = document.getElementById("blocks");
  var table = document.createElement('table');
  table.id = "blocks-table-" + number_of_blocks.toString();
  table.className = "blocks-table";

  var tr = document.createElement('tr');
  var input = document.createElement('input');
  input.type = "checkbox";
  input.value = "recmath";
  input.title = "Click if this all the items in this block should build into the last (RecMath)";
  tr.appendChild(input);
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

// Remove a block. If it's the last one create a new one. Update selector.
function remove_block() {
  var tableDiv = document.getElementById("blocks");
  var table = document.getElementById("blocks-table-" + number_of_blocks.toString());
  tableDiv.removeChild(table);
  var selector = document.getElementById("block-selector");
  selector.remove(number_of_blocks);
  number_of_blocks--;
  if (number_of_blocks  < 0) {
    add_block();
  }
}

// Extract the information we need.
function build_item_set() {
  for (i = 0; i <= number_of_blocks; i++) {
    var table = document.getElementById("blocks-table-" + i.toString());
    console.log(table.childNodes);

  }
}

// Run initial setup functions
add_block();
stats_table.createTable();
