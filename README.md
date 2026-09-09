# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_14:26:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 14:26:18 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:17:14 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:14:19 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:11:50 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-09 14:10:27 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-09 14:09:29 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:08:17 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-09 14:08:12 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:08:10 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:07:58 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:06:17 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:05:53 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:05:48 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.028 |  |
| 2026-09-09 14:05:36 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:05:15 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-09 14:04:41 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.019 |  |
| 2026-09-09 14:04:31 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-09 14:04:14 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-09 14:04:00 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:03:46 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.054 |  |
| 2026-09-09 14:03:40 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:03:25 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-09-09 14:03:19 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.067 |  |
| 2026-09-09 14:02:59 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-09 14:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:02:51 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:02:43 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:02:41 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-09 14:02:38 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.060 |  |
| 2026-09-09 14:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.041 |  |
| 2026-09-09 14:02:33 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:02:22 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-09 14:01:53 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:01:50 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:01:37 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:01:32 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:01:27 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-09-09 14:01:26 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:00:42 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:00:18 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:59:52 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:57:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 14:04:31 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-09 14:02:41 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-09 14:02:59 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-09 14:04:14 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-09 14:10:27 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-09 14:11:50 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-09 14:00:18 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:03:40 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:01:53 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:57:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:04:00 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:00:42 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:08:12 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:05:53 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:02:51 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:26:18 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:01:37 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:06:17 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:17:14 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:07:58 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:02:43 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:09:29 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:08:10 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:01:50 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:14:19 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:05:36 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:08:17 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-09 14:02:22 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-09 14:01:27 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-09-09 14:04:41 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.019 |  |
| 2026-09-09 14:03:25 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-09-09 14:05:15 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-09 14:05:48 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.028 |  |
| 2026-09-09 14:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.041 |  |
| 2026-09-09 14:03:46 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.054 |  |
| 2026-09-09 14:02:38 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.060 |  |
| 2026-09-09 14:03:19 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)