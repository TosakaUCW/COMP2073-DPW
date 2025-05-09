(function(window,$){
/***************永远的左右的滚动轮播组件 s***************/
function Playmoveimg(imgidz,options){
  var This=this;
  this.playcon=$("#"+imgidz);//总轮播的总父级
  this.playimg=this.playcon.find(".imglistcon");//包含切换元素的dom
  this.playimga=this.playimg.children();//需要用来切换的元素集合
  this.playlen=this.playimga.length;//需要切换的元素内容块数量
  this.showcon=[];
  this.nava=this.playcon.find(".imgnav");//导航
  this.nowid=0;//存储当前索引号
  this.timer=null;
  //默认参数
  this.setting={
    time:3000,//自动切换的时间间隙,如果设为0就是不支持自动切换
    sped:500,//切换速度
    direction:1,//默认是左右滚动,如查传入0即是上下滚动
    hclass:"active",//导航默认高亮样式
    lrbtn:true,//是否有左右切换按钮
    backfn:null//默认回调为空
  }
  this.setting=$.extend(this.setting,options)
  if(this.setting.lrbtn==true){//判断当前是否有左右按钮
    this.prebtn=this.playcon.find(".perbtn");
    this.nextbtn=this.playcon.find(".nextbtn");
  }
  for(var i=0;i<this.playlen;i++){
    this.showcon.push(this.playimga.eq(i).html());
  }
  if(this.setting.direction==1){
    this.everstep=this.playimga.eq(0).width();//每次走的步长值
  }else{
    this.everstep=this.playimga.eq(0).height();//每次走的步长值
  }
  this.initfn();//组件初始化
  this.adevent();//事件绑定
  this.autoplay();//自动轮播
}
//组件初始化
Playmoveimg.prototype.initfn=function() {
  var navstr = "",
      playstr = "";
  for (var i = 0; i < this.playlen; i++) {//根据要切换的内容块来自动生成导航
    i === 0 ? navstr += "<span class=" + this.setting.hclass + "></span>" : navstr += "<span></span>";
  }
  this.nava.html(navstr);
  playstr += "<li>" + this.showcon[0] + "</li>";
  playstr += "<li>" + this.showcon[1] + "</li>";
  this.playimg.html(playstr).css(this.setting.direction==1?"width":"height",this.everstep*2+"px");
  this.playimg.css(this.setting.direction==1?"height":"width","100%");
}

/*图片切换功能实现*/
//图片向左走功能实现
Playmoveimg.prototype.moveLfn=function(index){
  var This=this,
      oldindex=this.nowid,
      playimgch=This.playimg.children();
  if(index!=undefined){//如果有传入滚轮到某一个索引，就无需再执行加加运算
    this.nowid=index;
  }else{
    this.nowid++;
    if(this.nowid==this.playlen){
      this.nowid=0;
    }
  }
  if(this.playimg.css(this.setting.direction==1?"left":"top")===-this.everstep+"px"){//当向右切换到向左走的时候，要准备一下往左走的状态，也就是把初始的left由0改为负一个显示块的长度
    playimgch.eq(0).html(this.showcon[oldindex]);
    this.playimg.css(This.setting.direction==1?"left":"top",0);
    playimgch.eq(1).html(this.showcon[this.nowid]);
  }
  //滚播切换过程
  //滚播切换过程
  if(this.setting.direction==1){
    this.playimg.animate({"left":-this.everstep+"px"},this.setting.sped,function(){
      callback(This);
    })
  }else{
    this.playimg.animate({"top":-this.everstep+"px"},this.setting.sped,function(){
      callback(This);
    })
  }
  function callback(obj){
    var This=obj;
    playimgch.eq(0).html(This.showcon[This.nowid]);//把第一张与当前显示的相同
    This.playimg.css(This.setting.direction==1?"left":"top",0);//立即复位到0
    playimgch.eq(1).html(This.showcon[(This.nowid+1)==This.playlen?0:(This.nowid+1)]);//准备下一张要显示的
    This.hlnavFn(This.nowid);//高亮导航效果
    This.setting.backfn && This.setting.backfn(This.showcon,This.nowid);//执行回调，如果有传入回调
  }
}
//图片向右走功能实现
Playmoveimg.prototype.moveRfn=function(index){
  var This=this,
      oldindex=this.nowid,//存储未改变前的索引值
      playimgch=This.playimg.children();
  if(index!=undefined){//如果有传入滚轮到某一个索引，就无需再执行减减
    this.nowid=index;
  }else{
    this.nowid--;
    if(this.nowid<0){
      this.nowid=this.playlen-1;
    }
  }
  if(this.playimg.css(this.setting.direction==1?"left":"top")==="0px"){//当向左切换到向右走的时候，要准备一下往左走的状态，也就是把初始的left由0改为负一个显示块的长度
    playimgch.eq(1).html(this.showcon[oldindex]);
    this.playimg.css(This.setting.direction==1?"left":"top",-this.everstep+"px");
    playimgch.eq(0).html(this.showcon[this.nowid]);
  }
  //滚播切换过程
  if(this.setting.direction==1){
    this.playimg.animate({"left":0},this.setting.sped,function(){
      callback(This);
    })
  }else{
    this.playimg.animate({"top":0},this.setting.sped,function(){
      callback(This);
    })
  }
  function callback(obj){
    var This=obj;
        playimgch.eq(1).html(This.showcon[This.nowid]);//把第二块内容显示与当前的相同
    This.playimg.css(This.setting.direction==1?"left":"top",-This.everstep+"px");//并强行把二块图片设置为当前显示块
    playimgch.eq(0).html(This.showcon[(This.nowid-1)<0?(This.playlen-1):(This.nowid-1)]);//准备下一张要显示的
    This.hlnavFn(This.nowid);
    This.setting.backfn && This.setting.backfn(This.showcon,This.nowid);//执行回调，如果有传入回调
  }
}
//手动切换功能实现
Playmoveimg.prototype.adevent=function(){
  var This=this;
  if(this.prebtn){//上一张
    this.prebtn.on("click",function(){
      This.moveRfn();
    })
  }
  if(this.nextbtn){//下一张
    this.nextbtn.on("click",function(){
      This.moveLfn();
    })
  }
  this.nava.children().on("click",function(){
    var thisindex=$(this).index();
    if(This.nowid==thisindex){
      return;
    }else if(This.nowid>thisindex){
      This.moveRfn(thisindex);
    }else{
      This.moveLfn(thisindex);
    }
  })
  
}

window.Playmoveimg=Playmoveimg;
/***************永远的左右的滚动轮播组件 e***************/

/***************一进无缝滚动组件 s***************/
function Playimgone(imgidz,options){
  this.playo=$("#"+imgidz);
  this.playovero=this.playo.find(".play-list-con");
  this.playoverw=this.playovero.width();
  this.listcon=this.playovero.children();
  this.playlen=this.listcon.children().length;
  this.playw=this.listcon.children().outerWidth();
  this.playing=true;
  this.navo=null;
  this.lrbtna=null;
  this.timer=null;//定时器
  this.nowid=0;//当前在哪一张
  //默认参数
  this.setting={
    time:3000,//自动切换的时间间隙,如果设为0就是不支持自动切换
    sped:500,//切换速度
    navo:".imgnav",//导航默认样式
    hclass:"active",//导航默认高亮样式
    lrbtn:".actbtn",//是否有左右切换按钮
    golen:0,//初始步长
    backfn:null//默认回调为空
  }
  this.setting=$.extend(this.setting,options);
  if(this.setting.lrbtn!=""){//是否有左右切换按钮
    this.lrbtna=this.playo.find(this.setting.lrbtn)
  }
  this.initfn();//初始化
  this.adevent();
  if(this.setting.time!=0){
    this.autoplay();
  }
}
Playimgone.prototype.initfn=function(){
  var navstr = "",//导航html
      playstr = "",//播放块内容html
      This=this;
  //如果有导航，动态生成导航
  if(this.setting.navo!==""){
    this.nava=this.playo.find(this.setting.navo);
    for (var i = 0; i < this.playlen; i++) {//根据要切换的内容块来自动生成导航
      i === 0 ? navstr += "<span class=" + this.setting.hclass + "></span>" : navstr += "<span></span>";
    }
    this.nava.html(navstr);
  }
  //生成播放块内容
  this.playw=this.setting.golen==0?this.playw:this.setting.golen;
  this.listcon.css({"width":this.playlen*this.playw*2+"px"});//动态设置播放列表的宽度
  playstr=this.listcon.html();
  this.listcon.html(playstr+playstr);
}
//事件绑定
Playimgone.prototype.adevent=function(){
  var This=this;
  if(this.lrbtna!=null){
    this.lrbtna.eq(0).on("click",function(){
      if(This.nowid==0){
        This.nowid=-(This.playlen);
      }
      This.nowid++;
      This.playmoveper();
    })
    this.lrbtna.eq(1).on("click",function(){
      if(This.playing){
        This.playing=false;
        This.nowid--;
        This.playmovenext();
      }
    })
  }
  
  
}
//下一张播放函数
Playimgone.prototype.playmovenext=function(){
  var This=this;
  this.listcon.stop().animate({"left":this.nowid*this.playw+"px"},this.setting.sped,function(){
    This.playing=true;
    if(Math.abs(This.nowid)==This.playlen){
      This.nowid=0;
      This.listcon.css("left",0);
    }
  });
}
//上一张播放函数
Playimgone.prototype.playmoveper=function(){
  var This=this;
  if(Math.abs(This.nowid)==This.playlen-1){
      This.listcon.css("left","-"+this.playw*this.playlen+"px");
    }
  this.listcon.stop().animate({"left":this.nowid*this.playw+"px"},this.setting.sped,function(){
    This.playing=true;
    if(This.nowid==0){
      This.listcon.css("left","-"+this.playw*this.playlen+"px");
    }
  });
}
window.Playimgone=Playimgone;
/***************一进无缝滚动组件 e***************/
function objectfn(o){
  var F = function(){}
  F.prototype = o;
  return new F();
}
})(window,$)