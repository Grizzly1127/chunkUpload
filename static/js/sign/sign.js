/**
 * Created by lhx on 2017/12/20.
 */
function sign_in(){
    var username = document.getElementById('inputUser')
    var pwd = document.getElementById('inputPassword')
    $.ajax({
        //提交数据的类型 POST GET
        type:"POST",
        //提交的网址
        url:"http://127.0.0.1:8000/home/login",
        //提交的数据
        data:$("#sign-form").serialize(),
        //返回数据的格式
        datatype: "json",
        //成功返回之后调用的函数
        success:function(data){
            if(data.result){
                window.location.href = data.url;
            }
        },
        //调用出错执行的函数
        error: function(textStatus,a,b){
            //请求出错处理
            console.log("error");
            console.log(textStatus);
            console.log(a);
            console.log(b);
        }
    });
}