# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_09:03:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,305 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 09:03:55 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:03:51 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:03:46 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.015 |  |
| 2026-11-24 09:02:59 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.029 |  |
| 2026-11-24 09:02:51 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 09:02:50 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.057 |  |
| 2026-11-24 09:02:43 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-11-24 09:02:23 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:02:14 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-11-24 09:02:09 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 09:02:08 | Moraketiya (Walawe Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:02:03 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:01:51 | Giriulla (Maha Oya) | 3.18 | 🟢 Normal | -0.209 |  |
| 2026-11-24 09:01:50 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:01:47 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:01:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:00:40 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:00:36 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:00:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-24 08:36:29 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-24 08:27:39 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-24 08:24:08 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 09:02:09 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 09:02:51 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 08:04:24 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 08:27:39 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-24 08:02:12 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 08:00:54 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 08:10:47 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-11-24 09:03:51 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:00:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:00:36 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:00:40 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:01:50 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:03:55 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:02:03 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-24 08:03:16 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-24 08:05:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:02:08 | Moraketiya (Walawe Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:01:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 08:01:34 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:01:47 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-24 09:02:23 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-24 08:04:40 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-24 08:01:33 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-11-24 09:02:43 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-11-24 09:02:14 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-11-24 09:03:46 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.015 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 08:18:40 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.025 |  |
| 2026-11-24 09:02:59 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.029 |  |
| 2026-11-24 08:03:49 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2026-11-24 08:02:38 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-11-24 08:03:43 | Badalgama (Maha Oya) | 4.67 | 🟢 Normal | -0.031 |  |
| 2026-11-24 09:02:50 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.057 |  |
| 2026-11-24 08:03:43 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.058 |  |
| 2026-11-24 08:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.086 |  |
| 2026-11-24 08:03:57 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.095 |  |
| 2026-11-24 09:01:51 | Giriulla (Maha Oya) | 3.18 | 🟢 Normal | -0.209 |  |
| 2026-11-24 08:04:41 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.276 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)