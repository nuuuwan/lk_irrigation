# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_15:08:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 15:08:42 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.038 |  |
| 2026-03-13 15:08:07 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.019 |  |
| 2026-03-13 15:07:26 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-03-13 15:06:09 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-03-13 15:06:01 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-13 15:05:53 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:05:45 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:05:27 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-13 15:05:08 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-03-13 15:04:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-13 15:04:41 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-13 15:04:31 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:04:30 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:04:17 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 15:04:02 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.041 |  |
| 2026-03-13 15:03:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:03:22 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.068 |  |
| 2026-03-13 15:03:06 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.054 |  |
| 2026-03-13 15:03:01 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-13 15:02:42 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:02:42 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.051 |  |
| 2026-03-13 15:02:19 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-03-13 15:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-03-13 15:02:11 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:54 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:35 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-13 15:01:17 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:17 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:13 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-13 15:01:08 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:06 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-13 15:01:05 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-13 15:01:03 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:01 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:00:54 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-13 15:00:47 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.034 |  |
| 2026-03-13 15:00:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:26:59 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 15:06:09 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-03-13 15:00:54 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-13 15:04:41 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-13 15:04:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-13 15:01:35 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-13 15:05:27 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-13 15:01:13 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-13 15:01:06 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-13 15:04:17 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 15:06:01 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-13 15:04:31 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:02:11 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:17 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:54 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:10:09 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:03:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:00:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:17 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:01 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:02:42 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:05:53 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:04:30 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:03 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:01:08 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 15:05:45 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 14:05:14 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-03-13 15:01:05 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-13 15:03:01 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-13 15:08:07 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.019 |  |
| 2026-03-13 15:07:26 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-03-13 15:05:08 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-03-13 15:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-03-13 15:00:47 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.034 |  |
| 2026-03-13 15:08:42 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.038 |  |
| 2026-03-13 15:02:19 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-03-13 15:04:02 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.041 |  |
| 2026-03-13 15:02:42 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.051 |  |
| 2026-03-13 15:03:06 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.054 |  |
| 2026-03-13 15:03:22 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)