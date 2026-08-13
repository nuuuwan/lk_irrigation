# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_18:02:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,544 measurements** from **39** stations.
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
| 2026-08-13 18:02:13 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.068 |  |
| 2026-08-13 18:02:08 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 18:02:08 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:04 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:02 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:02:01 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:01:58 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:01:56 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:01:53 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-08-13 18:01:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-08-13 18:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.071 |  |
| 2026-08-13 18:01:18 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:01:11 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 18:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:00:36 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 18:00:23 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:00:21 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 18:00:19 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:00:10 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:26:07 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:18:05 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 17:03:52 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-13 17:13:06 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-13 18:00:21 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 18:02:08 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 18:01:11 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 18:00:36 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 17:05:20 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:08 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:09:38 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:02:16 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:03:59 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:01:18 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:00:10 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:01:56 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:00:23 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:05:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:05:44 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:03:52 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:26:07 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:00:31 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:04 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 16:06:00 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 17:18:05 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.008 |  |
| 2026-08-13 17:04:02 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-13 17:07:26 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-08-13 17:03:03 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:02:01 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:00:19 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-08-13 18:01:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-08-13 18:01:53 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-08-13 17:02:24 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | -0.030 |  |
| 2026-08-13 18:02:02 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:01:58 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:02:13 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.068 |  |
| 2026-08-13 18:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.071 |  |
| 2026-08-13 17:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)