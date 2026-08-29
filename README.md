# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_09:05:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,101 measurements** from **39** stations.
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
| 2026-08-29 09:05:15 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 09:05:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:05:08 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:05:04 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-08-29 09:04:56 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:04:39 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 09:04:27 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:03:52 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 09:03:50 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:03:46 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:03:43 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:03:42 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.022 |  |
| 2026-08-29 09:03:40 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-29 09:03:11 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:02:59 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.062 |  |
| 2026-08-29 09:02:21 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:02:05 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.096 |  |
| 2026-08-29 09:01:49 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-08-29 09:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:01:43 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:01:43 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-08-29 09:01:35 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:01:32 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-08-29 09:01:25 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:01:23 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.168 |  |
| 2026-08-29 09:01:22 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.073 |  |
| 2026-08-29 09:01:14 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:01:08 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 09:05:04 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-08-29 08:15:59 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-29 09:03:40 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-29 08:01:31 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-29 09:05:15 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 09:04:39 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 09:03:52 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 09:02:59 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 09:01:08 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:20:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:04:56 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:04:27 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:12:40 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:03:43 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:04:10 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:05:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:11:42 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:02:21 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:02:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:17:12 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:05:08 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:01:25 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:01:14 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:02:01 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:03:50 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:03:46 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:03:11 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:01:43 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:01:35 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-08-29 09:01:49 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-08-29 09:01:32 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-08-29 09:03:42 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.022 |  |
| 2026-08-29 08:07:25 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.046 |  |
| 2026-08-29 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.062 |  |
| 2026-08-29 09:01:22 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.073 |  |
| 2026-08-29 09:02:05 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.096 |  |
| 2026-08-29 09:01:43 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-08-29 09:01:23 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)