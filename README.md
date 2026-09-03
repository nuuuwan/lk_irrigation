# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_10:17:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,620 measurements** from **39** stations.
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
| 2026-09-03 10:17:24 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.016 |  |
| 2026-09-03 10:13:05 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:11:28 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:07:53 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-03 10:07:50 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.009 |  |
| 2026-09-03 10:07:48 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.144 |  |
| 2026-09-03 10:07:34 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.047 |  |
| 2026-09-03 10:07:28 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:07:05 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 10:06:09 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-03 10:05:56 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:05:48 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:05:25 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:04:40 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:04:07 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:58 | Thanamalwila (Kirindi Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-03 10:03:56 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:51 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:17 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:04 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:02:42 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:02:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:02:29 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:02:28 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-09-03 10:02:21 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-09-03 10:02:08 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.112 |  |
| 2026-09-03 10:01:55 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.079 |  |
| 2026-09-03 10:01:45 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:30 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -6.339 |  |
| 2026-09-03 10:01:22 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:18 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-03 10:01:15 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:14 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:00:51 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:00:39 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.011 |  |
| 2026-09-03 10:00:08 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:00:07 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 10:06:09 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-03 10:07:53 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-03 10:01:18 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-03 10:07:05 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 10:03:56 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:15 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:55 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:02:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:11:28 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:45 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:05:25 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:13:05 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:14 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:02:42 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:04:07 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:51 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:00:08 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:04 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:00:07 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:07:28 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:01:22 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:02:29 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:05:56 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:00:51 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:04:40 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:05:48 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:03:17 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 10:07:50 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.009 |  |
| 2026-09-03 10:03:58 | Thanamalwila (Kirindi Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-03 10:02:21 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-09-03 10:00:39 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.011 |  |
| 2026-09-03 10:17:24 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.016 |  |
| 2026-09-03 10:02:28 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-09-03 10:07:34 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.047 |  |
| 2026-09-03 10:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.079 |  |
| 2026-09-03 10:02:08 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.112 |  |
| 2026-09-03 10:07:48 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.144 |  |
| 2026-09-03 10:01:30 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -6.339 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)