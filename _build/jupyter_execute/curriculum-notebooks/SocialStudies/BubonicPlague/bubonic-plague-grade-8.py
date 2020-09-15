![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=SocialStudies/BubonicPlague/bubonic-plague-grade-8.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

%%html

<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide('500');
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show('500');
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>
<p> Code is hidden for ease of viewing. Click the Show/Hide button to see. </>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

# Bubonic Plague

## Black Death

### Grade 8 Social Sciences

The **Black Death** is an important historical event that took place during the 14th century. It was an *outbreak* of a disease called the *bubonic plague* that impacted mainly Europe and resulted in the death of roughly half of the European population over the course of five years.

In this notebook we will discuss this disease, the bubonic plague, illustrate the dynamic of how it did spread through Europe during the Black Death period, and illustrate the dramatic effect of the plague over a small English village through a mathematical model.

## The bubonic plague: an overview

The bubonic plague is a very serious *infectious disease* impacting human population for more than two thousand years. Infectious means that it is caused by a *pathogen*, i.e. a micro-organism that enters the human body and develops within the body, disrupting its normal way to function. This results in an *infection* which, in the case of the bubonic plague, is likely to be fatal unless it is treated by appropriate medications, a plague vaccine. 

The pathogen responsible of the bubonic plague is a *bacteria* called *Yersinia pestis*. This name is composed of the Latin name of the plague, *pestis* prefixed by a Latin version of the name of the person who first discovered the bacteria, [Alexandre Yersin](https://en.wikipedia.org/wiki/Alexandre_Yersin).

This infection causes flu-like symptoms such as headaches and a high fever, a common to many infections, together with visible symptoms such as the apparition in some specific parts of the body of swelling (named *bubos*, which gave it the name bubonic) and the development of black spots on the skin (which led to the name "Black Death"). Generally an untreated patient dies within a few days. 

## Infectious diseases

There are various types of pathogens that cause infectious diseases, including *viruses*, *bacteria*, and *parasites*. 

Viruses are responsible for diseases such as [influenza](https://en.wikipedia.org/wiki/Influenza) (know as the flu), [measles](https://en.wikipedia.org/wiki/Measles), and [mumps](https://en.wikipedia.org/wiki/Mumps)

Bacteria are responsible for diseases such as [tuberculosis](https://en.wikipedia.org/wiki/Tuberculosis), [tetanus](https://en.wikipedia.org/wiki/Tetanus), and [bubonic plague](https://en.wikipedia.org/wiki/Plague_(disease)).

Parasites are larger organisms that can [cause diseases](https://en.wikipedia.org/wiki/Parasitic_disease). Examples of human parasites include [pinworms](https://en.wikipedia.org/wiki/Pinworm_infection) and [swimmer's itch](https://en.wikipedia.org/wiki/Swimmer%27s_itch).

## How does the bubonic plague pathogen infect humans?

Someone becomes sick with the bubonic plague when *Yersinia pestis* enters its body, often when the individual is bitten by a *flea* that carries the pathogen. The flea is called a *vector* of the disease, it does not cause the disease by itself but helps the pathogen to move from the environment to the host. 

It is widely accepted that the kinds of fleas that carry *Yersinia pestis* are not human fleas (the kind that naturally feed on human blood) but *rodent* fleas. So why would they suddenly bite humans? The rodents they use to feed on are also infected by the plague agent, and so they die, forcing the fleas to look for other sources of food. If the rodent population (called the *reservoir* of the disease) lives close to human populations (like urban rats), then the natural new hosts are humans. The figure below illustrates this cycle. 

![plague transmission illustration](./images/plague-transmission.jpg)
Image from http://www.columbia.edu/itc/cerc/danoff-burg/invasion_bio/inv_spp_summ/Yersinia_pestis.htm

We will get back to this when explaining how the plague spread so well in Europe during the Black Death.

## Infectious diseases outbreaks

An *outbreak* occurs when a disease, that may already been present within a population, suddenly starts to infect more people than usual in a given place (in general a city or a region). When an outbreak spreads over a larger region it is called an *epidemic*, or even a *pandemic* when it happens over a very large region such as a continent.

Outbreaks occur very often, including the annual flu outbreak that hits every Canadian city every winter. This is not too scary and the local health authorities know how to handle it through vaccination campaigns. But even now more serious outbreaks occur quite often, such as the Ebola epidemic in Western Africa in 2013-2016 that caused thousands of death and was very challenging for local and global health authorities.

There have been many other dramatic outbreaks, epidemic and pandemics in history, the Black Death that we will describe below being one of the most present in human memory. But closer to us, we can think about several smallpox epidemic in the late 19th century that spread through Indigenous communities of the Pacific North West and had a devastating impact.

## The Black Death Timeline

The Black Death was a bubonic plague pandemic that concerned all of Western Europe. It started outside of Europe in Asia, where it infected soldiers of a Mongol army who were besieging a Genoese trade post in Crimea, the city of Kaffa. After the siege, the Genoese traders (from the Italian city of Geona) sailed back home without knowing they were themselves infected. This is how the disease was introduced in Western Europe. 

At the time people did not know the principles of infectious diseases and did not intervene quickly to try to contain the disease to a city or a few cities where the outbreak would have ended likely quickly. Instead, unaware of the dramatic situation that was unfolding, traders from Italian cities maintained very active relationships with the rest of Europe through marine or land trading routes. This resulted in the disease spreading very fast to Southern Europe within six months, and from there turning into a European-wide pandemic within three years.

The dynamic map below illustrates this.

Given there was no precise record of population numbers at this time, it is difficult to have a precise estimation of the number of death. But by analyzing local reports of casualties, historians have arrived to the conclusion that roughly half of the European population at this time died from the bubonic plague. We propose at the end of this notebook a small example based on real data of a 1665 plague outbreak in an English village that illustrates how quickly the bubonic plague can wipe out a community.

%%html

<style>

* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
    display: none;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: black;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #000000;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: right;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: black;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

</style>

<script>

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block"; 
  dots[slideIndex-1].className += " active";
}

</script>

<body>
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides">
    <div class="numbertext">1 / 9</div>
    <img src="./images/before_plague.jpg" style="width:75%;height:650px">
    <div class="text">Before Plague</div>
  </div>

  <div class="mySlides">
    <div class="numbertext">2 / 9</div>
    <img src="./images/1347.jpg" style="width:75%;height:650px">
    <div class="text">Plague Expansion 1347</div>
  </div>

  <div class="mySlides">
    <div class="numbertext">3 / 9</div>
    <img src="./images/mid_1348.jpg" style="width:75%;height:650px">
    <div class="text">Plague Expansion Mid 1348</div>
  </div>

  <div class="mySlides">
    <div class="numbertext">4 / 9</div>
    <img src="./images/early_1349.jpg" style="width:75%;height:650px">
    <div class="text">Plague Expansion Early 1349</div>
  </div>
 
<div class="mySlides">
    <div class="numbertext">5 / 9</div>
    <img src="./images/late_1349.jpg" style="width:75%;height:650px">
    <div class="text">Plague Expansion Late 1349</div>
  </div>

<div class="mySlides">
    <div class="numbertext">6 / 9</div>
    <img src="./images/1350.jpg" style="width:75%;height:650px">
    <div class="text">Plague Expansion by 1350</div>
  </div>

<div class="mySlides">
    <div class="numbertext">7 / 9</div>
    <img src="./images/1351.jpg" style="width:75%;height:650px">
    <div class="text">Plague Expansion by 1351</div>
  </div>

<div class="mySlides">
    <div class="numbertext">8 / 9</div>
    <img src="./images/after_1351.jpg" style="width:75%;height:650px">
    <div class="text">Plague Expansion After 1351</div>
  </div>

<div class="mySlides">
    <div class="numbertext">9 / 9</div>
    <img src="./images/minor-outbreak.jpg" style="width:75%;height:650px">
    <div class="text">Minor Outbreak</div>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>

<!-- The dots/circles -->
<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span> 
  <span class="dot" onclick="currentSlide(2)"></span> 
  <span class="dot" onclick="currentSlide(3)"></span> 
    <span class="dot" onclick="currentSlide(4)"></span> 
    <span class="dot" onclick="currentSlide(5)"></span> 
    <span class="dot" onclick="currentSlide(6)"></span> 
    <span class="dot" onclick="currentSlide(7)"></span> 
    <span class="dot" onclick="currentSlide(8)"></span> 
    <span class="dot" onclick="currentSlide(9)"></span> 
</div>
<figure>
<center>
<figcaption>The Black Death Timeline. Images Retrieved from <a href="https://en.wikipedia.org/wiki/Consequences_of_the_Black_Death">Wikipedia</a></figcaption>
</center>
</figure>
</body>

<h2 align='center'>Historical plague outbreaks</h2>

The Black Death was not the only major plague pandemic. Before this medieval pandemic, in the fifth century (in 541-542 precisely), the *Justinian Plague* developed as an epidemic in the  Eastern part of the Mediterranean region and many Mediterranean port cities. It is known as the first major plague pandemic.

The Black Death itself lasted much longer than the few years illustrated in the map above. The years 1347-1351 correspond to the most acute part of the pandemic. But after this, plague remained present in Europe for almost 400 years, flaring up here and there in dramatic outbreaks, although none that turned into a pandemic. People had learned from the Black Death, and as soon as plague reappeared in a community, the community was isolated to prevent the disease spread. Nevertheless, some important outbreaks impacted large cities such as the Great Plague of London (1665-1666) or the Marseille Plague (1722). This very long pandemic is known as the second major plague pandemic.

Past the Marseille plague in 1722, the disease seemed to disappear from Europe, although it remained present in Asia. This is there, in the Chinese province of the Yunan, in 1855 precisely, that the third major plague pandemic started. It did not move out of China for a long time, but then reached Hong-Kong in 1894, and from there, following again the maritime trade routes, it reached the rest of the world and was considered as an active pandemic by the World Health Organization until 1959.

Currently, there is no bubonic plague pandemic, but outbreaks occur regularly. The most serious ones are in the African island of Madagascar, but there are also regular small outbreaks in the South-West of the United States, where prairie dogs act as a reservoir for the disease.

---

<h2 align='center'>The discovery of the <i>Yersinia pestis</i> bacteria</h2>

This is during the 1894 Hong-Kong outbreak of the third pandemic that, finally, scientists discovered the cause of the bubonic plague. Until this date, people did not know what caused this dramatic disease. But during the 1984 outbreak, both French and Japanese authorities sent scientists, Alexandre Yersin for the French side and Kitasato Shibasaburō for the Japanese side, to try to discover the cause of the disease.

<figure>
<center>
<table>
<tr>
    <td><img src='./images/Kitasato_Shibasaburo.jpg' width=300px></td>
    <td><img src='./images/Alexandre_Yersin.jpg' width=325px></td>
</tr>
</table>
    <figcaption><a href="https://commons.wikimedia.org/wiki/File:Shibasaburo_Kitasato.jpg">Kitasato Shibasaburō (left)</a> and <a href="https://en.wikipedia.org/wiki/Alexandre_Yersin#/media/File:Petit-Yersin.jpg">Alexandre Yersin (right)</a></figcaption>
</center>
</figure>

Both were competing hard to be the first one to find the pathogen causing the disease. Yersin was fortunate enough that his lab was actually a shed with no cooling system, which resulted in the bacteria <i>Yersinia pestis</i> reproducing faster than in the well equipped lab of Shibasaburō, which lead him the finding the tiny micro-organisms in large numbers in the lungs of deceased patients.

---


<h2 align='center'>Was the Black Death a bubonic plague outbreak?</h2>

This is actually a good question. Indeed, nobody did the same work than Yersin and  Shibasaburō during the Black Death pandemic. Bacteria were actually not known at the time. So in order to declare it a plague, historians relied on written records from people chronicling the dramatic pandemic. Nevertheless, most chroniclers were not physicians and as such they did not use the medical vocabulary developed in the XIXth century when the mechanisms of infectious diseases were discovered. It did not help that, at the time of the Black Death, the word *plague* was   a generic word used to describe infectious diseases outbreaks in general.

As a result of this lack of precise documentation about the Black Death pandemic, there was a long-standing debate about the cause of this pandemic, with a strongly supported hypothesis that the disease was actually due to an Ebola-like virus. 

It is only in 2011, that an international team led by a Canadian scientist, <a href="https://socialsciences.mcmaster.ca/people/poinar-hendrik">Hendrik Poinar</a>, from McMaster University in Hamilton, was able to extract, from the dental pulp of the body of victims of the Black Death in London, the genome of the bacteria *Yersinia pestis*, thus closing the debate over the actual disease that caused the Black Death.

---

<h2 align='center'>Conclusion</h2>
The  Black Death was a dramatic event in European history, as shown by the extant and speed of its spread across the continent.  While it is now a well known event (a plague pandemic), it is interesting to reflect on the fact that this results from tremendous progress of sciences over the last century or so. Our understanding of this pandemic follows up from the discovery of infectious diseases, the precise identification of the plague agent and even very recent work on ancient DNA. The story is however not closed. The Plague stayed in Europe for almost 400 years after the Black Death before disappearing from the continent; it is still an open question to understand both how a disease can last for so long and why it can vanish quite suddenly with no human intervention.

---

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)