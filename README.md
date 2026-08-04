# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_18:11:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kithulgala — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 18:11:17 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | -0.038 |  |
| 2026-08-04 18:10:38 | Rathnapura (Kalu Ganga) | 6.15 | 🟡 Alert | -0.069 |  |
| 2026-08-04 18:09:59 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.027 |  |
| 2026-08-04 18:07:09 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.011 |  |
| 2026-08-04 18:07:07 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:06:25 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.059 |  |
| 2026-08-04 18:05:55 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.074 |  |
| 2026-08-04 18:05:34 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:05:14 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 18:04:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:04:55 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-04 18:04:11 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:03:47 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-08-04 18:03:44 | Hanwella (Kelani Ganga) | 5.34 | 🟢 Normal | -0.149 |  |
| 2026-08-04 18:03:23 | Deraniyagala (Kelani Ganga) | 3.34 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-08-04 18:03:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:03:08 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:26 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-08-04 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.031 |  |
| 2026-08-04 18:02:21 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-08-04 18:02:16 | Nawalapitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.060 |  |
| 2026-08-04 18:02:16 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.065 |  |
| 2026-08-04 18:02:15 | Kithulgala (Kelani Ganga) | 3.20 | 🟡 Alert | 0.149 | 🔺 Rising |
| 2026-08-04 18:02:07 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.032 |  |
| 2026-08-04 18:01:58 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:01:46 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 18:01:45 | Peradeniya (Mahaweli Ganga) | 4.70 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-04 18:01:41 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:27 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-08-04 18:01:23 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-08-04 18:01:18 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:15 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:01:01 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:01:00 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 18:02:15 | Kithulgala (Kelani Ganga) | 3.20 | 🟡 Alert | 0.149 | 🔺 Rising |
| 2026-08-04 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.031 |  |
| 2026-08-04 18:10:38 | Rathnapura (Kalu Ganga) | 6.15 | 🟡 Alert | -0.069 |  |
| 2026-08-04 18:03:23 | Deraniyagala (Kelani Ganga) | 3.34 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-08-04 18:01:23 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-08-04 18:01:45 | Peradeniya (Mahaweli Ganga) | 4.70 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-04 18:01:46 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 18:05:14 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 18:04:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:04:55 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:18 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:01:36 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:07:07 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:05:34 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:00 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:03:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:03:08 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:04:11 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:01:41 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:01:58 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:01:15 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:01:01 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-04 18:07:09 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.011 |  |
| 2026-08-04 18:01:27 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-08-04 18:02:26 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-08-04 18:03:47 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-08-04 18:02:21 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-08-04 18:09:59 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.027 |  |
| 2026-08-04 18:02:07 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.032 |  |
| 2026-08-04 18:11:17 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | -0.038 |  |
| 2026-08-04 18:06:25 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.059 |  |
| 2026-08-04 18:02:16 | Nawalapitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.060 |  |
| 2026-08-04 18:02:16 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.065 |  |
| 2026-08-04 18:05:55 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.074 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-04 18:03:44 | Hanwella (Kelani Ganga) | 5.34 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)