/* BAEZ.AI.STUDIO — progressive enhancement only. Every page reads fully without JS. */
(function(){
  var d=document, root=d.documentElement;
  root.classList.add('js');
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* mobile nav */
  var hdr=d.querySelector('.site-header'), mb=d.querySelector('.menu-btn');
  if(mb&&hdr){mb.addEventListener('click',function(){
    var open=hdr.classList.toggle('nav-open');mb.setAttribute('aria-expanded',open);
  });}

  /* tabs: [data-tabs] wraps .tab buttons + .panel sections */
  d.querySelectorAll('[data-tabs]').forEach(function(box){
    var tabs=[].slice.call(box.querySelectorAll('.tab')), panels=tabs.map(function(t){return d.getElementById(t.getAttribute('aria-controls'))});
    function pick(i,focus){tabs.forEach(function(t,j){var on=i===j;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;if(panels[j])panels[j].hidden=!on;});if(focus)tabs[i].focus();}
    tabs.forEach(function(t,i){
      t.addEventListener('click',function(){pick(i)});
      t.addEventListener('keydown',function(e){
        if(e.key==='ArrowRight'){e.preventDefault();pick((i+1)%tabs.length,true)}
        if(e.key==='ArrowLeft'){e.preventDefault();pick((i-1+tabs.length)%tabs.length,true)}
      });
    });
    var start=Math.max(0,tabs.findIndex(function(t){return t.getAttribute('aria-selected')==='true'})), h=location.hash.slice(1);
    panels.forEach(function(p,j){if(p&&p.id===h)start=j});
    pick(start);
  });

  /* hero loop: respect reduced motion, pause offscreen */
  d.querySelectorAll('video[data-ambient]').forEach(function(v){
    if(reduce){v.removeAttribute('autoplay');v.pause();v.querySelectorAll('source').forEach(function(s){s.remove()});v.load();return;}
    if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var p=v.play();if(p&&p.catch)p.catch(function(){})}else v.pause()})}).observe(v);}
  });

  /* below-the-fold videos: preload=none + data-src, loaded on approach */
  var lazy=d.querySelectorAll('video[data-lazy]');
  if(lazy.length){
    var load=function(v){v.querySelectorAll('source[data-src]').forEach(function(s){s.src=s.dataset.src;s.removeAttribute('data-src')});v.load();if(!reduce&&v.hasAttribute('data-autoplay')){var p=v.play();if(p&&p.catch)p.catch(function(){})}};
    if('IntersectionObserver' in window){
      var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){load(e.target);io.unobserve(e.target)}})},{rootMargin:'300px'});
      lazy.forEach(function(v){io.observe(v)});
    } else lazy.forEach(load);
  }

  /* showreel modal: iframe only injected on click */
  var dlg=d.getElementById('reel');
  if(dlg&&dlg.showModal){
    var slot=dlg.querySelector('.ratio');
    d.querySelectorAll('[data-reel]').forEach(function(b){b.addEventListener('click',function(e){
      e.preventDefault();
      var t=b.getAttribute('data-t')||'';
      slot.innerHTML='<iframe src="'+dlg.dataset.embed+'&autoplay=1'+(t?'#t='+t+'s':'')+'" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Baez Studio showreel"></iframe>';
      dlg.showModal();
    })});
    var close=function(){slot.innerHTML='';if(dlg.open)dlg.close()};
    dlg.querySelector('[data-close]').addEventListener('click',close);
    dlg.addEventListener('click',function(e){if(e.target===dlg)close()});
    dlg.addEventListener('close',function(){slot.innerHTML=''});
  }

  /* work filters */
  var fbox=d.querySelector('[data-filters]');
  if(fbox){
    fbox.hidden=false;
    var items=d.querySelectorAll('[data-cat]');
    fbox.querySelectorAll('.filter').forEach(function(b){b.addEventListener('click',function(){
      fbox.querySelectorAll('.filter').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
      var c=b.dataset.f;items.forEach(function(it){it.hidden=!(c==='all'||it.dataset.cat.split(' ').indexOf(c)>-1)});
    })});
  }

  /* conditional brief form */
  d.querySelectorAll('form[data-brief]').forEach(function(f){
    var radios=f.querySelectorAll('input[name="service"]');
    function sync(){
      var v=(f.querySelector('input[name="service"]:checked')||{}).value||'';
      f.querySelectorAll('.cond').forEach(function(c){
        var show=c.dataset.for.split(' ').indexOf(v)>-1;
        c.hidden=!show;c.querySelectorAll('input,select,textarea').forEach(function(i){i.disabled=!show});
      });
    }
    radios.forEach(function(r){r.addEventListener('change',sync)});
    var pre=new URLSearchParams(location.search).get('service');
    if(pre){var r=f.querySelector('input[name="service"][value="'+pre+'"]');if(r)r.checked=true}
    sync();
  });
})();
