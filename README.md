# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_03:30:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,806 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 03:30:14 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.008 |  |
| 2026-10-19 03:22:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.672 |  |
| 2026-10-19 03:20:07 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | -0.069 |  |
| 2026-10-19 03:18:36 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.024 |  |
| 2026-10-19 03:17:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.51 | 🟢 Normal | -0.672 |  |
| 2026-10-19 03:15:58 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.008 |  |
| 2026-10-19 03:12:41 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.027 |  |
| 2026-10-19 03:10:59 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-19 03:09:59 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-19 03:08:39 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -5.143 |  |
| 2026-10-19 03:07:15 | Rathnapura (Kalu Ganga) | 4.19 | 🟢 Normal | -5.143 |  |
| 2026-10-19 03:06:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-19 03:05:18 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 03:05:08 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | -0.021 |  |
| 2026-10-19 03:05:05 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | -144.000 |  |
| 2026-10-19 03:05:01 | Glencourse (Kelani Ganga) | 12.07 | 🟢 Normal | -144.000 |  |
| 2026-10-19 03:04:54 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-10-19 03:04:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:04:45 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.060 |  |
| 2026-10-19 03:04:45 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-19 03:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:04:02 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:03:46 | Moragaswewa (Deduru Oya) | 2.34 | 🟢 Normal | -0.082 |  |
| 2026-10-19 03:03:25 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.055 |  |
| 2026-10-19 03:03:04 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:02:57 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:02:52 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 03:02:51 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:02:44 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:02:41 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | -0.069 |  |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 03:02:26 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 03:30:14 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.008 |  |
| 2026-10-19 03:20:07 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | -0.069 |  |
| 2026-10-19 03:06:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-19 03:02:22 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-19 03:04:45 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-19 03:02:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-19 03:05:18 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 03:10:59 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-19 03:02:52 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 03:00:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:02:44 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:04:02 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:03:04 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:15:58 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.008 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:04:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:02:57 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:02:51 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:09:59 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-19 03:04:54 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-10-19 03:05:08 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | -0.021 |  |
| 2026-10-19 01:03:51 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-10-19 03:18:36 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.024 |  |
| 2026-10-19 03:12:41 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.027 |  |
| 2026-10-19 03:02:17 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.030 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-19 03:03:25 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.055 |  |
| 2026-10-19 03:01:16 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.060 |  |
| 2026-10-19 03:04:45 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.060 |  |
| 2026-10-19 03:03:46 | Moragaswewa (Deduru Oya) | 2.34 | 🟢 Normal | -0.082 |  |
| 2026-10-19 03:02:03 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.091 |  |
| 2026-10-19 03:01:14 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.130 |  |
| 2026-10-19 03:22:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.672 |  |
| 2026-10-19 03:01:57 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -2.602 |  |
| 2026-10-19 03:08:39 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -5.143 |  |
| 2026-10-19 03:05:05 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)