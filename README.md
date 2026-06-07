# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_15:20:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 15:20:43 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:14:32 | Rathnapura (Kalu Ganga) | 4.39 | 🟢 Normal | -0.026 |  |
| 2026-06-07 15:09:10 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.018 |  |
| 2026-06-07 15:09:06 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-07 15:07:17 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.075 |  |
| 2026-06-07 15:06:01 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-06-07 15:06:00 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 15:05:19 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-07 15:05:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-06-07 15:04:49 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:04:39 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:04:35 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 15:04:23 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-07 15:04:02 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.049 |  |
| 2026-06-07 15:03:54 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.032 |  |
| 2026-06-07 15:03:42 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:03:23 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-07 15:03:14 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.050 |  |
| 2026-06-07 15:03:12 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:03:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:03:02 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 15:02:52 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:02:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:02:41 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-06-07 15:02:39 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:02:28 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.012 |  |
| 2026-06-07 15:02:27 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 15:02:24 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-06-07 15:02:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:01:52 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 15:01:52 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:01:48 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:01:33 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:01:24 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.224 |  |
| 2026-06-07 15:01:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.72 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-07 15:00:41 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.021 |  |
| 2026-06-07 15:00:21 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:00:17 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 14:59:52 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 15:05:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-06-07 15:03:23 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-07 15:04:23 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-07 15:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.72 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-07 15:00:17 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 15:01:52 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 15:02:27 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 15:05:19 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-07 15:06:00 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 15:03:02 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 15:04:35 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 15:01:48 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:02:39 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:20:43 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:01:52 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:01:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:02:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:02:52 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:04:39 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:03:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:03:42 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:04:49 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:03:12 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:00:21 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:01:33 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 15:06:01 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-06-07 14:59:52 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-07 15:09:06 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-07 15:02:41 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-06-07 15:02:28 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.012 |  |
| 2026-06-07 15:09:10 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.018 |  |
| 2026-06-07 15:00:41 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.021 |  |
| 2026-06-07 15:14:32 | Rathnapura (Kalu Ganga) | 4.39 | 🟢 Normal | -0.026 |  |
| 2026-06-07 15:03:54 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.032 |  |
| 2026-06-07 15:04:02 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.049 |  |
| 2026-06-07 15:03:14 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.050 |  |
| 2026-06-07 15:02:24 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-06-07 15:07:17 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.075 |  |
| 2026-06-07 15:01:24 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)