# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_05:02:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,526 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 05:02:48 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.033 |  |
| 2026-11-21 05:02:39 | Urawa (Nilwala Ganga) | 1.80 | 🟢 Normal | -9.558 |  |
| 2026-11-21 05:02:22 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-21 05:02:14 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 05:02:13 | Peradeniya (Mahaweli Ganga) | 4.31 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-21 05:01:56 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-21 05:01:49 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 05:01:47 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-21 05:01:44 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 05:01:41 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.504 | 🔺 Rising |
| 2026-11-21 05:01:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 05:01:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-21 05:00:46 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | -9.558 |  |
| 2026-11-21 05:00:33 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-11-21 05:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.053 |  |
| 2026-11-21 05:00:21 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:53:21 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.504 | 🔺 Rising |
| 2026-11-21 04:51:46 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:47:40 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:16:07 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.034 |  |
| 2026-11-21 04:13:54 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.648 | 🔺 Rising |
| 2026-11-21 04:13:11 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.138 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 04:13:54 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.648 | 🔺 Rising |
| 2026-11-21 05:01:41 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.504 | 🔺 Rising |
| 2026-11-21 04:02:49 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-11-21 04:01:44 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-21 04:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-21 04:04:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-21 04:02:01 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-21 05:02:22 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-21 04:13:11 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-21 04:04:50 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-21 04:10:46 | Dunamale (Aththanagalu Oya) | 1.45 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-21 05:01:47 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-21 04:04:57 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-21 05:02:13 | Peradeniya (Mahaweli Ganga) | 4.31 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-21 04:06:26 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-21 05:02:14 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 05:01:49 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 04:03:29 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 04:01:13 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-21 05:01:44 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 05:01:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:47:40 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 05:01:56 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:29:43 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:07:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-21 05:00:21 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-21 05:01:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-21 05:02:48 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.033 |  |
| 2026-11-21 04:16:07 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.034 |  |
| 2026-11-21 05:00:33 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-11-21 04:06:15 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.048 |  |
| 2026-11-21 05:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.053 |  |
| 2026-11-21 04:09:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-11-21 04:06:17 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.082 |  |
| 2026-11-21 05:02:39 | Urawa (Nilwala Ganga) | 1.80 | 🟢 Normal | -9.558 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)