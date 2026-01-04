# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_07:39:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,193 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 07:39:36 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.066 |  |
| 2026-01-04 07:30:32 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-04 07:22:09 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:14:47 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-01-04 07:14:36 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.026 |  |
| 2026-01-04 07:12:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.034 |  |
| 2026-01-04 07:12:24 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-04 07:10:50 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-04 07:10:01 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-01-04 07:09:26 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-01-04 07:09:01 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.098 |  |
| 2026-01-04 07:08:51 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:07:18 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:07:03 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.170 |  |
| 2026-01-04 07:06:57 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-04 07:06:35 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:05:53 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-01-04 07:04:59 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-01-04 07:04:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 07:04:06 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:04:05 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:03:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.153 |  |
| 2026-01-04 07:03:50 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:03:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 07:03:19 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.013 |  |
| 2026-01-04 07:02:55 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:02:50 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.004 |  |
| 2026-01-04 07:02:32 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:02:27 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.020 |  |
| 2026-01-04 07:02:22 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-04 07:02:19 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-04 07:02:14 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-01-04 07:02:09 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-04 07:01:51 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-04 07:01:43 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:01:40 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.035 |  |
| 2026-01-04 07:01:30 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:00:43 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 07:04:59 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-01-04 07:06:57 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-04 07:12:24 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-04 07:30:32 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-04 07:02:09 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-04 07:04:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 07:02:19 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-04 07:02:22 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-04 07:03:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 07:00:43 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:08:51 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:01:30 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:02:55 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:04:05 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:02:32 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:05:35 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:06:35 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:07:18 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:01:43 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:03:50 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:22:09 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:04:06 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-04 07:02:50 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.004 |  |
| 2026-01-04 07:14:47 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-01-04 07:10:01 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-01-04 07:10:50 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-04 07:05:53 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-01-04 07:01:51 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-04 07:03:19 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.013 |  |
| 2026-01-04 07:02:27 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.020 |  |
| 2026-01-04 07:09:26 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-01-04 07:14:36 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.026 |  |
| 2026-01-04 07:02:14 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-01-04 07:12:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.034 |  |
| 2026-01-04 07:01:40 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.035 |  |
| 2026-01-04 07:39:36 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.066 |  |
| 2026-01-04 07:09:01 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.098 |  |
| 2026-01-04 07:03:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.153 |  |
| 2026-01-04 07:07:03 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)