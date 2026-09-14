# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_00:08:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,086 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 00:08:22 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-15 00:07:57 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.028 |  |
| 2026-09-15 00:07:52 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.029 |  |
| 2026-09-15 00:07:49 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-09-15 00:07:04 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-15 00:07:03 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-15 00:06:36 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.073 |  |
| 2026-09-15 00:05:59 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 00:05:38 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-15 00:05:23 | Thawalama (Gin Ganga) | 3.37 | 🟢 Normal | 0.856 | 🔺 Rising |
| 2026-09-15 00:05:09 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-15 00:05:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-15 00:04:45 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:04:22 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:57 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:45 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:44 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | 0.385 | 🔺 Rising |
| 2026-09-15 00:03:43 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-15 00:03:42 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:40 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 00:03:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:08 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-15 00:02:48 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-15 00:02:11 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:02:01 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:01:41 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.060 |  |
| 2026-09-15 00:00:10 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:50:10 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.073 |  |
| 2026-09-14 23:42:04 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:42:03 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:40:18 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.347 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 00:03:44 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | 0.385 | 🔺 Rising |
| 2026-09-15 00:05:23 | Thawalama (Gin Ganga) | 3.37 | 🟢 Normal | 0.856 | 🔺 Rising |
| 2026-09-15 00:07:49 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-09-14 23:09:14 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-09-15 00:05:09 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-15 00:05:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-15 00:08:22 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-15 00:07:03 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-15 00:02:48 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-14 23:07:29 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-14 23:09:53 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-15 00:07:04 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-15 00:03:08 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-15 00:03:40 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 00:05:59 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 00:03:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:02:01 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:01:41 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:07:08 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:45 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:04:45 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:00:10 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:02:11 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:57 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:04:45 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:42 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:03:37 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:43 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-15 00:05:38 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-14 23:10:20 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-09-15 00:07:57 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.028 |  |
| 2026-09-15 00:07:52 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.029 |  |
| 2026-09-14 23:07:44 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-09-15 00:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.060 |  |
| 2026-09-15 00:06:36 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.073 |  |
| 2026-09-14 23:40:18 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.347 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)