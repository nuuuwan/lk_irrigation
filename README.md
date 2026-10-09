# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_15:16:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 15:16:59 | Urawa (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.635 | 🔺 Rising |
| 2026-10-09 15:10:39 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-10-09 15:07:58 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-09 15:07:49 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-10-09 15:07:41 | Baddegama (Gin Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-10-09 15:07:38 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-10-09 15:06:00 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 15:05:58 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | -0.039 |  |
| 2026-10-09 15:05:51 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.042 |  |
| 2026-10-09 15:05:51 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.040 |  |
| 2026-10-09 15:05:12 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.060 |  |
| 2026-10-09 15:05:02 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:04:58 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.198 |  |
| 2026-10-09 15:04:30 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-09 15:04:30 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-09 15:04:26 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.042 |  |
| 2026-10-09 15:04:22 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.113 |  |
| 2026-10-09 15:04:11 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | -0.068 |  |
| 2026-10-09 15:04:09 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.031 |  |
| 2026-10-09 15:04:01 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 15:03:47 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 15:03:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:03:22 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.092 |  |
| 2026-10-09 15:03:17 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.75 | 🟢 Normal | -0.059 |  |
| 2026-10-09 15:02:37 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-10-09 15:02:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:02:34 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.145 |  |
| 2026-10-09 15:02:30 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:02:28 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:02:14 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | -0.051 |  |
| 2026-10-09 15:02:08 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-10-09 15:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-09 15:01:56 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-10-09 15:00:59 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-10-09 15:00:59 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 15:00:37 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:00:24 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 15:16:59 | Urawa (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.635 | 🔺 Rising |
| 2026-10-09 15:04:30 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-09 15:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-09 15:03:47 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 15:04:01 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 15:07:58 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-09 15:00:59 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 15:06:00 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 15:03:17 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:03:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:01:02 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:00:37 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:02:30 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:02:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:02:28 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:00:24 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:05:02 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-09 15:10:39 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-10-09 15:07:49 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-10-09 15:07:41 | Baddegama (Gin Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-10-09 15:04:30 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-09 15:07:38 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-10-09 15:00:59 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-10-09 15:02:08 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-10-09 15:02:37 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-10-09 15:01:56 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-10-09 15:04:09 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.031 |  |
| 2026-10-09 15:05:58 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | -0.039 |  |
| 2026-10-09 15:05:51 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.040 |  |
| 2026-10-09 15:04:26 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.042 |  |
| 2026-10-09 15:05:51 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.042 |  |
| 2026-10-09 15:02:14 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | -0.051 |  |
| 2026-10-09 15:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.75 | 🟢 Normal | -0.059 |  |
| 2026-10-09 15:05:12 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.060 |  |
| 2026-10-09 15:04:11 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | -0.068 |  |
| 2026-10-09 15:03:22 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.092 |  |
| 2026-10-09 15:04:22 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.113 |  |
| 2026-10-09 15:02:34 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.145 |  |
| 2026-10-09 15:04:58 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.198 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)