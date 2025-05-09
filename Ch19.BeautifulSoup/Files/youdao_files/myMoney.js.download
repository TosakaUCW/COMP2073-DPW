/* @update: 2016-3-2 :01:11:11*/
var assetsMyMoney = {
};
assetsMyMoney.detailTab = function () {
    assetsCommon.ui_selectListBox(function (e) {
        $('.tab_content').find('.tab_box').hide().eq(e).show()
    }, 200);
    var e = $('.ui-select-listBox').find('.ui-select-listBox-list--now').index();

	if(e > 0){
		var len = $('.tab_content').find('.tab_box').length;
		if(len){			
			if(len > 1){
				
			}else if(len == 1){
				e =0;
			}
		}
	}

    $('.tab_content').find('.tab_box').hide().eq(e).show()
},
assetsMyMoney.init = function () {
    
    this.detailTab();
    
},
$(function () {
    assetsMyMoney.init();
    
});
