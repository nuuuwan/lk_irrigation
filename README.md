# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_14:47:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,530 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 14:47:38 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:18:22 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:15:48 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.008 |  |
| 2026-02-08 14:14:40 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-02-08 14:14:03 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.025 |  |
| 2026-02-08 14:13:44 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:10:30 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-08 14:09:56 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:07:02 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-08 14:06:40 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-02-08 14:05:13 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 14:04:43 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:04:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:04:26 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.060 |  |
| 2026-02-08 14:03:39 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-08 14:03:35 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-08 14:03:31 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-08 14:03:23 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:03:06 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.050 |  |
| 2026-02-08 14:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:47 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:32 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-08 14:02:15 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:14 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:01 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:01:50 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:01:36 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-08 14:01:30 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:01:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.013 |  |
| 2026-02-08 14:01:21 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:01:21 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:01:12 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.010 |  |
| 2026-02-08 14:01:01 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 14:00:39 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 14:00:08 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | -0.102 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 14:10:30 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-08 14:01:36 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-08 14:07:02 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-08 14:05:13 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 14:00:39 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 14:01:01 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 14:01:30 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:01:50 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:03:23 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:18:22 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:13:44 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-08 13:04:18 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:01 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:47:38 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:01:21 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:14 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:01:21 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:04:43 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:04:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:15 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:09:56 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:47 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:04:26 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:15:48 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.008 |  |
| 2026-02-08 14:14:40 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-02-08 14:02:32 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-08 14:03:35 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-08 13:01:43 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-08 14:01:12 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.010 |  |
| 2026-02-08 14:03:39 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-08 14:01:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.013 |  |
| 2026-02-08 14:06:40 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-02-08 14:03:31 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-08 14:14:03 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.025 |  |
| 2026-02-08 14:03:06 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.050 |  |
| 2026-02-08 14:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.060 |  |
| 2026-02-08 14:00:08 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | -0.102 |  |
| 2026-02-08 12:06:56 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)