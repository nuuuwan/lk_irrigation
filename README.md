# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_14:23:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 14:23:03 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-27 14:10:33 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-27 14:08:40 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-03-27 14:08:30 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:08:20 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-03-27 14:08:17 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:08:05 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:07:06 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:06:42 | Rathnapura (Kalu Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-03-27 14:06:26 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.098 |  |
| 2026-03-27 14:06:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:06:18 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:05:43 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:05:12 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-27 14:05:04 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:04:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-27 14:04:17 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 14:04:16 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:04:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:03:38 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:03:34 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-27 14:03:26 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 14:03:20 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:03:11 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:02:43 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:02:41 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-27 14:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-03-27 14:02:29 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:02:15 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:01:58 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-27 14:01:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:01:34 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:01:12 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.201 |  |
| 2026-03-27 14:01:11 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-03-27 14:01:08 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:00:54 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:00:50 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.041 |  |
| 2026-03-27 14:00:28 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 14:10:33 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-27 14:04:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-27 14:23:03 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-27 14:05:12 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-27 14:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-27 14:03:26 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 14:04:17 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 14:02:41 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:00:28 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:04:16 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:01:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:06:18 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:02:29 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:00:54 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:07:06 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:03:20 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:02:43 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:01:34 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:08:05 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:05:04 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:03:38 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:06:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:08:17 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:04:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:03:11 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:08:30 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:05:43 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:01:08 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:02:15 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 14:08:40 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-03-27 14:01:11 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-03-27 14:08:20 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-03-27 14:03:34 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-27 14:01:58 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-27 14:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-03-27 14:06:42 | Rathnapura (Kalu Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-03-27 14:00:50 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.041 |  |
| 2026-03-27 14:06:26 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.098 |  |
| 2026-03-27 14:01:12 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)