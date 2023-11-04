$('#btnloaddata').click(function(){
    //alert('You clicked Me');
    var form_data=new FormData($("#upload-file")[0]);
    $.ajax({
        type:'POST',
        url:'/uploadajax',
        data:form_data,
        contentType:false,
        Cache:false,
        processData:false,
        success:function(data)
        {
            alert('Data uploaded successfully');
        },

    });
});