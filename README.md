# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_18:10:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,774 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 18:10:29 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:08:14 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 18:07:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:07:01 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.069 |  |
| 2026-09-15 18:06:51 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-09-15 18:06:23 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.019 |  |
| 2026-09-15 18:05:37 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:05:13 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 18:04:59 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 18:04:56 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 18:04:37 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-09-15 18:04:36 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.127 |  |
| 2026-09-15 18:04:29 | Baddegama (Gin Ganga) | 3.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 18:04:17 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:04:15 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-15 18:04:00 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-09-15 18:03:56 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.071 |  |
| 2026-09-15 18:03:26 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:03:00 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 18:02:59 | Panadugama (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.089 |  |
| 2026-09-15 18:02:54 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-09-15 18:02:45 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.102 |  |
| 2026-09-15 18:02:40 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.039 |  |
| 2026-09-15 18:02:39 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 18:02:33 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-15 18:02:31 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-15 18:02:28 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-15 18:02:22 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.814 | 🔺 Rising |
| 2026-09-15 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | -0.010 |  |
| 2026-09-15 18:02:02 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.098 |  |
| 2026-09-15 18:01:58 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.073 |  |
| 2026-09-15 18:01:49 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:01:37 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.072 |  |
| 2026-09-15 18:01:26 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-15 18:01:19 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 18:00:52 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:00:28 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 18:02:02 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.098 |  |
| 2026-09-15 18:02:22 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.814 | 🔺 Rising |
| 2026-09-15 18:02:28 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-15 18:01:26 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-15 18:02:33 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-15 18:05:13 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 18:04:29 | Baddegama (Gin Ganga) | 3.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 18:04:56 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 18:01:19 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 18:02:39 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 18:04:59 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 18:03:00 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 18:08:14 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 18:04:17 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:01:49 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:00:52 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:07:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:03:26 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:02:31 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:00:28 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:05:37 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:10:29 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:04:15 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-15 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | -0.010 |  |
| 2026-09-15 18:06:23 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.019 |  |
| 2026-09-15 18:06:51 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-09-15 18:04:00 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-09-15 18:02:54 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-09-15 18:04:37 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-09-15 18:02:40 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.039 |  |
| 2026-09-15 18:07:01 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.069 |  |
| 2026-09-15 18:03:56 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.071 |  |
| 2026-09-15 18:01:37 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.072 |  |
| 2026-09-15 18:01:58 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.073 |  |
| 2026-09-15 18:02:59 | Panadugama (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.089 |  |
| 2026-09-15 18:02:45 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.102 |  |
| 2026-09-15 18:04:36 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)