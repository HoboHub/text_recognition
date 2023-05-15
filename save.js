$(function(){
	$('.popupBubble').each(function(){
		// опции
		let distance = 10;
		let time = 250;
		let hideDelay = 500;
		
		let hideDelayTimer = null;
		
		// трэкер
		let beingShown = false;
		let shown = false;
		
		let trigger = $('.trigger', this);
		let popup = $('.popup', this).css('opacity',0);
		// 
		$("#copy_btn").click(function(){
			$(".result_textarea").select();
			document.execCommand('copy');

			if(hideDelayTimer) clearTimeout(hideDelayTimer);
			
			if(beingShown || shown) return;
			else{
				beingShown = true;
				
				popup.css({
					top:-75,
					left:-33,
					display:'block'
				})
				.animate({
					top: '-=' + distance + 'px',
					opacity:1
				},time,'swing',function(){
					beingShown = false;
					shown = true;
				});
			}

			// перезапуск таймера
			if(hideDelayTimer)clearTimeout(hideDelayTimer);

			hideDelayTimer = setTimeout(function(){
				hideDelayTimer = null;
				popup.animate({
					top: '-=' + distance + 'px',
					opacity: 0
				}, time, 'swing', function(){
					shown = false;
					// спрятать popup
					popup.css('display','none');
				});
			}, hideDelay);
		});
	});
});