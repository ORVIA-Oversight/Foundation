/* ORVIA Estate Golden Master v1.0.0 */
(function(){
 if(typeof document==='undefined'||document.documentElement.dataset.orviaEstateV1==='1')return;
 document.documentElement.dataset.orviaEstateV1='1';
 const rewrites=[['foundation.orvia.org.uk','orviafoundation.org.uk']];
 document.querySelectorAll('a[href]').forEach(a=>{
   try{
     const u=new URL(a.href,location.href);
     rewrites.forEach(([oldHost,newHost])=>{if(u.hostname===oldHost){u.hostname=newHost;a.href=u.toString();}});
     if(u.hostname==='command.orvia.org.uk'||u.hostname==='workspace.orvia.org.uk')a.remove();
   }catch{}
 });
 const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT),nodes=[];
 while(walker.nextNode())nodes.push(walker.currentNode);
 nodes.forEach(n=>{
   let t=n.nodeValue||'';
   rewrites.forEach(([oldHost,newHost])=>{t=t.split(oldHost).join(newHost);});
   t=t.replace(/\s*[·|]\s*ICO\s*(?:Registration\s*)?ZC152311/gi,'').replace(/ICO\s*(?:Registration\s*)?ZC152311/gi,'');
   n.nodeValue=t;
 });
 const s=document.createElement('style');s.textContent=`
 .orvia-estate-v1{font-family:Arial,Helvetica,sans-serif;background:#0B2450;color:#fff;border-bottom:3px solid #EAAA00;position:relative;z-index:9999}
 .orvia-estate-v1__inner{max-width:1220px;margin:auto;padding:9px 20px;display:flex;gap:18px;align-items:center;flex-wrap:wrap;font-size:13px}
 .orvia-estate-v1 a{color:#fff;text-decoration:none;font-weight:700}.orvia-estate-v1__push{margin-left:auto;display:flex;gap:14px}
 .orvia-estate-v1__explore{border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:5px 10px}
 .orvia-legal-v1{font-family:Arial,Helvetica,sans-serif;border-top:1px solid rgba(11,36,80,.14);margin-top:18px;padding:18px 0 0;font-size:12px;line-height:1.55}
 .orvia-legal-v1__facts,.orvia-legal-v1__trust,.orvia-legal-v1__policies{display:flex;gap:10px 16px;flex-wrap:wrap;align-items:center}.orvia-legal-v1__trust,.orvia-legal-v1__policies{margin-top:8px}
 .orvia-accounts-v1{margin-top:10px;padding:10px 12px;border-left:4px solid #EAAA00;background:rgba(234,170,0,.08)}
 @media(max-width:720px){.orvia-estate-v1__push{margin-left:0;width:100%}}
 `;document.head.appendChild(s);
 const bar=document.createElement('div');bar.className='orvia-estate-v1';bar.innerHTML=`<div class="orvia-estate-v1__inner"><a href="https://orvia.org.uk"><strong>ORVIA</strong></a><span>ORVIA Foundation</span><div class="orvia-estate-v1__push"><a class="orvia-estate-v1__explore" href="https://orvia.org.uk/products">Explore ORVIA</a><a href="https://orviafoundation.org.uk">This product</a></div></div>`;document.body.insertBefore(bar,document.body.firstChild);
 const footer=document.querySelector('footer');if(footer&&!footer.querySelector('[data-orvia-legal-v1]')){
   const wrap=document.createElement('div');wrap.className='orvia-legal-v1';wrap.dataset.orviaLegalV1='1';
   wrap.innerHTML=`<div class="orvia-legal-v1__facts"><strong>ORVIA Oversight Ltd</strong><span>Company 16123685</span><span>Registered in England and Wales</span><span>3rd Floor, 86–90 Paul Street, London EC2A 4NE</span><a href="tel:03300433703">0330 043 3703</a><a href="mailto:hello@orvia.org.uk">hello@orvia.org.uk</a><a href="https://orvia.org.uk">orvia.org.uk</a></div><div class="orvia-legal-v1__trust"><a href="https://www.armedforcescovenant.gov.uk/" target="_blank" rel="noopener">Armed Forces Covenant</a><span>ERS Bronze</span><span>Veteran-founded</span><a href="https://www.trustaveteran.com/team/orvia" target="_blank" rel="noopener">Trust A Veteran</a></div><div class="orvia-accounts-v1"><strong>Accounts filing status:</strong> Our first accounts are overdue. We are aware of the delay and are currently reconciling and preparing the accounts for filing. This is being treated as a priority, and this notice will be updated once the filing has been completed.</div><div class="orvia-legal-v1__policies"><a href="https://orvia.org.uk/privacy">Privacy</a><a href="https://orvia.org.uk/terms">Terms</a><a href="https://orvia.org.uk/cookies">Cookies</a><a href="https://orvia.org.uk/accessibility">Accessibility</a></div>`;
   (footer.querySelector('.shell,.wrap')||footer).appendChild(wrap);
 }
})();