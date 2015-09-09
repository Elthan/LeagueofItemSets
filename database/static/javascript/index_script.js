// Hide all links and images of champions that does not match query.
var filter_champs = function(value) {
  var champs = document.getElementById("champ-icons").querySelectorAll("a");

  for (i = 0; i < champs.length; i++){
    var champ = champs[i].children[0];
    if (champ.alt.toLowerCase().indexOf(value) > -1 ||
        champ.dataset.tags.toLowerCase().indexOf(value) > -1)
      champ.parentNode.classList.remove('hide');
    else
      champ.parentNode.classList.add('hide');
  }
}

// Edit function for the filter input.
var filter_edit = {
  // Binds evenlisteners so it works.
  bindEvents: function(div) {
    div.addEventListener('click', this.editFilter);
    var input = div.querySelector("input");
    input.addEventListener('blur', this.updateFilter);
    input.addEventListener('keypress', this.keypressFilter);
  },
  // For when they want to edit the field.
  editFilter: function() {
    var input = this.children[1];
    this.classList.add("edit");
    input.focus;
    input.setSelectionRange(0, input.value.length);
  },
  // Updating the span to show current search query and call filtering.
  updateFilter: function() {
    this.previousElementSibling.innerHTML = this.value;
    this.parentNode.classList.remove("edit");
    filter_champs(this.value.toLowerCase());
  },
  // Check if they pressed enter.
  keypressFilter: function(event) {
    if (event.which === 13)
      filter_edit.updateFilter.call(this);
  }
}

// Bind listeners to the div surrounding the filter input.
var add_listeners = function() {
  var filter_div = document.getElementById("filter-div");
  filter_edit.bindEvents(filter_div);
}

// Inital call when javascript loads.
add_listeners();
