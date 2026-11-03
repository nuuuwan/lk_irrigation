# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_09:21:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,571 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 09:21:32 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.025 |  |
| 2026-11-03 09:19:20 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.072 |  |
| 2026-11-03 09:14:25 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-11-03 09:11:19 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-11-03 09:09:46 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:08:40 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:07:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:06:55 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:06:44 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-11-03 09:06:40 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.179 |  |
| 2026-11-03 09:06:19 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:06:03 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-11-03 09:05:38 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.047 |  |
| 2026-11-03 09:05:29 | Moragaswewa (Deduru Oya) | 3.97 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-03 09:05:20 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-03 09:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-03 09:05:01 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.060 |  |
| 2026-11-03 09:04:46 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.128 |  |
| 2026-11-03 09:04:39 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.217 |  |
| 2026-11-03 09:04:17 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 09:03:53 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-03 09:03:30 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.137 |  |
| 2026-11-03 09:03:28 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.038 |  |
| 2026-11-03 09:03:23 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:03:22 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.050 |  |
| 2026-11-03 09:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:02:46 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.051 |  |
| 2026-11-03 09:02:40 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 09:02:24 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-03 09:02:10 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-11-03 09:02:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.040 |  |
| 2026-11-03 09:01:43 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:01:31 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.623 | 🔺 Rising |
| 2026-11-03 09:01:21 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:01:18 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.101 |  |
| 2026-11-03 09:01:15 | Wellawaya (Kirindi Oya) | 1.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 09:00:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:00:20 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:00:15 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 09:01:31 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.623 | 🔺 Rising |
| 2026-11-03 09:05:29 | Moragaswewa (Deduru Oya) | 3.97 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-03 09:02:24 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-03 09:05:20 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-03 09:04:17 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 09:01:15 | Wellawaya (Kirindi Oya) | 1.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 09:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-03 09:02:40 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 09:03:53 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-03 09:03:23 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:01:21 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:07:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:00:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:08:40 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:06:19 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:11:19 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-11-03 09:09:46 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:01:43 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:06:55 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:14:25 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-11-03 09:21:32 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.025 |  |
| 2026-11-03 09:06:03 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-11-03 09:06:44 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-11-03 09:03:28 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.038 |  |
| 2026-11-03 09:02:10 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-11-03 09:02:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.040 |  |
| 2026-11-03 09:00:15 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.044 |  |
| 2026-11-03 09:05:38 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.047 |  |
| 2026-11-03 09:03:22 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.050 |  |
| 2026-11-03 09:02:46 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.051 |  |
| 2026-11-03 09:05:01 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.060 |  |
| 2026-11-03 09:19:20 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.072 |  |
| 2026-11-03 08:06:23 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.098 |  |
| 2026-11-03 09:01:18 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.101 |  |
| 2026-11-03 09:04:46 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.128 |  |
| 2026-11-03 09:03:30 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.137 |  |
| 2026-11-03 09:06:40 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.179 |  |
| 2026-11-03 09:04:39 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.217 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)