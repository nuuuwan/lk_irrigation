# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_13:24:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,604 measurements** from **39** stations.
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
| 2026-08-05 13:24:15 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-08-05 13:15:20 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.080 |  |
| 2026-08-05 13:11:22 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:11:16 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-05 13:09:20 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.014 |  |
| 2026-08-05 13:07:25 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.027 |  |
| 2026-08-05 13:07:21 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:07:16 | Glencourse (Kelani Ganga) | 12.38 | 🟢 Normal | -0.028 |  |
| 2026-08-05 13:06:17 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:05:40 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-08-05 13:05:10 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-08-05 13:04:57 | Peradeniya (Mahaweli Ganga) | 5.98 | 🟡 Alert | 0.310 | 🔺 Rising |
| 2026-08-05 13:04:51 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:04:49 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.053 |  |
| 2026-08-05 13:04:49 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:04:48 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.046 |  |
| 2026-08-05 13:04:32 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:04:00 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-08-05 13:03:59 | Hanwella (Kelani Ganga) | 4.37 | 🟢 Normal | -0.050 |  |
| 2026-08-05 13:03:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:03:44 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.163 |  |
| 2026-08-05 13:03:29 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-05 13:03:29 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:03:25 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.059 |  |
| 2026-08-05 13:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.15 | 🟢 Normal | -0.059 |  |
| 2026-08-05 13:03:13 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:03:02 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-08-05 13:02:55 | Kithulgala (Kelani Ganga) | 2.66 | 🟢 Normal | -0.049 |  |
| 2026-08-05 13:02:40 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-08-05 13:02:25 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.041 |  |
| 2026-08-05 13:02:17 | Ellagawa (Kalu Ganga) | 8.86 | 🟢 Normal | -0.021 |  |
| 2026-08-05 13:01:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.094 |  |
| 2026-08-05 13:01:17 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:01:17 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:01:15 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:00:48 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-05 13:00:43 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.030 |  |
| 2026-08-05 13:00:36 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:00:28 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:00:16 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 13:04:57 | Peradeniya (Mahaweli Ganga) | 5.98 | 🟡 Alert | 0.310 | 🔺 Rising |
| 2026-08-05 13:11:16 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-05 13:00:48 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-05 13:00:28 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:03:29 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:06:17 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:03:13 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:07:21 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:03:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:01:17 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:04:32 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:11:22 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:04:51 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:01:17 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:01:15 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:00:36 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:04:49 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 13:05:40 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-08-05 13:03:29 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-05 13:03:02 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-08-05 13:09:20 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.014 |  |
| 2026-08-05 13:04:00 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-08-05 13:02:40 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-08-05 13:05:10 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-08-05 13:02:17 | Ellagawa (Kalu Ganga) | 8.86 | 🟢 Normal | -0.021 |  |
| 2026-08-05 13:07:25 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.027 |  |
| 2026-08-05 13:07:16 | Glencourse (Kelani Ganga) | 12.38 | 🟢 Normal | -0.028 |  |
| 2026-08-05 13:00:43 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.030 |  |
| 2026-08-05 13:24:15 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-08-05 13:02:25 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.041 |  |
| 2026-08-05 13:04:48 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.046 |  |
| 2026-08-05 13:02:55 | Kithulgala (Kelani Ganga) | 2.66 | 🟢 Normal | -0.049 |  |
| 2026-08-05 13:03:59 | Hanwella (Kelani Ganga) | 4.37 | 🟢 Normal | -0.050 |  |
| 2026-08-05 13:04:49 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.053 |  |
| 2026-08-05 13:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.15 | 🟢 Normal | -0.059 |  |
| 2026-08-05 13:03:25 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.059 |  |
| 2026-08-05 13:15:20 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.080 |  |
| 2026-08-05 13:01:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.094 |  |
| 2026-08-05 13:03:44 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)