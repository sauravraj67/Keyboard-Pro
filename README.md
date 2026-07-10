# Keyboard Pro



<img width="1158" height="550" alt="Screenshot 2026-06-08 170318" src="https://github.com/user-attachments/assets/841aec48-1cd3-44ef-9f79-7b16b6ec1393" />

I built a 65% layout keyboard based on Seed Studio Xiao nrf52840 also It will have a 3.7v battery and an 0.91 inch OLED Screen. Switches will be HotSwapable. I used expander to connect the rows and coluns because there weren't enough pins available.

## Features
-  nrf52840 Rp2040
- uses 65% Keyboard Layout 
-  Uses Keyboard Matrix
-  Had a rotor encoder and an 0.91 inch oled screen


  | Item | Price | Source |
|------|------:|--------|
| PCB + Shipping - Coupons | 25.14 | JLCPCB |
| KeyCaps | 15.04 | https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/gengar-anime-keycap-set/ |
| Hot-swap (pack of 10) × 7 | 5.50 | https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/kailh-hot-swap-socket/?attribute_pa_variations=white |
| Switches (pack of 10) × 7 | 22.10 | https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/hmx-xinhai-switch/?attribute_pa_key-switches=hmx-xinhai-45g |
| Stabilizers | 10.76 | https://meckeys.com/shop/accessories/keyboard-accessories/more/glorious-goat-stabilizers/ |
| Meckeys Shipping | 1.10 | https://meckeys.com |
| Expander × 2 | 6.22 | https://robu.in/product/pca9555dwr-texas-instruments-400khz-soic-24-300mil-i-o-expanders-rohs/ |
| XIAO BLE nRF52840 | 12.40 | https://robu.in/product/seeed-studio-xiao-ble-nrf52840/ |
| On-Off Switch | 1.12 | https://robu.in/product/os202011ma0qn1-ck-100ma-dpdt-12v-10000-times-plugin-slide-switches-rohs/ |
| 2MΩ Resistor | 0.13 | https://robu.in/product/crcw12062m20fkea-vishay-smd-chip-resistor-2-2-mohm-%c2%b1-1-250-mw-1206-3216-metric-thick-film-general-purpose/ |
| 806kΩ Resistor | 0.13 | https://robu.in/product/rc0402fr-07806kl-yageo-smd-chip-resistor-806-kohm-%c2%b1-1-63-mw-0402-1005-metric-thick-film-general-purpose/ |
| Robu Shipping | 1.10 | https://robu.in |
| Solder Paste for SMD Components | 2.70 | https://www.amazon.in/gp/product/B0GY879KCL/ |
| 1N4148W-T4 Diodes (Pack of 15) × 5 ( used amazon beacuse wasn't avilable anywhere else)| 11.78 | https://www.amazon.in/gp/product/B0FZL2D1GG/ |
| **Total** | **115.22** | |

### Schematic<br><br>

## Made the Key-Matrix 
Hours- 5.5 hr <br>
So I opened the schematics and added a key switch and a diode. Then I had my way toward how many switches would be there per row . The number of keys per row wasn't constant So I made a rough sketch about how would I assign the columns and rows to each Key switch. after that as I would be using keyboard matrix ,so I needed to add a diode to each key switch to prevent ghosting. Then I started making the switch layout . I also kept in mind that each switches aren't of same length so I had to use specific footprints for each switches specifically as per the 65 % standard layout. The Switches will be hot-swapable as well. While making the switch matrix it was a bit time consuming as I tried to organized the switches as well as per there layout ,so that it will be easy for me to connect the wires.While reviewing I found a few placement and footprint mistakes so I solved them then I moved toward making the rows and columns connection and adding the labels to them So this is how it looks.<img width="948" height="282" alt="Screenshot 2026-06-07 231856" src="https://github.com/user-attachments/assets/ef217032-1269-45cf-a9d6-eaad2f930c29" />

<br>

## Adding other components

Hours :- 2.5 hr <br>
So there is no footprint and symbol for the Xioa nRF52840 , So I downloaded them and added it to kicad also I knew that there weren't enough numbers of gpio pins on the Xiao nRF52840 so handle all the 15 columns and 5 rows So I needed to use an expander , So for that I used PCA9555D and read it's data sheet a bit , It will communicate to the MCU via I2C protocol , So I started adding the rows and columns label to it but even one expander wasn't enough So I had to add a second one to add the connections of all rows and columns then I did all the other connection on the expander.after that I added pins for Battery connection. the battery that we would be using will be of 3.7v lithium ion battery. and made a battery sense circuit. the nRF52840 has inbuild battery charging IC and it can control the charring part so I don't to add anything more after that I added a 4 pins for 0.91 inch oled display and added labels to it.after that I connected every label to the Xiao nRF52840. So this is how the final schematics look

<img width="1066" height="602" alt="Screenshot 2026-06-08 015730" src="https://github.com/user-attachments/assets/67299736-3179-49bb-b96d-e3e75a65549e" />

###  PCB Design<br><br>

## Started with PCB ( Component placement)
Hours :- 4.75 hours <br>
SO I started with the hard part. Arranging the switches . I used a Grid of 19.05U so that the switches snap easily but that wasn't the case . I tried to snap them with each other via using different grid sizes and moving them then they use to snap properly. It look me a long time snapping the switches and overt to that placing switches at the right Place because each rows doesn't have same number of rows I had to align the first switch to the right place , also I added Stabilizers for any switch whose footprint was over 2.25U. The main thing was choosing the right Switch while placing and the most hectic thing was that switches don't use to snap directly . I have to move it around using different grid sizes to achieve the goal . Then I added the Xiao nRF52840 to the right top side a bit away from the corner then added the switches after that placed the Oled screen in the free space and added the expanders in places where there was free space I made few alteration of the keyboard but finally ended up with this after that I placed the diodes near to each respective switch to which it was attached onto the bottom layer of the PCB then I added the boundaries and this is how PCB layout looks now.

<img width="1424" height="415" alt="Screenshot 2026-06-08 000432" src="https://github.com/user-attachments/assets/9e5d956d-002b-4feb-bf16-314c7110a9a4" />

 ## Routed the PCB 
 Hours :- 6.5 <br>

 So I stated with routing the PCB I initially routed the diodes to the switches then I moved and started making rows and columns . I tried to make as clean routs as possible then I started routing the rows and columns to the expander . I used vias where there weren't space to rout . I had to make few alteration while routing so that my routs looks clean and workable . Many a times there weren't a way to rout . So I had to re-rout few traces but I was able to rout it to the two expanders. Then I stared connecting the SDA/SCL lines to the MCU from the expander and the OLED screen after that I made connection for the battery pins and battery connected circuit. So after all the rout the PCB looks like this with all the clean straight routs .
<img width="1317" height="627" alt="Screenshot 2026-06-08 021926" src="https://github.com/user-attachments/assets/1e2d0f09-0347-46e1-8550-bb1a6d73e7ae" />
<img width="1521" height="525" alt="Screenshot 2026-06-08 021857" src="https://github.com/user-attachments/assets/633c3c71-19a1-455f-8207-f7405ff12a6a" />

###  Made and Polished the Case <br><br>
Hours :- 5.75 hours 

So I took the measurements of the keyboard then made a sketch of same size.after that I added 1 mm releat from each side and added a boundary sketch and curved it edges.after that I need to add sketches for holding the plates . So I added it's boundary and started making symmetric Rectangles and circles for holding the Plate boundary , I repeted it for the tob and bottom<img width="974" height="415" alt="Screenshot 2026-06-08 111706" src="https://github.com/user-attachments/assets/43728780-c7b1-48b8-b349-4d707a1cde1f" />then to the sides<img width="844" height="370" alt="Screenshot 2026-06-08 112854" src="https://github.com/user-attachments/assets/7b4c110e-eeb1-4119-8298-0eb835722b93" />after that I made a simple base then extruded it as per the needs to make the base Case basic design all the meserments were pre calculated.


<img width="1158" height="550" alt="Screenshot 2026-06-08 170318 - Copy" src="https://github.com/user-attachments/assets/4d891798-c0f3-4475-9df8-6684c0cb2afd" />
<img width="818" height="619" alt="Screenshot 2026-06-08 170339" src="https://github.com/user-attachments/assets/1a95979c-809d-485c-a2c8-ed636c6c98bc" />

<img width="1158" height="550" alt="Screenshot 2026-06-08 170318" src="https://github.com/user-attachments/assets/841aec48-1cd3-44ef-9f79-7b16b6ec1393" />
