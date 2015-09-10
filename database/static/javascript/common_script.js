// Hide all links and images of champions that does not match query.
var filter = function(value, img_type) {
  var icons = document.getElementById(img_type+"-div").querySelectorAll("img");

  for (i = 0; i < icons.length; i++){
    var icon = icons[i];
    if (icon.alt.toLowerCase().indexOf(value) > -1 ||
        icon.dataset.tags.toLowerCase().indexOf(value) > -1) {
      icon.parentNode.classList.remove('hide');
    } else {
      icon.parentNode.classList.add('hide');
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
