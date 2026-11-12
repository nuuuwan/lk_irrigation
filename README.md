# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_06:10:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 06:10:25 | Urawa (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.086 |  |
| 2026-11-12 06:09:36 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 06:07:42 | Thaldena (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.174 |  |
| 2026-11-12 06:07:25 | Holombuwa (Kelani Ganga) | 2.11 | 🟢 Normal | -0.209 |  |
| 2026-11-12 06:07:21 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-12 06:07:19 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-11-12 06:07:06 | Peradeniya (Mahaweli Ganga) | 5.36 | 🟡 Alert | -0.141 |  |
| 2026-11-12 06:05:44 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-12 06:05:34 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-12 06:05:22 | Thanamalwila (Kirindi Oya) | 3.52 | 🟢 Normal | -0.361 |  |
| 2026-11-12 06:05:11 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.271 |  |
| 2026-11-12 06:04:44 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 06:04:33 | Badalgama (Maha Oya) | 4.48 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-12 06:04:22 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.060 |  |
| 2026-11-12 06:04:15 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.174 |  |
| 2026-11-12 06:04:08 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | -0.136 |  |
| 2026-11-12 06:03:41 | Norwood (Kelani Ganga) | 1.56 | 🟡 Alert | 0.098 | 🔺 Rising |
| 2026-11-12 06:03:39 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | -0.010 |  |
| 2026-11-12 06:03:32 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 06:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.36 | 🟡 Alert | -0.020 |  |
| 2026-11-12 06:03:07 | Katharagama (Menik Ganga) | 0.87 | 🟢 Normal | -0.109 |  |
| 2026-11-12 06:02:57 | Thawalama (Gin Ganga) | 4.90 | 🟡 Alert | -0.141 |  |
| 2026-11-12 06:02:53 | Weraganthota (Mahaweli Ganga) | -1.07 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-12 06:02:51 | Dunamale (Aththanagalu Oya) | 4.18 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-11-12 06:02:42 | Hanwella (Kelani Ganga) | 5.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-12 06:02:36 | Magura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.000 |  |
| 2026-11-12 06:01:50 | Pitabeddara (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.248 |  |
| 2026-11-12 06:01:46 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.000 |  |
| 2026-11-12 06:01:43 | Nakkala (Kumbukkan Oya) | 1.96 | 🟢 Normal | -0.090 |  |
| 2026-11-12 06:01:33 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | -0.174 |  |
| 2026-11-12 06:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.098 |  |
| 2026-11-12 06:01:26 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | -0.701 |  |
| 2026-11-12 06:01:26 | Giriulla (Maha Oya) | 3.46 | 🟢 Normal | -0.164 |  |
| 2026-11-12 06:01:14 | Kuda Oya (Kirindi Oya) | 3.29 | 🟢 Normal | -0.363 |  |
| 2026-11-12 06:01:10 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.036 |  |
| 2026-11-12 06:01:03 | Wellawaya (Kirindi Oya) | 2.03 | 🟢 Normal | -0.253 |  |
| 2026-11-12 06:00:48 | Moragaswewa (Deduru Oya) | 3.62 | 🟢 Normal | -0.030 |  |
| 2026-11-12 05:56:28 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.129 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 06:09:36 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 06:03:32 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 06:03:41 | Norwood (Kelani Ganga) | 1.56 | 🟡 Alert | 0.098 | 🔺 Rising |
| 2026-11-12 06:02:51 | Dunamale (Aththanagalu Oya) | 4.18 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-11-12 06:07:19 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-11-12 06:02:36 | Magura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.000 |  |
| 2026-11-12 06:01:46 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.000 |  |
| 2026-11-12 06:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.36 | 🟡 Alert | -0.020 |  |
| 2026-11-12 06:07:06 | Peradeniya (Mahaweli Ganga) | 5.36 | 🟡 Alert | -0.141 |  |
| 2026-11-12 06:02:57 | Thawalama (Gin Ganga) | 4.90 | 🟡 Alert | -0.141 |  |
| 2026-11-12 06:01:26 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | -0.701 |  |
| 2026-11-12 06:02:53 | Weraganthota (Mahaweli Ganga) | -1.07 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-12 06:04:33 | Badalgama (Maha Oya) | 4.48 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-12 06:05:44 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-12 06:02:42 | Hanwella (Kelani Ganga) | 5.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-12 06:04:44 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-12 06:07:21 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-12 06:03:39 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | -0.010 |  |
| 2026-11-12 06:05:34 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-12 06:00:48 | Moragaswewa (Deduru Oya) | 3.62 | 🟢 Normal | -0.030 |  |
| 2026-11-12 06:01:10 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.036 |  |
| 2026-11-12 06:04:22 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.060 |  |
| 2026-11-12 06:10:25 | Urawa (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.086 |  |
| 2026-11-12 06:01:43 | Nakkala (Kumbukkan Oya) | 1.96 | 🟢 Normal | -0.090 |  |
| 2026-11-12 06:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.098 |  |
| 2026-11-12 06:03:07 | Katharagama (Menik Ganga) | 0.87 | 🟢 Normal | -0.109 |  |
| 2026-11-12 06:04:08 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | -0.136 |  |
| 2026-11-12 06:01:26 | Giriulla (Maha Oya) | 3.46 | 🟢 Normal | -0.164 |  |
| 2026-11-12 06:07:42 | Thaldena (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.174 |  |
| 2026-11-12 06:01:33 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | -0.174 |  |
| 2026-11-12 06:07:25 | Holombuwa (Kelani Ganga) | 2.11 | 🟢 Normal | -0.209 |  |
| 2026-11-12 06:01:50 | Pitabeddara (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.248 |  |
| 2026-11-12 06:01:03 | Wellawaya (Kirindi Oya) | 2.03 | 🟢 Normal | -0.253 |  |
| 2026-11-12 06:05:11 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.271 |  |
| 2026-11-12 06:05:22 | Thanamalwila (Kirindi Oya) | 3.52 | 🟢 Normal | -0.361 |  |
| 2026-11-12 06:01:14 | Kuda Oya (Kirindi Oya) | 3.29 | 🟢 Normal | -0.363 |  |
| 2026-11-12 05:16:02 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | -540.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)