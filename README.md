# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_12:11:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,216 measurements** from **39** stations.
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
| 2026-08-14 12:11:42 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-14 12:09:54 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-08-14 12:09:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-14 12:08:09 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:07:25 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:06:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:06:19 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-14 12:06:15 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:06:09 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-08-14 12:05:19 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:04:42 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:04:22 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-08-14 12:04:16 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-14 12:04:07 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:03:39 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 12:03:27 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-08-14 12:03:13 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-14 12:02:55 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-14 12:02:38 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-14 12:02:26 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:02:18 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:02:16 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:02:10 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:02:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:01:55 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.022 |  |
| 2026-08-14 12:01:54 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-14 12:01:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:01:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-14 12:01:15 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-14 12:01:15 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-08-14 12:01:10 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:00:54 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:00:49 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.022 |  |
| 2026-08-14 12:00:40 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:00:19 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-08-14 12:00:14 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-14 11:40:46 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.027 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 12:00:19 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-08-14 12:01:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-14 12:02:38 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-14 12:03:13 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-14 12:06:19 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-14 12:02:55 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-14 12:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 12:11:42 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-14 12:02:16 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:00:40 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:01:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:02:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:05:19 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:06:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:04:07 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:02:10 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:08:09 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:00:54 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:00:14 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:02:18 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:07:25 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:02:26 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:04:42 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:01:10 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:03:39 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 12:04:16 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-14 12:01:15 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-14 12:09:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-14 12:01:54 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-14 12:04:22 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-08-14 12:03:27 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-08-14 12:06:09 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-08-14 11:10:37 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.021 |  |
| 2026-08-14 12:01:15 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-08-14 12:00:49 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.022 |  |
| 2026-08-14 12:01:55 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.022 |  |
| 2026-08-14 12:09:54 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-08-14 11:04:38 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)