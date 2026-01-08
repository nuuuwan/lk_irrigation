# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_01:04:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,434 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 01:04:02 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:03:53 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:03:34 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-01-09 01:03:19 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-01-09 01:03:15 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:03:06 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:02:53 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-09 01:02:46 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 01:02:39 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:02:27 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:02:26 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:02:00 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:01:31 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.049 |  |
| 2026-01-09 01:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-09 01:01:16 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-09 01:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:00:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:00:47 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:36:26 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:31:15 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:16:57 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.102 |  |
| 2026-01-09 00:15:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-09 00:14:19 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:12:35 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.049 |  |
| 2026-01-09 00:12:03 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.783 | 🔺 Rising |
| 2026-01-09 00:11:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-09 00:11:01 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.049 |  |
| 2026-01-09 00:10:39 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.049 |  |
| 2026-01-09 00:09:37 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:08:56 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-01-09 00:08:22 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-01-09 00:07:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 00:12:03 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.783 | 🔺 Rising |
| 2026-01-09 01:03:34 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-01-09 00:01:31 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-09 00:15:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-09 00:11:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-09 01:01:16 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 01:02:46 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 01:00:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:02:27 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:01:27 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:01:53 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:30 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:02:39 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:54 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:02:38 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:03:15 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:02:00 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:04:02 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:03:53 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:00:47 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:07:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:31:15 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:03:06 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 01:02:26 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:08:22 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-01-09 00:08:56 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-01-09 01:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 00:04:27 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-01-09 01:02:53 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-09 01:03:19 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-01-09 00:01:51 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.026 |  |
| 2026-01-09 00:02:41 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.026 |  |
| 2026-01-09 00:01:19 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-09 01:01:31 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.049 |  |
| 2026-01-09 00:16:57 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)