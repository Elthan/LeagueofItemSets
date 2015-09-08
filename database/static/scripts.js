/***********
*
* Now a little bit cleaner
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
    "MoveSpeed": "Move Speed",
    "AttackSpeed": "Attack Speed",
    "LifeSteal": "Life steal",
    "SpellVamp": "Spellvamp",
    "MagicDamage": "Ability Points"
  },

  champ_stats: "",
  stats_table: "",

  createTable: function() {
    var tableDiv = document.getElementById("stats-table-div");
    var table = document.createElement("table");
    table.id = "stats-table";

    // Make an object out of the stats
    var champ_stats = tableDiv.dataset.stats;
    champ_stats = this.convertJSON(champ_stats)[0]

    delete champ_stats["ChampID"];
    delete champ_stats["AttackRange"];
    champ_stats["AttackSpeed"] = 0.625 / (1 + parseInt(champ_stats["AttackSpeedOffset"]));
    delete champ_stats["AttackSpeedOffset"];
    champ_stats["MagicDamage"] = 0;
    champ_stats["LifeSteal"] = 0;

    var count = 0;
    var tr = document.createElement('tr');

    // Create table without the per level stats
    for (stat in champ_stats) {
      if (!~stat.indexOf("PerLevel")) {
        var th = document.createElement('th');
        var td = document.createElement('td');

        th.classList.add("stats-header");
        td.classList.add("stats-cell");

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

  updateStats: function(adding, item_stats) {
    item_stats = this.convertJSON(item_stats)

    delete item_stats["ItemID"]

    for (index_stat in item_stats) {
      stat = index_stat;

      // Check if it contains various things, then remove or rename it if it does.
      var flat = ~stat.indexOf("Flat") ? true : false;
      stat = flat ? stat.slice(4) : stat.slice(7);
      stat = stat.slice(0,-3);
      stat = ~stat.indexOf("Pool") ? stat.slice(0,-4) : stat;
      stat = ~stat.indexOf("PhysicalDamage") ? "AttackDamage" : stat;
      stat = ~stat.indexOf("MovementSpeed") ? "MoveSpeed" : stat;
      stat = ~stat.indexOf("CritChance") ? "Crit" : stat;

      var td = document.getElementById(stat).children[0];
      var prev_val = parseFloat(td.innerHTML);
      var stat_val = stat == "Crit" || stat == "LifeSteal" ? item_stats[index_stat]*100 : item_stats[index_stat];
      var new_val = adding ? prev_val + stat_val : prev_val - stat_val;
      td.innerHTML = new_val.toFixed(3);
    }
  },

  // Convert the stats string to a Javascript object we can use.
  convertJSON: function(stat_string) {
    stat_string = stat_string.replace(/Decimal\(\'([\-\d\.]+)\'\)/g, '$1');
    stat_string = stat_string.replace(/'/g, '\"');
    stat_string = JSON.parse(stat_string);
    return stat_string
  },

  // When the selected block changes, we update the stats too.
  changeBlock: function(selector) {
    for (stat in this.champ_stats) {
      if (!~stat.indexOf("PerLevel")) {
        var td = document.getElementById(stat).children[0];
        td.innerHTML = this.champ_stats[stat];
      }
    }

    var selected = selector.value;
    var table = document.getElementById("blocks-table-" + selected);
    var items = table.querySelectorAll("img");

    for (i = 0; i < items.length; i++) {
      this.updateStats(true, items[i].dataset.stats);
    }
  }
}

var number_of_blocks = -1;
var img_id = 0;

// Add an item to the selected block
function add_item(path, item_id, item_stats) {
  var selected = document.getElementById("block-selector").value;
  var table = document.getElementById("blocks-table-" + selected);
  var td = document.createElement('td');
  var img = document.createElement('img');

  img.src = path;
  img.id = img_id.toString();
  img.alt = item_id;
  img.dataset.stats = item_stats;
  img_id++;
  img.addEventListener('click', function() { remove_item(img) });

  if (table.rows[0].children.length > 0) {
    td.appendChild( document.createTextNode('+') );
  }

  td.appendChild(img);
  table.rows[0].appendChild(td);
  stats_table.updateStats(true, item_stats);
}

// Remove item
function remove_item(item) {
  var tr = item.parentNode.parentNode;
  var next = item.parentNode.nextSibling;

  // If it's the first item remove the + sign from the now first item
  if (tr.children[0] === item.parentNode && next) {
      next.removeChild(next.childNodes[0]);
  }
  tr.removeChild(item.parentNode);

  // If its part of the selected block, substract stats from stats table.
  var selector = document.getElementById("block-selector");
  var index = selector.selectedIndex;
  if (tr.parentNode.children[0].id == selector.options[index].id)
    stats_table.updateStats(false, item.dataset.stats);
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
    this.classList.add("edit");
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
    this.parentNode.classList.remove("edit");
  },
  keypressCaption: function(event) {
    if (event.which === 13)
      caption_edit.updateCaption.call(this);
  }
}

// Create a new block with an editable caption and a td tag inside.
function add_block() {
  var tableDiv = document.getElementById("blocks");

  // Maximum number of blocks is 10.
  if (tableDiv.childElementCount >= 9) {
    return;
  }

  number_of_blocks++;

  // Create new table with unique id.
  var table = document.createElement('table');
  table.id = "blocks-table-" + number_of_blocks.toString();
  table.classList.add("blocks-table");
  // table.classList.add("hide");
  // table.classList.toggle("hide");

  // Create a row and the recmath checbox.
  var tr = document.createElement('tr');
  var input = document.createElement('input');
  input.type = "checkbox";
  input.value = "recmath";
  input.title = "Click if this all the items in this block should build into the last.";
  table.appendChild(input);

  // Text next to the checkbox
  var recmath = document.createElement('p');
  recmath.title = "Should all the items in this block build into the last?";
  recmath.classList.add("recmath-text");
  recmath.innerHTML = "Recmath";
  recmath.addEventListener('click', function (){
    var is_checked = input.checked;
    if (is_checked)
      input.checked = false;
    else
      input.checked = true;
  });
  table.appendChild(recmath);
  table.appendChild(tr);

  // Create the caption which is the block name.
  var caption = table.createCaption();
  caption.id = "block-caption-" + number_of_blocks.toString();
  caption.classList.add('block-caption');
  caption.innerHTML = "<span>Block</span> <input value='Block' />";
  caption.title = "Click me to set the name of block";
  caption_edit.bindEvents(table);

  // Create a button that hides the item set.
  var hide_button = document.createElement('button');
  hide_button.classList.add('hide-buttons');
  hide_button.innerHTML = "V";
  hide_button.title = "Toggle hiding of item set";
  hide_button.addEventListener('click', function() {
    table.rows[0].classList.toggle('hide');
    recmath.classList.toggle('hide');
    input.classList.toggle('hide');
    if (hide_button.innerHTML === "V")
      hide_button.innerHTML = ">";
    else
      hide_button.innerHTML = "V";
  });
  table.insertBefore(hide_button, caption);

  // Update the selector with the new table.
  var selector = document.getElementById("block-selector");
  var option = document.createElement("option")
  option.id = "block-caption-" + number_of_blocks.toString();
  option.value = number_of_blocks;
  option.innerHTML = caption.innerHTML;
  selector.appendChild( option );
  selector.selectedIndex = selector.length - 1;

  tableDiv.appendChild(table)
  stats_table.changeBlock(selector);
}

// Remove a block. If it's the last one create a new one. Update selector.
function remove_block() {
  var tableDiv = document.getElementById("blocks");
  var selector = document.getElementById("block-selector");
  var table = document.getElementById("blocks-table-" + selector.value);

  // Remove the block and the entry in the selector.
  tableDiv.removeChild(table);
  selector.remove(selector.selectedIndex);

  // We always want to have at least one block.
  if (tableDiv.childElementCount === 0)
    add_block();

  // Set the selector to the last entry in it.
  selector.selectedIndex = selector.length - 1;
  stats_table.changeBlock(selector);
}

// Extract the information we need and send us to the next page.
function build_item_set(path) {
  var blocks_div = document.getElementById("blocks");
  var item_set = {};
  var blocks = [];

  var name = document.getElementById("item-set-name");
  var map = document.getElementById("map-selector");

  item_set["name"] = name.innerHTML;
  item_set["map"] = map.options[map.selectedIndex].value;

  for (var i = 0; i <= number_of_blocks; i++) {
    var block = {};
    var table = blocks_div.children[i];

    block["name"] = table.children[0].children[0].innerHTML;
    block["recmath"] = table.children[1].checked;

    var items = {};
    var query = table.querySelectorAll("img");
    for (var k = 0; k < query.length; k++) {
      var item = query[k].alt;
      var number = items[item];
      number = (number == undefined) ? 1 : number + 1;
      items[item] = number;
    }

    block["items"] = items;
    blocks.push(block);
  }

  item_set["blocks"] = blocks;
  var json_item_set = JSON.stringify(item_set);

  var form = document.createElement('form');
  form.setAttribute("method", "post");
  form.setAttribute("action", path);

  // Create a hidden field with the JSON file.
  var hiddenField = document.createElement("input");
  hiddenField.setAttribute("type", "hidden");
  hiddenField.setAttribute("name", "item_set");
  hiddenField.setAttribute("value", json_item_set);
  form.appendChild(hiddenField);
  document.body.appendChild(form);
  form.submit();
}

// Add listeners to the buttons.
var add_listeners = function() {
  var build = document.getElementById("build");
  build.addEventListener('click', function() {
    build_item_set(build.dataset.url);
  });

  var add = document.getElementById("add");
  add.addEventListener('click', function() {
    add_block();
  });

  var remove = document.getElementById("remove");
  remove.addEventListener('click', function() {
    remove_block();
  });

  var selector = document.getElementById("block-selector");
  selector.addEventListener('change', function() {
    stats_table.changeBlock(this);
  });

  var items = document.getElementById("items").children;
  for (i = 0; i < items.length; i++) {
    item = items[i];
    item.addEventListener('click', function() {
      add_item( this.dataset.icon, this.dataset.id, this.dataset.stats );
    });
  }
};

// Run initial setup functions
add_block();
stats_table.createTable();
add_listeners();
