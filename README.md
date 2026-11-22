# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_03:02:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 03:02:59 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.082 |  |
| 2026-11-23 03:02:54 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:02:49 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.175 |  |
| 2026-11-23 03:02:39 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 03:02:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:02:13 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:01:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:01:44 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 03:01:33 | Moragaswewa (Deduru Oya) | 2.15 | 🟢 Normal | -0.061 |  |
| 2026-11-23 03:01:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:01:13 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 03:00:21 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-23 02:55:15 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.005 |  |
| 2026-11-23 02:44:25 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | -0.015 |  |
| 2026-11-23 02:29:25 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.054 |  |
| 2026-11-23 02:28:32 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-23 02:27:06 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.004 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 02:07:13 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-11-23 02:04:30 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-11-23 02:04:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 5.478 | 🔺 Rising |
| 2026-11-23 03:01:13 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 02:28:32 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 03:01:44 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 03:02:39 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 03:01:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 02:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:01:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 02:12:24 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:08 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-23 02:03:35 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-23 02:02:32 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:02:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 01:02:26 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 02:06:41 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 02:08:24 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-23 02:27:06 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.004 |  |
| 2026-11-23 02:55:15 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.005 |  |
| 2026-11-23 03:02:54 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:02:13 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-23 02:06:54 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.011 |  |
| 2026-11-23 02:44:25 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | -0.015 |  |
| 2026-11-23 03:00:21 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 02:13:46 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.037 |  |
| 2026-11-23 02:07:11 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.039 |  |
| 2026-11-23 02:05:50 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.043 |  |
| 2026-11-23 00:00:36 | Moraketiya (Walawe Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-11-23 02:29:25 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.054 |  |
| 2026-11-23 03:01:33 | Moragaswewa (Deduru Oya) | 2.15 | 🟢 Normal | -0.061 |  |
| 2026-11-23 03:02:59 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.082 |  |
| 2026-11-23 02:02:03 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.087 |  |
| 2026-11-23 03:02:49 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.175 |  |
| 2026-11-23 02:04:44 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -1.565 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)