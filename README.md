# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_14:28:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,682 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 14:28:24 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | -0.036 |  |
| 2026-11-04 14:14:28 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:14:21 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.044 |  |
| 2026-11-04 14:09:45 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.137 |  |
| 2026-11-04 14:09:26 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-11-04 14:08:58 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:07:30 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.018 |  |
| 2026-11-04 14:07:27 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.029 |  |
| 2026-11-04 14:06:37 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:05:56 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:05:32 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-11-04 14:05:05 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:05:02 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:04:57 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 14:04:49 | Badalgama (Maha Oya) | 3.84 | 🟢 Normal | -0.080 |  |
| 2026-11-04 14:04:47 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-11-04 14:04:34 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-11-04 14:04:20 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-11-04 14:04:17 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:04:10 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-11-04 14:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.06 | 🟡 Alert | -0.020 |  |
| 2026-11-04 14:03:06 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-11-04 14:02:59 | Moragaswewa (Deduru Oya) | 4.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 14:02:57 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:02:55 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:02:50 | Hanwella (Kelani Ganga) | 2.71 | 🟢 Normal | -0.071 |  |
| 2026-11-04 14:02:49 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.079 |  |
| 2026-11-04 14:02:35 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:02:07 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.119 |  |
| 2026-11-04 14:01:52 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:01:48 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.122 |  |
| 2026-11-04 14:01:45 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:01:40 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | -0.032 |  |
| 2026-11-04 14:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:01:06 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-04 14:00:56 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 14:00:43 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:00:24 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 14:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.06 | 🟡 Alert | -0.020 |  |
| 2026-11-04 14:04:20 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-11-04 14:02:59 | Moragaswewa (Deduru Oya) | 4.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 14:00:56 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 14:04:57 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 14:08:58 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:01:06 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:04:17 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:14:28 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:05:05 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:00:43 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:02:57 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:06:37 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:05:56 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:05:02 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:02:55 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:01:52 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:02:35 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:03:06 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-11-04 14:07:30 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.018 |  |
| 2026-11-04 14:09:26 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-11-04 14:04:10 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-11-04 14:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-04 14:07:27 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.029 |  |
| 2026-11-04 14:04:34 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-11-04 14:04:47 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-11-04 14:01:40 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | -0.032 |  |
| 2026-11-04 14:28:24 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | -0.036 |  |
| 2026-11-04 14:05:32 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-11-04 14:14:21 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.044 |  |
| 2026-11-04 14:00:24 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.050 |  |
| 2026-11-04 14:02:50 | Hanwella (Kelani Ganga) | 2.71 | 🟢 Normal | -0.071 |  |
| 2026-11-04 14:02:49 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.079 |  |
| 2026-11-04 14:04:49 | Badalgama (Maha Oya) | 3.84 | 🟢 Normal | -0.080 |  |
| 2026-11-04 14:02:07 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.119 |  |
| 2026-11-04 14:01:48 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.122 |  |
| 2026-11-04 14:09:45 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)