# Initial prompt, 2026-09-30 (Swedish original, verbatim)

Given to Claude Code (model Claude Fable 5.1) at 07:29 local time on 2026-09-30, with the
source material in `docs/` available to it. English translation: `2026-09-30-initial-model-prompt.en.md`.

---

Du ska bygga en första teknisk prototyp av en agentbaserad modell (ABM) för organiserad avfallsbrottslighet i Sverige.

Bakgrund
Projektet är forskningsnära. Forskargruppen har samlat kunskap om organiserad avfallsbrottslighet, svenska aktörer, myndighetsprocesser, ekonomiska incitament, brottsupplägg och relevant ABM-litteratur. Samma litteratur och underlag som använts i projektet finns i katalogen:

docs/

Du ska använda detta material som primär källa. Läs dokumenten innan du designar modellen. Om något inte stöds av källmaterialet ska du inte hitta på det. Markera i stället tydligt att det är ett antagande, en förenkling eller en öppen fråga.

Mål
Målet är inte att bygga en färdig vetenskapligt validerad modell. Målet är att skapa en första körbar prototyp som gör forskargruppens idéer konkreta och som hjälper oss att identifiera:

1. vilka agenter som behöver finnas,
2. vilka egenskaper agenterna behöver,
3. vilka relationer som behöver modelleras,
4. vilka beslut agenterna fattar,
5. vilka brottsförlopp/pathways som behöver finnas,
6. vilka myndighetsinterventioner som kan simuleras,
7. vilka data som behövs för kalibrering,
8. vilka delar som fortfarande saknar tillräckligt empiriskt stöd,
9. vilka outputs som är meningsfulla att mäta.

Arbetssätt
Arbeta iterativt och bygg en minimal men körbar modell först.

Viktigt:
- börja inte med ett stort eller komplext system,
- använd Python om inget i materialet starkt talar för något annat,
- välj en etablerad och enkel ABM-struktur eller ett lämpligt bibliotek om det förenklar arbetet,
- prioritera begriplighet och spårbarhet framför teknisk elegans,
- varje större modelleringsbeslut ska kunna härledas till källmaterialet eller markeras som ett explicit antagande.

Dokumentation
Skapa från början ett dokument, till exempel:

ABM_MODEL_NOTES.md

Det dokumentet ska uppdateras löpande under hela arbetet.

Dokumentet ska skrivas på svenska och vara avsett för en icke-teknisk läsare, exempelvis forskare, verksamhetsexperter eller beställare som inte kan programmering.

Det ska förklara:
- vad en ABM är i just detta projekt,
- vilka delar modellen består av,
- vilka agenter som finns,
- vad varje agent representerar,
- vilka egenskaper agenterna har,
- hur agenterna fattar beslut,
- hur de interagerar,
- vad modellens "environment"/landscape består av,
- vilka antaganden modellen gör,
- varför dessa antaganden görs,
- vilka val som bygger på källmaterial,
- vilka val som är provisoriska,
- vilka delar som är osäkra,
- hur simuleringen går till steg för steg,
- vilka scenarier/interventioner som kan testas,
- vilka resultat modellen producerar,
- hur resultaten ska tolkas,
- vad modellen inte kan säga,
- vilka data som senare behövs för bättre kalibrering och validering.

Undvik tekniskt språk när det inte behövs. Om tekniska begrepp används ska de förklaras direkt.

Källor
När du bygger modellen ska du först inventera dokumenten i docs/ och identifiera vilka som används till vad.

Skapa gärna en sektion i ABM_MODEL_NOTES.md:

"Källor och hur de används"

Där kan du exempelvis beskriva:
- metodlitteratur om ABM,
- forskning om organiserad brottslighet,
- forskning om illegala supply chains,
- svenska rapporter om avfallsbrott,
- material om myndighetsprocesser,
- fallstudier som Think Pink, Black Mass och Stena Recycling,
- material om risk, reward, effort och propensity,
- material om olika pathways till avfallsbrott.

Modellens första version
Utgå från materialet i docs/ och försök skapa en första konceptuell modell med så få agenttyper som möjligt.

Möjliga agenttyper att undersöka är exempelvis:
- avfallsproducenter,
- avfallsföretag,
- transportörer,
- mottagnings-/behandlingsanläggningar,
- brokers/mellanhänder,
- frontmän/formella företrädare,
- faktiska beslutsfattare,
- organiserade kriminella aktörer,
- tillsynsmyndigheter,
- polis/andra brottsbekämpande myndigheter.

Använd inte automatiskt alla. Bedöm utifrån källmaterialet vilka som faktiskt behövs i en första prototyp.

Modellen bör kunna representera att:
- avfall genereras,
- avfallet behöver tas om hand,
- olika aktörer kan välja mellan laglig och olaglig hantering,
- olaglig hantering kan vara ekonomiskt attraktiv genom undvikna kostnader,
- företag och individer kan vara olika benägna att bryta mot regler,
- risken för upptäckt påverkar beslut,
- myndigheter har begränsade resurser,
- tillsyn och kontroller kan förändra riskbilden,
- aktörer kan anpassa sig till kontroll och tillsyn.

Undersök särskilt om beslutslogiken kan uttryckas med den typ av nyttofunktion som finns i materialet:

U = reward + propensity - effort - risk

och där risk i sin tur kan bero på:
- sannolikhet att bli upptäckt,
- sannolikhet att bli sanktionerad,
- sanktionens storlek.

Använd dock inte formeln mekaniskt om underlagen visar att modellen behöver vara mer nyanserad.

Brottsförlopp
Materialet tyder på att avfallsbrott inte bör modelleras som en enda mekanism.

Undersök därför åtminstone följande pathways:
- illegal dumpning / illegal disposal,
- illegal avfallshantering som växer fram gradvis,
- felklassificering eller omklassificering av avfall,
- illegal transport/export,
- användning av legala bolag som fasad,
- användning av frontmän eller bolagsmäklare,
- manipulation av dokumentation,
- byte av bolag när tillsyn eller skulder ökar.

I första prototypen kan du välja en eller två pathways om det behövs för att hålla modellen liten.

Environment / landscape
En central fråga från forskargruppen är hur modellens "landscape" ska se ut.

Analysera källorna och dokumentera möjliga alternativ, exempelvis:
- geografisk miljö,
- nätverk av företag och personer,
- avfallsflöde/supply chain,
- regulatorisk miljö,
- kombination av nätverk och flöden.

Välj den enklaste struktur som räcker för en första prototyp och förklara varför.

Simulation
Bygg en tydlig simulationsloop.

Exempelvis:
1. avfall uppstår,
2. en aktör behöver hitta hantering,
3. möjliga alternativ identifieras,
4. agenten fattar beslut,
5. avfallet flyttas eller hanteras,
6. eventuellt brott sker,
7. myndigheter genomför vissa kontroller,
8. eventuella brott upptäcks,
9. sanktioner eller andra konsekvenser inträffar,
10. agenternas tillstånd uppdateras,
11. nästa tidssteg börjar.

Detta är bara ett exempel. Anpassa efter vad källmaterialet faktiskt stödjer.

Scenarier
Modellen bör tidigt kunna jämföra ett baseline-scenario med några enkla interventioner.

Exempel att undersöka:
- högre kontrollfrekvens,
- mer riktad tillsyn,
- högre sanktioner,
- bättre informationsdelning mellan myndigheter,
- högre upptäcktsrisk,
- kontroller riktade mot transportörer,
- kontroller riktade mot högriskföretag eller brokers.

Implementera bara sådana scenarier som går att motivera från källorna.

Outputs
Identifiera och implementera några få tydliga outputs, exempelvis:
- andel avfall som hanteras olagligt,
- antal illegala händelser,
- antal upptäckta brott,
- antal oupptäckta brott,
- ekonomisk vinst från illegal hantering,
- vilka agenttyper som oftast deltar,
- vilka aktörer som blir centrala i nätverket,
- hur resultatet förändras mellan olika interventioner.

Teknisk struktur
Strukturera koden så att det är lätt att:
- lägga till nya agenttyper,
- ändra parametrar,
- lägga till nya pathways,
- lägga till nya scenarier,
- byta ut syntetiska data mot verkliga data senare.

Separera gärna:
- agentdefinitioner,
- modell/simulationsloop,
- parametrar,
- scenarios,
- outputs,
- körscript,
- dokumentation.

Skapa gärna en enkel config-fil eller motsvarande så att parametrar inte behöver hårdkodas överallt.

Data
Första versionen får använda syntetiska eller förenklade data om det behövs.

Men:
- dokumentera tydligt vilka värden som är verkliga och vilka som är påhittade,
- använd inte påhittade värden som om de vore empiriskt belagda,
- identifiera vilka parametrar som senare bör kalibreras mot verkliga svenska data.

Validering
Bygg inte en fullständig valideringslösning nu, men skapa stöd för att senare kunna jämföra modellen med empiriska data.

Dokumentera vilka empiriska mönster från materialet som skulle kunna användas för validering, exempelvis:
- andel företag med kriminella kopplingar,
- struktur på företagsnätverk,
- antal transportörer,
- kontrollfrekvenser,
- typiska brottsförlopp,
- relation mellan legal och illegal avfallshantering,
- observerade fall som Think Pink, Black Mass eller Stena Recycling.

Arbetsordning
Arbeta ungefär i följande ordning:

1. Läs och inventera docs/.
2. Skriv en kort källöversikt i ABM_MODEL_NOTES.md.
3. Identifiera forskargruppens konceptuella modell.
4. Lista möjliga agenter, variabler, relationer och beslut.
5. Identifiera vad som är empiriskt belagt och vad som saknas.
6. Föreslå en minimal första ABM.
7. Dokumentera förslaget innan kodningen börjar.
8. Implementera modellen.
9. Kör några enkla simuleringar.
10. Dokumentera vad resultaten betyder.
11. Identifiera svagheter, dataluckor och nästa utvecklingssteg.
12. Förbättra prototypen om det går utan att göra modellen onödigt komplex.

När du gör större ändringar i modellen:
- uppdatera alltid ABM_MODEL_NOTES.md,
- skriv varför ändringen gjordes,
- skriv vilken källa eller vilket antagande som ligger bakom,
- skriv vad ändringen förväntas påverka.

Definition of done
Arbetet är klart när det finns:

- en körbar minimal ABM-prototyp,
- tydligt definierade agenter,
- definierade beslut och interaktioner,
- minst ett baseline-scenario,
- minst ett interventionsscenario,
- några enkla outputs,
- ett reproducerbart sätt att köra simuleringen,
- ett utförligt men lättbegripligt ABM_MODEL_NOTES.md,
- en lista över empiriska dataluckor,
- en lista över öppna forskningsfrågor,
- en bedömning av vad som krävs för att gå från prototyp till vetenskapligt användbar modell.

Viktig princip
Se prototypen som ett verktyg för att göra forskarnas antaganden explicita.

När du stöter på en fråga som exempelvis:
"hur stor ska sannolikheten vara att företag X väljer illegal hantering?"

ska du inte bara hitta på ett värde.

Gör i stället något i stil med:
- skapa en konfigurerbar parameter,
- välj ett neutralt demonstrationsvärde om det behövs för att kunna köra modellen,
- markera tydligt i dokumentationen att värdet är provisoriskt,
- skriv vilken typ av empirisk information som behövs för att ersätta det.

Målet är alltså lika mycket att upptäcka vilka frågor forskargruppen måste svara på som att skriva fungerande kod.
