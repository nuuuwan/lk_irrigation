# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--27_16:18:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,938 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-27 16:18:22 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:15:00 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:13:00 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:12:49 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:12:06 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-27 16:08:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:08:02 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:06:40 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-27 16:06:34 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:06:08 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.038 |  |
| 2026-08-27 16:05:56 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:05:03 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-27 16:04:43 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | -0.164 |  |
| 2026-08-27 16:04:37 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-27 16:04:14 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.049 |  |
| 2026-08-27 16:04:07 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 16:04:06 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:04:04 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.087 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-27 16:04:04 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-27 16:06:40 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-27 16:01:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-27 16:05:03 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-27 16:04:37 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-27 16:12:06 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-27 16:04:07 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 16:03:02 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 16:08:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:01:07 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:00:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:01:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:02:52 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:15:00 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-27 15:03:24 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:08:02 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:03:32 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:03:29 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:06:34 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:18:22 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:13:00 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:02:54 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:12:49 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:05:56 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:04:06 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:02:14 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:02:24 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-27 16:02:10 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-27 16:01:11 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-27 16:02:23 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-08-27 16:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-08-27 16:06:08 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.038 |  |
| 2026-08-27 16:02:35 | Hanwella (Kelani Ganga) | 1.93 | 🟢 Normal | -0.040 |  |
| 2026-08-27 16:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | -0.041 |  |
| 2026-08-27 16:04:14 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.049 |  |
| 2026-08-27 16:03:14 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | -0.058 |  |
| 2026-08-27 16:03:45 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.067 |  |
| 2026-08-27 16:01:51 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.081 |  |
| 2026-08-27 16:04:43 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)