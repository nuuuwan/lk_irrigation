# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_14:25:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 14:25:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:13:12 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-08-04 14:12:42 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2026-08-04 14:11:06 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-08-04 14:10:34 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.053 |  |
| 2026-08-04 14:08:12 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-08-04 14:07:38 | Rathnapura (Kalu Ganga) | 6.53 | 🟡 Alert | -0.115 |  |
| 2026-08-04 14:07:19 | Peradeniya (Mahaweli Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:06:49 | Glencourse (Kelani Ganga) | 13.22 | 🟢 Normal | -0.187 |  |
| 2026-08-04 14:06:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-04 14:04:25 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 14:04:22 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-08-04 14:04:17 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:04:12 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:03:59 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.157 |  |
| 2026-08-04 14:03:55 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | -0.015 |  |
| 2026-08-04 14:03:48 | Hanwella (Kelani Ganga) | 5.97 | 🟢 Normal | -0.152 |  |
| 2026-08-04 14:03:38 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.060 |  |
| 2026-08-04 14:03:28 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:03:19 | Nawalapitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-04 14:03:00 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:02:59 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.032 |  |
| 2026-08-04 14:02:53 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 14:02:38 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:02:38 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.38 | 🟡 Alert | -0.010 |  |
| 2026-08-04 14:02:10 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-08-04 14:02:02 | Kithulgala (Kelani Ganga) | 2.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 14:01:56 | Ellagawa (Kalu Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:35 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.040 |  |
| 2026-08-04 14:01:21 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:21 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:16 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:05 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:00:58 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:00:47 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 14:00:36 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:00:35 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.38 | 🟡 Alert | -0.010 |  |
| 2026-08-04 14:07:38 | Rathnapura (Kalu Ganga) | 6.53 | 🟡 Alert | -0.115 |  |
| 2026-08-04 14:03:19 | Nawalapitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-04 14:02:53 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 14:04:25 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 14:00:47 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 14:02:02 | Kithulgala (Kelani Ganga) | 2.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 14:00:58 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:02:38 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:25:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:21 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:56 | Ellagawa (Kalu Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:03:28 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:00:36 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:05 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:04:12 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:03:00 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:21 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:01:16 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:07:19 | Peradeniya (Mahaweli Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:04:17 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:20 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-04 14:11:06 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-08-04 14:12:42 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2026-08-04 14:04:22 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-08-04 14:06:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-04 14:08:12 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-08-04 14:03:55 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | -0.015 |  |
| 2026-08-04 14:02:10 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-08-04 14:02:59 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.032 |  |
| 2026-08-04 14:01:35 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.040 |  |
| 2026-08-04 14:13:12 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-08-04 14:10:34 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.053 |  |
| 2026-08-04 14:03:38 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.060 |  |
| 2026-08-04 14:00:15 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.113 |  |
| 2026-08-04 14:03:48 | Hanwella (Kelani Ganga) | 5.97 | 🟢 Normal | -0.152 |  |
| 2026-08-04 14:03:59 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.157 |  |
| 2026-08-04 14:06:49 | Glencourse (Kelani Ganga) | 13.22 | 🟢 Normal | -0.187 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)