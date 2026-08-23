# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_12:09:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,285 measurements** from **39** stations.
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
| 2026-08-23 12:09:25 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-08-23 12:07:01 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-23 12:06:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-08-23 12:06:15 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:05:44 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:05:07 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.041 |  |
| 2026-08-23 12:04:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:04:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:04:36 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:04:31 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.068 |  |
| 2026-08-23 12:04:30 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:41 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:32 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:26 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:18 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:14 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:03:11 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.013 |  |
| 2026-08-23 12:03:09 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:03:05 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:59 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:55 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:54 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.026 |  |
| 2026-08-23 12:02:53 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:35 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:02:21 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.029 |  |
| 2026-08-23 12:02:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:07 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:07 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:01:49 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.029 |  |
| 2026-08-23 12:01:47 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:01:40 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-08-23 12:01:33 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.086 |  |
| 2026-08-23 12:01:33 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:01:21 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:00:33 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-08-23 12:00:33 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:00:17 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 12:01:40 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-08-23 12:07:01 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-23 12:03:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:00:17 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:18 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:26 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:04:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:32 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:55 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:04:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:00:33 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:04:36 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:01:47 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:59 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:14 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:53 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:02:07 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:41 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:04:30 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:01:33 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:05 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 12:03:09 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:05:44 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:06:15 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:02:35 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:02:07 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-08-23 12:00:33 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-08-23 12:09:25 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-08-23 12:03:11 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.013 |  |
| 2026-08-23 12:02:54 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.026 |  |
| 2026-08-23 12:02:21 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.029 |  |
| 2026-08-23 12:01:49 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.029 |  |
| 2026-08-23 12:06:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-08-23 12:05:07 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.041 |  |
| 2026-08-23 12:04:31 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.068 |  |
| 2026-08-23 12:01:33 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)