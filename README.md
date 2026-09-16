# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_18:11:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,672 measurements** from **39** stations.
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
| 2026-09-16 18:11:41 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.086 |  |
| 2026-09-16 18:11:20 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-16 18:09:47 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:08:49 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 18:08:44 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:07:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:07:05 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:05:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 18:05:29 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.014 |  |
| 2026-09-16 18:04:50 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | -0.015 |  |
| 2026-09-16 18:04:34 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-09-16 18:04:23 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.070 |  |
| 2026-09-16 18:04:22 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.058 |  |
| 2026-09-16 18:04:03 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.059 |  |
| 2026-09-16 18:03:28 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-09-16 18:03:19 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.062 |  |
| 2026-09-16 18:03:10 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:02:59 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.051 |  |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:02:36 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:02:26 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:02:21 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.037 |  |
| 2026-09-16 18:02:18 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:54 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:53 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:47 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:31 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 18:01:26 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:12 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:04 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:47 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 18:00:44 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |
| 2026-09-16 18:00:17 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:00:16 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:00:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 18:01:12 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-09-16 18:04:34 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-09-16 18:11:20 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-16 18:00:44 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-16 18:00:47 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 18:01:31 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 18:05:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 18:08:49 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:00:16 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:53 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:26 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:02:21 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:47 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:00:17 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:09:47 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:54 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:03:10 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:08:44 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:07:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:00:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:02:36 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:02:18 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:02:26 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:01:04 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:05:29 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.014 |  |
| 2026-09-16 18:04:50 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | -0.015 |  |
| 2026-09-16 18:03:28 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-09-16 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.037 |  |
| 2026-09-16 18:02:59 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.051 |  |
| 2026-09-16 18:04:22 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.058 |  |
| 2026-09-16 18:04:03 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.059 |  |
| 2026-09-16 18:03:19 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.062 |  |
| 2026-09-16 18:04:23 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.070 |  |
| 2026-09-16 18:11:41 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.086 |  |
| 2026-09-16 18:00:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)