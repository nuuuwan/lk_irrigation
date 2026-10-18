# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_03:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,784 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 03:03:46 | Moragaswewa (Deduru Oya) | 2.34 | 🟢 Normal | -0.082 |  |
| 2026-10-19 03:03:25 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.055 |  |
| 2026-10-19 03:03:04 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:02:57 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:02:52 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 03:02:51 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:02:44 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:02:41 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-19 03:02:26 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 03:02:22 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-19 03:02:17 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.030 |  |
| 2026-10-19 03:02:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-19 03:02:03 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.091 |  |
| 2026-10-19 03:01:57 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -2.602 |  |
| 2026-10-19 03:01:16 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.060 |  |
| 2026-10-19 03:01:14 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.130 |  |
| 2026-10-19 03:00:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:59:11 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -2.602 |  |
| 2026-10-19 02:42:21 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | -0.091 |  |
| 2026-10-19 02:30:44 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 03:02:26 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 03:02:41 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-19 02:13:45 | Norwood (Kelani Ganga) | 1.51 | 🟡 Alert | -0.045 |  |
| 2026-10-19 03:02:22 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-19 02:02:14 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-19 03:02:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-19 02:01:15 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 03:02:52 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 03:00:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:02:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:02:28 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 01:12:45 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:02:44 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:05:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:07:32 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:03:04 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:04:28 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-19 02:03:37 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:02:57 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:02:51 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-19 02:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-19 02:04:52 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-19 02:04:39 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-10-19 01:03:51 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-10-19 03:02:17 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.030 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-19 02:08:53 | Baddegama (Gin Ganga) | 2.84 | 🟢 Normal | -0.038 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-19 03:03:25 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.055 |  |
| 2026-10-19 03:01:16 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.060 |  |
| 2026-10-19 03:03:46 | Moragaswewa (Deduru Oya) | 2.34 | 🟢 Normal | -0.082 |  |
| 2026-10-19 03:02:03 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.091 |  |
| 2026-10-19 01:07:52 | Glencourse (Kelani Ganga) | 12.21 | 🟢 Normal | -0.092 |  |
| 2026-10-19 01:07:32 | Rathnapura (Kalu Ganga) | 4.31 | 🟢 Normal | -0.114 |  |
| 2026-10-19 03:01:14 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.130 |  |
| 2026-10-19 02:04:34 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.818 |  |
| 2026-10-19 03:01:57 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -2.602 |  |
| 2026-10-19 00:14:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -2.667 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)