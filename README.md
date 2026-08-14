# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_01:17:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,700 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 01:17:06 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:11:55 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 01:11:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-15 01:07:40 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 01:07:09 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:07:05 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.050 |  |
| 2026-08-15 01:07:01 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:06:53 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-08-15 01:06:28 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-15 01:06:25 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-15 01:05:10 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-15 01:05:07 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-15 01:04:50 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-15 01:03:53 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 01:03:48 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-15 01:03:41 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:03:37 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:03:04 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:03:00 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:56 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:41 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-15 01:02:39 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-15 01:02:38 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-08-15 01:02:31 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-15 01:02:29 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-15 01:02:24 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:09 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:06 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 01:01:46 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:01:21 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:00:41 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 01:02:38 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-08-15 01:06:53 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-08-15 01:06:25 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-15 01:02:31 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-15 01:02:29 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-15 01:05:10 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-15 01:04:50 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-15 01:03:48 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-15 01:11:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-15 01:02:41 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-15 01:05:07 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-15 01:07:40 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 01:06:28 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-15 01:02:06 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 01:03:53 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 01:11:55 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 00:05:17 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:01:21 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:03:04 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:24 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:03:41 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 00:01:37 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 18:02:32 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:03:37 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 00:06:41 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:10:40 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:01:46 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:09 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:03:00 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:56 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:07:01 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:17:06 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:00:41 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:07:09 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:39 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-15 00:07:17 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-08-14 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-08-15 01:07:05 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.050 |  |
| 2026-08-14 18:01:00 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.055 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)