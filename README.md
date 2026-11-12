# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_19:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 19:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 19:02:54 | Nakkala (Kumbukkan Oya) | 2.05 | 🟢 Normal | 0.581 | 🔺 Rising |
| 2026-11-12 19:02:51 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.064 |  |
| 2026-11-12 19:02:44 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-11-12 19:02:39 | Hanwella (Kelani Ganga) | 4.75 | 🟢 Normal | -0.112 |  |
| 2026-11-12 19:02:32 | Moraketiya (Walawe Ganga) | 3.35 | 🟡 Alert | -0.299 |  |
| 2026-11-12 19:02:15 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-12 19:02:12 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-12 19:02:10 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-12 19:02:05 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | 0.147 | 🔺 Rising |
| 2026-11-12 19:01:59 | Thaldena (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.210 |  |
| 2026-11-12 19:01:50 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-12 19:01:49 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:01:10 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-12 19:01:06 | Wellawaya (Kirindi Oya) | 2.34 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-12 19:00:40 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 19:02:05 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | 0.147 | 🔺 Rising |
| 2026-11-12 18:08:38 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 18:05:33 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 19:02:15 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-12 18:03:31 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.000 |  |
| 2026-11-12 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | 0.000 |  |
| 2026-11-12 18:02:46 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.046 |  |
| 2026-11-12 19:02:32 | Moraketiya (Walawe Ganga) | 3.35 | 🟡 Alert | -0.299 |  |
| 2026-11-12 19:02:54 | Nakkala (Kumbukkan Oya) | 2.05 | 🟢 Normal | 0.581 | 🔺 Rising |
| 2026-11-12 18:05:59 | Pitabeddara (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-11-12 18:01:24 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-12 18:07:18 | Urawa (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-12 19:02:12 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 19:01:06 | Wellawaya (Kirindi Oya) | 2.34 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-12 19:01:10 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-12 18:01:32 | Peradeniya (Mahaweli Ganga) | 4.72 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-12 19:02:10 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-12 18:03:08 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 19:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 18:03:19 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:00:12 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:13:33 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:01:49 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:08:45 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:02:19 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-12 19:02:44 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-11-12 19:01:50 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-12 19:00:40 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | -0.021 |  |
| 2026-11-12 18:08:42 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-12 18:01:57 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | -0.032 |  |
| 2026-11-12 18:05:04 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.041 |  |
| 2026-11-12 19:02:51 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.064 |  |
| 2026-11-12 18:03:30 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.111 |  |
| 2026-11-12 19:02:39 | Hanwella (Kelani Ganga) | 4.75 | 🟢 Normal | -0.112 |  |
| 2026-11-12 19:01:59 | Thaldena (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.210 |  |
| 2026-11-12 18:03:43 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | -0.289 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)