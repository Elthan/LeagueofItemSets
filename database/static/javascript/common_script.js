// Hide all links and images of champions that does not match query.
var filter = function(value, img_type) {
  var icons = document.getElementById(img_type+"-icons-div").querySelectorAll("img");
  var value_list = value.split(" ");

  for (k = 0; k < icons.length; k++) {
    var icon = icons[k];
    var alt = icon.alt.toLowerCase();
    var tags = icon.dataset.tags.toLowerCase();

    for (i = 0; i < value_list.length; i++) {
      var filter_val = value_list[i];
      var minus = filter_val[0] == "-" ? true : false;
      if (minus)
        filter_val = filter_val.slice(1);
      var contains = (alt.indexOf(filter_val) > -1 || tags.indexOf(filter_val) > -1) ? true : false;

      if (!minus && !contains) {
        icon.parentNode.classList.add('hide');
      } else if (!minus && contains) {
        icon.parentNode.classList.remove('hide');
      } else if (minus && contains) {
        icon.parentNode.classList.add('hide');
        break;
      }
    }
  }
}

// Edit function for the filter input.
var filter_edit = {
  img_type: "",
  // Binds evenlisteners so it works.
  bindEvents: function(div, img_type) {
    this.img_type = img_type;
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
    filter(this.value.toLowerCase(), filter_edit.img_type);
  },
  // Check if they pressed enter.
  keypressFilter: function(event) {
    if (event.which === 13)
      filter_edit.updateFilter.call(this);
  }
}
