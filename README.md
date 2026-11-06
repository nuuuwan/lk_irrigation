# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_00:03:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,841 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 00:03:18 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | 0.122 | 🔺 Rising |
| 2026-11-07 00:03:10 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:03:00 | Giriulla (Maha Oya) | 3.31 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-11-07 00:02:55 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.686 | 🔺 Rising |
| 2026-11-07 00:02:38 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-11-07 00:02:36 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.078 |  |
| 2026-11-07 00:02:33 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:27 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.075 |  |
| 2026-11-07 00:02:21 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-07 00:02:16 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:13 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:08 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | -0.170 |  |
| 2026-11-07 00:02:07 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.050 |  |
| 2026-11-07 00:01:57 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-07 00:01:44 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:00:58 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-07 00:00:27 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.027 |  |
| 2026-11-06 23:38:30 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.027 |  |
| 2026-11-06 23:29:35 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 23:08:45 | Holombuwa (Kelani Ganga) | 4.40 | 🟠 Minor Flood | -0.349 |  |
| 2026-11-07 00:03:18 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | 0.122 | 🔺 Rising |
| 2026-11-06 23:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-11-07 00:02:55 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.686 | 🔺 Rising |
| 2026-11-06 23:03:07 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.642 | 🔺 Rising |
| 2026-11-07 00:03:00 | Giriulla (Maha Oya) | 3.31 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-11-07 00:02:38 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-11-06 22:09:55 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-07 00:02:21 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-06 23:06:58 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-11-06 23:07:56 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-06 23:22:44 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-06 23:07:49 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-06 23:12:55 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 23:05:22 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-06 23:02:15 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-07 00:01:57 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-06 23:05:28 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-06 23:13:10 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-06 23:02:20 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 00:02:16 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:33 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:03:01 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:03:10 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:13 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:02:36 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:03:35 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:02:57 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-11-06 23:04:23 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-07 00:00:58 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-07 00:00:27 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.027 |  |
| 2026-11-07 00:02:07 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.050 |  |
| 2026-11-07 00:02:27 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.075 |  |
| 2026-11-06 23:08:49 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.076 |  |
| 2026-11-07 00:02:36 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.078 |  |
| 2026-11-07 00:02:08 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)