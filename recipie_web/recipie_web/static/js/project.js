/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');

var ingredients = '';
var nutritional_values = '';

$('#recipie-text-save').click(function(e) {
   e.preventDefault();
   var foodName = $('#recipie-name').val(),
       nutritionalValues = nutritional_values;

   var data = {
       'name' : foodName,
       'nutritionals' : nutritionalValues
   }
   var ret = '';

   $.ajax({
      url:'/recipie/api/v1/food/?format=json',
      type:"POST",
      data:JSON.stringify(data),
      contentType:"application/json; charset=utf-8",
      dataType:"json",
      success: function(response) {
          foodId = response['id'];
          ret += 'Food ID : ' + foodId;
          $.each(ingredients, function (i, v) {
              var ingData = {
                  'name': v['name'],
                  'food': {'pk': foodId},
                  'quantity': v['quantity']
              }

              $.ajax({
                  url: '/recipie/api/v1/ingredient/?format=json',
                  type: "POST",
                  data: JSON.stringify(ingData),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                  success: function (response) {
                      ret += ' ingredient id : ' + response.id;
                      console.log(response);
                  }
              });
          });
      }});
console.log(ret);
});

$('#recipie-text').submit(function(e) {
   e.preventDefault();
   var text = $('#recipie-textarea').val();

   var url = '/recipie/recipie_to_nut';

   $.post(url, {'text' : text}, function(response) {
       var response = JSON.parse(response);
       console.log(response);
       //$('#nutritional-val-container').html(response);
       var missed = response['missed_ingredients'];
       //debugger;
       $('#missed-ingredients').hide();

       if (missed) {
        $('#missed-ingredients').show().html(missed);
       }
        ingredients = response['ingredients']['ingredients'];
       nutritional_values = response['nutritional_values'];
       var table = $('#nutrition-chart');
       var template = '<tr><th>Nutrition (Per 100 gm)</th><th>Quantity</th></tr>'
       for (i in response.nutritional_values) {
           var value = response.nutritional_values[i];

           value = Math.round(value * 100) / 100;
           template += '<tr><td>' + i +'</td><td>' + value + '</td></tr>'
       }
       table.html(template);

        $('#ingredients').text(JSON.stringify(nutritional_values));
   });
});
