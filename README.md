# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_22:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,464 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Thawalama — Alert; 🟡 Magura — Alert; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 22:03:03 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-11-09 22:03:03 | Dunamale (Aththanagalu Oya) | 4.40 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-09 22:02:55 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.031 |  |
| 2026-11-09 22:02:48 | Kuda Oya (Kirindi Oya) | 2.98 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-09 22:02:26 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | 0.642 | 🔺 Rising |
| 2026-11-09 22:02:08 | Deraniyagala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.394 |  |
| 2026-11-09 22:01:46 | Wellawaya (Kirindi Oya) | 2.55 | 🟢 Normal | -0.194 |  |
| 2026-11-09 22:01:41 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-09 22:01:17 | Moraketiya (Walawe Ganga) | 3.30 | 🟡 Alert | 1.506 | 🔺 Rising |
| 2026-11-09 22:01:13 | Kithulgala (Kelani Ganga) | 2.61 | 🟢 Normal | -0.231 |  |
| 2026-11-09 22:01:12 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 22:00:44 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-11-09 22:00:38 | Thawalama (Gin Ganga) | 4.43 | 🟡 Alert | 0.135 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 22:03:03 | Dunamale (Aththanagalu Oya) | 4.40 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-09 22:01:17 | Moraketiya (Walawe Ganga) | 3.30 | 🟡 Alert | 1.506 | 🔺 Rising |
| 2026-11-09 22:00:38 | Thawalama (Gin Ganga) | 4.43 | 🟡 Alert | 0.135 | 🔺 Rising |
| 2026-11-09 21:03:23 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | 0.127 | 🔺 Rising |
| 2026-11-09 21:09:02 | Baddegama (Gin Ganga) | 3.71 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-09 21:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.16 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-09 21:15:27 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-09 21:13:54 | Panadugama (Nilwala Ganga) | 5.30 | 🟡 Alert | -0.009 |  |
| 2026-11-09 22:02:55 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.031 |  |
| 2026-11-09 21:05:24 | Rathnapura (Kalu Ganga) | 4.76 | 🟢 Normal | 0.957 | 🔺 Rising |
| 2026-11-09 22:02:26 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | 0.642 | 🔺 Rising |
| 2026-11-09 21:05:02 | Glencourse (Kelani Ganga) | 14.25 | 🟢 Normal | 0.609 | 🔺 Rising |
| 2026-11-09 21:05:14 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-09 22:02:48 | Kuda Oya (Kirindi Oya) | 2.98 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-09 21:03:24 | Peradeniya (Mahaweli Ganga) | 4.81 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-09 22:01:41 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-09 21:05:45 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-09 21:09:05 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-09 21:09:35 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 21:07:22 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 22:01:12 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-09 21:02:40 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 21:05:14 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-09 21:02:11 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.011 |  |
| 2026-11-09 21:08:00 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-11-09 21:04:16 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-11-09 22:03:03 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-11-09 21:05:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-11-09 21:05:12 | Giriulla (Maha Oya) | 2.59 | 🟢 Normal | -0.040 |  |
| 2026-11-09 22:00:44 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-11-09 21:02:10 | Nawalapitiya (Mahaweli Ganga) | 3.27 | 🟢 Normal | -0.071 |  |
| 2026-11-09 22:01:46 | Wellawaya (Kirindi Oya) | 2.55 | 🟢 Normal | -0.194 |  |
| 2026-11-09 22:01:13 | Kithulgala (Kelani Ganga) | 2.61 | 🟢 Normal | -0.231 |  |
| 2026-11-09 21:07:04 | Thaldena (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.337 |  |
| 2026-11-09 22:02:08 | Deraniyagala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.394 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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