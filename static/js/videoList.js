function refreshPage(){
    window.location.reload();
} 
  const videoMap = {
    'a': 'static/beginner-alphabet/A.mp4',
    'b': 'static/beginner-alphabet/B.mp4',
    'c': 'static/beginner-alphabet/C.mp4',
    'd': 'static/beginner-alphabet/D.mp4',
    'e': 'static/beginner-alphabet/E.mp4',
    'f': 'static/beginner-alphabet/F.mp4',
    'g': 'static/beginner-alphabet/G.mp4',
    'h': 'static/beginner-alphabet/H.mp4',
    'i': 'static/beginner-alphabet/I.mp4',
    'j': 'static/beginner-alphabet/J.mp4',
    'k': 'static/beginner-alphabet/K.mp4',
    'l': 'static/beginner-alphabet/L.mp4',
    'm': 'static/beginner-alphabet/M.mp4',
    'n': 'static/beginner-alphabet/N.mp4',
    'o': 'static/beginner-alphabet/O.mp4',
    'p': 'static/beginner-alphabet/P.mp4',
    'q': 'static/beginner-alphabet/Q.mp4',
    'r': 'static/beginner-alphabet/R.mp4',
    's': 'static/beginner-alphabet/S.mp4',
    't': 'static/beginner-alphabet/T.mp4',
    'u': 'static/beginner-alphabet/U.mp4',
    'v': 'static/beginner-alphabet/V.mp4',
    'w': 'static/beginner-alphabet/W.mp4',
    'x': 'static/beginner-alphabet/X.mp4',
    'y': 'static/beginner-alphabet/Y.mp4',
    'z': 'static/beginner-alphabet/Z.mp4',

    '1': 'static/beginner-number/1.mp4',
    '2': 'static/beginner-number/2.mp4',
    '3': 'static/beginner-number/3.mp4',
    '4': 'static/beginner-number/4.mp4',
    '5': 'static/beginner-number/5.mp4',
    '6': 'static/beginner-number/6.mp4',
    '7': 'static/beginner-number/7.mp4',
    '8': 'static/beginner-number/8.mp4',
    '9': 'static/beginner-number/9.mp4',
    '10': 'static/beginner-number/10.mp4',

    'be careful': 'static/beginner-basic-phrases/Be careful.mp4',
    'busy': 'static/beginner-basic-phrases/Busy.mp4',
    'cold': 'static/beginner-basic-phrases/Cold.mp4',
    'dont want': 'static/beginner-basic-phrases/Don_t want.mp4',
    'excuse me': 'static/beginner-basic-phrases/Excuse me.mp4',
    'fine': 'static/beginner-basic-phrases/Fine.mp4',
    'finish': 'static/beginner-basic-phrases/Finish_done.mp4',
    'done': 'static/beginner-basic-phrases/Finish_done.mp4',
    'forget': 'static/beginner-basic-phrases/Forget.mp4',
    'go there': 'static/beginner-basic-phrases/Go there.mp4',
    'go': 'static/beginner-basic-phrases/Go.mp4',
    'good': 'static/beginner-basic-phrases/Good.mp4',
    'goodbye': 'static/beginner-basic-phrases/Goodbye.mp4',
    'great': 'static/beginner-basic-phrases/Great.mp4',
    'have': 'static/beginner-basic-phrases/Have.mp4',
    'hello my name is': 'static/beginner-basic-phrases/Hello my name is.mp4',
    'hello': 'static/beginner-basic-phrases/Hello.mp4',
    'help': 'static/beginner-basic-phrases/His_Her name is.mp4',
    'Hot': 'static/beginner-basic-phrases/Hot.mp4',
    'how are you': 'static/beginner-basic-phrases/How are you.mp4',
    'how': 'static/beginner-basic-phrases/How.mp4',
    'i love you': 'static/beginner-basic-phrases/I love you.mp4',
    'i`m fine': 'static/beginner-basic-phrases/I_m fine.mp4',
    'later': 'static/beginner-basic-phrases/Like.mp4',
    'listen': 'static/beginner-basic-phrases/Listen.mp4',
    'look': 'static/beginner-basic-phrases/Look.mp4',
    'maybe': 'static/beginner-basic-phrases/Maybe.mp4',
    'my name is': 'static/beginner-basic-phrases/My name is.mp4',
    'need': 'static/beginner-basic-phrases/Need.mp4',
    'nice to meet you': 'static/beginner-basic-phrases/Nice to meet you.mp4',
    'no problem': 'static/beginner-basic-phrases/No problem.mp4',
    'no': 'static/beginner-basic-phrases/No.mp4',
    'nothing': 'static/beginner-basic-phrases/Nothing.mp4',
    'please': 'static/beginner-basic-phrases/Please.mp4',
    'problem': 'static/beginner-basic-phrases/Problem.mp4',
    'ready': 'static/beginner-basic-phrases/Ready.mp4',
    'see you later': 'static/beginner-basic-phrases/See you later.mp4',
    'slow': 'static/beginner-basic-phrases/Slow.mp4',
    'slowly, please': 'static/beginner-basic-phrases/Slowly, please.mp4',
    'slowly': 'static/beginner-basic-phrases/Slowly.mp4',
    'sorry i don`t understand': 'static/beginner-basic-phrases/Sorry i don_t understand.mp4',
    'sorry': 'static/beginner-basic-phrases/Sorry.mp4',
    'so-so': 'static/beginner-basic-phrases/So-so.mp4',
    'take care': 'static/beginner-basic-phrases/Take Care.mp4',
    'thank you': 'static/beginner-basic-phrases/Thank you.mp4',
    'there': 'static/beginner-basic-phrases/There.mp4',
    'understand': 'static/beginner-basic-phrases/Understand.mp4',
    'understood': 'static/beginner-basic-phrases/Understood.mp4',
    'want': 'static/beginner-basic-phrases/Want.mp4',
    'welcome': 'static/beginner-basic-phrases/Welcome.mp4',
    'what do you want': 'static/beginner-basic-phrases/What do you want.mp4',
    'what': 'static/beginner-basic-phrases/What.mp4',
    'what`s up': 'static/beginner-basic-phrases/What_s up.mp4',
    'when': 'static/beginner-basic-phrases/When.mp4',
    'where': 'static/beginner-basic-phrases/Where.mp4',
    'which': 'static/beginner-basic-phrases/Which.mp4',
    'who': 'static/beginner-basic-phrases/Who.mp4',
    'why': 'static/beginner-basic-phrases/Why.mp4',
    'why?': 'static/beginner-basic-phrases/Why_.mp4',
    'wonderful': 'static/beginner-basic-phrases/Wonderful.mp4',
    'yes I understand': 'static/beginner-basic-phrases/Yes i understand.mp4',
    'yes': 'static/beginner-basic-phrases/Yes.mp4',
    'you`re': 'static/beginner-basic-phrases/You_re welcome.mp4',
    
    'aunt': 'static/intermediate-family/Aunt.mov',
    'baby': 'static/intermediate-family/Baby.MOV',
    'brother': 'static/intermediate-family/Brother.mov',
    'child': 'static/intermediate-family/Child.MOV',
    'cousin': 'static/intermediate-family/Cousin.MOV',
    'family': 'static/intermediate-family/Family.MOV',
    'father': 'static/intermediate-family/Father.MOV',
    'grandfather': 'static/intermediate-family/Grandfather.mov',
    'grandmother': 'static/intermediate-family/Grandmother.mov',
    'husband': 'static/intermediate-family/Husband.mov',
    'in law': 'static/intermediate-family/In-Law.mov',
    'in-law': 'static/intermediate-family/In-Law.mov',
    'mother': 'static/intermediate-family/Mother.mov',
    'nephew': 'static/intermediate-family/Nephew.mov',
    'niece': 'static/intermediate-family/Niece.mov',
    'parents': 'static/intermediate-family/Parents.mov',
    'relative': 'static/intermediate-family/Relative.mov',
    'sibling': 'static/intermediate-family/Sibling.MOV',
    'sister': 'static/intermediate-family/Sister.mov',
    'stepfather': 'static/intermediate-family/Stepfather.mov',
    'stepmother': 'static/intermediate-family/Stepmother.MOV',
    'uncle': 'static/intermediate-family/Uncle.mov',
    'wife': 'static/intermediate-family/WIFE.MOV',

    'afraid': 'static/intermediate-expression/Afraid.mp4',
    'angry': 'static/intermediate-expression/Angry.mp4',
    'annoyed': 'static/intermediate-expression/Annoyed.mp4',
    'bored': 'static/intermediate-expression/Bored.mp4',
    'confused': 'static/intermediate-expression/Confused.mp4',
    'envy': 'static/intermediate-expression/Envy.mp4',
    'excited': 'static/intermediate-expression/Excited.mp4',
    'happy': 'static/intermediate-expression/Happy.mp4',
    'hungry': 'static/intermediate-expression/Hungry.mp4',
    'pressure': 'static/intermediate-expression/Pressure.mp4',
    'sad': 'static/intermediate-expression/Sad.mp4',
    'safe': 'static/intermediate-expression/Safe.mp4',
    'shy': 'static/intermediate-expression/Shy.mp4',
    'tired': 'static/intermediate-expression/Tired.mp4',
    
    'april': 'static/intermediate-daily-phrase/april.mp4',
    'august': 'static/intermediate-daily-phrase/aug.mp4',
    'day': 'static/intermediate-daily-phrase/day.mp4',
    'december': 'static/intermediate-daily-phrase/dec.mp4',
    'february': 'static/intermediate-daily-phrase/feb.mp4',
    'friday': 'static/intermediate-daily-phrase/friday.mp4',
    'good afternoon': 'static/intermediate-daily-phrase/good afternoon.mp4',
    'good evening': 'static/intermediate-daily-phrase/good evening.mp4',
    'good morning': 'static/intermediate-daily-phrase/good morning.mp4',
    'hour': 'static/intermediate-daily-phrase/hour.mp4',
    'january': 'static/intermediate-daily-phrase/jan.mp4',
    'july': 'static/intermediate-daily-phrase/july.mp4',
    'june': 'static/intermediate-daily-phrase/june.mp4',
    'later': 'static/intermediate-daily-phrase/later.mp4',
    'march': 'static/intermediate-daily-phrase/march.mp4',
    'may': 'static/intermediate-daily-phrase/may.mp4',
    'minute': 'static/intermediate-daily-phrase/minute.mp4',
    'monday': 'static/intermediate-daily-phrase/monday.mp4',
    'month': 'static/intermediate-daily-phrase/month.mp4',
    'november': 'static/intermediate-daily-phrase/nov.mp4',
    'now': 'static/intermediate-daily-phrase/now.mp4',
    'october': 'static/intermediate-daily-phrase/oct.mp4',
    'saturday': 'static/intermediate-daily-phrase/saturday.mp4',
    'seconds': 'static/intermediate-daily-phrase/seconds.mp4',
    'september': 'static/intermediate-daily-phrase/sept.mp4',
    'sunday': 'static/intermediate-daily-phrase/sunday.mp4',
    'thursday': 'static/intermediate-daily-phrase/thursday.mp4',
    'today': 'static/intermediate-daily-phrase/today.mp4',
    'tomorrow': 'static/intermediate-daily-phrase/tomorrow.mp4',
    'tonight': 'static/intermediate-daily-phrase/tonight.mp4',
    'tuesday': 'static/intermediate-daily-phrase/tuesday.mp4',
    'wednesday': 'static/intermediate-daily-phrase/wednesday.mp4',
    'week': 'static/intermediate-daily-phrase/week.mp4',
    'year': 'static/intermediate-daily-phrase/year.mp4',
    'yesterday': 'static/intermediate-daily-phrase/yesterday.mp4',
    
    'i called my friends': 'static/advance-first-person/I called my friends.mp4',
    'i exercise in the morning': 'static/advance-first-person/I exercise in the morning.mp4',
    'i love reading books': 'static/advance-first-person/I love reading books.mp4',
    'i love watching movies': 'static/advance-first-person/I love watching movies.mp4',
    'i make the bed': 'static/advance-first-person/I make the bed.mp4',
    'i need to charge my phone': 'static/advance-first-person/I need to charge my phone.mp4',
    'i went to the store': 'static/advance-first-person/I went to the store.mp4',
    'i wrote in my journal': 'static/advance-first-person/I wrote in my journal.mp4',
    'my name is': 'static/advance-first-person/My name is.mp4',
    'sorry i don`t understand': 'static/advance-first-person/Sorry i don_t understand.mp4',
    'we listened to music': 'static/advance-first-person/We listened to music.mp4',
    'we played a board games': 'static/advance-first-person/We played a board games.mp4',
    'we prepare lunch': 'static/advance-first-person/We prepare lunch.mp4',
    'we took a nap': 'static/advance-first-person/We took a nap.mp4',
    'we walk the dog': 'static/advance-first-person/We walk the dog.mp4',
    'we want to go home': 'static/advance-first-person/We want to go home.mp4',
    'we went for a walk': 'static/advance-first-person/We went for a walk.mp4',

    'all done': 'static/advanced-basic-sentences/All done.mov',
    'can you help me': 'static/advanced-basic-sentences/Can you help me.mov',
    'happy anniversary': 'static/advanced-basic-sentences/Happy Anniversary.mov',
    'happy birthday': 'static/advanced-basic-sentences/Happy Birthday.mov',
    'happy new year': 'static/advanced-basic-sentences/Happy New Year.mov',
    'how old are you': 'static/advanced-basic-sentences/How old are you.mov',
    'i don`t understand': 'static/advanced-basic-sentences/I dont understand.mov',
    'i need help': 'static/advanced-basic-sentences/I need Help.mov',
    'merry christmas': 'static/advanced-basic-sentences/Merry Christmas.mov',
    'nice to meet you': 'static/advanced-basic-sentences/Nice to meet you.mov',
    'once upon a time': 'static/advanced-basic-sentences/Once upon a time.mov',
    'see you later': 'static/advanced-basic-sentences/See you later.mov',
    'what is your name': 'static/advanced-basic-sentences/What is your name.mov',
    'Where do you live': 'static/advanced-basic-sentences/Where do you live.mov'
    
  };

  const previewContainer = document.getElementById('preview-text');
  
  function showVideo() {
    const query = document.getElementById('interpreter').value.toLowerCase();
    const videoContainer = document.getElementById('intro')
    const info = document.getElementById('text2asl')
    const webc = document.getElementById('toggle-cam')
    const btnasl = document.getElementById('toggle-txt2asl')
    const cancel = document.getElementById('cancel-asl')
    const translateform = document.getElementById('container2')
    const gttsform = document.getElementById('container2a')
    var modal = document.getElementById("errortxt2asl");
    var errormessage = document.getElementById("errmess-txt2asl")
    var headerror = document.getElementById("titleerror")
    var span = document.getElementsByClassName("close")[0];

    if (query) {
        const videoFile = videoMap[query];
        if (videoFile) {
            const videoHtml = `
                <video src="${videoFile}" autoplay controls muted>
                    Your browser does not support the video tag.
                </video>
            `;
            info.innerHTML = "Translated";
            videoContainer.innerHTML = videoHtml;
            info.style.display = "block"
            previewContainer.innerHTML = `<p>"${query}"</p>`;
            btnasl.style.display = "none";
            cancel.style.display = "block";
            webc.disabled = true;
            translateform.style.display = 'block';
            gttsform.style.display = 'none';
        }
        else {
            modal.style.display = "block";
            headerror.innerText = "⚠️ ERROR: ASL NOT FOUND ⚠️"
            errormessage.innerHTML = "We were unable to recognize the ASL word you entered. This may be due to a typo, an uncommon word, or a phrase that doesn’t align with our ASL database. Please take a moment to review your input for any spelling errors or consider rephrasing your sentence for clarity. <br><br> If you’re still having trouble, you might try using different ASL word or checking for alternative expressions.<br><br>Thank you for your understanding!";
            videoContainer.innerHTML = `<img src="error.jpg"`;
            btnasl.style.display = "block";
            info.innerHTML = "Failed Translating!";
            cancel.innerText = "Reload";
            webc.disabled = false;
            gttsform.style.display = 'none';
            translateform.style.display = 'block';
        }
    }

  btnasl.onclick = function() {
      var textareaValue = document.getElementById("interpreter").value;

      if (textareaValue.trim() === "") {
          // Show the modal if textarea is empty
          modal.style.display = "block";
      }
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
      modal.style.display = "none";
      window.location.reload();
  }

        // When the user clicks anywhere outside of the modal, do nothing
        window.onclick = function(event) {
            if (event.target == modal) {
                // Prevent closing the modal by clicking the background
                // You can comment this line if you want to close modal when clicking background
                // modal.style.display = "none";
            }
        }
  
  }

  