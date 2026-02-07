from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>🌹 Special Rose Day 🌹</title>

<style>
body{
    margin:0;
    height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    font-family:'Segoe UI',sans-serif;
    background: radial-gradient(circle at top, #ffe6ec, #fff);
    overflow:hidden;
}

/* Floating hearts */
.heart{
    position:absolute;
    color:#ff4d6d;
    animation:float 6s linear infinite;
    font-size:18px;
}

@keyframes float{
    0%{ transform:translateY(100vh); opacity:0;}
    100%{ transform:translateY(-10vh); opacity:1;}
}

/* Title */
h1{
    color:#b3003c;
    margin-bottom:5px;
    animation:fadeIn 2s ease-in;
}

@keyframes fadeIn{
    from{opacity:0; transform:translateY(-20px);}
    to{opacity:1;}
}

/* Rose container */
.rose{
    position:relative;
    width:260px;
    height:260px;
    animation:bloom 2s ease-out;
}

@keyframes bloom{
    0%{transform:scale(0);}
    100%{transform:scale(1);}
}

/* Petals */
.petal{
    position:absolute;
    width:120px;
    height:160px;
    background: radial-gradient(circle at 30% 30%, #ff8fa3, #c70039 70%);
    border-radius:60%;
    cursor:pointer;
    transition:0.4s;
    box-shadow:0 10px 25px rgba(0,0,0,0.2);
}

.petal:hover{
    transform:scale(1.1);
    filter:brightness(1.2);
    box-shadow:0 0 20px #ff4d6d;
}

/* Petal positions */
.p1{ top:10px; left:70px;}
.p2{ top:60px; left:10px; transform:rotate(-35deg);}
.p3{ top:60px; right:10px; transform:rotate(35deg);}
.p4{ bottom:0px; left:50px; transform:rotate(-10deg);}
.p5{ bottom:0px; right:50px; transform:rotate(10deg);}
.p6{ top:90px; left:70px; background: radial-gradient(circle,#ffb3c1,#ff4d6d);}

/* Stem */
.stem{
    width:10px;
    height:170px;
    background:linear-gradient(#1b8a3e,#0f5c2e);
    margin-top:-20px;
    border-radius:10px;
}

/* Leaves */
.leaf{
    width:60px;
    height:30px;
    background:#2ecc71;
    position:relative;
    border-radius:60px 0 60px 0;
}

.leaf1{ top:-130px; left:-40px; transform:rotate(-30deg);}
.leaf2{ top:-150px; left:40px; transform:rotate(210deg);}

/* Message box */
#msg{
    margin-top:25px;
    font-size:20px;
    color:#b3003c;
    font-weight:bold;
    min-height:40px;
    text-align:center;
    padding:12px 25px;
    background:#fff0f5;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,0.1);
    opacity:0;
    transition:0.6s;
}

.show{ opacity:1 !important; }
</style>
</head>

<body>
<h1>🌹 Happy Rose Day 🌹</h1>
<p>Click every petal for a surprise ❤️</p>

<div class="rose">
    <div class="petal p1" onclick="show(0)"></div>
    <div class="petal p2" onclick="show(1)"></div>
    <div class="petal p3" onclick="show(2)"></div>
    <div class="petal p4" onclick="show(3)"></div>
    <div class="petal p5" onclick="show(4)"></div>
    <div class="petal p6" onclick="show(5)"></div>
</div>

<div class="stem"></div>
<div class="leaf leaf1"></div>
<div class="leaf leaf2"></div>

<div id="msg">🌸 Click a petal 🌸</div>

<script>
const messages = [
"🌹 You are the reason my heart smiles every day.",
"💖 Your presence makes my life more beautiful.",
"✨ Every moment with you feels magical.",
"🌸 I found my happiness the day I found you.",
"❤️ You are my today and all my tomorrows.",
"🌹 Happy Rose Day, my special one."
];

let clicked = new Set();

function show(i){
    const msgBox = document.getElementById("msg");
    msgBox.innerText = messages[i];
    msgBox.classList.add("show");
    clicked.add(i);

    if(clicked.size === 6){
        setTimeout(()=>{
            msgBox.innerText = "💍 I have something special to say… You mean everything to me ❤️";
        },2000);
    }
}

setInterval(()=>{
    let heart = document.createElement("div");
    heart.className="heart";
    heart.style.left=Math.random()*100+"vw";
    heart.innerText="❤";
    heart.style.fontSize=(12+Math.random()*20)+"px";
    document.body.appendChild(heart);
    setTimeout(()=>heart.remove(),6000);
},700);
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

