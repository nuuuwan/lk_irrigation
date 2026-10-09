# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_11:15:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,108 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 11:15:08 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:12:32 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-09 11:11:05 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-10-09 11:08:27 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.044 |  |
| 2026-10-09 11:07:27 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:07:26 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.115 |  |
| 2026-10-09 11:07:07 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.104 |  |
| 2026-10-09 11:06:57 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.051 |  |
| 2026-10-09 11:06:21 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | -0.354 |  |
| 2026-10-09 11:05:22 | Badalgama (Maha Oya) | 4.42 | 🟢 Normal | -0.149 |  |
| 2026-10-09 11:05:08 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.099 |  |
| 2026-10-09 11:04:59 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-10-09 11:04:46 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.021 |  |
| 2026-10-09 11:04:12 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-10-09 11:03:48 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-09 11:03:47 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-09 11:03:46 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:03:29 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.021 |  |
| 2026-10-09 11:03:26 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:03:24 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.089 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 11:02:27 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-10-09 11:03:48 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-09 11:03:01 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 11:00:53 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:02:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:07:27 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:03:26 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:00:37 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:01:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:00:59 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:15:08 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:03:46 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-09 11:02:10 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-09 11:12:32 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-09 11:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | -0.010 |  |
| 2026-10-09 11:03:47 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-09 11:01:56 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:00:42 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-09 11:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-09 11:01:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.013 |  |
| 2026-10-09 11:04:12 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-10-09 11:04:59 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-10-09 11:03:29 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.021 |  |
| 2026-10-09 11:04:46 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.021 |  |
| 2026-10-09 11:00:50 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.030 |  |
| 2026-10-09 11:11:05 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-10-09 11:08:27 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.044 |  |
| 2026-10-09 11:06:57 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.051 |  |
| 2026-10-09 11:03:07 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.068 |  |
| 2026-10-09 11:02:10 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.080 |  |
| 2026-10-09 11:02:50 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.081 |  |
| 2026-10-09 11:03:24 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.089 |  |
| 2026-10-09 11:05:08 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.099 |  |
| 2026-10-09 10:07:46 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | -0.102 |  |
| 2026-10-09 11:07:07 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.104 |  |
| 2026-10-09 11:02:09 | Panadugama (Nilwala Ganga) | 4.13 | 🟢 Normal | -0.107 |  |
| 2026-10-09 11:07:26 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.115 |  |
| 2026-10-09 11:05:22 | Badalgama (Maha Oya) | 4.42 | 🟢 Normal | -0.149 |  |
| 2026-10-09 11:06:21 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | -0.354 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)