$().ready(function(){
$(".save").click(function(){
	var title = $("#id_title").val();
	var text = $("#id_text").val();
	var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
	var post_data = {'title':title, 'text':text, 'csrfmiddlewaretoken':csrfmiddlewaretoken};
	console.log(post_data);	
	var formdata = new FormData();

    formdata.append("filedoc", uploadedfiles[index-1]);
    formdata.append("title", title);
    formdata.append("text", text);
    formdata.append('csrfmiddlewaretoken', csrfmiddlewaretoken);

	$("#output").html(title + " ; ");
	$.ajax({
		type: $('#myForm').attr('method'),
		url: '/post/1/edit/',
		data: $('#myForm').serialize(),
		dataType: "text",
		processData: false,
		success: function (response) {

		}
	});
});
});