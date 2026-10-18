# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_01:03:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,719 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 01:03:26 | Moragaswewa (Deduru Oya) | 2.56 | 🟢 Normal | -0.051 |  |
| 2026-10-19 01:03:08 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-10-19 01:02:59 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-10-19 01:02:48 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.060 |  |
| 2026-10-19 01:02:39 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 01:02:05 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-19 01:01:57 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 01:01:56 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.139 |  |
| 2026-10-19 01:01:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-19 01:01:47 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.112 |  |
| 2026-10-19 01:01:36 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-19 01:01:33 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 00:04:24 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 00:04:19 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-19 00:05:44 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | -0.029 |  |
| 2026-10-19 01:03:08 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-10-19 01:02:05 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-19 01:01:36 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-19 00:01:30 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-19 00:02:16 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-19 01:02:39 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 00:02:31 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 01:01:57 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 00:02:28 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-19 01:01:33 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 00:01:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-19 01:01:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-19 00:07:09 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 00:02:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 00:14:28 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-19 00:15:22 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.005 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-19 00:02:17 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-19 00:08:37 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-10-19 00:05:25 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.012 |  |
| 2026-10-19 00:07:57 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.018 |  |
| 2026-10-19 01:02:59 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-10-19 00:06:07 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-10-19 00:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-19 00:08:41 | Baddegama (Gin Ganga) | 2.92 | 🟢 Normal | -0.039 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-19 01:03:26 | Moragaswewa (Deduru Oya) | 2.56 | 🟢 Normal | -0.051 |  |
| 2026-10-19 00:01:17 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.053 |  |
| 2026-10-19 01:02:48 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.060 |  |
| 2026-10-19 00:02:34 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.080 |  |
| 2026-10-19 00:04:32 | Rathnapura (Kalu Ganga) | 4.43 | 🟢 Normal | -0.091 |  |
| 2026-10-19 01:01:47 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.112 |  |
| 2026-10-19 01:01:56 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.139 |  |
| 2026-10-19 00:14:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -2.667 |  |
| 2026-10-19 00:04:59 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -6.545 |  |

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)