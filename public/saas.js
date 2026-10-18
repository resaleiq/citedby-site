/* CitedBy SaaS views (RES-1497). Hash router; all dynamic text via textContent. Data from API (CONTRACT.md) or sample with ?demo=1. */
(function(){
const Q=new URLSearchParams(location.search),DEMO=Q.get("demo")==="1"||!!window.CB_FORCE_DEMO,S=window.CB_SAMPLE,root=document.getElementById("root");
const NS="http://www.w3.org/2000/svg";
const h=(t,a,...k)=>{const e=document.createElement(t);for(const x in a||{}){if(x==="class")e.className=a[x];else if(x.startsWith("on"))e.addEventListener(x.slice(2),a[x]);else if(a[x]!=null)e.setAttribute(x,a[x])}k.flat().forEach(c=>c!=null&&e.append(c.nodeType?c:document.createTextNode(c)));return e};
const sv=(t,a,...k)=>{const e=document.createElementNS(NS,t);for(const x in a||{})e.setAttribute(x,a[x]);k.forEach(c=>e.append(c));return e};
const tone=s=>s>=75?"pass":s>=40?"warn":"fail";
const LADDER=[[97,"A+"],[93,"A"],[90,"A-"],[87,"B+"],[83,"B"],[80,"B-"],[77,"C+"],[73,"C"],[70,"C-"],[60,"D"],[0,"F"]],grade=s=>LADDER.find(x=>s>=x[0])[1];
const SEVL={high:"High",medium:"Medium",low:"Low",pass:"Pass",unknown:"Not measured"};
const ICON={high:"M6 1l5.5 10h-11z",medium:"M1 1h10v10H1z",low:"M6 6m-5 0a5 5 0 1010 0a5 5 0 10-10 0",pass:"M1 6l3.5 3.5L11 2.5",unknown:"M2 6h8"};
const sev=k=>{const i=sv("svg",{viewBox:"0 0 12 12","aria-hidden":"true"},sv("path",k==="pass"?{d:ICON.pass,fill:"none",stroke:"currentColor","stroke-width":2}:k==="unknown"?{d:ICON.unknown,stroke:"currentColor","stroke-width":2}:{d:ICON[k],fill:"currentColor"}));return h("span",{class:"sev "+k},i,SEVL[k])};
function ring(score,size,label){const R=52,C=2*Math.PI*R,s=score==null?0:score;const w=h("div",{class:"ring "+tone(s),style:"--s:"+size+"px",role:"img","aria-label":"Score "+s+" out of 100, grade "+grade(s)});
 w.append(sv("svg",{viewBox:"0 0 120 120"},sv("circle",{class:"t",cx:60,cy:60,r:R,"stroke-width":size>100?12:14}),sv("circle",{class:"v",cx:60,cy:60,r:R,"stroke-width":size>100?12:14,"stroke-dasharray":(C*s/100)+" "+C})));
 const b=h("b",null,grade(s));if(size>100)b.append(h("small",null,s+" / 100"));else b.style.fontSize=Math.round(size*.36)+"px";w.append(b);return w}
const api=async p=>{if(DEMO){await new Promise(r=>setTimeout(r,120));return demo(p)}const r=await fetch("/api"+p,{credentials:"same-origin"});if(!r.ok){const e=new Error("http "+r.status);e.status=r.status;throw e}return r.json()};
function demo(p){const u=new URL(p,"http://x"),q=u.searchParams,path=u.pathname;
 if(path==="/projects")return{projects:S.projects};
 if(/^\/audits\/[^/]+$/.test(path)){if(path.endsWith("/fail"))throw Object.assign(new Error("x"),{status:422});return S.audit}
 if(path.endsWith("/pages")){let r=S.pages.slice();const sv=q.get("sev"),c=q.get("cat"),s=(q.get("q")||"").toLowerCase();
  if(sv)r=r.filter(p=>p[sv]>0);if(c)r=r.filter(p=>p.checks.some(k=>k.category===c&&k.status==="fail"));if(s)r=r.filter(p=>p.path.includes(s));
  const by=q.get("sort")||"score",d=q.get("dir")==="desc"?-1:1;r.sort((a,b)=>(a[by]>b[by]?1:a[by]<b[by]?-1:0)*d);const off=+q.get("off")||0;return{total:r.length,rows:r.slice(off,off+10).map(({checks,...x})=>x)}}
 if(path.endsWith("/page")){const x=S.pages.find(p=>p.url===q.get("url"));if(!x)throw Object.assign(new Error("x"),{status:404});return x}
 throw Object.assign(new Error("x"),{status:404})}
const ROUTE=()=>location.hash.replace(/^#/,"")||"/";
const go=p=>{location.hash=p};
const qs=o=>Object.entries(o).filter(([,v])=>v!==""&&v!=null).map(([k,v])=>k+"="+encodeURIComponent(v)).join("&");
let ME=null;fetch("/api/me",{credentials:"same-origin"}).then(r=>r.json()).then(m=>{ME=m;document.querySelectorAll(".acct").forEach(fillAcct)}).catch(()=>{});
const PN={single:"Single audit",starter:"Starter",pro:"Pro",agency:"Agency"};
function fillAcct(el){el.textContent="";if(DEMO){el.textContent="Sample data";return}if(!ME)return;
 if(!ME.signed_in){el.append(h("a",{href:"/signin?next="+encodeURIComponent("/app.html")},"Sign in"));return}
 el.append(h("span",{class:"mut small"},ME.email+(ME.plan?" · "+PN[ME.plan]:"")+" "),h("a",{href:"/plans"},"Plans")," ",ME.plan&&ME.plan!=="single"?h("a",{href:"#",onclick:e=>{e.preventDefault();fetch("/api/portal",{method:"POST",credentials:"same-origin",headers:{"Content-Type":"application/json"},body:"{}"}).then(r=>r.json()).then(j=>{if(j.url)location.href=j.url})}},"Billing"):null," ",h("a",{href:"/logout"},"Sign out"))}
function acctBox(){const e=h("span",{class:"acct"});fillAcct(e);return e}
function shell(cur,...content){root.textContent="";const brand=Q.get("brand");
 const nav=h("nav",{"aria-label":"Main"},...[["/","Projects"],["/new","New audit"]].concat(DEMO?[["/states","States"]]:[]).map(([p,l])=>h("a",{href:"#"+p,"aria-current":cur===p?"page":null},l)));
 root.append(h("header",{class:"topbar noprint"},h("div",{class:"in"},h("a",{class:"mark",href:"#/"},h("i"),"CitedBy"),nav,acctBox())),h("main",{class:"page",id:"main"},...content))}
function tabs(id,cur){return h("nav",{class:"tabs","aria-label":"Report"},...[["","Overview"],["/pages","Pages"],["/pdf","PDF report"]].map(([p,l])=>h("a",{href:"#/p/"+id+p,"aria-current":cur===p?"page":null},l)))}
function loading(){shell("/",h("div",{class:"panel","aria-busy":"true","aria-label":"Loading"},h("div",{class:"sk",style:"height:28px;width:40%"}),h("div",{class:"sk",style:"height:150px;margin:18px 0"}),h("div",{class:"sk",style:"height:16px;width:80%"})))}
function errState(title,msg,retry){shell("/",h("div",{class:"panel"},h("div",{class:"state err",role:"alert"},h("div",{class:"ico","aria-hidden":"true"},"!"),h("h2",null,title),h("p",null,msg),h("div",null,retry&&h("button",{class:"btn go",onclick:retry},"Try again")," ",h("a",{class:"btn",href:"#/"},"Back to projects")))))}
async function guard(fn){loading();try{await fn()}catch(e){if(e.status===401&&!DEMO){location.href="/signin?next="+encodeURIComponent(location.pathname+location.search+location.hash);return}errState(e.status===401?"Sign in to see this":e.status===404?"We can't find that":"We couldn't load this",e.status===401?"Your session ended. Sign in again to continue.":e.status===404?"The audit or page was removed, or the link is wrong.":"Nothing was lost. Check your connection and try again.",()=>render())}}
/* views */
async function projects(){const d=await api("/projects");if(!d.projects.length)return shell("/",h("div",{class:"panel"},h("div",{class:"state"},h("div",{class:"ico","aria-hidden":"true"},"+"),h("h2",null,"Audit your first site"),h("p",null,"Enter a URL. We crawl every page, analyse it and give you the exact fix for each issue."),h("a",{class:"btn go",href:"#/new"},"Start an audit"))));
 shell("/",h("div",{class:"head"},h("div",null,h("h1",null,"Projects"),h("p",null,d.projects.length+" sites, latest audit each")),h("a",{class:"btn go",href:"#/new"},"New audit")),
  h("div",{class:"panel flush"},...d.projects.map(p=>h("a",{class:"proj",href:"#/p/"+p.id},ring(p.score,56),h("span",{class:"hn"},p.host,p.sample?h("span",{class:"mut small"}," (sample)"):null),
   h("span",{class:"meta"},h("span",null,p.pages+" pages"),sev("high"),h("span",{class:"num"},p.high),sev("medium"),h("span",{class:"num"},p.medium),h("span",null,"Last audit "+p.last),trendSpark(p.trend))))))}
function trendSpark(t){const w=64,hh=20,mx=Math.max(...t,1),mn=Math.min(...t),pts=t.map((v,i)=>[i*w/(t.length-1||1),hh-2-(v-mn)/((mx-mn)||1)*(hh-4)]);return sv("svg",{width:w,height:hh,viewBox:`0 0 ${w} ${hh}`,role:"img","aria-label":"Score trend "+t.join(", ")},sv("polyline",{points:pts.map(p=>p.join(",")).join(" "),fill:"none",stroke:"#0F1B2D","stroke-width":2}))}
function trendChart(hist){const W=900,H=170,p=32,xs=i=>p+i*(W-2*p)/((hist.length-1)||1),ys=v=>H-p-(v/100)*(H-2*p);const s=sv("svg",{class:"trend",viewBox:`0 0 ${W} ${H}`,role:"img","aria-label":"Score by audit: "+hist.map(x=>x.d+" "+x.s).join(", ")});
 [0,50,100].forEach(v=>{s.append(sv("line",{x1:p,x2:W-p,y1:ys(v),y2:ys(v),stroke:"#E1E6ED"}));const t=sv("text",{x:0,y:ys(v)+4});t.textContent=v;s.append(t)});
 s.append(sv("polyline",{points:hist.map((x,i)=>xs(i)+","+ys(x.s)).join(" "),fill:"none",stroke:"#0F1B2D","stroke-width":3}));
 hist.forEach((x,i)=>{s.append(sv("circle",{cx:xs(i),cy:ys(x.s),r:5,fill:"#fff",stroke:"#0F1B2D","stroke-width":3}));const t=sv("text",{x:xs(i),y:H-6,"text-anchor":"middle"});t.textContent=x.d+" · "+x.s;s.append(t)});return s}
async function overview(id){const a=await api("/audits/"+id);if(a.status!=="done")return go("/crawl/"+id);const mx=Math.max(a.issues.high,a.issues.medium,a.issues.low,1),prev=a.history.length>1?a.history[a.history.length-2].s:null,dl=prev!=null?a.score-prev:null;
 shell("/",h("p",{class:"crumb"},h("a",{href:"#/"},"Projects")," / ",a.host),
  h("div",{class:"head"},h("div",null,h("h1",null,a.host,a.sample?h("span",{class:"mut small"}," (sample report)"):null),h("p",null,"Audited "+a.date+" · "+a.pages+" pages")),h("div",null,h("button",{class:"btn",onclick:()=>go("/new?host="+a.host)},"Re-crawl")," ",h("button",{class:"btn go",onclick:()=>go("/p/"+id+"/pages?sev=high")},"See the fixes"))),tabs(id,""),
  h("div",{class:"grid g21"},
   h("div",{class:"panel"},h("div",{class:"hero"},ring(a.score,176),h("div",{class:"stats"},
     h("div",{class:"stat"},h("b",{class:"num"},a.score,dl!=null?h("span",{class:"delta "+(dl>=0?"up":"down")},(dl>=0?"+":"")+dl+" since last"):null),h("span",null,"AI-readiness score")),
     h("div",{class:"stat"},h("b",{class:"num"},a.pages),h("span",null,"Pages checked")),
     h("div",{class:"stat"},h("b",{class:"num"},a.issues.high),h("span",null,"High issues")),
     h("div",{class:"stat"},h("b",{class:"num"},a.fixes.length),h("span",null,"Fixes to make first"))))),
   h("div",{class:"panel"},h("h2",null,"Issues by severity"),...["high","medium","low"].map(k=>h("a",{class:"sevrow",href:"#/p/"+id+"/pages?sev="+k,style:"text-decoration:none;color:inherit"},sev(k),h("div",{class:"bar "+k,"aria-hidden":"true"},h("i",{style:"width:"+a.issues[k]/mx*100+"%"})),h("b",{class:"num"},a.issues[k]))),h("p",{class:"mut small",style:"margin:10px 0 0"},"Counts are issues across all pages."))),
  h("div",{class:"grid g2",style:"margin-top:16px"},
   h("div",{class:"panel"},h("h2",null,"Top fixes"),...a.fixes.map(f=>h("div",{class:"fix"},sev(f.severity),h("a",{class:"tt",href:"#/p/"+id+"/pages?"+qs({sev:f.severity,cat:f.category})},f.title),h("span",{class:"num small"},f.pages+" pages"),h("span",{class:"sub"},"Claude's fix is on each page.")))),
   h("div",{class:"panel"},h("h2",null,"Category scores"),...a.categories.map(c=>h("a",{class:"cat",href:"#/p/"+id+"/pages?cat="+c.key,style:"text-decoration:none;color:inherit"},ring(c.score,56),h("span",{class:"nm"},c.label),h("span",{class:"ct"},c.issues+(c.issues===1?" check failing":" checks failing")),h("span",{class:"arrow","aria-hidden":"true"},"›"))))),
  h("div",{class:"panel",style:"margin-top:16px"},h("h2",null,"Score over time"),trendChart(a.history),h("p",{class:"mut small",style:"margin:6px 0 0"},"One point per audit. A re-crawl adds a point.")))}
async function pages(id){const P=new URLSearchParams(ROUTE().split("?")[1]||""),f={sev:P.get("sev")||"",cat:P.get("cat")||"",q:P.get("q")||"",sort:P.get("sort")||"score",dir:P.get("dir")||"asc",off:+P.get("off")||0};
 const d=await api("/audits/"+id+"/pages?"+qs(f)),set=o=>go("/p/"+id+"/pages?"+qs({...f,off:0,...o}));
 const sel=(k,opts)=>{const s=h("select",{class:"fld","aria-label":k==="sev"?"Severity":"Category",onchange:e=>set({[k]:e.target.value})},...opts.map(([v,l])=>h("option",{value:v,selected:f[k]===v?"":null},l)));return s};
 const th=(k,l)=>h("th",{"aria-sort":f.sort===k?(f.dir==="asc"?"ascending":"descending"):"none"},h("button",{onclick:()=>set({sort:k,dir:f.sort===k&&f.dir==="asc"?"desc":"asc"})},l+(f.sort===k?(f.dir==="asc"?" ↑":" ↓"):"")));
 const rows=d.rows.length?d.rows.map(p=>h("tr",null,h("td",{class:"url"},h("a",{href:"#/p/"+id+"/page?u="+encodeURIComponent(p.url),title:p.url},p.path)),h("td",{"data-l":"Score"},h("span",{class:"sc "+tone(p.score)},p.score)),
   h("td",{"data-l":"High"},p.high?h("span",{class:"sev high"},sev("high").lastChild.textContent==="High"?"":"",p.high):"–"),h("td",{"data-l":"Medium"},p.medium?h("span",{class:"sev medium"},p.medium):"–"),h("td",{"data-l":"Low"},p.low?h("span",{class:"sev low"},p.low):"–"),h("td",{"data-l":"Words",class:"num"},p.words))):[h("tr",null,h("td",{colspan:6},h("div",{class:"state"},h("div",{class:"ico","aria-hidden":"true"},"0"),h("h2",null,"No pages match"),h("p",null,"Remove a filter to see more pages."),h("button",{class:"btn",onclick:()=>go("/p/"+id+"/pages")},"Clear filters"))))];
 shell("/",h("p",{class:"crumb"},h("a",{href:"#/"},"Projects")," / ",h("a",{href:"#/p/"+id},"Report")," / Pages"),h("div",{class:"head"},h("h1",null,"Pages"),h("p",null,d.total+" pages")),tabs(id,"/pages"),
  h("div",{class:"panel flush"},h("div",{class:"filters"},h("input",{class:"fld",type:"search","aria-label":"Search by path",placeholder:"Search path",value:f.q,onkeydown:e=>{if(e.key==="Enter")set({q:e.target.value})}}),sel("sev",[["","All severities"],["high","Has High"],["medium","Has Medium"],["low","Has Low"]]),sel("cat",[["","All categories"],["crawl","AI crawlability"],["schema","Structured data"],["answer","Answerability"],["content","Content depth"],["tech","Technical health"]])),
   h("table",{class:"t"},h("thead",null,h("tr",null,th("path","Page"),th("score","Score"),th("high","High"),th("medium","Medium"),th("low","Low"),th("words","Words"))),h("tbody",null,...rows)),
   h("div",{class:"pager"},h("span",{class:"mut small"},d.total?(f.off+1)+" to "+Math.min(f.off+d.rows.length,d.total)+" of "+d.total:""),h("span",null,h("button",{class:"btn sm",disabled:f.off?null:"",onclick:()=>set({off:Math.max(0,f.off-10)})},"Previous")," ",h("button",{class:"btn sm",disabled:f.off+10<d.total?null:"",onclick:()=>set({off:f.off+10})},"Next"))))) }
const copyBtn=txt=>{const b=h("button",{class:"btn sm",type:"button"},"Copy");b.onclick=async()=>{try{await navigator.clipboard.writeText(txt);b.textContent="Copied"}catch(e){b.textContent="Select and copy"}setTimeout(()=>b.textContent="Copy",1800)};return b};
async function pageDetail(id){const u=new URLSearchParams(ROUTE().split("?")[1]||"").get("u"),p=await api("/audits/"+id+"/page?url="+encodeURIComponent(u));
 const fails=p.checks.filter(c=>c.status==="fail").sort((a,b)=>"highmediumlow".indexOf(a.severity)-"highmediumlow".indexOf(b.severity)),oks=p.checks.filter(c=>c.status!=="fail");
 const row=(c,open)=>{const d=h("details",{class:"chk",open:open?"":null},h("summary",null,sev(c.status==="fail"?c.severity:c.status==="unknown"?"unknown":"pass"),h("span",{class:"cn"},c.label,h("span",{class:"cc"},c.found)),h("span",{class:"mut small"},{crawl:"Crawlability",schema:"Structured data",answer:"Answerability",content:"Content",tech:"Technical"}[c.category])));
  const b=h("div",{class:"body"});if(c.fix){const cl=h("div",{class:"fixbox"},h("h4",null,"Recommended fix"),h("p",null,c.fix));if(c.code)cl.append(h("div",{class:"code"},h("pre",null,c.code),copyBtn(c.code)));b.append(cl)}else b.append(h("p",{class:"mut",style:"margin:0"},"Nothing to change."));d.append(b);return d};
 shell("/",h("p",{class:"crumb"},h("a",{href:"#/"},"Projects")," / ",h("a",{href:"#/p/"+id},"Report")," / ",h("a",{href:"#/p/"+id+"/pages"},"Pages")),h("div",{class:"head"},h("div",null,h("h1",{style:"word-break:break-all;font-size:clamp(22px,3vw,30px)"},p.path),h("p",null,h("a",{href:p.url,rel:"noopener"},p.url))),h("div",{style:"display:flex;gap:16px;align-items:center"},ring(p.score,72),h("button",{class:"btn go",onclick:()=>copyAll(fails)},"Copy all fixes"))),
  h("div",{class:"panel flush"},h("div",{class:"ph"},h("h2",null,fails.length+" to fix")),...fails.map((c,i)=>row(c,i===0))),h("div",{class:"panel flush",style:"margin-top:16px"},h("div",{class:"ph"},h("h2",null,oks.length+" passing")),...oks.map(c=>row(c,false))))}
function copyAll(fs){const t=fs.map(c=>"## "+c.label+"\n"+c.fix+(c.code?"\n\n"+c.code:"")).join("\n\n");navigator.clipboard&&navigator.clipboard.writeText(t)}
/* progress: polls /audits/<id> in real mode; animates the sample in demo */
function crawl(id){let st=DEMO?{status:"crawling",found:0,crawled:0,checked:0,judged:0,total:24,cur:"/"}:null;const feed=h("ul",{class:"feed","aria-label":"Pages as they are checked"}),meter=h("i"),nums={};
 const box=(k,l)=>{nums[k]=h("b",{class:"num"},"0");return h("div",{class:"panel"},nums[k],h("span",null,l))};
 const stages=h("ol",{class:"stages"}),SG=["Find pages","Fetch","Check","Analyse","Report"];
 const paint=s=>{["found","crawled","checked","judged"].forEach(k=>nums[k].textContent=s[k]);meter.style.width=Math.min(100,s.judged/Math.max(s.total,1)*100)+"%";const ix=s.status==="done"?5:s.crawled<s.total?(s.found<s.total?0:1):s.checked<s.total?2:3;stages.textContent="";SG.forEach((l,i)=>stages.append(h("li",{class:i<ix?"done":i===ix?"now":"","aria-current":i===ix?"step":null},l)));
  if(s.cur&&(!feed.firstChild||feed.firstChild.firstChild.textContent!==s.cur))feed.prepend(h("li",null,h("span",null,s.cur),h("span",null,s.status==="done"?"done":"checked")));return s};
 const host=Q.get("host")||"example-roaster.be";
 shell("/new",h("div",{class:"head"},h("div",null,h("h1",null,"Auditing "+host),h("p",null,"You can leave this page. We email you when the report is ready.")),h("a",{class:"btn noprint",href:"#/"},"Back to projects")),stages,
  h("div",{class:"counters",role:"status","aria-live":"polite"},box("found","Pages found"),box("crawled","Pages fetched"),box("checked","Pages checked"),box("judged","Pages analysed")),h("div",{class:"meter",role:"progressbar","aria-label":"Audit progress","aria-valuemin":0,"aria-valuemax":100},meter),
  h("div",{class:"panel flush",style:"margin-top:20px"},h("div",{class:"ph"},h("h2",null,"Live feed")),feed));
 const tick=async()=>{if(ROUTE()!=="/crawl/"+id)return;if(DEMO){const P=window.CB_SAMPLE.pages;st.found=Math.min(st.total,st.found+4);st.crawled=Math.min(st.found,st.crawled+3);st.checked=Math.min(st.crawled,st.checked+2);st.judged=Math.min(st.checked,st.judged+1);st.cur=P[Math.max(0,st.checked-1)].path;if(st.judged>=st.total)st.status="done";paint(st);if(st.status==="done")return setTimeout(()=>go("/p/demo"),900)}
  else{try{const a=await api("/audits/"+id);paint({status:a.status,found:a.progress.found,crawled:a.progress.crawled,checked:a.progress.checked,judged:a.progress.judged,total:a.progress.total_est||a.progress.found,cur:a.progress.current_url});if(a.status==="done")return go("/p/"+id);if(a.status==="failed")return errState("The audit stopped",a.error||"We could not finish crawling this site.",()=>go("/new?host="+host))}catch(e){}}
  setTimeout(tick,DEMO?700:2000)};paint(st||{status:"crawling",found:0,crawled:0,checked:0,judged:0,total:1});tick()}
function startAudit(v,tries){tries=tries||0;const here="/app.html?host="+encodeURIComponent(v)+"&go=1#/new";
 return fetch("/api/audits",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({url:v})}).then(r=>r.json().then(j=>({r,j}))).then(({r,j})=>{
  if(r.ok)return go("/crawl/"+j.id);
  if(r.status===401){location.href="/signin?next="+encodeURIComponent(here);return}
  if(r.status===402&&Q.get("paid")==="1"&&tries<12){shell("/new",h("div",{class:"panel",style:"max-width:720px;margin:24px auto"},h("h1",null,"Confirming your payment"),h("p",{class:"mut"},"This takes a few seconds. We start the crawl as soon as it is confirmed.")));return new Promise(ok=>setTimeout(ok,2500)).then(()=>startAudit(v,tries+1))}
  if(r.status===402){location.href="/plans?next="+encodeURIComponent(here);return}
  if(r.status===429)return errState("Limit reached",j.reason||j.error==="crawls"?"You have used this month's audits for your plan. Upgrade for more.":"Too many audits started. Try again later.",()=>newAudit());
  errState("We could not start the audit",j.error||"Check the address and try again.",()=>newAudit())}).catch(()=>errState("We could not start the audit","Check your connection and try again.",()=>newAudit()))}
function newAudit(){const host=Q.get("host")||"";const f=h("form",{class:"urlf",onsubmit:e=>{e.preventDefault();const v=f.elements.url.value.trim();if(!v)return;if(DEMO)return go("/crawl/demo");startAudit(v)}},
  h("label",{class:"sr",for:"u"},"Site address"),h("input",{class:"fld",id:"u",name:"url",placeholder:"yourshop.com",autocomplete:"url",required:"",value:host}),h("button",{class:"btn go"},"Audit this site"));
 shell("/new",h("div",{class:"panel",style:"max-width:720px;margin:24px auto"},h("h1",null,"Audit a site"),h("p",{class:"mut"},"We crawl every page we can reach, up to your plan's page limit."),f));
 if(host&&Q.get("go")==="1"&&!DEMO)startAudit(host)}
function pdf(id){return api("/audits/"+id).then(a=>{const brand=(Q.get("brand")||"").replace(/[^\p{L}\p{N} .&'-]/gu,"").slice(0,40),logo=Q.get("logo");document.body.classList.add("pdfmode");
 const cover=h("div",{class:"cover"},logo&&/^https:\/\//.test(logo)?h("img",{src:logo,alt:brand||"",style:"max-height:48px;max-width:240px"}):h("span",{class:"brand"},brand||"CitedBy"),h("h1",null,"AI search readiness report"),h("p",{class:"mut"},a.host+" · "+a.date+(brand?" · Prepared by "+brand:"")));
 shell("/",cover,h("div",{class:"noprint head"},h("div",null,h("h1",null,"PDF report"),h("p",null,"Add ?brand=Your agency&logo=https://… to the address to white-label it.")),h("button",{class:"btn go",onclick:()=>print()},"Print or save as PDF")),
  h("div",{class:"panel"},h("div",{class:"hero"},ring(a.score,160),h("div",{class:"stats"},h("div",{class:"stat"},h("b",null,a.pages),h("span",null,"Pages")),h("div",{class:"stat"},h("b",null,a.issues.high),h("span",null,"High issues")),h("div",{class:"stat"},h("b",null,a.issues.medium),h("span",null,"Medium issues")),h("div",{class:"stat"},h("b",null,a.issues.low),h("span",null,"Low issues"))))),
  h("div",{class:"panel",style:"margin-top:16px"},h("h2",null,"Category scores"),...a.categories.map(c=>h("div",{class:"cat"},ring(c.score,48),h("span",{class:"nm"},c.label),h("span",{class:"ct"},c.issues+(c.issues===1?" check failing":" checks failing"))))),
  h("div",{class:"panel",style:"margin-top:16px"},h("h2",null,"Fix first"),...a.fixes.map(f=>h("div",{class:"fix"},sev(f.severity),h("b",null,f.title),h("span",{class:"num small"},f.pages+" pages")))),
  h("p",{class:"mut small"},"Checks run on the HTML each page serves. A check we could not read is shown as not measured, never as a pass."))})}
function states(){shell("/states",h("div",{class:"head"},h("h1",null,"States"),h("p",null,"Empty, loading and error, as shipped.")),h("div",{class:"grid g2"},
 h("div",{class:"panel"},h("div",{class:"state"},h("div",{class:"ico"},"+"),h("h2",null,"Audit your first site"),h("p",null,"Enter a URL. We crawl every page, analyse it and give you the exact fix for each issue."),h("a",{class:"btn go",href:"#/new"},"Start an audit"))),
 h("div",{class:"panel","aria-busy":"true"},h("div",{class:"sk",style:"height:28px;width:40%"}),h("div",{class:"sk",style:"height:120px;margin:18px 0"}),h("div",{class:"sk",style:"height:16px;width:80%"})),
 h("div",{class:"panel"},h("div",{class:"state err"},h("div",{class:"ico"},"!"),h("h2",null,"We couldn't crawl example.com"),h("p",null,"The site returned 403 to our crawler on every page. Allow CitedBy's crawler in your firewall, then try again."),h("button",{class:"btn go"},"Try again"))),
 h("div",{class:"panel"},h("div",{class:"state"},h("div",{class:"ico"},"0"),h("h2",null,"No issues here"),h("p",null,"Every check passed on this page."),h("a",{class:"btn",href:"#/"},"Back to projects")))))}
function render(){document.body.classList.remove("pdfmode");const r=ROUTE(),p=r.split("?")[0];let m;
 if(p==="/")return guard(projects);if(p==="/new")return newAudit();if(p==="/states")return states();
 if(m=p.match(/^\/crawl\/([\w-]+)$/))return crawl(m[1]);
 if(m=p.match(/^\/p\/([\w-]+)$/))return guard(()=>overview(m[1]));
 if(m=p.match(/^\/p\/([\w-]+)\/pages$/))return guard(()=>pages(m[1]));
 if(m=p.match(/^\/p\/([\w-]+)\/page$/))return guard(()=>pageDetail(m[1]));
 if(m=p.match(/^\/p\/([\w-]+)\/pdf$/))return guard(()=>pdf(m[1]));
 errState("We can't find that","Check the address.")}
window.CB={ring,sev,h,sv,tone};if(!root)return;window.addEventListener("hashchange",()=>{render();scrollTo(0,0)});render();
})();
