/* Sample data in the report API shape (docs: saas/CONTRACT.md). Fictional site, labelled "sample" everywhere it shows. */
(function(){
const CATS=[["technical","Links, speed and indexing"],["structure","Titles, headings and schema"],["render","Readable content"],["access","AI-search readiness"],["answers","Answer quality"]];
const CHK={
 robots_ai:["access","AI crawlers allowed in robots.txt","high","GPTBot and ClaudeBot are blocked by a blanket Disallow.","Your robots.txt blocks GPTBot and ClaudeBot, so ChatGPT and other assistants cannot read this page. Allow them for the public pages.","User-agent: GPTBot\nAllow: /\n\nUser-agent: ClaudeBot\nAllow: /"],
 js_render:["access","Content readable without JavaScript","high","The served HTML has 41 words; the rendered page has 600.","Most AI crawlers do not run JavaScript. Render the main copy on the server so it is in the first HTML response.",null],
 schema_org:["structure","Organization schema","medium","No Organization JSON-LD found.","Add Organization markup on the home page so assistants can tie the brand name to the site.",'<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Organization","name":"Example Roaster","url":"https://example-roaster.be"}\n</script>'],
 schema_product:["structure","Product and Offer schema","medium","Product schema without price or availability.","Add Offer with price, currency and availability so assistants can quote the price.",'"offers":{"@type":"Offer","price":"14.50","priceCurrency":"EUR","availability":"https://schema.org/InStock"}'],
 faq_schema:["structure","FAQ schema","low","Questions on the page, no FAQPage markup.","Mark up the questions already on the page.",'{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Do you ship to Germany?","acceptedAnswer":{"@type":"Answer","text":"Yes, in 3 to 5 days."}}]}'],
 answer_first:["answers","Answer in the first 100 words","high","The first paragraph is a brand slogan; the answer starts at word 210.","Open with the plain answer to the question this page exists for. Suggested rewrite of your opening:","Example Roaster roasts single-origin coffee in Ghent and ships whole beans across the EU in 3 to 5 days. A 250 g bag starts at EUR 9.80."],
 headings:["answers","Headings match buyer questions","medium","Two H1s; headings are labels, not questions.","Use one H1 and phrase section headings the way buyers ask.",null],
 own_facts:["render","Specific facts a model can quote","medium","No price, size or delivery time in the visible text.","Add the numbers a buyer asks for next to the product name.",null],
 thin:["render","Enough substance for the topic","low","312 words on a page that other sites cover in 900.","Add sizing, care and comparison sections.",null],
 title_desc:["technical","Title and meta description","pass","Title 54 characters, description 148.",null,null],
 canonical:["technical","Canonical URL","pass","Canonical points to itself.",null,null],
 status:["technical","Status and redirects","pass","200, no redirect chain.",null,null],
 alt:["technical","Image alt text","low","6 of 14 images have no alt text.","Describe each product image in one short sentence.",null]};
const PATHS=["/","/shop","/shop/ethiopia-guji","/shop/colombia-huila","/shop/espresso-blend","/shop/decaf","/subscriptions","/brew-guides","/brew-guides/v60","/brew-guides/aeropress","/about","/shipping","/returns","/faq","/wholesale","/blog/best-beans-for-espresso","/blog/how-to-store-coffee","/blog/grind-size-chart","/blog/ethical-sourcing","/gift-cards","/contact","/blog/cold-brew-ratio","/blog/moka-vs-espresso","/privacy"];
const keys=Object.keys(CHK),fails=["robots_ai","js_render","answer_first"];
function pageChecks(i){const out=[];keys.forEach((k,j)=>{const b=CHK[k];let st=b[2];
  if(k==="robots_ai"&&i>0)st="high";
  if(k!=="robots_ai"&&st!=="pass"&&(i*7+j*5+i*j)%3===0)st="pass";
  if(k==="thin"&&i%5===2)st="medium";
  if((i*7+j*3)%5===0&&st==="pass")st="medium";
  if(i%4===1&&k==="js_render")st="pass";
  if(i%3===0&&k==="answer_first")st="pass";
  if(i>12&&k==="schema_product")st="pass";
  out.push({key:k,label:b[1],category:b[0],status:st==="pass"?"pass":"fail",severity:st==="pass"?null:st,found:b[3],fix:st==="pass"?null:b[4],code:st==="pass"?null:b[5]})});return out}
const pages=PATHS.map((p,i)=>{const c=pageChecks(i),n={high:0,medium:0,low:0};c.forEach(x=>x.severity&&n[x.severity]++);
  const score=Math.max(18,Math.round(100-n.high*13-n.medium*6-n.low*2.5));return{url:"https://example-roaster.be"+p,path:p,score,high:n.high,medium:n.medium,low:n.low,words:200+((i*131)%900),status:200,checks:c}});
const CS=[48,57,52,71,88],avg=Math.round(CS.reduce((a,b)=>a+b,0)/5);
const sum=k=>pages.reduce((a,p)=>a+p[k],0);
const fixes=[["robots_ai","high"],["js_render","high"],["answer_first","high"],["schema_org","medium"],["schema_product","medium"],["headings","medium"]].map(([k,s])=>({id:k,title:CHK[k][1],severity:s,pages:pages.filter(p=>p.checks.find(c=>c.key===k&&c.status==="fail")).length,category:CHK[k][0]}));
const cats=CATS.map(([k,l],i)=>{const sc=CS[i];return{key:k,label:l,score:sc,issues:keys.filter(x=>CHK[x][0]===k&&CHK[x][2]!=="pass").length}});
window.CB_SAMPLE={
 projects:[{id:"demo",host:"example-roaster.be",score:avg,pages:pages.length,high:sum("high"),medium:sum("medium"),low:sum("low"),last:"18 Oct 2026",trend:[41,44,49,avg],sample:true},
  {id:"demo2",host:"example-studio.eu",score:81,pages:212,high:2,medium:19,low:40,last:"16 Oct 2026",trend:[70,74,78,81],sample:true},
  {id:"demo3",host:"example-clinic.fr",score:63,pages:58,high:11,medium:30,low:12,last:"11 Oct 2026",trend:[63,63,60,63],sample:true}],
 audit:{id:"demo",host:"example-roaster.be",status:"done",date:"18 Oct 2026",score:avg,pages:pages.length,issues:{high:sum("high"),medium:sum("medium"),low:sum("low")},
  categories:cats,fixes:fixes,history:[{d:"4 Oct",s:41},{d:"11 Oct",s:52},{d:"18 Oct",s:avg}],sample:true},
 pages:pages};
})();
