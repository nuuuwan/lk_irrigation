# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_10:12:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 10:12:06 | Magura (Kalu Ganga) | 5.55 | 🟡 Alert | -0.019 |  |
| 2026-09-21 10:08:30 | Panadugama (Nilwala Ganga) | 5.81 | 🟡 Alert | -144.000 |  |
| 2026-09-21 10:08:29 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -144.000 |  |
| 2026-09-21 10:08:28 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -144.000 |  |
| 2026-09-21 10:08:27 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -144.000 |  |
| 2026-09-21 10:08:25 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -144.000 |  |
| 2026-09-21 10:06:17 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2026-09-21 10:06:03 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.090 |  |
| 2026-09-21 10:05:35 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-21 10:05:30 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.019 |  |
| 2026-09-21 10:05:16 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-09-21 10:04:39 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-21 10:03:59 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.022 |  |
| 2026-09-21 10:03:57 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-21 10:03:46 | Rathnapura (Kalu Ganga) | 5.77 | 🟡 Alert | -0.033 |  |
| 2026-09-21 10:03:45 | Baddegama (Gin Ganga) | 3.93 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 10:03:28 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.432 |  |
| 2026-09-21 10:03:26 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-21 10:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.78 | 🟠 Minor Flood | 0.049 | 🔺 Rising |
| 2026-09-21 10:03:22 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-09-21 10:03:21 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.042 |  |
| 2026-09-21 10:03:20 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:03:13 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 10:03:06 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-09-21 10:02:59 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:02:56 | Hanwella (Kelani Ganga) | 6.43 | 🟢 Normal | -0.109 |  |
| 2026-09-21 10:02:54 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-09-21 10:02:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:02:31 | Deraniyagala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.041 |  |
| 2026-09-21 10:02:31 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-21 10:02:21 | Ellagawa (Kalu Ganga) | 8.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 10:02:15 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:02:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:02:10 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.093 |  |
| 2026-09-21 10:02:09 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.020 |  |
| 2026-09-21 10:02:08 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.023 |  |
| 2026-09-21 10:02:08 | Glencourse (Kelani Ganga) | 13.70 | 🟢 Normal | -0.251 |  |
| 2026-09-21 10:01:59 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:01:46 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:01:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:01:35 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.131 |  |
| 2026-09-21 10:00:43 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:58:25 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 10:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.78 | 🟠 Minor Flood | 0.049 | 🔺 Rising |
| 2026-09-21 10:03:45 | Baddegama (Gin Ganga) | 3.93 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 10:03:13 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 10:12:06 | Magura (Kalu Ganga) | 5.55 | 🟡 Alert | -0.019 |  |
| 2026-09-21 10:03:46 | Rathnapura (Kalu Ganga) | 5.77 | 🟡 Alert | -0.033 |  |
| 2026-09-21 10:08:30 | Panadugama (Nilwala Ganga) | 5.81 | 🟡 Alert | -144.000 |  |
| 2026-09-21 10:03:26 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-21 10:05:35 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-21 10:02:21 | Ellagawa (Kalu Ganga) | 8.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 10:02:31 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-21 10:03:57 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-21 10:02:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:01:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:00:43 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:58:25 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:03:20 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:01:59 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:02:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:01:46 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:02:15 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:02:59 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:04:39 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-21 10:06:17 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2026-09-21 10:05:30 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.019 |  |
| 2026-09-21 10:02:09 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.020 |  |
| 2026-09-21 10:03:06 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-09-21 10:03:22 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-09-21 10:03:59 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.022 |  |
| 2026-09-21 10:02:08 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.023 |  |
| 2026-09-21 10:05:16 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-09-21 10:02:31 | Deraniyagala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.041 |  |
| 2026-09-21 10:02:54 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-09-21 10:03:21 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.042 |  |
| 2026-09-21 10:06:03 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.090 |  |
| 2026-09-21 10:02:10 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.093 |  |
| 2026-09-21 10:02:56 | Hanwella (Kelani Ganga) | 6.43 | 🟢 Normal | -0.109 |  |
| 2026-09-21 10:01:35 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.131 |  |
| 2026-09-21 10:02:08 | Glencourse (Kelani Ganga) | 13.70 | 🟢 Normal | -0.251 |  |
| 2026-09-21 10:03:28 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.432 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)