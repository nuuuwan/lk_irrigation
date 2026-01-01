# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_16:45:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,846 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 16:45:22 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-01-01 16:30:49 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:17:57 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:15:42 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.008 |  |
| 2026-01-01 16:08:54 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:08:25 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:07:55 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-01-01 16:06:21 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:05:41 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:05:40 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-01-01 16:05:02 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:04:47 | Horowpothana (Yan Oya) | 3.43 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-01 16:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-01-01 16:04:02 | Siyambalanduwa (Heda Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-01-01 16:03:54 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:03:34 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:03:28 | Thanthirimale (Malwathu Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:03:22 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-01 16:03:16 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-01 16:03:02 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:02:56 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:02:50 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-01 16:02:46 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:02:32 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-01 16:02:27 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.030 |  |
| 2026-01-01 16:02:21 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:02:17 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.060 |  |
| 2026-01-01 16:01:48 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:01:47 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.120 |  |
| 2026-01-01 16:01:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.034 |  |
| 2026-01-01 16:01:35 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:01:23 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:01:22 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.529 | 🔺 Rising |
| 2026-01-01 16:01:02 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:00:59 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.040 |  |
| 2026-01-01 16:00:24 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:00:14 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 16:01:22 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.529 | 🔺 Rising |
| 2026-01-01 16:07:55 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-01-01 16:03:16 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-01 16:04:47 | Horowpothana (Yan Oya) | 3.43 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-01 16:02:50 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-01 16:02:32 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-01 16:01:02 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:03:34 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:30:49 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:17:57 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:06:21 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:01:48 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:01:35 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:03:02 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:03:54 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:05:02 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:05:41 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:49 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:08:54 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-01 16:15:42 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.008 |  |
| 2026-01-01 16:03:28 | Thanthirimale (Malwathu Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:08:25 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:02:46 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:00:24 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:01:23 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:00:14 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:02:56 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:02:21 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-01 16:04:02 | Siyambalanduwa (Heda Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-01-01 16:05:40 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-01-01 16:45:22 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-01-01 16:03:22 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-01 16:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-01-01 16:02:27 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.030 |  |
| 2026-01-01 16:01:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.034 |  |
| 2026-01-01 16:00:59 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.040 |  |
| 2026-01-01 16:02:17 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.060 |  |
| 2026-01-01 16:01:47 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)