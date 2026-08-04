# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_17:12:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,869 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kithulgala — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 17:12:26 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.017 |  |
| 2026-08-04 17:10:34 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.009 |  |
| 2026-08-04 17:10:10 | Rathnapura (Kalu Ganga) | 6.22 | 🟡 Alert | -0.105 |  |
| 2026-08-04 17:09:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:08:38 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | -0.096 |  |
| 2026-08-04 17:06:56 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.028 |  |
| 2026-08-04 17:06:55 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-08-04 17:06:32 | Peradeniya (Mahaweli Ganga) | 4.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-04 17:05:58 | Kithulgala (Kelani Ganga) | 3.06 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-08-04 17:05:54 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:05:53 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:05:39 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:05:34 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-04 17:05:22 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:05:12 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | -0.038 |  |
| 2026-08-04 17:04:43 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | -0.029 |  |
| 2026-08-04 17:03:21 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:03:09 | Hanwella (Kelani Ganga) | 5.49 | 🟢 Normal | -0.161 |  |
| 2026-08-04 17:02:51 | Deraniyagala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.510 | 🔺 Rising |
| 2026-08-04 17:02:46 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:02:42 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-04 17:02:38 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-04 17:02:32 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.023 |  |
| 2026-08-04 17:02:29 | Nawalapitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.030 |  |
| 2026-08-04 17:02:10 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-08-04 17:02:07 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 17:01:49 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.078 |  |
| 2026-08-04 17:01:36 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:01:33 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-08-04 17:01:20 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.103 |  |
| 2026-08-04 17:01:18 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-04 17:01:17 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 17:01:12 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:01:03 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:00:50 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:00:49 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:00:39 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:00:21 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.064 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 17:05:58 | Kithulgala (Kelani Ganga) | 3.06 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-08-04 17:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | -0.029 |  |
| 2026-08-04 17:10:10 | Rathnapura (Kalu Ganga) | 6.22 | 🟡 Alert | -0.105 |  |
| 2026-08-04 17:02:51 | Deraniyagala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.510 | 🔺 Rising |
| 2026-08-04 17:02:38 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-04 17:05:34 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-04 17:06:32 | Peradeniya (Mahaweli Ganga) | 4.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-04 17:01:17 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 17:02:07 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 17:02:46 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:00:49 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:01:03 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:03:21 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:01:36 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:05:54 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:01:12 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:05:22 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:05:53 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:09:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:00:50 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:05:39 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:00:39 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 17:10:34 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.009 |  |
| 2026-08-04 17:01:18 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-04 17:02:42 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-04 17:06:55 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-08-04 17:12:26 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.017 |  |
| 2026-08-04 17:02:10 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-08-04 17:01:33 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-08-04 17:02:32 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.023 |  |
| 2026-08-04 17:06:56 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.028 |  |
| 2026-08-04 17:02:29 | Nawalapitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.030 |  |
| 2026-08-04 17:05:12 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | -0.038 |  |
| 2026-08-04 17:00:21 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.064 |  |
| 2026-08-04 17:01:49 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.078 |  |
| 2026-08-04 17:08:38 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | -0.096 |  |
| 2026-08-04 17:01:20 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.103 |  |
| 2026-08-04 17:03:09 | Hanwella (Kelani Ganga) | 5.49 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)