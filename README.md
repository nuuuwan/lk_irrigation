# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_13:09:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,367 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 13:09:59 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 13:09:46 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:09:14 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:09:06 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-01-24 13:07:55 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-24 13:07:52 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:07:11 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:06:58 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.064 |  |
| 2026-01-24 13:06:41 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:06:04 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-01-24 13:06:01 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.167 |  |
| 2026-01-24 13:05:54 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 13:05:07 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:05:00 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-24 13:04:30 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.030 |  |
| 2026-01-24 13:04:20 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.058 |  |
| 2026-01-24 13:04:00 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:03:31 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.041 |  |
| 2026-01-24 13:03:25 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:03:12 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.041 |  |
| 2026-01-24 13:03:00 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:02:56 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:02:48 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:02:46 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:02:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:02:21 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:02:20 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:45 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:19 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:18 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-24 13:01:14 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:10 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:07 | Weraganthota (Mahaweli Ganga) | -2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:00:40 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:00:40 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 13:01:18 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-24 13:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-24 13:05:00 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-24 13:09:59 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 13:05:54 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 13:01:07 | Weraganthota (Mahaweli Ganga) | -2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:14 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:02:48 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:04:20 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:03:25 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:00:40 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:09:14 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:02:20 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 12:02:35 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 12:04:20 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:06:41 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:05:07 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:45 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:09:46 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:02:46 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:07:52 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:19 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:04:00 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:01:10 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:07:11 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 13:07:55 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-24 13:09:06 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-01-24 13:02:56 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:03:00 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:02:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:00:40 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:02:21 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-24 13:06:04 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-01-24 13:04:30 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.030 |  |
| 2026-01-24 13:03:31 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.041 |  |
| 2026-01-24 13:03:12 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.041 |  |
| 2026-01-24 13:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.058 |  |
| 2026-01-24 13:06:58 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.064 |  |
| 2026-01-24 13:06:01 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)