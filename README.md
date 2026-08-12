# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_19:14:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,709 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 19:14:26 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:13:50 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-12 19:13:21 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 19:12:40 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:12:38 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:11:26 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-12 19:09:13 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-12 19:07:24 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:06:37 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:06:15 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:05:45 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-12 19:05:36 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.028 |  |
| 2026-08-12 19:05:34 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.029 |  |
| 2026-08-12 19:05:19 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:05:05 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 19:02:59 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-08-12 19:02:05 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-08-12 19:05:45 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-12 19:13:50 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-12 19:09:13 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-12 19:11:26 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-12 19:01:09 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-12 18:02:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 19:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 19:13:21 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 19:00:13 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:05:19 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:05:05 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:01:03 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:42 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:03:11 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:04:29 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:00:45 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:06:37 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:03:17 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:00:42 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:03:17 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:04:44 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:06:15 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:12:38 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:01:32 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:39 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:02:17 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:12:40 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:14:26 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:01:37 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:07:24 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-12 19:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-08-12 19:05:36 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.028 |  |
| 2026-08-12 19:05:34 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.029 |  |
| 2026-08-12 19:02:19 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-08-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.031 |  |
| 2026-08-12 19:02:33 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.039 |  |
| 2026-08-12 19:04:22 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)