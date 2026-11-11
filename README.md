# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_02:15:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,401 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Peradeniya — Alert; 🟡 Panadugama — Alert; 🟡 Rathnapura — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 02:15:40 | Katharagama (Menik Ganga) | 1.00 | 🟢 Normal | -0.057 |  |
| 2026-11-12 02:13:23 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-12 02:12:58 | Panadugama (Nilwala Ganga) | 5.76 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2026-11-12 02:09:56 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 02:08:02 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-11-12 02:07:58 | Urawa (Nilwala Ganga) | 3.00 | 🟡 Alert | -0.144 |  |
| 2026-11-12 02:06:10 | Holombuwa (Kelani Ganga) | 3.19 | 🟡 Alert | -0.087 |  |
| 2026-11-12 02:05:39 | Kuda Oya (Kirindi Oya) | 2.69 | 🟢 Normal | 0.575 | 🔺 Rising |
| 2026-11-12 02:05:33 | Thaldena (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.637 |  |
| 2026-11-12 02:05:15 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-12 02:04:32 | Rathnapura (Kalu Ganga) | 5.27 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2026-11-12 02:03:51 | Giriulla (Maha Oya) | 3.66 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-11-12 02:03:35 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.071 |  |
| 2026-11-12 02:03:19 | Thawalama (Gin Ganga) | 5.13 | 🟡 Alert | -0.072 |  |
| 2026-11-12 02:03:14 | Peradeniya (Mahaweli Ganga) | 5.72 | 🟡 Alert | 0.220 | 🔺 Rising |
| 2026-11-12 02:02:56 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.005 |  |
| 2026-11-12 02:02:36 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-11-12 02:02:20 | Thanamalwila (Kirindi Oya) | 3.32 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-12 02:02:18 | Hanwella (Kelani Ganga) | 5.03 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 02:02:15 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 02:02:15 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-11-12 02:02:11 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.062 |  |
| 2026-11-12 02:02:01 | Moraketiya (Walawe Ganga) | 4.12 | 🟡 Alert | 0.000 |  |
| 2026-11-12 02:02:01 | Wellawaya (Kirindi Oya) | 2.78 | 🟢 Normal | -0.711 |  |
| 2026-11-12 02:01:48 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 02:01:47 | Nakkala (Kumbukkan Oya) | 2.70 | 🟢 Normal | -0.402 |  |
| 2026-11-12 02:01:38 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 1.434 | 🔺 Rising |
| 2026-11-12 02:01:27 | Ellagawa (Kalu Ganga) | 8.36 | 🟢 Normal | -0.010 |  |
| 2026-11-12 02:00:16 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-12 02:00:10 | Siyambalanduwa (Heda Oya) | 2.46 | 🟢 Normal | -0.073 |  |
| 2026-11-12 01:56:32 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 1.434 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 02:09:56 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 02:02:15 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 02:03:14 | Peradeniya (Mahaweli Ganga) | 5.72 | 🟡 Alert | 0.220 | 🔺 Rising |
| 2026-11-12 02:12:58 | Panadugama (Nilwala Ganga) | 5.76 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2026-11-12 02:04:32 | Rathnapura (Kalu Ganga) | 5.27 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2026-11-12 01:02:52 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-12 01:03:24 | Magura (Kalu Ganga) | 5.29 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-11-12 02:02:01 | Moraketiya (Walawe Ganga) | 4.12 | 🟡 Alert | 0.000 |  |
| 2026-11-12 00:12:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.000 |  |
| 2026-11-12 02:03:19 | Thawalama (Gin Ganga) | 5.13 | 🟡 Alert | -0.072 |  |
| 2026-11-12 02:06:10 | Holombuwa (Kelani Ganga) | 3.19 | 🟡 Alert | -0.087 |  |
| 2026-11-12 02:07:58 | Urawa (Nilwala Ganga) | 3.00 | 🟡 Alert | -0.144 |  |
| 2026-11-12 02:01:38 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 1.434 | 🔺 Rising |
| 2026-11-12 02:05:39 | Kuda Oya (Kirindi Oya) | 2.69 | 🟢 Normal | 0.575 | 🔺 Rising |
| 2026-11-12 02:03:51 | Giriulla (Maha Oya) | 3.66 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-11-12 02:08:02 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-11-12 02:02:20 | Thanamalwila (Kirindi Oya) | 3.32 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-12 02:05:15 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-12 02:00:16 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-12 02:02:18 | Hanwella (Kelani Ganga) | 5.03 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 01:07:13 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-12 02:13:23 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-12 02:01:48 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-12 02:02:56 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.005 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-12 02:01:27 | Ellagawa (Kalu Ganga) | 8.36 | 🟢 Normal | -0.010 |  |
| 2026-11-12 02:02:15 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-11-12 02:02:36 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-11-12 02:15:40 | Katharagama (Menik Ganga) | 1.00 | 🟢 Normal | -0.057 |  |
| 2026-11-12 02:02:11 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.062 |  |
| 2026-11-12 02:03:35 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.071 |  |
| 2026-11-12 02:00:10 | Siyambalanduwa (Heda Oya) | 2.46 | 🟢 Normal | -0.073 |  |
| 2026-11-12 01:12:41 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.199 |  |
| 2026-11-12 01:04:11 | Padiyathalawa (Maduru Oya) | 3.30 | 🟢 Normal | -0.290 |  |
| 2026-11-12 02:01:47 | Nakkala (Kumbukkan Oya) | 2.70 | 🟢 Normal | -0.402 |  |
| 2026-11-12 02:05:33 | Thaldena (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.637 |  |
| 2026-11-12 02:02:01 | Wellawaya (Kirindi Oya) | 2.78 | 🟢 Normal | -0.711 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)