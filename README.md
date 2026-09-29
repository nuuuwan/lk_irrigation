# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_22:13:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,523 measurements** from **39** stations.
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
| 2026-09-29 22:13:24 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.037 |  |
| 2026-09-29 22:13:22 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.017 |  |
| 2026-09-29 22:13:15 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:09:01 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:07:28 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:07:11 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-29 22:05:37 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:05:07 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-09-29 22:05:07 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.041 |  |
| 2026-09-29 22:04:49 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:04:27 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 22:04:19 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:04:01 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:03:56 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:03:47 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2026-09-29 22:03:31 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:03:28 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:51 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:48 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.051 |  |
| 2026-09-29 22:02:39 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-09-29 22:02:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:29 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.012 |  |
| 2026-09-29 22:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:13 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:03 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-29 22:01:49 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:01:34 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-29 22:01:27 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.030 |  |
| 2026-09-29 22:01:21 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-09-29 22:01:18 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-29 22:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:01:11 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-29 22:00:39 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.011 |  |
| 2026-09-29 22:00:25 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 22:01:34 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-29 21:01:18 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-29 22:07:11 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-29 22:00:25 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 22:04:27 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 22:03:31 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:13 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:03:56 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:13:15 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:04:19 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:04:01 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:01:49 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:05:37 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:04:49 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:03:28 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:07:28 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:09:01 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:51 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:01:11 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-29 22:01:18 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:04:01 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-09-29 22:02:03 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-29 22:05:07 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-09-29 22:00:39 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.011 |  |
| 2026-09-29 22:02:39 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-09-29 22:02:29 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.012 |  |
| 2026-09-29 22:13:22 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.017 |  |
| 2026-09-29 22:01:21 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-09-29 22:01:27 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.030 |  |
| 2026-09-29 22:13:24 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.037 |  |
| 2026-09-29 22:03:47 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2026-09-29 22:05:07 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.041 |  |
| 2026-09-29 22:02:48 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)