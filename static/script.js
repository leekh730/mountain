$("#mtlist tr").click(function(){
    var str="" // 문자열 저장
    var tdArr = new Array(); // 배열 선언
    var tr = $(this); // 현재 클릭된 Row(<tr>)
    var td = tr.children(); //tr의 자식 노드는 td
    var lat = td.eq(4).text().split(',')[0]
    var lon = td.eq(4).text().split(',')[1]
    var latlon = lat+lon
    //var latlon = td.eq(4).text()
    console.log('위도 : '+lat ,'경도 :'+lon)
    console.log(latlon)
    location.href='../detail/'+latlon

    //console.log('클릭한 row의 데이터 : ' + tr.text()); //tr.text()는 클릭된 row에 있는 모든 값을 가져옴
    
    // 반복문을 이용해서 배열에 값을 담아 사용할 수 있음.
    td.each(function(i){
        tdArr.push(td.eq(i).text());
    });
