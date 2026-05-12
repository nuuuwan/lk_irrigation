# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_21:08:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,114 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 21:08:24 | Rathnapura (Kalu Ganga) | 3.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 21:08:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-12 21:07:40 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.264 |  |
| 2026-05-12 21:06:21 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-12 21:05:22 | Katharagama (Menik Ganga) | 1.87 | 🟢 Normal | -0.087 |  |
| 2026-05-12 21:05:18 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-12 21:05:06 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.085 |  |
| 2026-05-12 21:03:52 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 21:03:47 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:03:46 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 21:03:27 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:03:25 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.019 |  |
| 2026-05-12 21:03:17 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:03:17 | Thawalama (Gin Ganga) | 2.81 | 🟢 Normal | -0.316 |  |
| 2026-05-12 21:03:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 21:02:57 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-12 21:02:41 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 21:02:41 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.041 |  |
| 2026-05-12 21:02:26 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:02:18 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:02:11 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-05-12 21:02:08 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:02:08 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | -0.176 |  |
| 2026-05-12 21:02:01 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:01:58 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:01:56 | Siyambalanduwa (Heda Oya) | 1.60 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2026-05-12 21:01:37 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:01:25 | Thaldena (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.110 |  |
| 2026-05-12 21:01:22 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:01:04 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 21:00:53 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.090 |  |
| 2026-05-12 21:00:26 | Nakkala (Kumbukkan Oya) | 3.90 | 🟢 Normal | -0.200 |  |
| 2026-05-12 20:20:39 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 20:17:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.119 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 21:01:56 | Siyambalanduwa (Heda Oya) | 1.60 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2026-05-12 21:02:57 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-12 21:08:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-12 20:11:51 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-12 21:05:18 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-12 18:05:40 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 21:03:46 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 21:03:52 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 21:01:04 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 21:03:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 21:06:21 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-12 21:02:41 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 21:08:24 | Rathnapura (Kalu Ganga) | 3.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 21:01:37 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:02:26 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:03:17 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:01:58 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:08:00 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:03:47 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-12 21:02:18 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:02:01 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:03:27 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:02:08 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:01:22 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-12 21:02:11 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-05-12 21:03:25 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.019 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-12 21:02:41 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.041 |  |
| 2026-05-12 21:05:06 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.085 |  |
| 2026-05-12 21:05:22 | Katharagama (Menik Ganga) | 1.87 | 🟢 Normal | -0.087 |  |
| 2026-05-12 21:00:53 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.090 |  |
| 2026-05-12 21:01:25 | Thaldena (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.110 |  |
| 2026-05-12 21:02:08 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | -0.176 |  |
| 2026-05-12 21:00:26 | Nakkala (Kumbukkan Oya) | 3.90 | 🟢 Normal | -0.200 |  |
| 2026-05-12 21:07:40 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.264 |  |
| 2026-05-12 21:03:17 | Thawalama (Gin Ganga) | 2.81 | 🟢 Normal | -0.316 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)