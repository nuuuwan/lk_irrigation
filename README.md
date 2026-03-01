# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_15:09:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,357 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 15:09:32 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-03-01 15:08:29 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:07:29 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-01 15:06:33 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-01 15:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-01 15:06:08 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-01 15:05:23 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:05:18 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:04:21 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.018 |  |
| 2026-03-01 15:04:00 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-01 15:03:58 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:03:25 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:03:01 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:58 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:55 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:53 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:36 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-03-01 15:02:34 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-03-01 15:02:30 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.128 |  |
| 2026-03-01 15:02:21 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:18 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:18 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:18 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.064 |  |
| 2026-03-01 15:02:10 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-03-01 15:02:03 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.051 |  |
| 2026-03-01 15:01:54 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:52 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:47 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-03-01 15:01:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.011 |  |
| 2026-03-01 15:01:07 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:00:46 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:00:11 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:59:30 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-01 14:30:22 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.018 |  |
| 2026-03-01 14:17:32 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 15:04:00 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-01 14:04:09 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-01 15:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-01 15:07:29 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-01 14:06:23 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-01 14:59:30 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-01 15:02:18 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:00:46 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:08:29 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:54 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:53 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:47 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:00:11 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:05:23 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:03:01 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:05:18 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:07 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:55 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:01:52 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:58 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:03:25 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:03:58 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:21 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:02:18 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:17:32 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.008 |  |
| 2026-03-01 15:06:33 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-01 15:06:08 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-01 15:02:34 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-03-01 15:09:32 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-03-01 15:01:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-03-01 15:01:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.011 |  |
| 2026-03-01 15:04:21 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.018 |  |
| 2026-03-01 15:02:36 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-03-01 15:02:10 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-03-01 15:02:03 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.051 |  |
| 2026-03-01 15:02:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.064 |  |
| 2026-03-01 14:09:55 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.085 |  |
| 2026-03-01 15:02:30 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)