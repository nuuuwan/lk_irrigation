# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_01:21:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **253,001 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 01:21:02 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:21:01 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:15:51 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:10:05 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-09-06 01:10:01 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-06 01:06:52 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:06:35 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.234 |  |
| 2026-09-06 01:06:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-06 01:06:07 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-09-06 01:05:26 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-09-06 01:05:15 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:04:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:04:10 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-06 01:03:54 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:03:46 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:03:15 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:03:06 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:34 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:26 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:24 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:06 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.041 |  |
| 2026-09-06 01:02:04 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:03 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-06 01:01:55 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-09-06 01:01:53 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:44 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-09-06 01:01:36 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:20 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:13 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 01:00:30 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-09-06 01:00:11 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.081 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 01:01:44 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-09-06 01:10:05 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-09-06 01:06:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-06 01:10:01 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-06 01:01:13 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 01:03:46 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:24 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:04:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:05:15 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:03:15 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:48 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-06 00:17:48 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:53 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:04 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-06 00:18:53 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:36 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 00:01:21 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:26 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:15:51 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:21:02 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:48 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:03:06 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-06 00:12:17 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:20 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:02:34 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 00:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-09-06 01:06:07 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-09-06 01:04:10 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-06 01:02:03 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-06 01:01:55 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-09-06 01:05:26 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-09-06 00:07:55 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2026-09-06 01:02:06 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.041 |  |
| 2026-09-05 18:09:31 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.049 |  |
| 2026-09-06 01:00:30 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-09-06 01:00:11 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.081 |  |
| 2026-09-06 01:06:35 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)