$('#select_categories').change(function() {
    var value = $('#select_categories').val();
    $.ajax({
        url: '/dashboard/levelzero_selected/',
        method: 'POST',
        data: {
            'selected_category': value,
        },
        success: function(data){
            $('#levelone_placeholder').empty()
            $('#leveltwo_placeholder').empty()
            $('#levelthree_placeholder').empty()
            $('#levelone_placeholder').append(
                `<option id='levelone_placeholder'">-------------</option>`
            )
            $('#leveltwo_placeholder').append(
                `<option id='leveltwo_placeholder'">-------------</option>`
            )
            $('#levelthree_placeholder').append(
                `<option id='levelthree_placeholder'">-------------</option>`
            )
                for (i = 0; i < data['result'].length; i++) {
                    $('#levelone_placeholder').append(
                        `<option id='levelone_placeholder' value="` + data['result'][i] + `">` + data['result'][i] + `</option>`
                    );

                }
        }

    });
});

$('#levelone_placeholder').change(function() {
    var value = $('#levelone_placeholder').val();
    $.ajax({
        url: '/dashboard/levelone_selected/',
        method: 'POST',
        data: {
            'selected_category_one': value,
        },
        success: function(data){
            $('#leveltwo_placeholder').empty()
            $('#levelthree_placeholder').empty()
            $('#leveltwo_placeholder').append(
                `<option id='leveltwo_placeholder'">-------------</option>`
            )
            $('#levelthree_placeholder').append(
                `<option id='levelthree_placeholder'">-------------</option>`
            )
                for (i = 0; i < data['result'].length; i++) {
                    $('#leveltwo_placeholder').append(
                        `<option id='leveltwo_placeholder' value="` + data['result'][i] + `">` + data['result'][i] + `</option>`
                    );

                }
        }

    });
});

$('#leveltwo_placeholder').change(function() {
    var value = $('#leveltwo_placeholder').val();
    $.ajax({
        url: '/dashboard/leveltwo_selected/',
        method: 'POST',
        data: {
            'selected_category_one': value,
        },
        success: function(data){
            $('#levelthree_placeholder').empty()
            $('#levelthree_placeholder').append(
                `<option id='levelthree_placeholder'">-------------</option>`
            )
                for (i = 0; i < data['result'].length; i++) {
                    $('#levelthree_placeholder').append(
                        `<option id='levelthree_placeholder' value="` + data['result'][i] + `">` + data['result'][i] + `</option>`
                    );

                }
        }

    });
});