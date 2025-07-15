$('h1').each(function(){
            
            var p = $(this),
                spans = $('<span>' + p.text().split('').join('</span><span>') + '</span>'),
                originalContent = p.html();
                
            p.height(p.height()).html(spans);
            
            var spanDimensions = $.map(spans, function(span){
                return $(span).position();
            });
            
            spans.css({
                position: 'absolute',
                top: -(p.offset().top + 100)
            });
            
            p.css('visibility', 'visible');
            
            setTimeout(function(){
                
                
                
                spans.each(function(i, span){
                    
                    $(span).css('left', Math.random() * p.width());
                    
                    setTimeout(function(){
                        $(span).animate(spanDimensions[i], 400, !spans[i+1] && function(){
                            p.html(originalContent);    
                        });
                    }, i * 50)
                    
                });
                
            }, 500);

            
        });
            