# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_15:17:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,792 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 15:17:34 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.017 |  |
| 2026-08-04 15:13:48 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:13:11 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:11:20 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.030 |  |
| 2026-08-04 15:11:10 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:07:55 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.167 |  |
| 2026-08-04 15:07:39 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-04 15:06:27 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:06:15 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-08-04 15:05:19 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:04:42 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-08-04 15:04:38 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-08-04 15:04:25 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-08-04 15:04:19 | Rathnapura (Kalu Ganga) | 6.43 | 🟡 Alert | -0.106 |  |
| 2026-08-04 15:04:18 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-04 15:03:56 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-08-04 15:03:53 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-08-04 15:03:49 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.050 |  |
| 2026-08-04 15:03:41 | Hanwella (Kelani Ganga) | 5.83 | 🟢 Normal | -0.140 |  |
| 2026-08-04 15:03:39 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:03:34 | Nawalapitiya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-08-04 15:03:30 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-04 15:02:58 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 15:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.37 | 🟡 Alert | -0.010 |  |
| 2026-08-04 15:02:38 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:02:38 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-08-04 15:02:27 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.024 |  |
| 2026-08-04 15:02:21 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:02:15 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 15:02:09 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.048 |  |
| 2026-08-04 15:02:08 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:02:08 | Peradeniya (Mahaweli Ganga) | 4.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-04 15:01:59 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-04 15:01:58 | Ellagawa (Kalu Ganga) | 8.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 15:01:42 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-04 15:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:01:33 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:01:26 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-04 15:01:12 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:00:57 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:00:29 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:00:16 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 15:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.37 | 🟡 Alert | -0.010 |  |
| 2026-08-04 15:04:19 | Rathnapura (Kalu Ganga) | 6.43 | 🟡 Alert | -0.106 |  |
| 2026-08-04 15:04:38 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-08-04 15:04:25 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-08-04 15:01:59 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-04 15:01:42 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-04 15:04:18 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-04 15:01:58 | Ellagawa (Kalu Ganga) | 8.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 15:02:08 | Peradeniya (Mahaweli Ganga) | 4.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-04 15:01:26 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-04 15:02:58 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 15:02:15 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 15:00:29 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:00:16 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:02:08 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:13:48 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:03:39 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:05:19 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:02:38 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:01:12 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:01:33 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:11:10 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:06:27 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-04 15:07:39 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-04 15:03:34 | Nawalapitiya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-08-04 15:03:30 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-04 15:06:15 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-08-04 15:17:34 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.017 |  |
| 2026-08-04 15:04:42 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-08-04 15:02:38 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-08-04 15:02:27 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.024 |  |
| 2026-08-04 15:11:20 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.030 |  |
| 2026-08-04 15:03:56 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-08-04 15:02:09 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.048 |  |
| 2026-08-04 15:03:49 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.050 |  |
| 2026-08-04 15:03:53 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-08-04 15:03:41 | Hanwella (Kelani Ganga) | 5.83 | 🟢 Normal | -0.140 |  |
| 2026-08-04 15:07:55 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)