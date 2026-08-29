# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_15:02:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,332 measurements** from **39** stations.
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
| 2026-08-29 15:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:41 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-08-29 15:02:40 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:38 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:36 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-29 15:02:30 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.041 |  |
| 2026-08-29 15:02:27 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-08-29 15:02:22 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-29 15:02:17 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:04 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-29 15:02:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:01 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:01:44 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.060 |  |
| 2026-08-29 15:01:40 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:01:30 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 15:01:15 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:57 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:49 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 15:00:49 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:41 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:29:09 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.007 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 14:03:36 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-29 14:15:22 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-29 15:02:22 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-29 14:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 14:13:29 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-29 15:02:04 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-29 15:02:36 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-29 14:05:38 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 15:01:30 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 15:00:49 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 14:29:09 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-29 14:03:16 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 13:00:09 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:41 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:38 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:09:40 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:01 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:00:34 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:49 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:10:51 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:08:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:17 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:40 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:57 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:01:15 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:09:01 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:01:40 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:52 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:06:00 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:00:50 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-29 15:02:27 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-08-29 15:02:41 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-08-29 15:02:30 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.041 |  |
| 2026-08-29 14:05:34 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.049 |  |
| 2026-08-29 15:01:44 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)