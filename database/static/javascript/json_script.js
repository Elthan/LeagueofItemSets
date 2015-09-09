
// Make the JSON look better by using HTML syntax.
var beautify = function (json) {
  var beautiful_json = json.replace(/ /gi, "&nbsp").replace(/\n/gi, "<br />")
  .replace(/\"([\w]+)\":/gi, "<b>$1:</b>").replace(/\"*([\w\d]+)\"*,/gi, "$1,");
  return beautiful_json;
}

// Beautify as soon as the page has loaded.
window.addEventListener('load', function() {
  var json = document.getElementById("beautiful-json");
  var beautiful_json = beautify(json.dataset.json);
  json.innerHTML = beautiful_json;
});
