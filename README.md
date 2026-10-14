# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_03:05:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,188 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 03:05:10 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-10-15 03:04:49 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:04:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:04:35 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:04:14 | Rathnapura (Kalu Ganga) | 4.51 | 🟢 Normal | -0.217 |  |
| 2026-10-15 03:04:03 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-15 03:03:53 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.050 |  |
| 2026-10-15 03:03:53 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-15 03:03:51 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.069 |  |
| 2026-10-15 03:03:43 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-10-15 03:03:29 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-10-15 03:03:09 | Giriulla (Maha Oya) | 3.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-15 03:02:40 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:02:34 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-10-15 03:02:17 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-10-15 03:02:02 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-10-15 03:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-10-15 03:01:44 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:01:41 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:01:25 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.264 |  |
| 2026-10-15 03:01:11 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:00:26 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-15 02:42:24 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:38:10 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-15 02:32:35 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.007 |  |
| 2026-10-15 02:32:23 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -1.895 |  |
| 2026-10-15 02:31:26 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | -1.895 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 02:09:57 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-15 03:03:29 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-10-15 01:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.000 |  |
| 2026-10-15 01:06:29 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | -0.030 |  |
| 2026-10-15 02:32:23 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -1.895 |  |
| 2026-10-15 03:02:34 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-10-15 02:01:20 | Glencourse (Kelani Ganga) | 13.44 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-10-15 03:02:02 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-10-15 02:07:41 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-15 03:03:53 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-15 02:19:03 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-15 03:00:26 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-15 02:02:18 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 03:04:03 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-15 03:03:09 | Giriulla (Maha Oya) | 3.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-15 02:01:54 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-15 02:04:29 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 02:02:18 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:01:11 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:01:41 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:04:49 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:04:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:01:44 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:04:35 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:01:45 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:32:35 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.007 |  |
| 2026-10-15 00:24:41 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-10-15 03:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-10-15 03:05:10 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-10-15 03:03:43 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-10-15 03:03:53 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.050 |  |
| 2026-10-15 02:06:16 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.063 |  |
| 2026-10-15 03:03:51 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.069 |  |
| 2026-10-15 03:04:14 | Rathnapura (Kalu Ganga) | 4.51 | 🟢 Normal | -0.217 |  |
| 2026-10-15 02:08:47 | Holombuwa (Kelani Ganga) | 2.35 | 🟢 Normal | -0.248 |  |
| 2026-10-15 03:01:25 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)