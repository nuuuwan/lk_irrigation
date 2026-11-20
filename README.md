# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_04:16:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,507 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 04:16:07 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.034 |  |
| 2026-11-21 04:13:54 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.648 | 🔺 Rising |
| 2026-11-21 04:13:11 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-21 04:10:46 | Dunamale (Aththanagalu Oya) | 1.45 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-21 04:09:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-11-21 04:07:33 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.065 |  |
| 2026-11-21 04:07:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:06:26 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-21 04:06:17 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.082 |  |
| 2026-11-21 04:06:15 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.048 |  |
| 2026-11-21 04:05:59 | Moraketiya (Walawe Ganga) | 2.80 | 🟢 Normal | 0.968 | 🔺 Rising |
| 2026-11-21 04:04:57 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-21 04:04:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-21 04:04:50 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-21 04:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.082 |  |
| 2026-11-21 04:03:30 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-21 04:03:29 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 04:03:10 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:02:56 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:02:49 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-11-21 04:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-21 04:02:22 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-11-21 04:02:20 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:02:09 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-21 04:02:01 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-21 04:01:44 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-21 04:01:38 | Peradeniya (Mahaweli Ganga) | 4.22 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-11-21 04:01:27 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:01:15 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:01:13 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:00:10 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 04:05:59 | Moraketiya (Walawe Ganga) | 2.80 | 🟢 Normal | 0.968 | 🔺 Rising |
| 2026-11-21 04:13:54 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.648 | 🔺 Rising |
| 2026-11-21 04:02:49 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-11-21 04:01:44 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-21 04:01:38 | Peradeniya (Mahaweli Ganga) | 4.22 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-11-21 04:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-21 04:04:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-21 04:02:01 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-21 04:02:22 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-11-21 04:02:09 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-21 04:13:11 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-21 04:04:50 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-21 04:03:30 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-21 04:10:46 | Dunamale (Aththanagalu Oya) | 1.45 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-21 04:04:57 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-21 00:15:47 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-21 04:06:26 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-21 04:03:29 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 04:01:13 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:02:20 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:01:27 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:02:56 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:01:15 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:29:43 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:03:10 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 04:07:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-21 03:03:15 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-21 04:16:07 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.034 |  |
| 2026-11-21 04:06:15 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.048 |  |
| 2026-11-21 04:00:10 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.050 |  |
| 2026-11-21 04:09:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-11-21 04:07:33 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.065 |  |
| 2026-11-21 04:06:17 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.082 |  |
| 2026-11-21 04:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.082 |  |
| 2026-11-21 03:38:01 | Urawa (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.227 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)