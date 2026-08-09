# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_14:13:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,820 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 14:13:41 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.061 |  |
| 2026-08-09 14:10:28 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:09:30 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:07:45 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 14:07:13 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:06:46 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:06:09 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-09 14:05:58 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:04:42 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-08-09 14:04:30 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 14:04:27 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:04:22 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.77 | 🟢 Normal | -0.051 |  |
| 2026-08-09 14:03:53 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-09 14:03:46 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:03:30 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:03:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.090 |  |
| 2026-08-09 14:03:22 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:03:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:02:49 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-09 14:02:42 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-09 14:02:36 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | -0.127 |  |
| 2026-08-09 14:02:33 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 14:02:29 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.039 |  |
| 2026-08-09 14:02:27 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:02:21 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.011 |  |
| 2026-08-09 14:02:07 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:59 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.020 |  |
| 2026-08-09 14:01:52 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:47 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:18 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 14:01:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:11 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:08 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.010 |  |
| 2026-08-09 14:01:07 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-09 14:00:55 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:00:12 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 14:03:53 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-09 13:10:36 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-09 14:02:33 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 14:07:45 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 14:06:09 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-09 14:01:18 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 14:04:30 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 14:02:27 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:02:07 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:03:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:09:38 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:00:12 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:04:22 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:03:22 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:52 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:03:46 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:47 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:04:27 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:05:58 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:06:46 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:07:13 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:11 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:05:14 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:09:30 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:10:28 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:03:30 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:02:49 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-09 14:01:08 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.010 |  |
| 2026-08-09 14:02:42 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-09 14:01:07 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-09 14:02:21 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.011 |  |
| 2026-08-09 14:01:59 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.020 |  |
| 2026-08-09 14:04:42 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-08-09 14:02:29 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.039 |  |
| 2026-08-09 14:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.77 | 🟢 Normal | -0.051 |  |
| 2026-08-09 14:13:41 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.061 |  |
| 2026-08-09 14:03:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.090 |  |
| 2026-08-09 14:02:36 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)