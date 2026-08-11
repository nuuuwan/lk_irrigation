# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_20:09:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 20:09:59 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-11 20:09:58 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:08:56 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.019 |  |
| 2026-08-11 20:08:23 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | -0.031 |  |
| 2026-08-11 20:07:55 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:07:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | -0.028 |  |
| 2026-08-11 20:06:55 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:06:46 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:06:29 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.038 |  |
| 2026-08-11 20:06:29 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.046 |  |
| 2026-08-11 20:05:26 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:05:22 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:04:58 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-11 20:04:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.101 |  |
| 2026-08-11 20:04:30 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:04:22 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:04:20 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-11 20:04:02 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:40 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:24 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:03 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:03:01 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:02:47 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:02:23 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:02:20 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-11 20:02:13 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:01:36 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -1.800 |  |
| 2026-08-11 20:01:26 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-11 20:01:16 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -1.800 |  |
| 2026-08-11 20:01:14 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:01:12 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.022 |  |
| 2026-08-11 20:00:59 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-08-11 19:45:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 20:09:59 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-11 20:04:58 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-11 20:01:26 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-11 20:04:20 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-11 20:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-11 20:05:26 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:01:14 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:40 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:24 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:15:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:01 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:03:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:05:22 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:02:23 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:02:20 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:04:23 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:04:02 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:09:58 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:01:06 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:06:55 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:00:45 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:04:30 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-08-11 20:04:22 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:06:46 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:07:55 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:02:13 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:02:47 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:03:03 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-08-11 20:00:59 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-08-11 20:08:56 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.019 |  |
| 2026-08-11 20:01:12 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.022 |  |
| 2026-08-11 20:07:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | -0.028 |  |
| 2026-08-11 20:08:23 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | -0.031 |  |
| 2026-08-11 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.031 |  |
| 2026-08-11 20:06:29 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.038 |  |
| 2026-08-11 20:06:29 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.046 |  |
| 2026-08-11 20:04:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.101 |  |
| 2026-08-11 20:01:36 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -1.800 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)