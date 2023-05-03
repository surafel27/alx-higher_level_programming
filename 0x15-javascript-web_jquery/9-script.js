$(function () {
  fetch('https://fourtonfish.com/hellosalut/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const hello = data.hello;
      $('#hello').text(hello);
    });
});
