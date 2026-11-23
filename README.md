# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_21:03:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,889 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 21:03:10 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:03:04 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 21:03:04 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.031 |  |
| 2026-11-23 21:02:52 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 21:02:51 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-23 21:02:39 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 21:02:35 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.267 |  |
| 2026-11-23 21:02:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-23 21:02:21 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:16 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.035 |  |
| 2026-11-23 21:02:14 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.146 |  |
| 2026-11-23 21:02:11 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:06 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:46 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:46 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-11-23 21:01:31 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-11-23 21:01:29 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:00:36 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:00:34 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 20:08:58 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-11-23 20:02:59 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-23 21:02:39 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 20:05:46 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-23 20:02:41 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-23 21:00:34 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 21:03:04 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 21:02:52 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 21:00:36 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:29 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:02:10 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:01:48 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:00:59 | Moraketiya (Walawe Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:21 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:03:10 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:46 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:05:43 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:11 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:09:10 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-11-23 21:02:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-23 20:03:21 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-23 21:02:51 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 20:05:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.028 |  |
| 2026-11-23 21:01:46 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-11-23 21:01:31 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-11-23 20:04:21 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.031 |  |
| 2026-11-23 21:03:04 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.031 |  |
| 2026-11-23 20:04:50 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.035 |  |
| 2026-11-23 21:02:16 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.035 |  |
| 2026-11-23 20:03:04 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-23 20:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.062 |  |
| 2026-11-23 20:03:43 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.082 |  |
| 2026-11-23 20:06:25 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.106 |  |
| 2026-11-23 21:02:14 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.146 |  |
| 2026-11-23 21:02:35 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)