# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_03:05:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,552 measurements** from **39** stations.
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
| 2026-08-17 03:05:33 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 03:05:29 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 03:04:59 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:04:46 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:04:00 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-17 03:03:57 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:03:53 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:03:16 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:03:05 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 03:02:52 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:02:49 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-08-17 03:02:35 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 03:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-08-17 03:02:20 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:02:04 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-17 03:02:01 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:02:00 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 03:01:23 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 03:01:13 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-17 03:01:05 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:00:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:00:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-17 02:39:10 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 03:04:00 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-17 03:00:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-17 02:10:33 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-17 03:02:04 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-17 03:02:35 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 02:39:10 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 03:05:33 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 02:02:03 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-17 03:01:23 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 03:02:00 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 03:03:05 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 03:05:29 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 03:01:05 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:04:59 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:02:01 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:03:53 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:57 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:01:53 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:00:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:02:20 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:03:16 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:02:52 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:03:23 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:10:59 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:04:46 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 03:03:57 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:02:30 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:06:27 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:08:34 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-08-17 03:01:13 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-08-17 02:07:29 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-08-17 02:02:10 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-08-17 03:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-08-17 02:03:34 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.013 |  |
| 2026-08-17 02:10:57 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.018 |  |
| 2026-08-17 03:02:49 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-08-17 01:01:29 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)