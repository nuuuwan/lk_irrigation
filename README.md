# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_20:34:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,909 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 20:34:16 | Moragaswewa (Deduru Oya) | 4.24 | 🟢 Normal | -0.022 |  |
| 2026-11-04 20:11:21 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | -0.038 |  |
| 2026-11-04 20:10:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-11-04 20:10:14 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.179 |  |
| 2026-11-04 20:08:05 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.012 |  |
| 2026-11-04 20:07:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-04 20:07:24 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 20:06:26 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.075 |  |
| 2026-11-04 20:06:03 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-04 20:05:58 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.009 |  |
| 2026-11-04 20:05:26 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | 0.424 | 🔺 Rising |
| 2026-11-04 20:04:35 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.021 |  |
| 2026-11-04 20:04:08 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-04 20:04:05 | Ellagawa (Kalu Ganga) | 6.63 | 🟢 Normal | -0.073 |  |
| 2026-11-04 20:03:42 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-04 20:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-04 20:03:34 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.041 |  |
| 2026-11-04 20:03:34 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-11-04 20:03:16 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-11-04 20:03:08 | Kuda Oya (Kirindi Oya) | 3.28 | 🟢 Normal | 0.760 | 🔺 Rising |
| 2026-11-04 20:03:02 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 20:02:35 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-11-04 20:02:33 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 20:02:27 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.021 |  |
| 2026-11-04 20:02:20 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 20:02:16 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-11-04 20:02:09 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 20:10:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-11-04 20:03:08 | Kuda Oya (Kirindi Oya) | 3.28 | 🟢 Normal | 0.760 | 🔺 Rising |
| 2026-11-04 20:05:26 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | 0.424 | 🔺 Rising |
| 2026-11-04 20:02:01 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-11-04 20:04:08 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-04 20:00:28 | Wellawaya (Kirindi Oya) | 2.43 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-04 20:07:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-04 19:15:23 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-04 20:06:03 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-04 20:07:24 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 20:02:20 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 20:01:23 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-04 20:01:25 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 20:02:09 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-04 20:03:02 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 20:01:51 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-04 20:02:33 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 20:01:43 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 20:05:58 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.009 |  |
| 2026-11-04 20:02:35 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-11-04 20:02:16 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-11-04 20:03:34 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-11-04 20:08:05 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.012 |  |
| 2026-11-04 20:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-04 20:02:27 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.021 |  |
| 2026-11-04 20:04:35 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.021 |  |
| 2026-11-04 20:01:53 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-11-04 20:34:16 | Moragaswewa (Deduru Oya) | 4.24 | 🟢 Normal | -0.022 |  |
| 2026-11-04 20:03:42 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-04 20:03:16 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 20:11:21 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | -0.038 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-04 20:03:34 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.041 |  |
| 2026-11-04 20:00:56 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.057 |  |
| 2026-11-04 20:04:05 | Ellagawa (Kalu Ganga) | 6.63 | 🟢 Normal | -0.073 |  |
| 2026-11-04 20:06:26 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.075 |  |
| 2026-11-04 20:10:14 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)