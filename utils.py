from bs4 import BeautifulSoup
disease_dic = {
    'Apple___Apple_scab': """ <b>Crop</b>: Apple <br/>Disease: Apple Scab<br/>
        <br/> Cause of disease:
        <br/><br/> 1. Apple scab overwinters primarily in fallen leaves and in the soil. Disease development is favored by wet, cool weather that generally occurs in spring and early summer.
        <br/> 2. Fungal spores are carried by wind, rain or splashing water from the ground to flowers, leaves or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection. The longer the leaves remain wet, the more severe the infection will be. Apple scab spreads rapidly between 55-75 degrees Fahrenheit.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Choose resistant varieties when possible.
        <br/>2. Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring
        
        <br/>3. Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.
        <br/>4. Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores.""",

    'Apple___Black_rot': """ <b>Crop</b>: Apple <br/>Disease: Black Rot<br/>
        <br/> Cause of disease:
        <br/><br/>Black rot is caused by the fungus Diplodia seriata (syn Botryosphaeria obtusa).The fungus can infect dead tissue as well as living trunks, branches, leaves and fruits. In wet weather, spores are released from these infections and spread by wind or splashing water. The fungus infects leaves and fruit through natural openings or minor wounds.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Prune out dead or diseased branches.
        <br/>2. Prune out dead or diseased branches.
        
        <br/>3. Remove infected plant material from the area.
        <br/>4. Remove infected plant material from the area.
        <br/>5. Be sure to remove the stumps of any apple trees you cut down. Dead stumps can be a source of spores.""",

    'Apple___Cedar_apple_rust': """ <b>Crop</b>: Apple <br/>Disease: Cedar Apple Rust<br/>
        <br/> Cause of disease:
        <br/><br/>Cedar apple rust (Gymnosporangium juniperi-virginianae) is a fungal disease that depends on two species to spread and develop. It spends a portion of its two-year life cycle on Eastern red cedar (Juniperus virginiana). The pathogen’s spores develop in late fall on the juniper as a reddish brown gall on young branches of the trees.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Since the juniper galls are the source of the spores that infect the apple trees, cutting them is a sound strategy if there aren’t too many of them.
        <br/>2. While the spores can travel for miles, most of the ones that could infect your tree are within a few hundred feet.
        
        <br/>3. The best way to do this is to prune the branches about 4-6 inches below the galls.""",



    'Apple___healthy': """ <b>Crop</b>: Apple <br/>Disease: No disease<br/>
        <br/><br/> Don't worry. Your crop is healthy. Keep it up !!!""",



    'Grape___Black_rot': """ <b>Crop</b>: Grape <br/>Disease: Black Rot<br/>
        <br/> Cause of disease:
        <br/><br/> 1. The black rot fungus overwinters in canes, tendrils, and leaves on the grape vine and on the ground. Mummified berries on the ground or those that are still clinging to the vines become the major infection source the following spring.
        <br/> 2. During rain, microscopic spores (ascospores) are shot out of numerous, black fruiting bodies (perithecia) and are carried by air currents to young, expanding leaves. In the presence of moisture, these spores germinate in 36 to 48 hours and eventually penetrate the leaves and fruit stems. 
        <br/> 3. The infection becomes visible after 8 to 25 days. When the weather is wet, spores can be released the entire spring and summer providing continuous infection.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Space vines properly and choose a planting site where the vines will be exposed to full sun and good air circulation. Keep the vines off the ground and insure they are properly tied, limiting the amount of time the vines remain wet thus reducing infection.
        <br/>2. Keep the fruit planting and surrounding areas free of weeds and tall grass. This practice will promote lower relative humidity and rapid drying of vines and thereby limit fungal infection.
        
        <br/>3. Use protective fungicide sprays. Pesticides registered to protect the developing new growth include copper, captan, ferbam, mancozeb, maneb, triadimefon, and ziram. Important spraying times are as new shoots are 2 to 4 inches long, and again when they are 10 to 15 inches long, just before bloom, just after bloom, and when the fruit has set.""",



    'Grape___Esca_(Black_Measles)': """ <b>Crop</b>: Grape <br/>Disease: Black Measles<br/>
        <br/> Cause of disease:
        <br/><br/> 1. Black Measles is caused by a complex of fungi that includes several species of Phaeoacremonium, primarily by P. aleophilum (currently known by the name of its sexual stage, Togninia minima), and by Phaeomoniella chlamydospora.
        <br/> 2. The overwintering structures that produce spores (perithecia or pycnidia, depending on the pathogen) are embedded in diseased woody parts of vines. The overwintering structures that produce spores (perithecia or pycnidia, depending on the pathogen) are embedded in diseased woody parts of vines.
        <br/> 3. During fall to spring rainfall, spores are released and wounds made by dormant pruning provide infection sites.
        <br/> 4. Wounds may remain susceptible to infection for several weeks after pruning with susceptibility declining over time.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Post-infection practices (sanitation and vine surgery) for use in diseased, mature vineyards are not as effective and are far more costly than adopting preventative practices (delayed pruning, double pruning, and applications of pruning-wound protectants) in young vineyards. 
        <br/>2. Sanitation and vine surgery may help maintain yields. In spring, look for dead spurs or for stunted shoots. Later in summer, when there is a reduced chance of rainfall, practice good sanitation by cutting off these cankered portions of the vine beyond the canker, to where wood appears healthy. Then remove diseased, woody debris from the vineyard and destroy it.
        
        <br/>3. The fungicides labeled as pruning-wound protectants, consider using alternative materials, such as a wound sealant with 5 percent boric acid in acrylic paint (Tech-Gro B-Lock), which is effective against Eutypa dieback and Esca, or an essential oil (Safecoat VitiSeal).""",

    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': """ <b>Crop</b>: Grape <br/>Disease: Leaf Blight<br/>
        <br/> Cause of disease:
        <br/><br/> 1. Apple scab overwinters primarily in fallen leaves and in the soil. Disease development is favored by wet, cool weather that generally occurs in spring and early summer.
        <br/> 2. Fungal spores are carried by wind, rain or splashing water from the ground to flowers, leaves or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection. The longer the leaves remain wet, the more severe the infection will be. Apple scab spreads rapidly between 55-75 degrees Fahrenheit.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Choose resistant varieties when possible.
        <br/>2. Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring
        
        <br/>3. Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.
        <br/>4. Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores.""",

    'Grape___healthy': """ <b>Crop</b>: Grape <br/>Disease: No disease<br/>
        <br/><br/> Don't worry. Your crop is healthy. Keep it up !!!""",



    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': """<b> Crop</b> : Grape <br/> Disease: Leaf Spot""",


    'Orange___Haunglongbing_(Citrus_greening)': """ <b>Crop</b>: Orange <br/>Disease: Citrus Greening<br/>
        <br/> Cause of disease:
        <br/><br/>  Huanglongbing (HLB) or citrus greening is the most severe citrus disease, currently devastating the citrus industry worldwide. The presumed causal bacterial agent Candidatus Liberibacter spp. affects tree health as well as fruit development, ripening and quality of citrus fruits and juice.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. In regions where disease incidence is low, the most common practices are avoiding the spread of infection by removal of symptomatic trees, protecting grove edges through intensive monitoring, use of pesticides, and biological control of the vector ACP.
        <br/>2. According to Singerman and Useche (2016), CHMAs coordinate insecticide application to control the ACP spreading across area-wide neighboring commercial citrus groves as part of a plan to address the HLB disease.
        
        <br/>3. In addition to foliar nutritional sprays, plant growth regulators were tested, unsuccessfully, to reduce HLB-associated fruit drop (Albrigo and Stover, 2015).""",



    'Potato___healthy': """ <b>Crop</b>: Potato <br/>Disease: No disease<br/>
        <br/><br/> Don't worry. Your crop is healthy. Keep it up !!!""",


    'Strawberry___healthy': """ <b>Crop</b>: Strawberry <br/>Disease: No disease<br/>
        <br/><br/> Don't worry. Your crop is healthy. Keep it up !!!""",



    'Potato___Early_blight': """ <b>Crop</b>: Potato <br/>Disease: Early Blight<br/>
        <br/> Cause of disease:
        <br/><br/> 1. Early blight (EB) is a disease of potato caused by the fungus Alternaria solani. It is found wherever potatoes are grown. 
        <br/> 2. The disease primarily affects leaves and stems, but under favorable weather conditions, and if left uncontrolled, can result in considerable defoliation and enhance the chance for tuber infection. Premature defoliation may lead to considerable reduction in yield.
        <br/> 3. Primary infection is difficult to predict since EB is less dependent upon specific weather conditions than late blight.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Plant only diseasefree, certified seed. 
        <br/>2. Follow a complete and regular foliar fungicide spray program.
        
        <br/>3. Practice good killing techniques to lessen tuber infections.
        <br/>4. Allow tubers to mature before digging, dig when vines are dry, not wet, and avoid excessive wounding of potatoes during harvesting and handling.""",


    'Potato___Late_blight': """ <b>Crop</b>: Potato <br/>Disease: Late Blight<br/>
        Late blight is a potentially devastating disease of potato, infecting leaves, stems and fruits of plants. The disease spreads quickly in fields and can result in total crop failure if untreated. Late blight of potato was responsible for the Irish potato famine of the late 1840s.              
        <br/> Cause of disease:
        <br/><br/> 1. Late blight is caused by the oomycete Phytophthora infestans. Oomycetes are fungus-like organisms also called water molds, but they are not true fungi.
        <br/> 2. There are many different strains of P. infestans. These are called clonal lineages and designated by a number code (i.e. US-23). Many clonal lineages affect both tomato and potato, but some lineages are specific to one host or the other.
        <br/> 3. The host range is typically limited to potato and tomato, but hairy nightshade (Solanum physalifolium) is a closely related weed that can readily become infected and may contribute to disease spread. Under ideal conditions, such as a greenhouse, petunia also may become infected.
        
        
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Seed infection is unlikely on commercially prepared tomato seed or on saved seed that has been thoroughly dried.
        <br/>2. Inspect tomato transplants for late blight symptoms prior to purchase and/or planting, as tomato transplants shipped from southern regions may be infected
        
        <br/>3. If infection is found in only a few plants within a field, infected plants should be removed, disced-under, killed with herbicide or flame-killed to avoid spreading through the entire field.""",


    'Squash___Powdery_mildew': """ <b>Crop</b>: Squash <br/>Disease: Powdery mildew<br/>
        <br/> Cause of disease:
        <br/><br/> 1. Powdery mildew infections favor humid conditions with temperatures around 68-81° F
        <br/> 2. In warm, dry conditions, new spores form and easily spread the disease.
        <br/> 3. Symptoms of powdery mildew first appear mid to late summer in Minnesota.  The older leaves are more susceptible and powdery mildew will infect them first.
        <br/> 4. Wind blows spores produced in leaf spots to infect other leaves.
        <br/> 5. Under favorable conditions, powdery mildew can spread very rapidly, often covering all of the leaves.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Apply fertilizer based on soil test results. Avoid over-applying nitrogen.
        <br/>2. Provide good air movement around plants through proper spacing, staking of plants and weed control.
        
        <br/>3. Once a week, examine five mature leaves for powdery mildew infection. In large plantings, repeat at 10 different locations in the field.
        <br/>4. If susceptible varieties are growing in an area where powdery mildew has resulted in yield loss in the past, fungicide may be necessary.""",


    'Strawberry___Leaf_scorch': """ <b>Crop</b>: Strawberry <br/>Disease: Leaf Scorch<br/>
        <br/> Cause of disease:
        <br/><br/> 1. Scorched strawberry leaves are caused by a fungal infection which affects the foliage of strawberry plantings. The fungus responsible is called Diplocarpon earliana.
        <br/> 2. Strawberries with leaf scorch may first show signs of issue with the development of small purplish blemishes that occur on the topside of leaves.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Since this fungal pathogen over winters on the fallen leaves of infect plants, proper garden sanitation is key.
        <br/>2. This includes the removal of infected garden debris from the strawberry patch, as well as the frequent establishment of new strawberry transplants.
        
        <br/>3. The avoidance of waterlogged soil and frequent garden cleanup will help to reduce the likelihood of spread of this fungus.""",

   
}
# Loop through each entry in the dictionary
for key, value in disease_dic.items():
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(value, 'html.parser')
    # Extract the text content
    text_content = soup.get_text()
    # Update the dictionary entry with the text content
    disease_dic[key] = text_content
