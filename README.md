# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--28_16:10:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,068 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 16:10:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:53 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:52 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:46 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:06 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:00 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:44 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:38 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-01-28 16:05:20 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-01-28 16:05:15 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:13 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-28 16:05:00 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:04:39 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:04:34 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-28 16:04:23 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.095 |  |
| 2026-01-28 16:03:33 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-01-28 16:03:13 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:03:09 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-28 16:02:59 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:02:49 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:02:27 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-28 16:02:23 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:02:12 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:59 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-28 16:01:26 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:22 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-28 16:01:17 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:14 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:06 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.172 |  |
| 2026-01-28 16:00:36 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:00:32 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-28 16:00:06 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 15:03:21 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-28 16:04:34 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-28 16:03:09 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-28 16:00:32 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-28 16:01:22 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-28 16:00:06 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-28 16:02:27 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-28 16:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-28 16:02:59 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:00:36 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:00 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 15:02:09 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:13 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:02:12 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-28 15:08:12 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:06 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:17 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:10:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:52 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:14 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:46 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:02:49 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:03:13 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:00 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:06:53 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:15 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:01:26 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:44 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:04:39 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:02:23 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-28 15:08:38 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-28 16:05:20 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-01-28 16:01:59 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-28 16:03:33 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-01-28 16:05:38 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-01-28 16:04:23 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.095 |  |
| 2026-01-28 16:01:06 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)