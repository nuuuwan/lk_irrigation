# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_00:25:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 00:25:51 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:18:54 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:12:47 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:08:53 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 00:08:48 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:07:56 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-11-20 00:07:01 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.014 |  |
| 2026-11-20 00:06:58 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:06:52 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:06:09 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.025 |  |
| 2026-11-20 00:05:40 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:05:28 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-11-20 00:05:04 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:04:51 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-20 00:04:36 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.005 |  |
| 2026-11-20 00:04:22 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-20 00:04:12 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:04:09 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:03:51 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:02:46 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:02:34 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-11-20 00:02:31 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-20 00:02:29 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:02:22 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:02:19 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-11-20 00:02:14 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-20 00:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-20 00:01:08 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:01:06 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:00:42 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 00:00:17 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 00:05:28 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-11-20 00:02:31 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-20 00:04:51 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-20 00:08:53 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 00:00:17 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 00:00:42 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 18:00:52 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:05:40 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:22 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:35 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:03:51 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:02:14 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:06:58 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:02:22 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:08:48 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:04:12 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:25:51 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:01:06 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:18:54 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:02:29 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:04:09 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:05:04 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:12:47 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 18:01:52 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:03:59 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:01:08 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:06:52 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:04:36 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.005 |  |
| 2026-11-19 23:02:07 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.005 |  |
| 2026-11-19 18:05:17 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-11-20 00:07:56 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-11-20 00:04:22 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-20 00:02:34 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-11-20 00:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-20 00:02:19 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-11-20 00:07:01 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.014 |  |
| 2026-11-20 00:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-20 00:06:09 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.025 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)