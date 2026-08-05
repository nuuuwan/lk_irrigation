# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_23:17:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,977 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 23:17:04 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | -0.008 |  |
| 2026-08-05 23:14:52 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-08-05 23:12:44 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:10:18 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 23:02:48 | Peradeniya (Mahaweli Ganga) | 5.40 | 🟡 Alert | -0.324 |  |
| 2026-08-05 22:06:10 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-05 23:01:06 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 23:12:44 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:03:01 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-05 22:02:03 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:04:19 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:00:49 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:02:40 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:04:07 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:05:54 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:04:46 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:01:31 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 23:17:04 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | -0.008 |  |
| 2026-08-05 23:09:51 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-08-05 23:14:52 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-05 22:03:02 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-05 23:10:18 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-08-05 23:01:58 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | -0.011 |  |
| 2026-08-05 23:03:36 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-08-05 23:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.011 |  |
| 2026-08-05 23:10:01 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-08-05 23:01:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.016 |  |
| 2026-08-05 23:07:53 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-08-05 22:02:21 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-08-05 23:01:12 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.026 |  |
| 2026-08-05 23:04:40 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-08-05 23:02:41 | Kithulgala (Kelani Ganga) | 2.52 | 🟢 Normal | -0.030 |  |
| 2026-08-05 23:01:13 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.030 |  |
| 2026-08-05 23:00:46 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.031 |  |
| 2026-08-05 23:03:57 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-08-05 23:02:30 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.033 |  |
| 2026-08-05 23:02:21 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.062 |  |
| 2026-08-05 23:04:44 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.071 |  |
| 2026-08-05 22:02:02 | Rathnapura (Kalu Ganga) | 3.53 | 🟢 Normal | -0.107 |  |
| 2026-08-05 23:01:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)