# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_15:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,496 measurements** from **39** stations.
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
| 2026-08-22 15:13:08 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:10:05 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-08-22 15:08:57 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.047 |  |
| 2026-08-22 15:07:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:06:17 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-22 15:06:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:05:55 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-22 15:05:53 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:04:48 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-08-22 15:04:42 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.049 |  |
| 2026-08-22 15:04:40 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:04:40 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:04:01 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-22 15:04:00 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | -0.048 |  |
| 2026-08-22 15:03:45 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:30 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-08-22 15:03:30 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:21 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:14 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-08-22 15:03:08 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:48 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-08-22 15:02:36 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:35 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-08-22 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.020 |  |
| 2026-08-22 15:02:18 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:16 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:10 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:10 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-08-22 15:02:10 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-22 15:02:09 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:01:56 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:01:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:01:41 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-22 15:01:18 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.026 |  |
| 2026-08-22 15:01:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:01:13 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:01:07 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.023 |  |
| 2026-08-22 15:00:31 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 15:02:10 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-08-22 15:05:55 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-22 15:02:10 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-22 15:04:01 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-22 15:01:41 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-22 15:01:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:01:56 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:30 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:01:13 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:21 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:13:08 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:04:40 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:06:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:36 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:05:53 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:01:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:16 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:08 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:14 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:09 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:04:40 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:07:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:03:45 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:02:10 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-22 15:06:17 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-22 15:03:30 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-08-22 15:00:31 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-08-22 15:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-08-22 15:02:35 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-08-22 15:04:48 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-08-22 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.020 |  |
| 2026-08-22 15:01:07 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.023 |  |
| 2026-08-22 15:01:18 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.026 |  |
| 2026-08-22 15:10:05 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-08-22 15:02:48 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-08-22 15:08:57 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.047 |  |
| 2026-08-22 15:04:00 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | -0.048 |  |
| 2026-08-22 15:04:42 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)