(this["webpackJsonpauth0-react-sample"]=this["webpackJsonpauth0-react-sample"]||[]).push([[0],{56:function(e,t){},75:function(e,t,a){e.exports=a(95)},92:function(e,t,a){},93:function(e,t,a){},94:function(e,t,a){},95:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),c=a(28),l=a.n(c),o=a(9),u=a(99),i=a(6),s=a(97),m=a(57),p=function(){return r.a.createElement("footer",{className:"bg-light p-3 text-center"},r.a.createElement("div",{className:"logo"}),r.a.createElement("p",null,"Sample project provided by"," ",r.a.createElement("a",{target:"_blank",rel:"noopener noreferrer",href:"https://auth0.com"},"Auth0")))},E=function(){return r.a.createElement("div",{className:"spinner"},r.a.createElement("img",{src:"https://cdn.auth0.com/blog/auth0-react-sample/assets/loading.svg",alt:"Loading"}))},f=a(17),d=a(102),h=a(104),b=a(98),v=function(){var e=Object(i.b)().logout;return r.a.createElement(b.a,{onClick:function(){return e({returnTo:window.location.origin})},variant:"danger",className:"btn-margin"},"Log Out")},g=function(){var e=Object(i.b)().loginWithRedirect;return r.a.createElement(b.a,{onClick:function(){return e()},variant:"primary",className:"btn-margin"},"Log In")},j=function(){var e=Object(i.b)().loginWithRedirect;return r.a.createElement(b.a,{onClick:function(){return e({screen_hint:"signup"})},variant:"primary",className:"btn-margin"},"Sign Up")},O=function(){return r.a.createElement(d.a,{className:"mr-auto"},r.a.createElement(d.a.Link,{as:f.b,to:"/",exact:!0,activeClassName:"router-link-exact-active"},"Home"),r.a.createElement(d.a.Link,{as:f.b,to:"/profile",exact:!0,activeClassName:"router-link-exact-active"},"Profile"),r.a.createElement(d.a.Link,{as:f.b,to:"/external-api",exact:!0,activeClassName:"router-link-exact-active"},"External API"))},y=function(){var e=Object(i.b)().isAuthenticated;return r.a.createElement(d.a,{className:"justify-content-end"},e?r.a.createElement(v,null):r.a.createElement("div",{className:"sign"},r.a.createElement(g,null),r.a.createElement(j,null)))},x=function(){return r.a.createElement(h.a,{bg:"light",expand:"md"},r.a.createElement(u.a,null,r.a.createElement(h.a.Brand,{as:f.b,className:"logo",to:"/"}),r.a.createElement(O,null),r.a.createElement(y,null)))},k=a(103),C=a(67),N=a(69);k.a.registerLanguage("json",C.a);var w=function(e){var t=e.children;return r.a.createElement(k.a,{language:"json",style:N.a},t)},S=a(74),A=function(e){var t=e.component,a=Object(S.a)(e,["component"]);return r.a.createElement(o.a,Object.assign({component:Object(i.c)(t,{onRedirecting:function(){return r.a.createElement(E,null)}})},a))},T=a(8),B=a.n(T),P=a(13),F=a(11),R=a(105),I=a(7);var L=function(e){var t=e.id,a=e.name,c=e.age,l=e.gender,o=Object(n.useState)(!1),u=Object(F.a)(o,2),s=u[0],m=u[1],p=function(){return m(!1)},E=Object(i.b)().isAuthenticated,f=Object(i.b)().getAccessTokenSilently,d=function(){var e=Object(P.a)(B.a.mark((function e(a){var n,r;return B.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a.preventDefault(),e.next=3,f();case 3:return n=e.sent,r={method:"DELETE",headers:{Authorization:"Bearer ".concat(n)}},e.next=7,fetch("".concat("https://hidden-basin-96158.herokuapp.com/","/actors/").concat(t),r).then((function(e){return e.json()})).then((function(e){console.log(e)}));case 7:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();return r.a.createElement(R.a,{style:{width:"18rem"}},r.a.createElement(R.a.Body,null,r.a.createElement(R.a.Title,null,a),r.a.createElement(R.a.Subtitle,{className:"mb-2 text-muted"},c),r.a.createElement(R.a.Subtitle,{className:"mb-2 text-muted"},l),r.a.createElement(r.a.Fragment,null,r.a.createElement(b.a,{variant:"primary",onClick:function(){return m(!0)}},"View Actor"),r.a.createElement(I.a,{show:s,onHide:p},r.a.createElement(I.a.Header,{closeButton:!0},r.a.createElement(I.a.Title,null,a)),r.a.createElement(I.a.Body,null,r.a.createElement("ul",null,r.a.createElement("li",null,"Name : ",a),r.a.createElement("li",null,"Age : ",c),r.a.createElement("li",null,"Gender : ",l))),r.a.createElement(I.a.Footer,null,r.a.createElement(b.a,{variant:"secondary",onClick:p},"Close"),E&&r.a.createElement(b.a,{type:"submit",variant:"primary",onClick:function(e){d(e),p()}},"Remove"))))))},H=a(26);var _=function(e){e.actors;var t=Object(n.useState)(!1),a=Object(F.a)(t,2),c=a[0],l=a[1],o=function(){return l(!1)},u=Object(n.useState)(""),s=Object(F.a)(u,2),m=s[0],p=s[1],E=Object(n.useState)(""),f=Object(F.a)(E,2),d=f[0],h=f[1],v=Object(n.useState)(""),g=Object(F.a)(v,2),j=g[0],O=g[1],y=Object(i.b)().getAccessTokenSilently,x=function(){var e=Object(P.a)(B.a.mark((function e(t){var a,n;return B.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return console.log("hereeeeeeeeeee"),t.preventDefault(),console.log("I am here",m),e.next=5,y();case 5:return a=e.sent,n={method:"POST",headers:{"Content-Type":"application/json",Authorization:"Bearer ".concat(a)},body:JSON.stringify({name:m,age:d,gender:j})},console.log(">>>>>>>>>>>>>>>>",n),e.next=10,fetch("".concat("https://hidden-basin-96158.herokuapp.com/","/actors/create"),n).then((function(e){return e.json()})).then((function(e){console.log(e)}));case 10:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();return r.a.createElement(r.a.Fragment,null,r.a.createElement(b.a,{variant:"primary",onClick:function(){return l(!0)}},"Create Actor"),r.a.createElement(I.a,{show:c,onHide:o},r.a.createElement(I.a.Header,{closeButton:!0},r.a.createElement(I.a.Title,null,"Create an Actor")),r.a.createElement(I.a.Body,null,r.a.createElement(H.a.Group,null,r.a.createElement(H.a.Control,{value:m,onChange:function(e){return p(e.target.value)},type:"text",placeholder:"Name"}),r.a.createElement("br",null),r.a.createElement(H.a.Control,{value:d,onChange:function(e){return h(e.target.value)},type:"text",placeholder:"Age"}),r.a.createElement("br",null),r.a.createElement(H.a.Control,{value:j,onChange:function(e){return O(e.target.value)},as:"select",className:"my-1 mr-sm-2",id:"inlineFormCustomSelectPref",custom:!0},r.a.createElement("option",{value:"0"},"Choose..."),r.a.createElement("option",{value:"male"},"Male"),r.a.createElement("option",{value:"female"},"Female")),r.a.createElement("br",null))),r.a.createElement(I.a.Footer,null,r.a.createElement(b.a,{variant:"secondary",onClick:o},"Close"),r.a.createElement(b.a,{type:"submit",variant:"primary",onClick:function(e){x(e),o()}},"Create"))))},M=a(100);a(92);var D=function(){var e=Object(n.useState)([{id:1,name:"test",age:20,gender:"male"}]),t=Object(F.a)(e,2),a=t[0],c=t[1],l=Object(i.b)().isAuthenticated;return Object(n.useEffect)((function(){(function(){var e=Object(P.a)(B.a.mark((function e(){return B.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("".concat("https://hidden-basin-96158.herokuapp.com/","/actors")).then((function(e){return e.json()})).then((function(e){var t=e.actors;c(t)}));case 2:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}})()()}),[]),console.log("Actors",a),r.a.createElement("div",{className:"actors"},r.a.createElement(M.a,null,a.map((function(e){return r.a.createElement(L,{id:e.id,name:e.name,age:e.age,gender:e.gender})}))),l&&r.a.createElement(_,{actors:a}))};var J=function(e){var t=e.id,a=e.title,c=e.release_date,l=Object(n.useState)(!1),o=Object(F.a)(l,2),u=o[0],s=o[1],m=function(){return s(!1)},p=Object(i.b)().isAuthenticated,E=Object(i.b)().getAccessTokenSilently,f=function(){var e=Object(P.a)(B.a.mark((function e(a){var n,r;return B.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a.preventDefault(),e.next=3,E();case 3:return n=e.sent,r={method:"DELETE",headers:{Authorization:"Bearer ".concat(n)}},e.next=7,fetch("".concat("https://hidden-basin-96158.herokuapp.com/","/movies/").concat(t),r).then((function(e){return e.json()})).then((function(e){console.log(e)}));case 7:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();return r.a.createElement("div",null,r.a.createElement(R.a,{style:{width:"18rem"}},r.a.createElement(R.a.Body,null,r.a.createElement(R.a.Title,null,a),r.a.createElement(R.a.Subtitle,{className:"mb-2 text-muted"},c),r.a.createElement(r.a.Fragment,null,r.a.createElement(b.a,{variant:"primary",onClick:function(){return s(!0)}},"View Movie"),r.a.createElement(I.a,{show:u,onHide:m},r.a.createElement(I.a.Header,{closeButton:!0},r.a.createElement(I.a.Title,null,a)),r.a.createElement(I.a.Body,null,r.a.createElement("ul",null,r.a.createElement("li",null,"Title : ",a),r.a.createElement("li",null,"Release_date : ",c))),r.a.createElement(I.a.Footer,null,r.a.createElement(b.a,{variant:"secondary",onClick:m},"Close"),p&&r.a.createElement(b.a,{type:"submit",variant:"primary",onClick:function(e){f(e),m()}},"Remove")))))))};var z=function(e){e.movies;var t=Object(n.useState)(!1),a=Object(F.a)(t,2),c=a[0],l=a[1],o=function(){return l(!1)},u=Object(n.useState)(""),s=Object(F.a)(u,2),m=s[0],p=s[1],E=Object(n.useState)(""),f=Object(F.a)(E,2),d=f[0],h=f[1],v=Object(i.b)().getAccessTokenSilently,g=function(){var e=Object(P.a)(B.a.mark((function e(t){var a,n;return B.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return console.log("hereeeeeeeeeee"),t.preventDefault(),console.log("I am here",m),e.next=5,v();case 5:return a=e.sent,n={method:"POST",headers:{"Content-Type":"application/json",Authorization:"Bearer ".concat(a)},body:JSON.stringify({title:m,release_date:d})},console.log(">>>>>>>>>>>>>>>>",n),e.next=10,fetch("".concat("https://hidden-basin-96158.herokuapp.com/","/movies/create"),n).then((function(e){return e.json()})).then((function(e){console.log(e)}));case 10:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();return r.a.createElement(r.a.Fragment,null,r.a.createElement(b.a,{variant:"primary",onClick:function(){return l(!0)}},"Create Movie"),r.a.createElement(I.a,{show:c,onHide:o},r.a.createElement(I.a.Header,{closeButton:!0},r.a.createElement(I.a.Title,null,"Create an Movie")),r.a.createElement(I.a.Body,null,r.a.createElement(H.a.Group,null,r.a.createElement(H.a.Control,{value:m,onChange:function(e){return p(e.target.value)},type:"text",placeholder:"Title"}),r.a.createElement("br",null),r.a.createElement(H.a.Control,{type:"datetime-local",onChange:function(e){return h(e.target.value)},className:"my-1 mr-sm-2"}),r.a.createElement("br",null))),r.a.createElement(I.a.Footer,null,r.a.createElement(b.a,{variant:"secondary",onClick:o},"Close"),r.a.createElement(b.a,{type:"submit",variant:"primary",onClick:function(e){g(e),o()}},"Create"))))};var G=function(){var e=Object(n.useState)([{id:1,title:"test",release_date:"5-11-2016"}]),t=Object(F.a)(e,2),a=t[0],c=t[1],l=Object(i.b)().isAuthenticated;return Object(n.useEffect)((function(){(function(){var e=Object(P.a)(B.a.mark((function e(){return B.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("".concat("https://hidden-basin-96158.herokuapp.com/","/movies")).then((function(e){return e.json()})).then((function(e){var t=e.movies;c(t)}));case 2:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}})()()}),[]),console.log("Movies",a),r.a.createElement("div",null,a.map((function(e){return r.a.createElement(J,{id:e.id,title:e.title,release_date:e.release_date})})),l&&r.a.createElement(z,{movies:a}))},W=a(101),U=function(){var e=Object(n.useState)(""),t=Object(F.a)(e,2),a=t[0],c=t[1],l="https://hidden-basin-96158.herokuapp.com/",o=Object(i.b)().getAccessTokenSilently,s=function(){var e=Object(P.a)(B.a.mark((function e(){var t,a;return B.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,fetch("".concat(l,"/actors"));case 3:return t=e.sent,e.next=6,t.json();case 6:a=e.sent,c(a),e.next=13;break;case 10:e.prev=10,e.t0=e.catch(0),c(e.t0.message);case 13:case"end":return e.stop()}}),e,null,[[0,10]])})));return function(){return e.apply(this,arguments)}}(),m=function(){var e=Object(P.a)(B.a.mark((function e(){var t,a,n;return B.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,o();case 3:return t=e.sent,e.next=6,fetch("".concat(l,"/actors/1"),{headers:{Authorization:"Bearer ".concat(t)}});case 6:return a=e.sent,e.next=9,a.json();case 9:n=e.sent,c(n),e.next=16;break;case 13:e.prev=13,e.t0=e.catch(0),c(e.t0.message);case 16:case"end":return e.stop()}}),e,null,[[0,13]])})));return function(){return e.apply(this,arguments)}}();return r.a.createElement(u.a,{className:"mb-5"},r.a.createElement("h1",null,"External API"),r.a.createElement("p",null,"You use will use a button to call an external API using an access token, and the API will validate it using the API's audience value."," ",r.a.createElement("strong",null,"This route should be private"),"."),r.a.createElement(W.a,null,r.a.createElement(b.a,{onClick:s,color:"primary",className:"mt-5"},"Get Public Message"),r.a.createElement(b.a,{onClick:m,color:"primary",className:"mt-5"},"Get Private Message")),a&&r.a.createElement("div",{className:"mt-5"},r.a.createElement("h6",{className:"muted"},"Result"),r.a.createElement(w,null,JSON.stringify(a,null,2))))},V=function(){return r.a.createElement(n.Fragment,null,r.a.createElement(D,null),r.a.createElement(G,null),r.a.createElement("hr",null))},Y=function(){var e=Object(i.b)().user,t=e.name,a=e.picture,n=e.email;return r.a.createElement(u.a,{className:"mb-5"},r.a.createElement(s.a,{className:"align-items-center profile-header mb-5 text-center text-md-left"},r.a.createElement(m.a,{md:2},r.a.createElement("img",{src:a,alt:"Profile",className:"rounded-circle img-fluid profile-picture mb-3 mb-md-0"})),r.a.createElement(m.a,{md:!0},r.a.createElement("h2",null,t),r.a.createElement("p",{className:"lead text-muted"},n))),r.a.createElement(s.a,null,r.a.createElement(w,null,JSON.stringify(e,null,2))))},q=a(56),K=a.n(q),Q=(a(93),function(){return Object(i.b)().isLoading?r.a.createElement(E,null):r.a.createElement("div",{id:"app",className:"d-flex flex-column h-100"},r.a.createElement(x,null),r.a.createElement(u.a,{className:"flex-grow-1 mt-5"},r.a.createElement(o.c,null,r.a.createElement(o.a,{path:"/",exact:!0,component:V}),r.a.createElement(A,{path:"/actor",component:K.a}),r.a.createElement(A,{path:"/profile",component:Y}),r.a.createElement(A,{path:"/external-api",component:U}))),r.a.createElement(p,null))}),X=function(e){var t=e.children,a=Object(o.f)();return r.a.createElement(i.a,{domain:"dev-12thxr6i.us.auth0.com",clientId:"OBbqRxSTa2PCRNYaWEgeRWAykTfm3bux",redirectUri:window.location.origin,onRedirectCallback:function(e){a.push((null===e||void 0===e?void 0:e.returnTo)||window.location.pathname)},audience:"http://localhost:5000/api"},t)};a(94);l.a.render(r.a.createElement(f.a,null,r.a.createElement(X,null,r.a.createElement(Q,null))),document.getElementById("root"))}},[[75,151,152]]]);
//# sourceMappingURL=main.ccd4a008.chunk.js.map