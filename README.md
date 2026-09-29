# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_16:08:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,295 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 16:08:21 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:08:08 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:08:01 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:07:43 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-09-29 16:07:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:06:20 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:06:15 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.038 |  |
| 2026-09-29 16:05:43 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.038 |  |
| 2026-09-29 16:05:20 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:04:28 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-09-29 16:04:07 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-29 16:04:05 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 16:04:04 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 16:03:58 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-09-29 16:03:55 | Dunamale (Aththanagalu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:03:46 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:03:43 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.040 |  |
| 2026-09-29 16:03:33 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:03:29 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | -0.072 |  |
| 2026-09-29 16:03:21 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:03:14 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-09-29 16:02:40 | Baddegama (Gin Ganga) | 2.98 | 🟢 Normal | -0.043 |  |
| 2026-09-29 16:02:38 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:02:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:53 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:32 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:01:31 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:14 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:00:57 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:00:52 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:00:42 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:00:20 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 16:07:43 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-09-29 16:03:58 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-09-29 16:04:07 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-29 16:04:05 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 16:04:04 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 16:00:20 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 16:01:31 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:00:42 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:14 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:07:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:05:20 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:08:21 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:53 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:56 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:02:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:01:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:02:38 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:01:31 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:08:45 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:03:46 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-29 16:08:01 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:06:20 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:03:21 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:03:33 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:03:55 | Dunamale (Aththanagalu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:08:08 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-09-29 16:01:32 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-09-29 15:00:36 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:02:35 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-09-29 16:04:28 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-09-29 16:03:14 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-09-29 16:06:15 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.038 |  |
| 2026-09-29 16:05:43 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.038 |  |
| 2026-09-29 16:03:43 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.040 |  |
| 2026-09-29 16:02:40 | Baddegama (Gin Ganga) | 2.98 | 🟢 Normal | -0.043 |  |
| 2026-09-29 15:08:25 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.043 |  |
| 2026-09-29 15:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.052 |  |
| 2026-09-29 16:03:29 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)