# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_17:21:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,734 measurements** from **39** stations.
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
| 2026-08-11 17:21:12 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-08-11 17:16:24 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.026 |  |
| 2026-08-11 17:15:48 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-11 17:13:02 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:12:29 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-08-11 17:08:01 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:07:25 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:07:24 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:06:59 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:06:50 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-08-11 17:06:42 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:05:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.115 |  |
| 2026-08-11 17:05:01 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:04:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:04:24 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:04:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:03:43 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:03:20 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:03:17 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.024 |  |
| 2026-08-11 17:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:03:08 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:03:06 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:55 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:02:45 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.060 |  |
| 2026-08-11 17:02:40 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:33 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:22 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 17:02:20 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:20 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 17:02:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:11 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:01:26 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:01:21 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.055 |  |
| 2026-08-11 17:01:16 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.020 |  |
| 2026-08-11 17:01:13 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.013 |  |
| 2026-08-11 17:01:09 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-08-11 17:01:05 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:00:54 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-08-11 17:00:40 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 17:15:48 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-11 17:02:20 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 17:02:22 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 17:00:40 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 17:06:42 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:03:06 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:40 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:01:05 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:07:25 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:03:20 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:20 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:04:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:03:43 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:11 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:04:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:08:01 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:02:33 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-08-11 17:12:29 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-08-11 17:06:50 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-08-11 17:04:24 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:05:01 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:02:55 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:01:26 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:03:08 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:13:02 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:06:59 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-08-11 17:01:13 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.013 |  |
| 2026-08-11 17:00:54 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-08-11 17:01:16 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.020 |  |
| 2026-08-11 17:01:09 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-08-11 17:03:17 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.024 |  |
| 2026-08-11 17:16:24 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.026 |  |
| 2026-08-11 17:21:12 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-08-11 17:01:21 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.055 |  |
| 2026-08-11 17:02:45 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.060 |  |
| 2026-08-11 17:05:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)