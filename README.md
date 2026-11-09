# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_21:15:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,451 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Thawalama — Alert; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 21:15:27 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-09 21:13:54 | Panadugama (Nilwala Ganga) | 5.30 | 🟡 Alert | -0.009 |  |
| 2026-11-09 21:09:35 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 21:09:26 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-09 21:09:05 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-09 21:09:02 | Baddegama (Gin Ganga) | 3.71 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-09 21:08:00 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-11-09 21:07:44 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-09 21:07:22 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 21:07:20 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | 0.516 | 🔺 Rising |
| 2026-11-09 21:07:04 | Thaldena (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.337 |  |
| 2026-11-09 21:05:45 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-09 21:05:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-11-09 21:05:24 | Rathnapura (Kalu Ganga) | 4.76 | 🟢 Normal | 0.957 | 🔺 Rising |
| 2026-11-09 21:05:16 | Norwood (Kelani Ganga) | 1.58 | 🟡 Alert | -0.117 |  |
| 2026-11-09 21:05:14 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-09 21:05:14 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-09 21:05:12 | Giriulla (Maha Oya) | 2.59 | 🟢 Normal | -0.040 |  |
| 2026-11-09 21:05:02 | Glencourse (Kelani Ganga) | 14.25 | 🟢 Normal | 0.609 | 🔺 Rising |
| 2026-11-09 21:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.16 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-09 21:04:16 | Deraniyagala (Kelani Ganga) | 2.71 | 🟢 Normal | -0.464 |  |
| 2026-11-09 21:04:16 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-11-09 21:04:04 | Kithulgala (Kelani Ganga) | 2.83 | 🟢 Normal | -0.334 |  |
| 2026-11-09 21:03:24 | Peradeniya (Mahaweli Ganga) | 4.81 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-09 21:03:23 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | 0.127 | 🔺 Rising |
| 2026-11-09 21:03:02 | Thawalama (Gin Ganga) | 4.30 | 🟡 Alert | 0.116 | 🔺 Rising |
| 2026-11-09 21:03:01 | Wellawaya (Kirindi Oya) | 2.74 | 🟢 Normal | -0.237 |  |
| 2026-11-09 21:02:55 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | 0.000 |  |
| 2026-11-09 21:02:48 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-11-09 21:02:40 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 21:02:38 | Nakkala (Kumbukkan Oya) | 1.94 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-09 21:02:33 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.050 |  |
| 2026-11-09 21:02:11 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.011 |  |
| 2026-11-09 21:02:10 | Nawalapitiya (Mahaweli Ganga) | 3.27 | 🟢 Normal | -0.071 |  |
| 2026-11-09 21:00:19 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 21:03:23 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | 0.127 | 🔺 Rising |
| 2026-11-09 21:03:02 | Thawalama (Gin Ganga) | 4.30 | 🟡 Alert | 0.116 | 🔺 Rising |
| 2026-11-09 21:09:02 | Baddegama (Gin Ganga) | 3.71 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-09 21:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.16 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-09 21:02:55 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | 0.000 |  |
| 2026-11-09 21:15:27 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-09 21:13:54 | Panadugama (Nilwala Ganga) | 5.30 | 🟡 Alert | -0.009 |  |
| 2026-11-09 21:05:16 | Norwood (Kelani Ganga) | 1.58 | 🟡 Alert | -0.117 |  |
| 2026-11-09 21:05:24 | Rathnapura (Kalu Ganga) | 4.76 | 🟢 Normal | 0.957 | 🔺 Rising |
| 2026-11-09 21:05:02 | Glencourse (Kelani Ganga) | 14.25 | 🟢 Normal | 0.609 | 🔺 Rising |
| 2026-11-09 21:07:20 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | 0.516 | 🔺 Rising |
| 2026-11-09 21:05:14 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-09 21:02:48 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-11-09 21:03:24 | Peradeniya (Mahaweli Ganga) | 4.81 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-09 21:09:26 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-09 21:05:45 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-09 21:02:38 | Nakkala (Kumbukkan Oya) | 1.94 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-09 21:09:05 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-09 21:07:44 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-09 21:00:19 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-09 21:09:35 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 21:07:22 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-09 21:02:40 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 21:05:14 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-09 21:02:11 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.011 |  |
| 2026-11-09 21:08:00 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-11-09 21:04:16 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-11-09 21:05:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-11-09 21:05:12 | Giriulla (Maha Oya) | 2.59 | 🟢 Normal | -0.040 |  |
| 2026-11-09 21:02:33 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.050 |  |
| 2026-11-09 21:02:10 | Nawalapitiya (Mahaweli Ganga) | 3.27 | 🟢 Normal | -0.071 |  |
| 2026-11-09 21:03:01 | Wellawaya (Kirindi Oya) | 2.74 | 🟢 Normal | -0.237 |  |
| 2026-11-09 21:04:04 | Kithulgala (Kelani Ganga) | 2.83 | 🟢 Normal | -0.334 |  |
| 2026-11-09 21:07:04 | Thaldena (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.337 |  |
| 2026-11-09 21:04:16 | Deraniyagala (Kelani Ganga) | 2.71 | 🟢 Normal | -0.464 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)