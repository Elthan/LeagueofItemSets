// Bind listeners to the div surrounding the filter input.
var add_listeners = function() {
  var filter_div = document.getElementById("filter-div");
  filter_edit.bindEvents(filter_div, "champ");
}

// Inital call when javascript loads.
add_listeners();
