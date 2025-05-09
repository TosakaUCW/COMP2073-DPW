
$(function () {
	// 事件分发
	function emit(elem, type, callback) {
	    $(document).delegate(elem, type, function(e) {
	        callback.call(e.target, e);
	    })
	};
	/** 
	* @name 底部点击微信弹窗 
	* @import js/nwd_common.js 
	* @author lihe 
	* @revise time:2016-04-07 14:20 
	*/ 
	var $windowmask= $('.windowmask') 
	$footwx = $('.footWx'); 
	emit(".footwxPop", "click", footWxEvent) 
	emit(".wxclose", "click", wxcloseEvent) 
	function footWxEvent () { 
		$windowmask.show(); 
		$footwx.slideDown(); 
	} 
	function wxcloseEvent () { 
		$windowmask.hide(); 
		$footwx.slideUp(); 
	}

	//嘉财有道点击修改按钮
	$('.alt_jiacai_btn').click(function () {
		$('.alt_jiacai').slideDown();
	});
	$('.alt_close').click(function () {
		$('.alt_jiacai').slideUp();
	});
	// 确认提现
	$('.count_pop').click(function () {
		var w_pop3box = $('.cash_pop').width();
        var h_pop3box = $('.cash_pop').height();
        $('.cash_pop').css({
        	'margin-left':-(w_pop3box/2)+'px',
        	'margin-top':-(h_pop3box/2)+'px'
        });
		$('.cash_pop').slideDown();
		$('.mask').show();
	})
	//我要充值快捷支付通过银行卡号查找
	$('.find_bankCard').click(function () {
		var w_pop3box = $('.findBankCard_pop').width();
		var h_pop3box = $('.findBankCard_pop').height();
		$('.findBankCard_pop').css({
        	'margin-left':-(w_pop3box/2)+'px',
        	'margin-top':-(h_pop3box/2)+'px'
        });
		$('.findBankCard_pop').slideDown();
		$('.mask').show();
	});
	$('.find_bankCard2').click(function () {
		var w_pop3box = $('.findBankCard_pop').width();
		var h_pop3box = $('.findBankCard_pop').height();
		$('.findBankCard_pop').css({
        	'margin-left':-(w_pop3box/2)+'px',
        	'margin-top':-(h_pop3box/2)+'px'
        });
		$('.findBankCard_pop').slideDown();
		$('.mask').show();
		$('.addbank_pop2').hide();
	});
	// 我要充值更多银行
	$('.otherbank1').click(function () {
		var w_pop3box = $('.addbank_pop2').width();
		var h_pop3box = $('.addbank_pop2').height();
		$('.addbank_pop2').css({
        	'margin-left':-(w_pop3box/2)+'px',
        	'margin-top':-(h_pop3box/2)+'px'
        });
		$('.addbank_pop2').slideDown();
		$('.mask').show();
        
	});
	// 我要充值快捷支付添加银行卡
	$('.otherbank').click(function () {
		var w_pop3box = $('.addbank_pop1').width();
		var h_pop3box = $('.addbank_pop1').height();
		$('.addbank_pop1').css({
        	'margin-left':-(w_pop3box/2)+'px',
        	'margin-top':-(h_pop3box/2)+'px'
        });
		$('.addbank_pop1').slideDown();
		$('.mask').show();
        
	});
	// 我要提现添加银行卡
	$('.otherbank').click(function () {
		var w_pop3box = $('.addbank_pop').width();
		var h_pop3box = $('.addbank_pop').height();
		$('.addbank_pop').css({
        	'margin-left':-(w_pop3box/2)+'px',
        	'margin-top':-(h_pop3box/2)+'px'
        });
		$('.addbank_pop').slideDown();
		$('.mask').show();
        
	});
	//嘉财有道到期退出
	$('.due_out').click(function () {
		var w_pop3box = $('.jiacai_pop').width();
		var h_pop3box = $('.jiacai_pop').height();
		$('.jiacai_pop').css({
        	'margin-left':-(w_pop3box/2)+'px',
        	'margin-top':-(h_pop3box/2)+'px'
        });
		$('.jiacai_pop').slideDown();
		$('.mask').show();
	});
	// 小秘书立即预约弹窗
	$('.orderBtn').click(function () {
		$('.order_Pop ').slideDown();
		$('.mask').show();
	});
	// 点击立即预约里面的确定按钮
	$("#ordConfirm").click(function () {
		$('.ordAction').hide();
		$('.ordAlt').show();
	});
	// 点击修改预约按钮
	$('.orderAltbtn').click(function () {
		$('.order_AltPop').slideDown();
		$('.mask').show();
	});
	// 确认修改预约按钮
	$('#ordAltConfirm').click(function () {
		$('.ordSave').show();
		$('.ordAlt').hide();
	});
	// 保存修改预约按钮
	$('#ordSaveBtn').click(function () {
		$('.orderAlt_Pop').slideDown();
		$('.mask').show();
	});
	// 确认修改
	$('#isordAltConfirm').click(function () {
		$('.ordAction').hide();
		$('.ordAlt').hide();
		$('.ordSave').show();
	});
	// 保存后确认修改
	$('#isordConfirm').click(function () {
		$('.ordAction').hide();
		$('.ordAlt').show();
		$('.ordSave').hide();
	});
	// 取消预约
	$('.orderCancel').click(function () {
		$('.orderCancel_Pop').slideDown();
		$('.mask').show();
	});
	// 确认取消预约
	$('#ordAltConfirm').click(function () {
		$('.ordAlt').hide();
		$('.ordAction').show();
		$('#ordSaveBtn').hide();
	});
	// 关闭弹窗
	$('.popClose').click(function () {
		$(this).parent().parent('.popCon').slideUp();
		$('.mask').hide();
	});

	$('.btnclose').click(function () {
		$(this).parents('.popCon').slideUp();
		$('.mask').hide();
	})

	emit(".pop", "click", popEvent)//点击弹窗1
	emit(".popmax", "click", popmaxEvent)//点击弹窗2
	emit(".popmin", "click", pop3Event);//添加弹窗3
	emit(".popclose1", "click", popclose1Event);//点击关闭按钮 关闭弹窗
	emit(".popclose2", "click", popclose2Event);//点击关闭按钮 关闭弹窗
	emit(".popclose3", "click", popclose3Event);//点击关闭按钮 关闭弹窗
	emit(".conform_btn", "click", conformeEvent);//点击确认按钮 关闭弹窗
	emit(".conform_btn2", "click", conforme2Event);//点击确认按钮 关闭弹窗
	emit(".conform_btn3", "click", conforme3Event);//点击确认按钮 关闭弹窗
	emit(".cancel_btn", "click", cancelEvent);//点击取消按钮 关闭弹窗
	emit(".cancel_btn3", "click", cancel3Event);//点击取消按钮 关闭弹窗
	emit(".singlecheckbox","click", singlecheckEvent);//单选
	emit(".allcheck","click", allcheckEvent);//全选
	var isCreatePop = false;
	var isMaxCreatePop = false;
	function  popEvent () {
		if(!isCreatePop)
		{
			var oMask = $(document.createElement('div')),
			    oPop = $(document.createElement('div')),
			    oPoptop =$(document.createElement('div')),
			    oPoptitle = $(document.createElement('span')),
			    oClose = $(document.createElement('a')),
			    oPopcon = $(document.createElement('div')),
			    oPopconbox = $(document.createElement('div')),
			    oPopp = $(document.createElement('p')),
			    isDelbtn = $(document.createElement('div')),
			    conform_btn = $(document.createElement('a')),
			    cancel_btn = $(document.createElement('a'))
	        oMask.addClass('mask')
	        $("body").append(oMask);
	        oPop.addClass('popbox wid_w440 popminbox pop1');
	        oPoptop.addClass('topper clearfix');
	        oPoptitle.html("删除银行卡"); 
	        oPoptitle.addClass('fl fs_16 fc_3');
	        oClose.addClass('fr icon_user icon_user_bankclose popclose1');
	        oPopcon.addClass('middle');
	        oPopconbox.addClass('content pad_t30 pad_b30 pad_l30 pad_r30 txt_center');
	        isDelbtn.addClass('isDelbtn');
	        conform_btn.addClass('btn btn_36c btn_size100 conform_btn pad_t10 pad_b10');
	        cancel_btn.addClass('btn btn_bgfff btn_size100 cancel_btn mar_l20 pad_t10 pad_b10');
	        conform_btn.html('确认');
	        cancel_btn.html('取消');
	        oPop.append(oPoptop).append(oPopcon);
	        oPoptop.append(oPoptitle).append(oClose);
	        oPopcon.append(oPopconbox);
	        oPopconbox.append(oPopp).append(isDelbtn);
	        isDelbtn.append(conform_btn).append(cancel_btn);
	        oPopp.html('您确定要删除(6201********9527)此卡吗');
	        $("body").append(oPop);
	        var w_popminbox = $('.popminbox').width();
	        var h_popminbox = $('.popminbox').height();
	        $('.popminbox').css({
	        	'margin-left':-(w_popminbox/2)+'px',
	        	'margin-top':-(h_popminbox/2)+'px'
	        });
	        isCreatePop = true;
		}
		else
		{
			$('.mask').show();
			$('.pop1').show();
		}
		
	}
	function popmaxEvent () {
			var w_popmaxbox = $('.popmaxbox').width();
	        var h_popmaxbox = $('.popmaxbox').height();
	        $('.popmaxbox').css({
	        	'margin-left':-(w_popmaxbox/2)+'px',
	        	'margin-top':-(h_popmaxbox/2)+'px'
	        });
			isMaxCreatePop = true;
			$('.mask').show();
			$('.pop2').show();

	}
	function pop3Event () {
			var w_pop3box = $('.pop3').width();
	        var h_pop3box = $('.pop3').height();
	        $('.popmaxbox').css({
	        	'margin-left':-(w_pop3box/2)+'px',
	        	'margin-top':-(h_pop3box/2)+'px'
	        });
			isMaxCreatePop = true;
			$('.mask').show();
			$('.pop3').show();
	}
	// function popmaxEvent () {
	// 	var oMask = $(document.createElement('div')),
	// 		    oPopmax = $(document.createElement('div')),
	// 		    oPoptop =$(document.createElement('div')),
	// 		    oPoptitle = $(document.createElement('span')),
	// 		    oClose = $(document.createElement('a')),
	// 		    oPopcon = $(document.createElement('div')),
	// 		    oPopconbox = $(document.createElement('div'))
	//         oMask.addClass('mask')
	//         $("body").append(oMask);
	//         oPopmax.addClass('popboxmax wid_w624 popmaxbox');
	//         oPoptop.addClass('topper clearfix');
	//         oPoptitle.html("修改银行卡"); 
	//         oPoptitle.addClass('fl fs_16 fc_3');
	//         oClose.addClass('fr icon_user icon_user_bankclose popclose');
	//         oPopcon.addClass('middle');
	//         oPopconbox.addClass('content pad_t30 pad_b30 pad_l30 pad_r30 txt_center');
	//         oPopmax.append(oPoptop).append(oPopcon);
	//         oPoptop.append(oPoptitle).append(oClose);
	//         oPopcon.append(oPopconbox);
	//         $("body").append(oPopmax);
	// 		var html = "<div class='control-group mar_t20 mar_b20 clearfix'>"+"<label class='wid_w120 mar_r20 fc_3  fl label'>持卡人</label>"+"<div class='fl'>"+"<input type='text' class='input1 input_w260'  placeholder='saier' onfocus=''>"+"<div style='display:none'><i class='icon icon_nset'></i><span>请输入*******!</span></div>	"+"</div>"+"</div>";
	//         var html = "<div class='control-group mar_t20 mar_b20 clearfix'><label class='wid_w120 mar_r20 fc_3  fl label'>持卡人</label><div class='fl'><input type='text' class='input1 input_w260'  placeholder='saier' onfocus=''><div style='display:none'><i class='icon icon_nset'></i><span>请输入*******!</span></div></div></div>"+
	//         "<div class='control-group mar_t20 mar_b20 clearfix'><label class='wid_w120 mar_r20 fc_3  fl label'>银行卡号</label><div class='fl'><input type='text' class='input1 input_w260'  placeholder='saier' onfocus=''><div style='display:none'><i class='icon icon_nset'></i><span>请输入*******!</span></div></div></div>";
	//         $('.popboxmax .content').html(html);
	// }
	function popclose1Event () {
		$('.mask').hide()
		//var $pop = $(this).parents().find('.pop')
		$('.pop1').hide();
	}
	function popclose2Event () {
		$('.mask').hide()
		$('.pop2').hide();
	}
	function popclose3Event () {
		$('.mask').hide()
		$('.pop3').hide();
	}
	function conformeEvent () {
		$('.pop1').hide();
		$('.mask').hide()
	}
	function conforme2Event () {
		$('.pop2').hide();
		$('.mask').hide()
	}
	function conforme3Event () {
		$('.pop3').hide();
		$('.mask').hide()
	}
	function cancelEvent () {
		$('.pop1').hide();
		$('.mask').hide()
	}
	function cancel3Event () {
		$('.pop3').hide();
		$('.mask').hide()
	}
	emit(".singlecheckbox","click", singlecheckEvent);//复选框
	emit(".allcheck","click", allcheckEvent);//全选
	function singlecheckEvent () {
		$(".allcheck").attr("checked",$('.singlecheckbox').length == $("input[name='singleBox']:checked").length ? true : false);
		$('.allcheck').parent().addClass('icon_user_ncheck').removeClass('icon_user_ycheck');
		if($(this).is(':checked') == true)
		{
			$(this).parent().addClass('icon_user_ycheck').removeClass('icon_user_ncheck');
		}
		else
		{
			$(this).parent().addClass('icon_user_ncheck').removeClass('icon_user_ycheck');
		}
	}
	
	function allcheckEvent () {
		$('.singlecheckbox').attr("checked",this.checked);
		if($(this).is(':checked') == true){
			$(this).parent().addClass('icon_user_ycheck').removeClass('icon_user_ncheck');
			$('.singlecheckbox').parent().addClass('icon_user_ycheck').removeClass('icon_user_ncheck');
		}
		else
		{
			$(this).parent().addClass('icon_user_ncheck').removeClass('icon_user_ycheck');
			$('.singlecheckbox').parent().addClass('icon_user_ncheck').removeClass('icon_user_ycheck');
		}
		
	}
/*	function goTopEx(){
        function getScrollTop(){
                return document.documentElement.scrollTop?document.documentElement.scrollTop:document.body.scrollTop;
            }
        function setScrollTop(value){
                document.documentElement.scrollTop?document.documentElement.scrollTop=value:document.body.scrollTop=value;
            }
        window.onscroll=function(){
			getScrollTop()>0?obj.style.display="block":obj.style.display="none";
			var scrollTop=$(document).scrollTop();
			var wHeight=$(window).height();
						
		}
		var obj=document.getElementById("tbar");
        obj.onclick=function(){
            var goTop=setInterval(scrollMove,10);
            function scrollMove(){
                    setScrollTop(getScrollTop()/1.1);
                    if(getScrollTop()<1)clearInterval(goTop);
                }
        }
    }
	
	function toolbar(){
		var html = "<div class='floatbox01'>"+"<a href='http://www.niwodai.com/daikuan/jiekuan.html' rel='nofollow'  class='linka daikuan' target='_blank'>&nbsp;</a>"+"<a href='page230.html' rel='nofollow'  class='linka feedback' target='_blank'>&nbsp;</a>"+"<a id='onlineQQService' rel='nofollow'  class='linka onlineqq'>&nbsp</a>"+
		"<a href='#' rel='nofollow'  class='linka onlinewx' target='_blank'><i><em>&nbsp;</em>关注微信公众号“你我贷”。随时随地尊享一对一客服服务，您就是我们的VIP。</i></a>"+
		"<a href='javascript:;' rel='nofollow' class='back-top' rel='nofollow'  id='tbar' style='display:none; z-index:9999'><i></i></a></div>";
		$('body').append(html);
	}
	*/
	//在线客服
		/*toolbar();
		goTopEx();
		var newright = $("body").width()/2+605;
		$(".floatbox01").css({"left":newright,"bottom":"40px","position":"fixed"})
		*/
	//关闭弹框
	$(".icon_close").click(function(){
		$(".dailogCon").slideUp();
	})
	// 头部导航条鼠标浮动
	
	var navLi = $(".nwd_navCon li");
		navLi.hover(
			function(){
			if($(this).index()==1||$(this).index()==2||$(this).index()==3||$(this).index()==5){
				$(this).children('.investCon').addClass('investbox');
				$(this).find(".invest_list").stop(true).slideDown("fast");
			}
		},function(){
			if($(this).index()==1||$(this).index()==2||$(this).index()==3||$(this).index()==5){
				$(".invest_list").stop(true).slideUp("fast");
				$(this).children(".investCon").removeClass('investbox');
		}
		}
		);//导航菜单
		
		
	var loginNavLi = $(".nwd_navCon li .LedgerCon");
		loginNavLi.hover(
			function(){
				$(this).addClass("Ledgerbox");
				$(".Ledger_list").stop(true).slideDown();
			},function(){
				$(".Ledger_list").stop(true).slideUp();
				$(this).removeClass("Ledgerbox");
			}	
		);//我的账户
	
	// 用户头像身份验证鼠标浮动
	var safeMsg_span = $('.safeMsg .status');
	var idenyz = $('.safeMsg .idenyz');
	var phoneyz = $('.safeMsg .phoneyz');
	var bankyz = $('.safeMsg .bankyz');
	var mailyz = $('.safeMsg .mailyz');
	safeMsg_span.hover(function () {
		if($(this).index() == 0){
			$('.safeMsg .idenyz').show();
		};
		if($(this).index() == 1){
			$('.safeMsg .phoneyz').show();
		}
		if($(this).index() == 2){
			$('.safeMsg .bankyz').show();
		}
		if($(this).index() == 3){
			$('.safeMsg .mailyz').show();
		}
	},function(){
		if($(this).index() == 0){
			$('.safeMsg .idenyz').hide();
		};
		if($(this).index() == 1){
			$('.safeMsg .phoneyz').hide();
		}
		if($(this).index() == 2){
			$('.safeMsg .bankyz').hide();
		}
		if($(this).index() == 3){
			$('.safeMsg .mailyz').hide();
		}
	});
	idenyz.hover(function () {
			$('.safeMsg .idenyz').show();
	},function(){
			$('.safeMsg .idenyz').hide();
	});
	phoneyz.hover(function () {
			$('.safeMsg .phoneyz').show();
	},function(){
			$('.safeMsg .phoneyz').hide();
	});
	bankyz.hover(function () {
			$('.safeMsg .bankyz').show();
	},function(){
			$('.safeMsg .bankyz').hide();
	});
	mailyz.hover(function () {
			$('.safeMsg .mailyz').show();
	},function(){
			$('.safeMsg .mailyz').hide();
	});
	//日历
	$(function () {
		$(".ui-datepicker-calendar tr").each(function(){
			$(this).find("td:first").addClass('l_border');
		}) 
		$(".ui-datepicker-calendar tbody").find('tr:first').find('td:first').addClass('firstTd');
		$('.ui-datepicker-calendar tbody').find('tr:last').find('td').addClass('lastTd');
	})
	
})

// 底部
function showWechat() {
	// alert();
}

///***tab切换***///

$(".tab_title li").click(function(){
	$(this).addClass("curron").siblings().removeClass("curron");
	$(".tab_content .tab_box").eq($(this).index()).show().siblings().hide();
	oNum = $(this).index()
})
// 模拟plasepho
$(".bankmember .input").each(function(){
	var thisVal=$(this).val();
	if(thisVal!="")
    {
	   $(this).siblings("span").hide();
    }
	else
	{
	    $(this).siblings("span").show();
    }    
	$(this).focus(function(){
	 	$(this).siblings("span").hide();
	}).blur(function(){
		var val=$(this).val();
		if(val!="")
		{
			$(this).siblings("span").hide();
		}
		else
		{
			$(this).siblings("span").show();
		} 
	});
	
	// 我的积分弹窗
	
//弹框
var plusBankBg,showForm1,showForm;

 function showCon_0(){
 	plusBankBg=$('.plusBankBg');
 	showForm=$('.plusBank');
 	plusBankBg.show();
 	showForm.slideDown();
 }


function showCon_1(){
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank1');
	plusBankBg.show();
	showForm1.slideDown();
	if($('.inputFocus1').size()>0){
		$('.inputFocus1').focus();
	}
}
function showPop () {
	$('.plusBankBg').show();
	$('.pop1').slideDown();
	$('.box').show();
	$('.box2').hide();
	$('.next_out').show();
	$('.next_out2').hide();
	$('.nextli').addClass('next');
    $('.nextstp2').removeClass('step-3').addClass('step-2');

}
function showCon_2(){
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank2');
	plusBankBg.show();
	showForm1.slideDown();
}
function showCon_3(){  //微信专用弹层
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank2');
	plusBankBg.show();
	showForm1.slideDown();
}
function showCon_4(){ //全局实名认证专用
	plusBankBg=$('.plusBankBg');
	showForm1=$('.real-name');
	plusBankBg.show();
	showForm1.slideDown();
}

function showCon_5(){ //全局实名认证专用
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank5');
	plusBankBg.show();
	showForm1.slideDown();
}

function showCon_6(){ //全局实名认证专用
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank6');
	plusBankBg.show();
	showForm1.slideDown();
}

 function closeAll_0(){
 	plusBankBg=$('.plusBankBg');
 	showForm=$('.plusBank');
 	plusBankBg.hide();
 	showForm.slideUp();
 }

function closeAll_1(){
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank1');
	showForm=$('.plusBank');
	plusBankBg.hide();
	showForm1.slideUp();
	showForm.slideUp();
}
function closeAll_2(){
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank2');
	plusBankBg.hide();
	showForm1.slideUp();
}
function closeAll_5(){
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank5');
	plusBankBg.hide();
	showForm1.slideUp();
}

function closeAll_6(){
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank6');
	plusBankBg.hide();
	showForm1.slideUp();
}

function surebank(){
		$('#mybank').hide();
		$('.bankMegTab').show();
		$('#myotherbank').show();
		$('.new-shortcut-1 ul').empty();
		var newmybank=($('.new-shortcut-allbank li.selectli').html());
		var newbankshow= $('#newmyseceltbankshowa ul').append('<li class=selectli>'+newmybank+'</li><li class=otherbank><a href=#>选择其他银行</a></li>');
		closeAll_5();
		$('.input_bank').focus();
	}
function closeAll_3(){ //微信专用弹层
	plusBankBg=$('.plusBankBg');
	showForm1=$('.plusBank2');
	plusBankBg.hide();
	showForm1.slideUp();
}
function closeAll_4(){ //全局实名认证专用
	plusBankBg=$('.plusBankBg');
	showForm1=$('.real-name');
	plusBankBg.hide();
	showForm1.slideUp();
}
/*关闭弹出层背景*/

$(document).ready(function() {
	
	$(".c2 .i2").siblings('a').click(function(){
		$(".href").slideDown(400);
		$(".plusBankBg").show();
	})
	$(".c2 .i3").siblings('a').click(function(){
		$(".mail").slideDown(400);
		$(".plusBankBg").show();
	})
	$(".plus_c").click(function(){
		$(".plusBankBg").hide();
		$(".plusBank").slideUp(400);
		$('.pop1').slideUp();

	})
	
});
});

/************头像等比处理**********/
var Util = Util || {};
Util.scale = function (tx,maxWidth,maxHeight) {
	var maxWidth = maxWidth; 
	var maxHeight = maxHeight; 
	var zoomTimes; 
	tx.each(function () {	
		var curWidth = $(this).width(); 
		var curHeight = $(this).height();
		//console.log(curHeight);
		if (curWidth >maxWidth) { 
			$(this).width(maxWidth); 
			zoomTimes = curWidth / maxWidth; 
			$(this).height(curHeight / zoomTimes);
			var curH = curHeight / zoomTimes
			var curWid = $(this).width(maxWidth)
			$(this).css({
				'top':'50%',
				'margin-top':-curH/2+'px'
			});
		} else {
			if (curHeight > maxHeight) {
			$(this).height(maxHeight); 
			zoomTimes = curHeight / maxHeight; 
			$(this).width(curWidth / zoomTimes) 
			var curW = curWidth / zoomTimes
			$(this).css({
				'left':'50%',
				'margin-left':-curW/2+'px',
				
			});
		} 
		} 
	}); 

}
Util.scale($('.bigmytxPic'),94,94);
Util.scale($('.smallmytxPic'),42,42);

//---底部SEO用---------------
(function(){
	var O = $('.lunbo1'),
		H = _H = O.children('li').height(),
		N = O.children('li').length;
		for(var i = 0; i<N-1; i++){
			$(".lunbo1").animate({marginTop: '-'+_H+'px'}, 1000);
			_H = H+_H;
		}
})();
