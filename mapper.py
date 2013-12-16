#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os,sys
import logging
import ast
import string


class wiki_pop:
     def __init__(self):
          
          self.logger_file = "wiki_log_mapper1.txt"
          self.forbid = set(('hi','hey','im','urs','ur','hav','didnt','tat','wen','1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'much', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us','u', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your'))



          self.spanish = "un una unas unos uno sobre todo también tras otro algún alguno alguna algunos algunas ser es soy eres somos sois estoy esta estamos estais estan como en para atras porque por qué estado estaba ante antes siendo ambos pero por poder puede puedo podemos podeis pueden fui fue fuimos fueron hacer hago hace hacemos haceis hacen cada fin incluso primero desde conseguir consigo consigue consigues conseguimos consiguen ir voy va vamos vais van vaya gueno ha tener tengo tiene tenemos teneis tienen el la lo las los su aqui mio tuyo ellos ellas nos nosotros vosotros vosotras si dentro solo solamente saber sabes sabe sabemos sabeis saben ultimo largo bastante haces muchos aquellos aquellas sus entonces tiempo verdad verdadero verdadera cierto ciertos cierta ciertas intentar intento intenta intentas intentamos intentais intentan dos bajo arriba encima usar uso usas usa usamos usais usan emplear empleo empleas emplean ampleamos empleais valor muy era eras eramos eran modo bien cual cuando donde mientras quien con entre sin trabajo trabajar trabajas trabaja trabajamos trabajais trabajan podria podrias podriamos podrian podriais yo aquel".decode('utf-8')

          self.french ="un una unas unos uno sobre todo también tras otro algún alguno alguna algunos algunas ser es soy eres somos sois estoy esta estamos estais estan como en para atras porque por qué estado estaba ante antes siendo ambos pero por poder puede puedo podemos podeis pueden fui fue fuimos fueron hacer hago hace hacemos haceis hacen cada fin incluso primero desde conseguir consigo consigue consigues conseguimos consiguen ir voy va vamos vais van vaya gueno ha tener tengo tiene tenemos teneis tienen el la lo las los su aqui mio tuyo ellos ellas nos nosotros vosotros vosotras si dentro solo solamente saber sabes sabe sabemos sabeis saben ultimo largo bastante haces muchos aquellos aquellas sus entonces tiempo verdad verdadero verdadera cierto ciertos cierta ciertas intentar intento intenta intentas intentamos intentais intentan dos bajo arriba encima usar uso usas usa usamos usais usan emplear empleo empleas emplean ampleamos empleais valor muy era eras eramos eran modo bien cual cuando donde mientras quien con entre sin trabajo trabajar trabajas trabaja trabajamos trabajais trabajan podria podrias podriamos podrian podriais yo aquel".decode('utf-8')
        
          self.dutch = "an af al als bij dan dat die dit een en er had heb hem het hij hoe hun ik in is je kan me men met mij nog nu of ons ook te tot uit van was wat we wel wij zal ze zei zij zo zou".decode('utf-8')
 
          
          self.german = " aber als am an auch auf aus bei bin bis bist da dadurch daher darum das daß dass dein deine dem den der des dessen deshalb die dies dieser dieses doch dort du durch ein eine einem einen einer eines er es euer eure für hatte hatten hattest hattet hier hinter ich ihr ihre im in ist ja jede jedem jeden jeder jedes jener jenes jetzt kann kannst können könnt machen mein meine mit muß mußt musst müssen müßt nach nachdem nein nicht nun oder seid sein seine sich sie sind soll sollen sollst sollt sonst soweit sowie und unser unsere unter vom von vor wann warum was weiter weitere wenn wer werde werden werdet weshalb wie wieder wieso wir wird wirst wo woher wohin zu zum zur über".decode('utf-8')
          
          self.italian = " a adesso ai al alla allo allora altre altri altro anche ancora avere aveva avevano ben buono che chi cinque comprare con consecutivi consecutivo cosa cui da del della dello dentro deve devo di doppio due e ecco fare fine fino fra gente giu ha hai hanno ho il indietro invece io la lavoro le lei lo loro lui lungo ma me meglio molta molti molto nei nella no noi nome nostro nove nuovi nuovo o oltre ora otto peggio pero persone piu poco primo promesso qua quarto quasi quattro quello questo qui quindi quinto rispetto sara secondo sei sembra sembrava senza sette sia siamo siete solo sono sopra soprattutto sotto stati stato stesso su subito sul sulla tanto te tempo terzo tra tre triplo ultimo un una uno va vai voi volte vostro ".decode('utf-8')
            
          self.norwagian = " alle andre arbeid av begge bort bra bruke da denne der deres det din disse du eller en ene eneste enhver enn er et folk for fordi forsøke fra få før først gjorde gjøre god gå ha hadde han hans hennes her hva hvem hver hvilken hvis hvor hvordan hvorfor i ikke inn innen kan kunne lage lang lik like makt mange med meg meget men mens mer mest min mye må måte navn nei ny nå når og også om opp oss over part punkt på rett riktig samme sant si siden sist skulle slik slutt som start stille så tid til tilbake tilstand under ut uten var ved verdi vi vil ville vite vår være vært å".decode('utf-8')

          self.polish = "a aby ale bardziej bardzo bez bo bowiem był była było były będzie co czy czyli dla dlatego do gdy gdzie go i ich im innych iż jak jako jednak jego jej jest jeszcze jeśli już kiedy kilka która które którego której który których którym którzy lub ma mi między mnie mogą może można na nad nam nas naszego naszych nawet nich nie nim niż o od oraz po pod poza przed przede przez przy również się sobie swoje są ta tak takie także tam te tego tej ten też to tu tych tylko tym u w we wiele wielu więc wszystkich wszystkim wszystko właśnie z za zawsze ze że ".decode('utf-8')

          self.portugese = " último é acerca agora algmas alguns ali ambos antes apontar aquela aquelas aquele aqueles aqui atrás bem bom cada caminho cima com como comprido conhecido corrente das debaixo dentro desde desligado deve devem deverá direita diz dizer dois dos e ela ele eles em enquanto então está estão estado estar estará este estes esteve estive estivemos estiveram eu fará faz fazer fazia fez fim foi fora horas iniciar inicio ir irá ista iste isto ligado maioria maiorias mais mas mesmo meu muito muitos nós não nome nosso novo o onde os ou outro para parte pegar pelo pessoas pode poderá podia por porque povo promeiro quê qual qualquer quando quem quieto são saber sem ser seu somente têm tal também tem tempo tenho tentar tentaram tente tentei teu teve tipo tive todos trabalhar trabalho tu um uma umas uns usa usar valor veja ver verdade verdadeiro você".decode('utf-8')

          self.turkish = " acaba altmış altı ama bana bazı belki ben benden beni benim beş bin bir biri birkaç birkez birşey birşeyi biz bizden bizi bizim bu buna bunda bundan bunu bunun da daha dahi de defa diye doksan dokuz dört elli en gibi hem hep hepsi her hiç iki ile INSERmi ise için katrilyon kez ki kim kimden kime kimi kırk milyar milyon mu mü mı nasıl ne neden nerde nerede nereye niye niçin on ona ondan onlar onlardan onları onların onu otuz sanki sekiz seksen sen senden seni senin siz sizden sizi sizin trilyon tüm ve veya ya yani yedi yetmiş yirmi yüz çok çünkü üç şey şeyden şeyi şeyler şu şuna şunda şundan şunu".decode('utf-8')

          self.hungarian = " a az egy be ki le fel meg el át rá ide oda szét össze vissza de hát és vagy hogy van lesz volt csak nem igen mint én te õ mi ti õk ön".decode('utf-8')

          self.english = " a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself yourselves ".decode('utf-8')

          self.czech = " dnes cz timto budes budem byli jses muj svym ta tomto tohle tuto tyto jej zda proc mate tato kam tohoto kdo kteri mi nam tom tomuto mit nic proto kterou byla toho protoze asi ho nasi napiste re coz tim takze svych jeji svymi jste aj tu tedy teto bylo kde ke prave ji nad nejsou ci pod tema mezi pres ty pak vam ani kdyz vsak ne jsem tento clanku clanky aby jsme pred pta jejich byl jeste az bez take pouze prvni vase ktera nas novy tipy pokud muze design strana jeho sve jine zpravy nove neni vas jen podle zde clanek uz email byt vice bude jiz nez ktery by ktere co nebo ten tak ma pri od po jsou jak dalsi ale si ve to jako za zpet ze do pro je na".decode('utf-8')

          self.catalan = " de es i a o un una unes uns un tot també altre algun alguna alguns algunes ser és soc ets som estic està estem esteu estan com en per perquè per que estat estava ans abans éssent ambdós però per poder potser puc podem podeu poden vaig va van fer faig fa fem feu fan cada fi inclòs primer des de conseguir consegueixo consigueix consigueixes conseguim consigueixen anar haver tenir tinc te tenim teniu tene el la les els seu aquí meu teu ells elles ens nosaltres vosaltres si dins sols solament saber saps sap sabem sabeu saben últim llarg bastant fas molts aquells aquelles seus llavors sota dalt ús molt era eres erem eren mode bé quant quan on mentre qui amb entre sense jo aquell ".decode('utf-8')

          self.danish = " af alle andet andre at begge da de den denne der deres det dette dig din dog du ej eller en end ene eneste enhver et fem fire flere fleste for fordi forrige fra få før god han hans har hendes her hun hvad hvem hver hvilken hvis hvor hvordan hvorfor hvornår i ikke ind ingen intet jeg jeres kan kom kommer lav lidt lille man mand mange med meget men mens mere mig ned ni nogen noget ny nyt nær næste næsten og op otte over på se seks ses som stor store syv ti til to tre ud var ".decode('utf-8')
           


          self.all_stop = "ön össze õ õk þey þeyden þeyi þeyler þu þuna þunda þundan þunu ¿e Å últim último úrsula ús žmogus žmones 15px 200px 250px 300px 3px a a's año aan abans aber able about above aby aby acaba according accordingly acerca across actually adesso af af after afterwards again against agora ai ain't aj al al al al ale ale algún algmas algo algun alguna algunas algunes alguno algunos alguns ali alla alle aller allo allora allow allows almost alone along alors already als also altý although altmýþ altre altri altro always am ama amb ambdós ambos among amongst ampleamos an anar anche ancora and andare ander andet andre ani another ans ant ante antes any anybody anyhow anyone anything anyway anyways anywhere ao apart apie apontar appear appreciate appropriate aquel aquela aquelas aquele aqueles aquell aquellas aquelles aquellos aquells aqui ar arba arbeid arcadio are aren't around arriba as asi aside ask asking associated at atras atrás até au aš auch aucuns auf aus aussi autre aux av available avait avant avec avere aveva avevano avoir away awfully az az bajo bana bardziej bardzo bastant fas bastante bazý be beþ became because become becomes becoming been before beforehand begge behind bei being believe belki below bem ben benden bene beni benim beside besides best bet better between beyond bez bien bij bin bir birþey birþeyi biri birkaç birkez bis bist biz bizden bizi bizim black bo bom bon bort both bowiem bra brief bruke bu bude budem budes buna bunda bundan bunu bunun buono but buti butu buvo by by³ by³a by³o by³y byl byla byli byt bé bêdzie c'est c'mon c's c'était ca cada came caminho can can't cannot cant car casa category causar cause causes cd ce cela cercare certain certainly ces cette ceux changes chaque che che chi chiese chose ci cia cierta ciertas ciertos cima cinque cjb clanek clanku clanky clearly co coisa colspan com come comes comme comment como comprare comprido con concerning conhecido consecutivi consecutivo consegueixo conseguim conseguimos conseguir consequently consider considering consigo consigue consigueix consigueixen consigueixes consiguen consigues contain containing contains coronel corrente corresponding così cosa cosa could couldn't coup course coz cual cuando cui currently cz czy czyli d'un d'une dört da da daß dabar dadurch daha daher dahi dal dalla dalsi dalt dan dann dano dans dar darum das dass dass dat daug daugiau de de debaixo decir dedans defa definitely dehors dei dein deine dejar del della delle dello dem den denne dentro depuis der deres des des described desde deshalb design desligado despite después dessen det det detonando dette deux deve devem deverá devo devrait di dia dich did didn't die dies dieser dieses different dig din dins dir direita disambig disse distribuído dit diye diz dizer dla dlatego dnes do doch does doesn't dog doing dois doit doksan dokuz don't donc donde done doppio dort dos dovere down downwards droite du due durch during début día e each ecco edu een eg egy eight ein eine eine einem einen einer eines either ej el ela ele eles ella ellas elle eller elles elli ellos ells els else elsewhere em eme empleais emplean emplear empleas empleo en en en gibi encima encontrar encore end ene eneste eneste enhver enn enough enquanto ens entirely entonces entre então eo er eramos eran erano eras erem eren eres es es especially essai esse est est esta estaba estado estais estamos estan estar estar estará estat estava este estem estes esteu esteve estic estive estivemos estiveram estoy está està estão et et etc ets etwas eu euer eure even ever every everybody everyone everything everywhere ex exactly example except exclusivamente fÅ fÛr fÛrst før fa faig faire fait faites falar fan far fare fará fatto faz fazer fazia fece fel fem fer feu few fez fi fi ficar fifth fim fin fine fino fire first five flere fleste für foi fois folk followed following follows font for fora force fordi fordi former formerly forrige fra forsÛke forth four fr fra fragen from fue fue fuer fueron fui fuimos fuori further furthermore få gÅ gal gali ganz gdy gdzie gente get gets getting giu given gives gjÛre gjorde gli go goes going gone got gotten grand gratuitamente greetings gross guardare gueno gut ha hab haben haber hace haceis hacemos hacen hacer haces had hadde hadn't hago hai han han hanno happens har hardly has hasn't hasta hat hatte hatten hattest hattet haut have haven't haver having he he he's heb hello help hem hence hendes hennes hep hepsi her here here's hereafter hereby herein hereupon hers herself het hi hier hier hinter hij him himself his hither hiç ho hoe hoeren hogy hombre home hopefully horas hors how how howbeit however hát hu hun hva hvad hvem hver hvilken hvis hvor hvordan hvorfor hvornår i i'd i'll i'm i've i¿ ich ici ide oda ie if igen ignored ihm ihn ihnen ihr ihre iki ikke il ile im immediate immer in inasmuch inc inclòs incluso ind indeed indicate indicated indicates indietro invece ingen iniciar inicio inn innen inner innych INSERmi insofar instead intenta intentais intentamos intentan intentar intentas intento internacionais intet into inward io ir irá is ise isn't ist ista iste isto it it it'd it'll it's its itself iš için j'ai ja ja jak jako jam jamais jau je je juste je¶li jede jedem jeden jeder jedes jednak jeg jego jeho jei jeigu jej jeji jejich jen jener jenes jeres jest jeste jeszcze jetzt ji jie jine jis jiz jo jog jos josé jsem jses jsme jsou já jste ju ju¿ juk juos jus just können könnt kýrk ka kad kai kaip kam kan kann kannst kas katrilyon kde kdo kdyz ke keep keeps kein kept kez ki ki kiedy kilka kim kimden kime kimi know known knows ko koennen kol kom kommer konnte kopf która które którego której który których którym którzy ktera ktere kteri kterou ktery kunne kur kuris la labai lage lang largo las last lately later latter latterly lav lavoro le least lei les less lest lesz let let's leur lhe lidt ligado lik like liked likely lille little livro llarg llavors llegar llevar lo look looking looks loro los ltd lub lui lungo lupin là là mÅ mÅte mý ma machen mai mainly maintenant maioria maiorias mais makt mal man man mand mange mano many mas mate material may maybe mdash me mean meanwhile med meget meglio mehr mein meine men mens mentre mer mere merely mes mesmo mest met meu mezi mi mich mientras mig might mij milyar milyon min mine mint mio mir mirar mismo mit miêdzy mü müßt mnie müssen mo¿e mo¿na mode modo mog± moi moins molt molta molti molto molts mon more moreover most mostly mot más mu muß mußt much mucho muchos muito muitos muj musst must musu muy muze my mye myself même même nós nÅ nÅr nær næste næsten na nach nachdem nad nam name namely napiste nas nasýl nasi naszego naszych navn nawet über nbsp nd ndash ne near nearly nebo nebuvo necessary ned neden need needs nei nein neither nejsou nel nella nem neni vas nera nerde nerede nereye nes net never nevertheless neville new next nez ni ni¿ nic nich nicht nie nieko niente nim nine niye niçin nl no no nobody noch noche nog nogen noget noi nome nommés non none noone nor normally nors nos nosaltres nosotros nosso nostro not nothing notre nous nous nouveaux nove novel novidade novo novy now nowhere nu nunca nuo nuovi nuovo nur ny nyt não üç o où obviously od oder of off often og ogsÅ oh ok okay old oltre om on ona once ondan onde one ones onlar onlarýn onlardan onlari only ons onto onu otuz ook op opp or ora oraz os oss other others otherwise otro otte otto ou ought our ours ourselves out outro outside over overall own pÅ pagar pak par par para parce parecer parole part parte particular particularly pas pasake pasar pat pats pegar peggio pela pelas pelo pensar per per que però perché perguntar perhaps pero perquè persone personnes pessoa pessoal pessoas petit peu peut più piton piu pièce pl placed please plupart plus po poco pod pode podeis podem podemos poden poder poderá podia podeu podle podria podriais podriamos podrian podrias poi pokud por por qué porque porta portaldetonando porte possa possible potser pour pourquoi pouze povo poza prave pred pres presumably pri prie prieš primer primero desde primo pro probably proc promeiro promesso proprio protegido proto protoze provides prvni przed przede przez przy pt pta puc puede pueden puedo puerta puis punkt på qu'il qua qual qualquer quan quand quando quant quarto quasi quattro que quedar quel quel quella quelles quello quelque quels quem questo questo qui quien quieto quindi quinto quite qué qv równie¿ ragazzo rapaz rather rd re really reasonably redirect regarding regardless regards relatively respectively responsabiliza rett right riktig rispetto ro rogue ron rony rá ru répondit s sólo s± ta sa sa sabe sabeis sabem sabemos saben saber sabes sabeu sagen sah said same samme sanki sans sant sap saps sara savo saw say saying says schon se second secondly secondo see seeing seem seemed seeming seems seen segundo sehen sei seid sein seine sekiz seks seksen self selves sem sembra sembrava sempre sen senden seni senin sense sensible sent senza ser serious seriously ses sette seu seulement seus seven several shall she should shouldn't si sia siamo sich siden sie sien siendo siete silente sin since sind sist six siz sizden sizi sizin siê skulle sl slik slutt snape so sobie sobre soc sofija sois solament solamente soll sollen sollst sollt solo sols som some somebody somehow somente someone something sometime sometimes somewhat somewhere somos son sono sonst sont soon sopra soprattutto sorry sota sotto sous soweit sowie soy soyez specified specify specifying sr át stare start stati stato stava stesso still stille sÅ stor store strana stub su sua sub subito such sujet sul sulla suo sup sur sure sus sv sve svych svym svymi swoje syv szét são t t's ta taciau tada tai taip tak tak¿e take taken takie takze tal tam también també também tan tandis tanto tare tarp tato te te¿ tedy tego tej tell tellement tels tem tema tempo temps ten tends tene teneis tenemos tener tengo tenho tenim tenir teniu tentar tentaram tente tentei tento ter terzo tes testa teto bylo teu teve th than thank thanks thanx that that's thats the their theirs them themselves then thence there there's thereafter thereby therefore therein theres thereupon these they they'd they'll they're they've think third this thorough thoroughly those though three through throughout thru thus ti tid tiek tiempo tiene tienen tik til tilbake tilstand tim timto tinc tinha tio tipo tipy tive tüm to todel todo todos together tohle toho tohoto tom tomto tomuto ton too took tot tous tout toward towards tra trabaja trabajais trabajamos trabajan trabajar trabajas trabajo trabalhar trabalho tras tratar tre tried tries trilyon triplo trop truly try trying très tu turi tuto tutto tuyo twice two ty tych tylko tym tyto têm tête u už ud ueber uit ultimo um uma umas un una unas und under une unes unfortunately unless unlikely uno unos uns unser unsere unter until unto up upon us usa usais usamos usan usar usas use used useful user user_talk uses using uso usually ut utc uten uz vÖre vÖrt vÅr va va va vagy vai vaig vais value vam vamos van var various vase vaya ve ve ved veja vel velho ver ver verdad verdade verdadeiro verdadera cierto verdadero verdi vernon vers very veya vez vi via vice viena vienas vil ville vis visi viskas vissza vite viz você voi voie voient voir voix volt csak volte volver vom von vont vor vosaltres vosotras vosotros vostro votre vous voy vs vsak vu w w³a¶nie wann want wants war warum was was wasn't wat way we we'd we'll we're we've weiter weitere wel welcome well wenn went wer werde werden werdet were weren't weshalb what what's whatever when whence whenever where where's whereafter whereas whereby wherein whereupon wherever whether which while whither who who's whoever whole whom whose why wie wieder wiele wielu wieso wij will willing wir wird wirst wish with within without wiêc wo woher wohin wollen won't wonder would wouldn't wszystkich wszystkim wszystko wuerde y ya yani yedi yes yet yetmiþ yeux yirmi yüz yo you you'd you'll you're you've your yours yourself yourselves yra z za zal zawsze zda zde ze zei zero zh zij zio zo zou zpet zpravy zu zum zur à é él én és éssent étaient était état étions été ça çünkü çok è être".decode('utf-8')

 
          self.stop_word_sen = self.danish +" " +self.catalan + " "+ self.czech + " "+self.english +" " +self.hungarian +" "+" " +self.turkish +" " +self.portugese +" " +self.polish +" "+ self.norwagian +" "+ self.italian +" "+ self.german +" "+ self.spanish +" "+ self.french +" "+ self.dutch
          stop_sen = self.stop_word_sen + " "+self.all_stop
          self.forbid.update(set(stop_sen.split(" ")))


     def initialize_logger(self):
          
         logging.basicConfig(filename=self.logger_file, level=logging.INFO)
         logging.info("Initialized logger")
         
     def mapper(self):
          #self.initialize_logger()
         
          #Mapper function for preprocessing
          #f=open('tweets_file','r')
          #output = open('output','a')
          for line in sys.stdin:
          #for line in f:
               try:
                    if not line:
                         #print "line was empty"
                         continue
                    tweet_obj = ast.literal_eval(line.decode('utf-8'))
                    line = tweet_obj.get('text')
                    word_list = line.split()
                    for word in word_list:
                         if not word.strip():
                            continue                         
                         word = word.strip()
        
                         if len(word) < 3:
                            continue

                         if not word.isalnum() or not  word[0].isalpha():
                                continue

                         if word[0]=='@' or word[0:4]=="http" or word=="RT":
                              continue
                         out = word.translate(string.maketrans("",""), string.punctuation)
                         outword = out.strip()
                         if outword:
                              if outword.lower() not in self.forbid:
                                   print "%s\t1" % (outword.lower())
                                   #output.write(outword.lower()+"\t"+"1"+"\n")

               except:
                    continue
          #f.close()
          #output.close()
                                    
               
                    

                    
           
if __name__ == "__main__":
    wp_obj = wiki_pop()
    wp_obj.mapper() 
                

        
        