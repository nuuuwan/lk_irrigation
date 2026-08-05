# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_15:13:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,682 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 15:13:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-05 15:09:31 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:07:25 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.028 |  |
| 2026-08-05 15:07:22 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:06:59 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:06:40 | Rathnapura (Kalu Ganga) | 4.27 | 🟢 Normal | -0.107 |  |
| 2026-08-05 15:06:28 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.065 |  |
| 2026-08-05 15:06:26 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.038 |  |
| 2026-08-05 15:05:48 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:05:18 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:04:56 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-08-05 15:04:35 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-08-05 15:04:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:04:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:04:09 | Glencourse (Kelani Ganga) | 12.33 | 🟢 Normal | -0.030 |  |
| 2026-08-05 15:03:33 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | -0.050 |  |
| 2026-08-05 15:03:20 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:19 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:17 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:06 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:03 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-05 15:02:55 | Kithulgala (Kelani Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-08-05 15:02:23 | Peradeniya (Mahaweli Ganga) | 6.30 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-08-05 15:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.03 | 🟢 Normal | -0.060 |  |
| 2026-08-05 15:02:17 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.012 |  |
| 2026-08-05 15:02:17 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-08-05 15:02:02 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | -0.020 |  |
| 2026-08-05 15:01:58 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:01:56 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-08-05 15:01:55 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.163 |  |
| 2026-08-05 15:01:43 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.064 |  |
| 2026-08-05 15:01:42 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-05 15:01:42 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-05 15:01:41 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:00:59 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-08-05 15:00:17 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.081 |  |
| 2026-08-05 15:00:13 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:00:11 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 15:00:08 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 15:02:23 | Peradeniya (Mahaweli Ganga) | 6.30 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-08-05 15:13:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-05 15:01:42 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-05 15:00:11 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 15:05:18 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:00:08 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:04:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:06:59 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:20 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:09:31 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:05:48 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:01:58 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:04:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:06 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:01:41 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:07:22 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:00:13 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:03:17 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:04:56 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-08-05 15:01:42 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-05 15:02:55 | Kithulgala (Kelani Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-08-05 15:03:03 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-05 15:01:56 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-08-05 15:00:59 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-08-05 15:02:17 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.012 |  |
| 2026-08-05 15:04:35 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-08-05 15:02:02 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | -0.020 |  |
| 2026-08-05 15:07:25 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.028 |  |
| 2026-08-05 15:02:17 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-08-05 15:04:09 | Glencourse (Kelani Ganga) | 12.33 | 🟢 Normal | -0.030 |  |
| 2026-08-05 15:06:26 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.038 |  |
| 2026-08-05 15:03:33 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | -0.050 |  |
| 2026-08-05 15:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.03 | 🟢 Normal | -0.060 |  |
| 2026-08-05 15:01:43 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.064 |  |
| 2026-08-05 15:06:28 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.065 |  |
| 2026-08-05 15:00:17 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.081 |  |
| 2026-08-05 15:06:40 | Rathnapura (Kalu Ganga) | 4.27 | 🟢 Normal | -0.107 |  |
| 2026-08-05 15:01:55 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)