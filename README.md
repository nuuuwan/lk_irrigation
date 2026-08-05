# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_04:15:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 04:15:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:13:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:12:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.026 |  |
| 2026-08-06 04:11:19 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:07:30 | Peradeniya (Mahaweli Ganga) | 4.26 | 🟢 Normal | -0.248 |  |
| 2026-08-06 04:07:15 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:06:02 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:05:35 | Glencourse (Kelani Ganga) | 11.44 | 🟢 Normal | -0.060 |  |
| 2026-08-06 04:05:33 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:05:17 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:04:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:04:41 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-08-06 04:04:36 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:04:07 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:04:00 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-06 04:03:44 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-08-06 04:03:35 | Kithulgala (Kelani Ganga) | 2.49 | 🟢 Normal | -0.021 |  |
| 2026-08-06 04:03:30 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-08-06 04:03:17 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:03:17 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.070 |  |
| 2026-08-06 04:03:12 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:02:48 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:02:34 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 04:02:28 | Nawalapitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-08-06 04:01:31 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.113 |  |
| 2026-08-06 04:01:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.016 |  |
| 2026-08-06 04:01:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 04:00:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:45:03 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 03:09:09 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-06 04:01:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 04:02:34 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 04:04:36 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:15:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:04:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:45:03 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:05:17 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:06:02 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:03:17 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:13:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:00:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:03:12 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:05:33 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:04:07 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:11:19 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:07:15 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:02:48 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:06:07 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 03:04:49 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | -0.005 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-06 04:03:44 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-08-06 04:04:00 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-06 03:02:07 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-08-06 04:01:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.016 |  |
| 2026-08-06 03:15:46 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.016 |  |
| 2026-08-06 04:04:41 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-08-06 04:02:28 | Nawalapitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-08-06 04:03:30 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-08-06 04:03:35 | Kithulgala (Kelani Ganga) | 2.49 | 🟢 Normal | -0.021 |  |
| 2026-08-06 04:12:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.026 |  |
| 2026-08-06 04:05:35 | Glencourse (Kelani Ganga) | 11.44 | 🟢 Normal | -0.060 |  |
| 2026-08-06 04:03:17 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.070 |  |
| 2026-08-06 04:01:31 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.113 |  |
| 2026-08-06 03:02:27 | Ellagawa (Kalu Ganga) | 8.05 | 🟢 Normal | -0.160 |  |
| 2026-08-06 04:07:30 | Peradeniya (Mahaweli Ganga) | 4.26 | 🟢 Normal | -0.248 |  |
| 2026-08-06 03:12:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)