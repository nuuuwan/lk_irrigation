# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_07:22:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,025 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 07:22:42 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.022 |  |
| 2026-03-13 07:17:24 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-13 07:11:44 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-03-13 07:09:17 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:08:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:08:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 07:07:32 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-03-13 07:07:15 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:07:05 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:07:03 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.018 |  |
| 2026-03-13 07:06:54 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:06:10 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-03-13 07:05:50 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:05:49 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-13 07:05:30 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 07:05:13 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.134 |  |
| 2026-03-13 07:05:05 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-03-13 07:04:38 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:04:03 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:03:51 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-13 07:03:50 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-13 07:03:43 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 07:03:29 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:03:25 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 07:03:22 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.102 |  |
| 2026-03-13 07:02:57 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-13 07:02:57 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 07:02:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.133 |  |
| 2026-03-13 07:02:27 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:02:26 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-13 07:02:11 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 07:02:07 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:01:48 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-13 07:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:01:40 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-03-13 07:00:51 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:00:11 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:00:09 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 07:06:10 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-03-13 07:11:44 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-03-13 07:02:57 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-13 07:02:26 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-13 07:01:48 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-13 07:17:24 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-13 07:05:49 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-13 07:03:50 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-13 07:03:51 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-13 07:03:43 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 07:05:30 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 07:02:57 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 07:02:11 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 07:03:25 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 07:08:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 07:00:51 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:07:05 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:02:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:33:29 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:08:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:04:03 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:04:38 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:00:11 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:03:29 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:06:54 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:05:50 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:02:07 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:09:17 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:07:15 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 07:07:32 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-03-13 07:07:03 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.018 |  |
| 2026-03-13 07:05:05 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-03-13 07:01:40 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-03-13 07:22:42 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.022 |  |
| 2026-03-13 07:00:09 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.090 |  |
| 2026-03-13 07:03:22 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.102 |  |
| 2026-03-13 07:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.133 |  |
| 2026-03-13 07:05:13 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)