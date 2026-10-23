# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_13:20:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,806 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 13:20:16 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.023 |  |
| 2026-10-23 13:16:11 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.033 |  |
| 2026-10-23 13:10:31 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-10-23 13:09:52 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 13:08:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:07:13 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.037 |  |
| 2026-10-23 13:07:00 | Thanthirimale (Malwathu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:06:57 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.060 |  |
| 2026-10-23 13:06:50 | Putupaula (Kalu Ganga) | 2.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-23 13:06:22 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:06:19 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.055 |  |
| 2026-10-23 13:06:11 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.063 |  |
| 2026-10-23 13:06:11 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.070 |  |
| 2026-10-23 13:05:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:05:02 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-10-23 13:04:44 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:04:38 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-10-23 13:04:26 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:04:24 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.040 |  |
| 2026-10-23 13:04:21 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:03:55 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:03:38 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.060 |  |
| 2026-10-23 13:03:32 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:03:30 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:03:28 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.098 |  |
| 2026-10-23 13:03:20 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-10-23 13:03:15 | Moragaswewa (Deduru Oya) | 4.70 | 🟢 Normal | -0.048 |  |
| 2026-10-23 13:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.030 |  |
| 2026-10-23 13:03:00 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-23 13:02:10 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | -0.032 |  |
| 2026-10-23 13:01:44 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-10-23 13:01:39 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.140 |  |
| 2026-10-23 13:01:23 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:01:18 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:01:08 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:01:03 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:00:33 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 13:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.030 |  |
| 2026-10-23 13:03:00 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-23 13:09:52 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 13:06:50 | Putupaula (Kalu Ganga) | 2.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-23 13:06:22 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:01:18 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:01:03 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:05:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:00:59 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:07:00 | Thanthirimale (Malwathu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:08:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:03:32 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:01:23 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:10:31 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-10-23 13:04:38 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-10-23 13:04:26 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:03:55 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:04:44 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:01:08 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:04:21 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:03:30 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-23 13:00:33 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-10-23 13:01:44 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-10-23 12:01:03 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-23 13:03:20 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-10-23 13:05:02 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-10-23 13:20:16 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.023 |  |
| 2026-10-23 13:02:10 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | -0.032 |  |
| 2026-10-23 13:16:11 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.033 |  |
| 2026-10-23 13:07:13 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.037 |  |
| 2026-10-23 13:04:24 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.040 |  |
| 2026-10-23 13:03:15 | Moragaswewa (Deduru Oya) | 4.70 | 🟢 Normal | -0.048 |  |
| 2026-10-23 13:06:19 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.055 |  |
| 2026-10-23 13:03:38 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.060 |  |
| 2026-10-23 13:06:57 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.060 |  |
| 2026-10-23 13:06:11 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.063 |  |
| 2026-10-23 13:06:11 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.070 |  |
| 2026-10-23 13:03:28 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.098 |  |
| 2026-10-23 13:01:39 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)