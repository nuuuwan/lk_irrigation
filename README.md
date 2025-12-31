# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_12:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 12:12:12 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-31 12:12:02 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.018 |  |
| 2025-12-31 12:08:12 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:07:32 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:07:17 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:07:14 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-31 12:07:13 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 12:06:26 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-31 12:06:03 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.028 |  |
| 2025-12-31 12:05:58 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:05:54 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 12:05:03 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.019 |  |
| 2025-12-31 12:04:51 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:04:48 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 12:04:35 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:04:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:04:13 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:04:03 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.064 |  |
| 2025-12-31 12:03:50 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:03:48 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:03:20 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:51 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.101 |  |
| 2025-12-31 12:02:42 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:33 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 12:02:22 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:20 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-31 12:02:09 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:06 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2025-12-31 12:01:48 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:45 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:37 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:24 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:13 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:00:30 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:00:20 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.032 |  |
| 2025-12-31 12:00:11 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 12:02:20 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-31 12:12:12 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-31 12:05:54 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 12:04:48 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 12:02:33 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 12:07:13 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 12:00:11 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:37 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:00:30 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:45 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:03:20 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:03:50 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:08:12 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:07:17 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:04:35 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:03:48 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:24 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:04:51 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:07:32 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:04:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:48 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:01:13 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:05:58 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:42 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:22 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:04:13 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:02:09 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:06:26 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-31 12:07:14 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-31 12:02:06 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2025-12-31 12:12:02 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.018 |  |
| 2025-12-31 12:05:03 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.019 |  |
| 2025-12-31 12:06:03 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.028 |  |
| 2025-12-31 12:00:20 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.032 |  |
| 2025-12-31 12:04:03 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.064 |  |
| 2025-12-31 12:02:51 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)