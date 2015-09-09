var filter_champs = function(value) {
  var champs = document.getElementById("champ-icons").querySelectorAll("a");

  for (i = 0; i < champs.length; i++){
    var champ = champs[i];
    console.log("Compare: " + champ.children[0].alt + " | " + value);
    if (champ.children[0].alt.toLowerCase().indexOf(value) > -1)
      champ.classList.remove('hide');
    else
      champ.classList.add('hide');
  }
}

var filter_edit = {
  bindEvents: function(div) {
    div.addEventListener('click', this.editFilter);
    var input = div.querySelector("input");
    input.addEventListener('blur', this.updateFilter);
    input.addEventListener('keypress', this.keypressFilter);
  },
  editFilter: function() {
    var input = this.children[1];
    this.classList.add("edit");
    input.focus;
    input.setSelectionRange(0, input.value.length);
  },
  updateFilter: function() {
    this.previousElementSibling.innerHTML = this.value;
    this.parentNode.classList.remove("edit");
    filter_champs(this.value.toLowerCase());
  },
  keypressFilter: function(event) {
    if (event.which === 13)
      filter_edit.updateFilter.call(this);
  }
}

var add_listeners = function() {
  var filter_div = document.getElementById("filter-div");
  filter_edit.bindEvents(filter_div);
}

add_listeners();
