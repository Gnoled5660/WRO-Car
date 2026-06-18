# WRO-Car

<img width="687" height="417" alt="Bildschirmfoto 2026-06-14 um 00 26 38" src="https://github.com/user-attachments/assets/310a2844-c835-4c8b-9a23-23499022453c" />

# Description

This car is meant to be used for a competition called WRO in the category Future-engineers. The goal is to have a car that drives autonomously around obstacles, in lapses ,as fast as possible, without having a collision with the wall or the obstacles. The obstacles may have different colors. Depending on the color, the car has to either drive around it from the left side or from the right side. 

All the 3D CAD models of the car, have been designed entirely from scratch. It is very much possible to design this with much cheaper electronics, but for this competition, we used some higher quality components, as we had a sponsor. 

The car is mainly seperated in two layers. One being the bottom layer, where almost all the non logical electrical components are, and one being the second layer, where all the logical electrical components are.

# Motivation

The main reason why I built this car is because it was required for a robotics competition. This is my first robotics competition, meaning I haven't got that much experience yet, but throughout this project, I have learned a lot about how these electrical components can work together, to be able to move itself. 

# Assembling and Wiring

Assembling it is quite straight forward. All the 3D CAD components have holes, where you can place a heated thread insert inside and screw the parts together. Every component is meant to be screwed or sticked together with glue.

Wiring is also fairly simple. Most of the components have either copper on the pad, so that you can solder the cable on to it or there are pin headers that you can simply connect to it. You just have to be careful with connecting it to the right pins or connecting V+ and Ground correctly. It is also important to use a wire with at least 18 or 20 AWG for the power supply, as it needs to be able to deliver a maximum of 5-6A. The rest of the signal pins can be connected with jumper cables.

The tires are lego tires, as well as the bar that holds the tire. However, it is completely possible to use 3D printed tires. Just be aware, that you might loose some grip.

# CAD Assembly
Starting with the main body, you need to insert heated threat inserts into all of the holes. All the holes are designed for M3 screws.<img width="332" height="280" alt="Bildschirmfoto 2026-06-18 um 15 12 34" src="https://github.com/user-attachments/assets/64fb71e9-f33d-419d-9bdf-8717af95c45b" />


<img width="302" height="335" alt="Bildschirmfoto 2026-06-18 um 15 10 32" src="https://github.com/user-attachments/assets/e1852d2e-8d99-4cf2-8f14-1e99c179da7e" />

<img width="331" height="323" alt="Bildschirmfoto 2026-06-18 um 15 15 00" src="https://github.com/user-attachments/assets/19ae350e-9b49-44eb-8bbf-df7a6ca96e78" />

Afterwards, you can add the rest of the components for the steering gear. All the parts that are red in this picture need a steel rod, to ensure flawless rotations.

<img width="281" height="241" alt="Bildschirmfoto 2026-06-18 um 15 17 59" src="https://github.com/user-attachments/assets/7ce5a8a6-a79a-4839-9cd6-bd5c0724463c" />

Now you can add the rest of the mounts.

<img width="372" height="337" alt="Bildschirmfoto 2026-06-18 um 15 20 35" src="https://github.com/user-attachments/assets/578a8d61-6184-4304-bf17-b4d61962753c" />

This part is a little bit tricky. It is important, that the servo mounts are added first and then comes the camera mount, because this why it is easier to reach the screws with a screwdriver. 

<img width="343" height="339" alt="Bildschirmfoto 2026-06-18 um 15 21 45" src="https://github.com/user-attachments/assets/bcdf8f44-55a8-4a9b-baa3-83b3ed0d193e" />

The pillars for the second layer also need to be screwed. There is one screw hole on the bottom and two holes for threat inserts on the top. 

<img width="604" height="445" alt="Bildschirmfoto 2026-06-18 um 15 23 50" src="https://github.com/user-attachments/assets/2b1bc03a-f4e4-4520-b185-a9c2280e05fe" />

After screwing every component to the mounts, it should look something like this.

<img width="632" height="467" alt="Bildschirmfoto 2026-06-18 um 15 25 58" src="https://github.com/user-attachments/assets/e871349b-84ce-4ce1-ab0d-4835590de573" />

Now for the second layer, the screw sizes may vary from each other, as every component has different sizes of mounting holes. In the cad files you can look up how big the holes of the components are. They are usually 0.2mm bigger than the actual screw.

<img width="388" height="225" alt="Bildschirmfoto 2026-06-18 um 15 27 07" src="https://github.com/user-attachments/assets/709ac8d5-d14a-472e-863b-b812adff4c94" />

If everything is built correctly, the result should look like this one.

<img width="637" height="473" alt="Bildschirmfoto 2026-06-18 um 15 29 22" src="https://github.com/user-attachments/assets/15733156-84eb-4795-858e-d277db7f5306" />




# Usage
The car is meant to be driven autonomously, but withthe raspberry pi5, it is also possible to program it to drive manually. The autonomous car can drive around in lapses and avoid obstacles.

# Firmware
To run the code, you just have to upload the python file on to the raspberry pi 5. Note that you have to setup the pi5 first, including inserting a SD card, as the pi5 usually doesn't come with a SD card. 

<img width="900" height="614" alt="Bildschirmfoto 2026-06-14 um 11 54 30" src="https://github.com/user-attachments/assets/c77949a3-9d41-49cf-bd3d-2dc2900bcc03" />

Then you can glue the these parts of the steering gear onto the main body. You also have to insert a steel rod from the top to the bottom, to ensure that the component can rotate freely. The steel rods should have a diameter of 3mm.

<img width="1688" height="2588" alt="Copy of fallout_zine_template-6" src="https://github.com/user-attachments/assets/e304b716-b2f3-44da-bacf-75173e7d4731" />


# BOM
|-----------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|Openmv H7 Plus         |Camera  |https://www.amazon.de/-/en/OpenMV-Cam-H7-Plus-Genuine-5MP/dp/B09WYQMDX2/ref=sr_1_1?crid=33PNR0X7MA4PN&dib=eyJ2IjoiMSJ9.Yc_Q0-hCd894n0G_bcZZcF-f-0dkgnJoI8TKEcn1adATHiwsHjOMsxN7wypOpl445D9UYHXL3-2f1G2MCrllQKvYyIBBfu8C0GBJ0G2BgiBJ5IAXfwfOIi8dYh07ZJqTczDMK1Ti4RFudyy5RdPc3PD2aKzn7GRjS-fHbqec4vrbJbEd_h3x2N8cVPhwFZIU8HSlvxaCvJnZKwT1FoPzDOHvl0mTq68b7PU9RntbvncqKXu-aS0xdyZ3n2rLu-sr1Gl_DVk6oFdqXrtLrIkLRkhFRnhVgK6GzlRqNTeNUs0.MOA0BK3GUTmC_OpycZaZHIXYmecJ_UzOdp4w1p16jns&dib_tag=se&keywords=openmv+cam+h7+plus&qid=1773569554&sprefix=openmv+cam+h7+plus|124                 |1                                                            |Amazon                                                                                                                        |
|JGA-370                |Motor   |https://smartfactory24.de/en/products/dc-motor-6v-12v-24v-elektrische-getriebe-motor-hohe-ausgerichtet-jga25-370?variant=51531346706775&country=DE&currency=EUR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gad_source=1&gad_campaignid=23078644272&gbraid=0AAAAABXW-xJgV7ZDjl7QhOxfMb-yjwhyP&gclid=Cj0KCQjw4a3OBhCHARIsAChaqJOaSRpLTh0fsLKQK0RWMPgRs7d4cWUzSukIZcd0dJkx4TjQAPaBgE0aArDKEALw_wcB|15                  |1                                                            |Smartfactory24                                                                                                                |
|Polulu g2 High-power   |Motor driver|https://botland.de/dc-motortreiber/5990-g2-high-power-18v17-einkanal-treiber-fur-30v-17a-motoren-pololu-2991-5904422367244.html                                                                                                                                              |36                  |1                                                            |Botland                                                                                                                       |
|Tower Pro MG92B        |Servo Steering Joint|https://www.roboter-bausatz.de/p/tower-pro-mg92b-digitaler-mini-servo-mit-metallgetriebe?srsltid=AfmBOoptf3cbFYxvsTGS84BmE45A6R3zUI0CShGOaZyWRLzGi3AGPMfw                                                                                                                    |13                  |1                                                            |Roboter-Bausatz                                                                                                               |
|Raspberry Pi 5         |Main Processing Unit|https://www.amazon.de/-/en/Raspberry-Pi-SC1111-5-4gb/dp/B0CK3L9WD3/ref=sr_1_5?crid=36AVD0ZZE5SZ0&dib=eyJ2IjoiMSJ9.EK5CW71bdOZ_PC0v3vsz9JpWoieDSCeytda8d4WgxFziUHshaXTL9Xvo-U4XPeJGsoNIptDfLO5Gdmu3iYHGkzYbqbonKS_RnCaW3opI0RO0-G5c3XaN9z2VeFNu78_M-iyJ32J2wdw99mxXYmMpYJia9_mn6pmXI-EZZv7vz-cUKgApsVaoCA1vnUg-R-5RAldoOzeB2mFsAzOl2pP0QuBXNj-AObWkhTQWVvce4nM.p_X96cPFrw-Gq8VXtIR3PLt3J5k_RC2q4fMz2b1ORNk&dib_tag=se&keywords=raspberry+pi+5|90                  |1                                                            |Amazon                                                                                                                        |
|PDB                    |Power distribution|https://www.premium-modellbau.de/matek-pdb-bis-zu-12s-mit-bec-und-sensor-pdb-hex?gad_source=1&gad_campaignid=1653543034&gbraid=0AAAAADoWh8vq4HTlLxcMn6O5SG_jzf-_S&gclid=Cj0KCQjwsdnNBhC4ARIsAA_3heiXH-VMz8y7B4xgwzPU8bZL5MXNiugnjZ5kKnQfz4J71pPAZLxocBQaArh0EALw_wcB         |25                  |1                                                            |Premium-Modellbau                                                                                                             |
|7.4V Battery           |Battery Power supply|https://www.amazon.de/OVONIC-Battery-Aircraft-Helicopter-Specially/dp/B08R726FTY/ref=sr_1_1_sspa?crid=1E0OZ2GXTSZS3&dib=eyJ2IjoiMSJ9.s_6FaY-dbbLpIezeLhlTQYzq897T9NT2auMXMoNAw6HgE8SYOfhL5l9404tka5E2Z9h9dYeZPtUeWBTyyWY3Sk6XzDAgKqMw06cX8txP3yDEI5zdFdlC4NVAmfU-csw8a30OcJS2-OpkrD-u5Fsq7RqLKYNk4UGZNGPfGgvdDSpKiku_DlEQ-I8Gjxc4rT35QxCHNfUNMzB962QQChKio_58Zk_1ZGDNyS3QimgtJSXb7aavRasmmHkeqzhvlUgathSGZLkn3RmamRP62mYyBlwwvhmbww6Boo17IYhMtUg.VD-Ak2KE3fU-C1060KKJ_NIA69O490IhtgK3ZEtst1E&dib_tag=se|28                  |1                                                            |Amazon                                                                                                                        |
|T-Dean Male Plug       |Adapter to connect to Battery|https://www.amazon.de/Premium-Goldstecker-Stecker-verzinnt-Modellbau®/dp/B07C1JSV15/ref=asc_df_B07C1JSV15?mcid=3f313e58521b3b4d985251ab4e02ac79&th=1&tag=googshopde-21&linkCode=df0&hvadid=725809613218&hvpos=&hvnetw=g&hvrand=17068902777536047627&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9044393&hvtargid=pla-2399552437568&hvocijid=17068902777536047627-B07C1JSV15-&hvexpln=0|4                   |1                                                            |Amazon                                                                                                                        |
|LTC3780                |Step down converter for motor|https://www.roboter-bausatz.de/p/spannungswandler-step-up-down-10a-dc-5v-32v-auf-1v-30v-ltc3780?sPartner=8&gad_source=1&gad_campaignid=12461217733&gbraid=0AAAAADKFiCA2CUl6FXfvpSPqSp_gMUlyD&gclid=Cj0KCQjwsdnNBhC4ARIsAA_3hej1hF1s0BhS1Nl0tT3tRvsYVuLvOZ-1uehZM4YjyWUVFrmTMn6BzDwaAoptEALw_wcB|18                  |1                                                            |Roboter-Bausatz                                                                                                               |
|D36V50F5               |Step down converter for pi5|https://botland.de/abwartswandler/16392-d36v50f5-5v-8a-abwartswandler-pololu-4091-5904422372125.html                                                                                                                                                                         |29                  |1                                                            |Botland                                                                                                                       |
|MicroSD                |For the pi5|https://www.voelkner.de/index.php?mp=products&file=info&ref=55&products_id=13003717&offer=5ae32255ce3f38b1b20f0e9f7366d203&utm_source=google&utm_medium=organic&utm_campaign=fpla&campaign_type=pla?utm_content=extern&gad_source=1&gad_campaignid=22425498201&gbraid=0AAAAAD7b-ka0VgyLEpV7-XglIPuidhcNp&gclid=CjwKCAjwntHPBhAaEiwA_Xp6RrpTBfn5mAIwplC1VRg6xP65GMKrtbOur4KKCp3QNVD4UdRaTCyZuBoCnwoQAvD_BwE|11                  |1                                                            |voelkner                                                                                                                      |
|total                  |        |                                                                                                                                                                                                                                                                             | 393                |                                                             |                                                                                                                              |



