function get_minion_data(){
    $.ajax({
        type: "GET",
        url: "/salt/minion",
        //data: null,
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(msg){
           $("#minions_all").html(msg['keys_ok']);
           $("#minions_online").html(msg['online']);
           $("#minions_down").html(msg['offline']);
           $("#keys_ok").html(msg['keys_ok']);
           $("#keys_pre").html(msg['keys_pre']);
           $("#keys_rej").html(msg['keys_rej']);
        },
    error:function(){ 
          alert("提示：数据加载失败！");
        }
    });
       };
