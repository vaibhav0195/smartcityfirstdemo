$( document ).ready(function() {
    console.log( "ready!" );
    function changeImage(element){
    $.get('thumb?imageName=' + element.name, function(data){
        try{
            document.getElementById("labelledMatter").style.visibility = "visible";
        }
        catch(err){

        }
        $(".textcont").remove();
        $(".DocumentItem1").append("<div class=\"textcont text-center\"></div>");
        parsedData = JSON.parse(data)
        folder = parsedData.folder
        imageName = parsedData.imageData
//        postProcessedData = parsedData.postProcessInfo

        basename = imageName.substring(0, imageName.indexOf('.'))
        ext = imageName.substring(imageName.indexOf('.'))
        //document.getElementsByName("originalImage")[0].src = '/static/images/' + folder + '/' + basename + '_boundary' + ext  //since actualimage.jpg is same as actualimage_boundary.jpg
//        document.getElementById("audioTag").load();  //since actualimage.jpg is same as actualimage_boundary.jpg
//        document.getElementById("orignalImage").src = '../../static/' + folder+'/audios' + '/' + imageName;  //since actualimage.jpg is same as actualimage_boundary.jpg
//        document.getElementsByName("segmentedImage")[0].src = '/static/images/' + folder + '/segmented.' + basename + ext
//        $('.textcont').append((parsedData.text));

//        $('.billDate')[0].innerHTML = postProcessedData.billDate;
//        $('.billNumber')[0].innerHTML = postProcessedData.billNumber;
//        $('.billTime')[0].innerHTML = postProcessedData.billTime;
//        $('.billTotal')[0].innerHTML = postProcessedData.billTotal;

   });

}

$(document).on('change', '.btn-file :file', function() {
   var input = $(this),
   numFiles = input.get(0).files ? input.get(0).files.length : 1,
   label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
   $("#button").click();
});
//console.log($("#fileUploadForm"));
$("#fileUploadForm").click(function(){
   $("#uploaddiv").hide()

   $("#parentupload").append("<div class=\"col-lg-12 col-sm-6 col-12 uploaddivnew\"><span class=\"file-input btn btn-block btn-primary btn-file\"><h4><b>Processing&hellip;</b></h4></span></div>")
    $('#jinjaTable').hide();
    $('#tableWithServerData').hide();
   $(".textcont").remove();
   var county = $('#inputGroupSelect01 option:selected');
   var season = $('#inputGroupSelect02 option:selected');
   var abundance = $('#inputGroupSelect03 option:selected');
   var lifestage = $('#inputGroupSelect04 option:selected');
   var gender = $('#inputGroupSelect06 option:selected');
   var scientistname = $('#inputGroupSelect07 option:selected');
//   var selected = $('#my-dropdown option:selected');
   var dataTosend = {"county":county[0].text,"season":season[0].text,"abundance":abundance[0].text,"lifestage":lifestage[0].text,
   "gender":gender[0].text,"scientistname":scientistname[0].text};
//   var selected = $('#my-dropdown option:selected');
   $.ajax({
       url: window.location.pathname,
       type: 'POST',
       data: JSON.stringify(dataTosend),
       async: true,
       success: function (data) {
            parsedData = JSON.parse(data)
            var myTableDiv = document.getElementById("jinjaTable")
            var table = document.createElement('TABLE')
            var tableBody = document.createElement('TBODY')

            table.border = '1'
            table.appendChild(tableBody);

            var heading = parsedData.heading;
            var dataToFill = parsedData.rowValues;
            var tr = document.createElement('TR');
            tableBody.appendChild(tr);
            for (var i = 0; i < heading.length; i++) {
                var th = document.createElement('TH')
                th.width = '75';
                th.appendChild(document.createTextNode(heading[i]));
                tr.appendChild(th);

            }
            for (var i = 0; i < dataToFill.length; i++) {
                var tr = document.createElement('TR');
                for (var j = 0; j < dataToFill[i].length; j++) {
                    var td = document.createElement('TD')
                    td.appendChild(document.createTextNode(dataToFill[i][j]));
                    tr.appendChild(td)
                }
                tableBody.appendChild(tr);
            }
             myTableDiv.appendChild(table)
            $('.uploaddivnew').remove();
            $("#jinjaTable").show();
            $("#uploaddiv").show();
        },
        error:function(){
            alert("Error occured while processing the image. Please try again.");
            $('.uploaddivnew').remove();
            $("#uploaddiv").show();
            $("[name='"+firstImage+"']").click();
        },
       cache: false,
       contentType: false,
       processData: false
   });


   return false;
});
});

