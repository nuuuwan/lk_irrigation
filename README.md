# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_20:03:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,849 measurements** from **39** stations.
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
| 2026-11-23 20:03:04 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-11-23 20:02:59 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-23 20:02:45 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.074 |  |
| 2026-11-23 20:02:41 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-23 20:02:39 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 20:02:16 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:02:10 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:01:48 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:01:33 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-23 20:01:26 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-11-23 20:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.062 |  |
| 2026-11-23 20:00:59 | Moraketiya (Walawe Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:00:50 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 19:04:24 | Peradeniya (Mahaweli Ganga) | 3.31 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-23 20:02:59 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-23 20:02:41 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-23 19:03:50 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 20:00:50 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 20:02:39 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 19:00:11 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:02:10 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:12:42 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:10:03 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:01:48 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:00:59 | Moraketiya (Walawe Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:01:37 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:22:37 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 20:02:16 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:05:10 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:05:10 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:08:36 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:02:54 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 19:05:54 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-23 19:02:21 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-23 19:01:35 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-23 19:13:17 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.018 |  |
| 2026-11-23 19:06:24 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.019 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-23 20:01:33 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 19:04:44 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.029 |  |
| 2026-11-23 20:01:26 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-11-23 19:03:15 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.030 |  |
| 2026-11-23 19:09:19 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.036 |  |
| 2026-11-23 19:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | -0.040 |  |
| 2026-11-23 20:03:04 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-23 19:05:14 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.058 |  |
| 2026-11-23 20:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.062 |  |
| 2026-11-23 20:02:45 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)