# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_16:30:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 16:30:48 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -1.500 |  |
| 2026-01-31 16:30:24 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -1.500 |  |
| 2026-01-31 16:27:54 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-31 16:27:37 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:22:35 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:10:08 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-01-31 16:09:10 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-01-31 16:08:36 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 16:08:29 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 16:08:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.037 |  |
| 2026-01-31 16:08:10 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.045 |  |
| 2026-01-31 16:08:04 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:07:56 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:07:19 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:05:59 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:04:57 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -1.500 |  |
| 2026-01-31 16:04:50 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:04:30 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-01-31 16:04:13 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-31 16:04:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 16:03:54 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-31 16:03:41 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:03:35 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:03:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2026-01-31 16:03:12 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:03:08 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-31 16:02:57 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:02:38 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-01-31 16:02:30 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 16:02:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 16:02:16 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:02:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 16:01:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:01:44 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:01:11 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-31 16:01:10 | Manampitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-31 16:01:07 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:00:14 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-31 15:59:47 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 16:00:14 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-31 16:08:36 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 16:01:10 | Manampitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-31 16:03:54 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-31 16:02:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 16:04:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 16:02:30 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 16:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 16:08:29 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 16:27:54 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-31 16:08:04 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:02:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:07:56 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:02:16 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:03:41 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:27:37 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:02:57 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:03:12 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:01:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:05:59 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:07:19 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:01:44 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:03:35 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:04:50 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:09:10 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:59:47 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:01:07 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:22:35 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-01-31 16:10:08 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-01-31 16:04:13 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-31 16:01:11 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-31 16:02:38 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-01-31 16:04:30 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-01-31 16:03:08 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-31 16:08:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.037 |  |
| 2026-01-31 16:08:10 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.045 |  |
| 2026-01-31 16:03:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2026-01-31 16:30:48 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)