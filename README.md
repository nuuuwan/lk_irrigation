# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_03:16:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,770 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 03:16:38 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:15:53 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:15:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:15:11 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:15:09 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:11:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.026 |  |
| 2026-08-15 03:10:20 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:07:26 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-15 03:06:24 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:06:17 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.074 |  |
| 2026-08-15 03:06:07 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-15 03:06:03 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:05:56 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:05:41 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:05:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-15 03:05:19 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:04:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:04:35 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:04:25 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-15 03:04:21 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-08-15 03:04:04 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:04:02 | Deraniyagala (Kelani Ganga) | 3.16 | 🟢 Normal | 0.498 | 🔺 Rising |
| 2026-08-15 03:03:44 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 03:02:07 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.843 | 🔺 Rising |
| 2026-08-15 03:04:02 | Deraniyagala (Kelani Ganga) | 3.16 | 🟢 Normal | 0.498 | 🔺 Rising |
| 2026-08-15 03:04:21 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-08-15 03:05:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-15 02:01:23 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-15 03:04:25 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-15 03:02:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-15 03:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-15 03:07:26 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-15 03:02:52 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-15 03:02:50 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 03:06:07 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-15 03:01:50 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:01:15 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:03:44 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:04:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:02:22 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 00:01:37 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 18:02:32 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:06:03 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:04:35 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:10:20 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:16:38 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:15:11 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:01:32 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-15 01:02:09 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:02:52 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:02:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:05:41 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:15:53 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:05:19 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:15:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:06:24 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:03:17 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-08-15 03:11:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.026 |  |
| 2026-08-15 03:02:35 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-08-14 18:01:00 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.055 |  |
| 2026-08-15 03:06:17 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)