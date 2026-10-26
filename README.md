# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_12:09:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,440 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Nawalapitiya — Alert; 🟡 Norwood — Alert; 🟡 Kithulgala — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 12:01:27 | Holombuwa (Kelani Ganga) | 4.65 | 🟠 Minor Flood | 0.708 | 🔺 Rising |
| 2026-10-26 12:09:48 | Rathnapura (Kalu Ganga) | 7.62 | 🟠 Minor Flood | 0.292 | 🔺 Rising |
| 2026-10-26 12:02:21 | Nawalapitiya (Mahaweli Ganga) | 3.93 | 🟡 Alert | 0.654 | 🔺 Rising |
| 2026-10-26 12:02:15 | Norwood (Kelani Ganga) | 2.26 | 🟡 Alert | 0.255 | 🔺 Rising |
| 2026-10-26 12:07:32 | Kithulgala (Kelani Ganga) | 3.14 | 🟡 Alert | 0.207 | 🔺 Rising |
| 2026-10-26 12:04:21 | Dunamale (Aththanagalu Oya) | 3.41 | 🟡 Alert | 0.127 | 🔺 Rising |
| 2026-10-26 12:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.082 | 🔺 Rising |
| 2026-10-26 12:05:15 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -0.019 |  |
| 2026-10-26 12:02:41 | Deraniyagala (Kelani Ganga) | 3.34 | 🟢 Normal | 1.018 | 🔺 Rising |
| 2026-10-26 11:09:35 | Urawa (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.551 | 🔺 Rising |
| 2026-10-26 12:02:22 | Peradeniya (Mahaweli Ganga) | 4.35 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-10-26 12:06:52 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | 0.470 | 🔺 Rising |
| 2026-10-26 12:06:01 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-10-26 12:02:23 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-26 12:05:29 | Galgamuwa (Mee Oya) | 3.12 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-26 12:01:44 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-26 12:03:49 | Ellagawa (Kalu Ganga) | 8.81 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-26 12:04:14 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-26 12:07:18 | Giriulla (Maha Oya) | 3.12 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-26 12:01:33 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-26 12:05:19 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-26 12:03:57 | Hanwella (Kelani Ganga) | 4.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 12:08:29 | Baddegama (Gin Ganga) | 2.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-26 12:01:45 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 12:00:15 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 12:02:54 | Moragaswewa (Deduru Oya) | 4.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 12:02:08 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 12:00:15 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 12:03:05 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-26 12:03:50 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 12:07:37 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 12:04:58 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 12:02:10 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 12:03:33 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 12:02:16 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-26 12:02:26 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-26 12:02:51 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | -0.021 |  |
| 2026-10-26 12:01:34 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.022 |  |
| 2026-10-26 12:09:37 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.028 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)