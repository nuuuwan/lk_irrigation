# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_15:18:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **57,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 15:18:55 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:14:18 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:12:51 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:09:55 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-01-27 15:08:35 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:06:42 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:05:52 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:05:48 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-27 15:05:27 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-27 15:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:05:00 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 15:04:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.081 |  |
| 2026-01-27 15:04:29 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:04:21 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-01-27 15:04:04 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:55 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-01-27 15:03:52 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:48 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:30 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:28 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:24 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-01-27 15:03:13 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:02 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:02:48 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-27 15:02:30 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:02:20 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:02:19 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:02:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-27 15:01:59 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 15:01:44 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.059 |  |
| 2026-01-27 15:01:38 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:29 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 15:01:25 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:20 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:04 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:00:45 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:00:42 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 15:05:27 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-27 15:02:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-27 15:05:00 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 15:01:29 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 15:01:59 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 15:02:48 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-27 15:02:20 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:24 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:00:45 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:20 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:04:29 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:25 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:04:04 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:02:19 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:30 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:52 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:14:18 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:06:42 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:12:51 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:38 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:48 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:00:42 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:13 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:08:35 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:05:52 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:02 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:01:04 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:18:55 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:28 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:02:30 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-27 15:03:55 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-01-27 15:05:48 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-27 15:04:21 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-01-27 15:09:55 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-01-27 15:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-01-27 15:01:44 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.059 |  |
| 2026-01-27 15:04:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)