# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_18:45:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,573 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 18:45:53 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-01-24 18:45:51 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-01-24 18:18:07 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:16:00 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:11:02 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 18:09:20 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-01-24 18:07:02 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:06:56 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:06:39 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:05:30 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 18:05:25 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:05:19 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:04:47 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:04:47 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 18:04:35 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:04:26 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:04:06 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:48 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:28 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:07 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.061 |  |
| 2026-01-24 18:02:51 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-24 18:02:48 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:02:42 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:02:35 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 18:02:29 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:02:18 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:01:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:39 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:13 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:13 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:11 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:05 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-24 18:00:32 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 18:00:28 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:00:22 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:00:14 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:00:14 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 18:45:53 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-01-24 18:02:51 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-24 18:01:05 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-24 18:04:47 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 18:11:02 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 18:05:30 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 18:00:32 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 18:02:35 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 18:00:14 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:48 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:04:47 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:00:28 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:18:07 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:04:26 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:28 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:11 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:04:06 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:04:35 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:02:29 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:02:42 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:06:39 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:05:25 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:13 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:16:00 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:01:13 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:02:18 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:09:20 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-01-24 18:05:19 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:06:56 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:02:48 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:07:02 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:00:14 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:00:22 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:03:07 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)