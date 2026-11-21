# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_01:02:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 01:02:54 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-11-22 01:02:26 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-22 01:02:19 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-22 01:02:14 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:02:06 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.051 |  |
| 2026-11-22 01:02:04 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:57 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.100 |  |
| 2026-11-22 01:01:49 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.070 |  |
| 2026-11-22 01:01:46 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:32 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-11-22 01:01:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:27 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:17 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-22 01:01:15 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 00:01:13 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-11-22 00:03:15 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-22 00:04:04 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-22 01:02:19 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-22 01:02:26 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-22 01:01:17 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-22 00:04:39 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 00:09:18 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-22 00:00:33 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:12:53 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:02:04 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:27 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:46 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:02:14 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:55 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:46 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:08:25 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:12:30 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-22 00:02:22 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-11-22 00:02:24 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-11-22 00:10:00 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-11-22 01:01:32 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-11-22 01:02:54 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-11-22 00:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.032 |  |
| 2026-11-22 00:06:27 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -0.039 |  |
| 2026-11-22 00:05:56 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.042 |  |
| 2026-11-22 00:04:25 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.051 |  |
| 2026-11-22 01:02:06 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.051 |  |
| 2026-11-22 00:03:21 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.051 |  |
| 2026-11-22 01:01:49 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.070 |  |
| 2026-11-22 01:01:15 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.071 |  |
| 2026-11-22 01:01:57 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.100 |  |
| 2026-11-22 00:02:47 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)