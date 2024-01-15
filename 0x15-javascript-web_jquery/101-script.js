$(document).ready(function() {
  function addItem() {
    $('<li>Item</li>').appendTo('.my_list');
  }

  function removeItem() {
    $('.my_list li:last').remove();
  }

  function clearList() {
    $('.my_list li').remove();
  }

  $('#add_item').click(addItem);
  $('#remove_item').click(removeItem);
  $('#clear_list').click(clearList);
});
