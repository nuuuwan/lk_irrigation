# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_03:31:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,438 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 03:31:47 | Magura (Kalu Ganga) | 5.41 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-11-12 03:31:10 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-12 03:16:39 | Nakkala (Kumbukkan Oya) | 2.40 | 🟢 Normal | -0.240 |  |
| 2026-11-12 03:12:43 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.005 |  |
| 2026-11-12 03:12:24 | Wellawaya (Kirindi Oya) | 2.42 | 🟢 Normal | -0.307 |  |
| 2026-11-12 03:12:10 | Moraketiya (Walawe Ganga) | 4.50 | 🟡 Alert | 0.325 | 🔺 Rising |
| 2026-11-12 03:11:04 | Rathnapura (Kalu Ganga) | 5.40 | 🟡 Alert | 0.117 | 🔺 Rising |
| 2026-11-12 03:10:16 | Magura (Kalu Ganga) | 5.35 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-11-12 03:09:01 | Glencourse (Kelani Ganga) | 13.97 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-12 03:08:29 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | -0.297 |  |
| 2026-11-12 03:08:00 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 03:07:40 | Hanwella (Kelani Ganga) | 5.10 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-12 03:07:37 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 03:06:56 | Katharagama (Menik Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-12 03:06:43 | Siyambalanduwa (Heda Oya) | 2.35 | 🟢 Normal | -0.099 |  |
| 2026-11-12 03:06:40 | Peradeniya (Mahaweli Ganga) | 5.70 | 🟡 Alert | -0.019 |  |
| 2026-11-12 03:06:19 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.000 |  |
| 2026-11-12 03:05:49 | Norwood (Kelani Ganga) | 1.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-12 03:05:30 | Holombuwa (Kelani Ganga) | 2.76 | 🟢 Normal | -0.435 |  |
| 2026-11-12 03:05:02 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.068 |  |
| 2026-11-12 03:04:57 | Thawalama (Gin Ganga) | 5.05 | 🟡 Alert | -0.078 |  |
| 2026-11-12 03:04:33 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-12 03:04:19 | Padiyathalawa (Maduru Oya) | 2.80 | 🟢 Normal | -0.250 |  |
| 2026-11-12 03:04:17 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-11-12 03:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.41 | 🟡 Alert | -0.818 |  |
| 2026-11-12 03:03:11 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-12 03:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.42 | 🟡 Alert | -0.818 |  |
| 2026-11-12 03:02:45 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | -0.020 |  |
| 2026-11-12 03:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.818 |  |
| 2026-11-12 03:02:24 | Thanamalwila (Kirindi Oya) | 3.50 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-12 03:02:19 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-12 03:02:10 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-12 03:01:58 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 03:01:39 | Ellagawa (Kalu Ganga) | 8.36 | 🟢 Normal | 0.000 |  |
| 2026-11-12 03:01:31 | Kuda Oya (Kirindi Oya) | 3.45 | 🟢 Normal | 0.816 | 🔺 Rising |
| 2026-11-12 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -3.972 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 03:08:00 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 03:07:37 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 03:12:10 | Moraketiya (Walawe Ganga) | 4.50 | 🟡 Alert | 0.325 | 🔺 Rising |
| 2026-11-12 03:31:47 | Magura (Kalu Ganga) | 5.41 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-11-12 02:12:58 | Panadugama (Nilwala Ganga) | 5.76 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2026-11-12 03:11:04 | Rathnapura (Kalu Ganga) | 5.40 | 🟡 Alert | 0.117 | 🔺 Rising |
| 2026-11-12 03:06:19 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.000 |  |
| 2026-11-12 03:06:40 | Peradeniya (Mahaweli Ganga) | 5.70 | 🟡 Alert | -0.019 |  |
| 2026-11-12 03:04:57 | Thawalama (Gin Ganga) | 5.05 | 🟡 Alert | -0.078 |  |
| 2026-11-12 03:08:29 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | -0.297 |  |
| 2026-11-12 03:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.41 | 🟡 Alert | -0.818 |  |
| 2026-11-12 03:01:31 | Kuda Oya (Kirindi Oya) | 3.45 | 🟢 Normal | 0.816 | 🔺 Rising |
| 2026-11-12 02:08:02 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-11-12 03:02:24 | Thanamalwila (Kirindi Oya) | 3.50 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-12 03:04:17 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-11-12 03:09:01 | Glencourse (Kelani Ganga) | 13.97 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-12 03:03:11 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-12 03:04:33 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-12 03:07:40 | Hanwella (Kelani Ganga) | 5.10 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-12 03:01:58 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 03:05:49 | Norwood (Kelani Ganga) | 1.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-12 03:12:43 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.005 |  |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-12 03:01:39 | Ellagawa (Kalu Ganga) | 8.36 | 🟢 Normal | 0.000 |  |
| 2026-11-12 03:06:56 | Katharagama (Menik Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-12 03:31:10 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-12 03:02:10 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-12 03:02:19 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-12 03:02:45 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | -0.020 |  |
| 2026-11-12 03:05:02 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.068 |  |
| 2026-11-12 03:06:43 | Siyambalanduwa (Heda Oya) | 2.35 | 🟢 Normal | -0.099 |  |
| 2026-11-12 03:16:39 | Nakkala (Kumbukkan Oya) | 2.40 | 🟢 Normal | -0.240 |  |
| 2026-11-12 03:04:19 | Padiyathalawa (Maduru Oya) | 2.80 | 🟢 Normal | -0.250 |  |
| 2026-11-12 03:12:24 | Wellawaya (Kirindi Oya) | 2.42 | 🟢 Normal | -0.307 |  |
| 2026-11-12 03:05:30 | Holombuwa (Kelani Ganga) | 2.76 | 🟢 Normal | -0.435 |  |
| 2026-11-12 02:05:33 | Thaldena (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.637 |  |
| 2026-11-12 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -3.972 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)