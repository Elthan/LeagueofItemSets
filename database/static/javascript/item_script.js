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
    "MagicDamage": "Ability Power"
  },

  champ_stats: "",
  stats_table: "",

  // Create the table.
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

  // Make the stats presentable.
  trimStats: function(stat) {
    // Check if it contains various things, then remove or rename it if it does.
    // stat.indexOf() equals -1 if it can't find it, ~ flips it so it's 0 (false).
    var base = ~stat.indexOf("Base") ? true : false;
    stat = base ? stat.slice(4) : stat;
    var flat = ~stat.indexOf("Flat") ? true : false;
    if (!base)
      stat = flat ? stat.slice(4) : stat.slice(7);
    stat = stat.slice(0,-3);
    stat = ~stat.indexOf("Pool") ? stat.slice(0,-4) : stat;
    stat = ~stat.indexOf("PhysicalDamage") ? "AttackDamage" : stat;
    stat = ~stat.indexOf("MovementSpeed") ? "MoveSpeed" : stat;
    stat = ~stat.indexOf("CritChance") ? "Crit" : stat;
    return stat;
  },

  // Update the table with by either adding or removing item stats.
  updateStats: function(adding, item_stats) {
    item_stats = this.convertJSON(item_stats)
    delete item_stats["ItemID"];
    for (index_stat in item_stats) {
      var base = ~index_stat.indexOf("Base") ? true : false;
      var flat = ~index_stat.indexOf("Flat") ? true : false;
      var stat = this.trimStats(index_stat);
      var td = document.getElementById(stat).children[0];
      var prev_val = parseFloat(td.innerHTML);
      var stat_val = 0;
      if (base)
        stat_val += (this.champ_stats[stat] * (item_stats[index_stat]) / 100);
      else
        stat_val = (stat == "Crit" || stat == "LifeSteal") ? item_stats[index_stat]*100 : item_stats[index_stat];
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

// Add an item to the selected block
function add_item(item) {
  var selected = document.getElementById("block-selector").value;
  var table = document.getElementById("blocks-table-" + selected);
  var gold_cost = table.querySelector(".gold-cost");
  var td = document.createElement('td');
  var img = document.createElement('img');

  var prev_cost = parseInt(gold_cost.innerHTML);
  gold_cost.innerHTML = prev_cost + parseInt(item.dataset.cost);

  img.src = item.dataset.icon;
  img.id = item.id;
  img.dataset.stats = item.dataset.stats;
  img.dataset.cost = item.dataset.cost;
  img.addEventListener('click', function() { remove_item(img) });

  if (table.rows[0].children.length > 0) {
    td.appendChild( document.createTextNode('+') );
  }

  td.appendChild(img);
  table.rows[0].appendChild(td);
  stats_table.updateStats(true, item.dataset.stats);
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

  var gold_cost = tr.parentNode.querySelector(".gold-cost");
  var prev_cost = parseInt(gold_cost.innerHTML);
  gold_cost.innerHTML = prev_cost - parseInt(item.dataset.cost);

  // If its part of the selected block, substract stats from stats table.
  var selector = document.getElementById("block-selector");
  var index = selector.selectedIndex;
  if (tr.parentNode.querySelector("caption").id == selector.options[index].id)
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

// Create a new block.
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

  // Total gold cost of items
  var gold_cost = document.createElement('p');
  gold_cost.title = "Total gold cost of all the items in this block.";
  gold_cost.classList.add('gold-cost');
  gold_cost.appendChild( document.createTextNode(0) );
  table.appendChild(gold_cost);
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
  hide_button.innerHTML = ">";
  hide_button.title = "Toggle hiding of item set";
  hide_button.addEventListener('click', function() {
    toggle_block(table, recmath, input, caption, gold_cost, this);
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

// Show or hide the block.
function toggle_block(table, recmath, input, caption, gold, button) {
    table.rows[0].classList.toggle('hide');
    recmath.classList.toggle('hide');
    input.classList.toggle('hide');
    caption.classList.toggle('shrink');
    gold.classList.toggle('gold-cost-shrink');
    button.classList.toggle('hide-buttons-shrink');
    if (button.innerHTML === "V")
      button.innerHTML = ">";
    else
      button.innerHTML = "V";
}

// Show or hide items.
function toggle_items(button) {
  var items_div = document.getElementById("items-div");
  items_div.classList.toggle('hide');
  if (button.innerHTML == "^")
    button.innerHTML = "V";
  else
    button.innerHTML = "^";

  var toggle_div = button.parentNode;
  if (toggle_div.classList.contains('toggle-items')) {
    toggle_div.classList.add('toggle-items-hidden');
    toggle_div.classList.remove('toggle-items');
  } else {
    toggle_div.classList.add('toggle-items');
    toggle_div.classList.remove('toggle-items-hidden');
  }
}

// Extract the information we need and send us to the next page.
function build_item_set(path) {
  var blocks_div = document.getElementById("blocks");
  var item_set = {};
  var blocks = [];

  var name = document.getElementById("item-set-name");
  var map = document.getElementById("map-selector");

  item_set["name"] = name.value;
  item_set["map"] = map.value;

  for (var i = 0; i < blocks_div.childElementCount; i++) {
    var block = {};
    var table = blocks_div.children[i];

    block["name"] = table.querySelector("caption").querySelector("span").innerHTML;
    block["recmath"] = table.querySelector("input").checked;

    var items = {};
    var query = table.querySelectorAll("img");
    for (var k = 0; k < query.length; k++) {
      var item = query[k].id;
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

// Populate with information about the item.
function item_info(item)  {
  // Add the items name.
  var item_name = document.getElementById("item-info-name");
  while(item_name.lastChild)
    item_name.removeChild(item_name.lastChild);
  item_name.appendChild( document.createTextNode(item.alt) );

  // Add the items icon.
  var item_icon = document.getElementById("item-info-icon");
  while(item_icon.lastChild)
    item_icon.removeChild(item_icon.lastChild);
  var clone_icon = item.parentNode.cloneNode(true);
  var clone_icon_image = clone_icon.querySelector("img");
  clone_icon_image.addEventListener('click', function() {
    add_item(this);
  });
  item_icon.appendChild(clone_icon);

  // Add items description.
  var item_description = document.getElementById("item-info-description");
  while(item_description.lastChild)
    item_description.removeChild(item_description.lastChild);
  item_description.appendChild( document.createTextNode(item.dataset.description) );

  // Add items stats.
  var item_stats_field = document.getElementById("item-info-stats");
  var index_stats = stats_table.convertJSON(item.dataset.stats);
  delete index_stats["ItemID"];
  var stats_string = "";
  for (stats in index_stats)
    stats_string += "<p class=\"item-info-left\">" +
                    stats_table.stats_names[stats_table.trimStats(stats)] +
                    ":</p><p class=\"item-info-right\">"
                    + index_stats[stats] + "</p><br />";
  item_stats_field.innerHTML = stats_string;

  // Add the items that the item builds into.
  var field = document.getElementById("item-builds-field");
  while (field.lastChild)
    field.removeChild(field.lastChild);
  var into = JSON.parse(item.dataset.into.replace(/'/g, "\""));
  if (into[0] != "") {
    field.parentNode.classList.remove('hide');
    for (i = 0; i < into.length; i++) {
      var into_item = document.getElementById(into[i]);
      var clone_into = into_item.parentNode.cloneNode(true);
      var clone_into_image = clone_into.querySelector("img");
      clone_into_image.addEventListener('click', function() {
        item_info(this);
      });
      field.appendChild(clone_into);
    }
  } else {
    field.parentNode.classList.add('hide');
  }
}

// Remove unwanted items.
function remove_items() {
  var items = document.getElementById("item-icons").querySelectorAll("img");
  // TODO: Find out what needs to be removed.
}

function filter_string(value) {
  var filter_div = document.getElementById("filter-div");
  filter_div.querySelector("span").innerHTML = value;
  filter_div.querySelector("input").value = value;
  filter(value, "item");
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

  var items_div = document.getElementById("item-icons-div").querySelectorAll("img");
  for (i = 0; i < items_div.length; i++) {
    item = items_div[i];
    item.addEventListener('click', function() {
      item_info(this);
    });
    item.addEventListener('dblclick', function() {
      add_item(this);
    });
  }

  var toggle_items_button = document.getElementById("items-button");
  toggle_items_button.addEventListener('click', function(){
    toggle_items(this);
  });

  var filter_div = document.getElementById("filter-div");
  filter_edit.bindEvents(filter_div, "item");

  var filter_buttons_div = document.getElementById("filter-buttons-div");

  var filter_all = filter_buttons_div.querySelector("#filter-all");
  filter_all.addEventListener('click', function() {
    filter_string("");
  });

  var filter_attack = filter_buttons_div.querySelector("#filter-attack");
  filter_attack.addEventListener('click', function() {
    filter_string("damage -spelldamage");
  });

  var filter_armor = filter_buttons_div.querySelector("#filter-armor");
  filter_armor.addEventListener('click', function() {
    filter_string("armor");
  });

  var filter_health = filter_buttons_div.querySelector("#filter-health");
  filter_health.addEventListener('click', function() {
    filter_string("health");
  });

  var filter_mana = filter_buttons_div.querySelector("#filter-mana");
  filter_mana.addEventListener('click', function() {
    filter_string("mana");
  });

  var filter_consumable = filter_buttons_div.querySelector("#filter-consumable");
  filter_consumable.addEventListener('click', function() {
    filter_string("consumable");
  });

  var filter_boots = filter_buttons_div.querySelector("#filter-boots");
  filter_boots.addEventListener('click', function() {
    filter_string("boots -nonbootsmovement");
  });

  var filter_nonboots = filter_buttons_div.querySelector("#filter-nonboots");
  filter_nonboots.addEventListener('click', function() {
    filter_string("nonbootsmovement");
  });
};

// Run initial setup functions
add_block();
stats_table.createTable();
add_listeners();
