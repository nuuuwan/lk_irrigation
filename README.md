# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_06:12:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,450 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 06:12:32 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -1.066 |  |
| 2026-11-03 06:11:47 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-03 06:09:18 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.022 |  |
| 2026-11-03 06:09:05 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | -0.081 |  |
| 2026-11-03 06:07:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 06:06:57 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.043 |  |
| 2026-11-03 06:06:30 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.136 |  |
| 2026-11-03 06:06:22 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.112 |  |
| 2026-11-03 06:06:13 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.049 |  |
| 2026-11-03 06:06:10 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.181 |  |
| 2026-11-03 06:06:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.126 |  |
| 2026-11-03 06:05:33 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.090 |  |
| 2026-11-03 06:05:14 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.150 |  |
| 2026-11-03 06:05:13 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:05:12 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-03 06:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-11-03 06:04:34 | Wellawaya (Kirindi Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:04:32 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 06:04:24 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-03 06:04:05 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-03 06:04:04 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.062 |  |
| 2026-11-03 06:03:48 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.034 |  |
| 2026-11-03 06:03:35 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | 0.772 | 🔺 Rising |
| 2026-11-03 06:03:25 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-03 06:03:17 | Wellawaya (Kirindi Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:03:10 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-11-03 06:02:53 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.171 |  |
| 2026-11-03 06:02:49 | Moragaswewa (Deduru Oya) | 3.48 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-11-03 06:02:23 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:01:43 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:01:41 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:01:35 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-03 06:01:25 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.217 |  |
| 2026-11-03 06:01:20 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.032 |  |
| 2026-11-03 06:01:13 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-11-03 06:01:09 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:00:13 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-03 06:00:11 | Rathnapura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.113 |  |
| 2026-11-03 05:55:39 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -1.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 06:03:35 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | 0.772 | 🔺 Rising |
| 2026-11-03 06:01:13 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-11-03 06:02:49 | Moragaswewa (Deduru Oya) | 3.48 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-11-03 06:03:25 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-03 06:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-03 06:11:47 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-03 06:04:24 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-03 06:00:13 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 06:04:05 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-03 06:04:32 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 06:07:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 06:04:34 | Wellawaya (Kirindi Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:01:09 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:05:13 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:02:23 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:05:12 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:01:41 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:01:35 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-03 06:09:18 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.022 |  |
| 2026-11-03 06:01:20 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.032 |  |
| 2026-11-03 06:03:48 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.034 |  |
| 2026-11-03 06:03:10 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-11-03 06:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-11-03 06:06:57 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.043 |  |
| 2026-11-03 06:06:13 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.049 |  |
| 2026-11-03 06:04:04 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.062 |  |
| 2026-11-03 06:09:05 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | -0.081 |  |
| 2026-11-03 06:05:33 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.090 |  |
| 2026-11-03 06:06:22 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.112 |  |
| 2026-11-03 06:00:11 | Rathnapura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.113 |  |
| 2026-11-03 06:06:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.126 |  |
| 2026-11-03 06:06:30 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.136 |  |
| 2026-11-03 06:05:14 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.150 |  |
| 2026-11-03 06:02:53 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.171 |  |
| 2026-11-03 06:06:10 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.181 |  |
| 2026-11-03 06:01:25 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.217 |  |
| 2026-11-03 06:12:32 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -1.066 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)