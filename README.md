# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_11:06:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,726 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 11:06:47 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:06:43 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:06:33 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-24 11:05:57 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:05:35 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:05:27 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.019 |  |
| 2026-02-24 11:05:08 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:05:04 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.021 |  |
| 2026-02-24 11:04:59 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.028 |  |
| 2026-02-24 11:04:50 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-02-24 11:04:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-24 11:04:21 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-24 11:04:04 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:03:56 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-24 11:03:41 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:03:31 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-24 11:03:13 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:03:10 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.066 |  |
| 2026-02-24 11:03:00 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:51 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-02-24 11:02:46 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:46 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:33 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:02:23 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-02-24 11:02:23 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:07 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:06 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:01:43 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.083 |  |
| 2026-02-24 11:01:38 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:01:31 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:01:10 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:00:55 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-02-24 11:00:34 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-02-24 11:00:29 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-02-24 10:38:34 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.013 |  |
| 2026-02-24 10:18:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-02-24 10:17:29 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.066 |  |
| 2026-02-24 10:15:10 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 11:02:23 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-02-24 11:00:29 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-02-24 11:04:21 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-24 11:06:33 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-24 11:03:31 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-24 11:04:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-24 11:02:46 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:03:00 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:23 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:01:38 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:46 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:07 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:05:35 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:06:47 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:05:08 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:03:41 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:04:04 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:02:06 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:06:09 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 11:06:43 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:03:13 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:05:57 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:02:33 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:01:31 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:01:10 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-02-24 11:02:51 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-02-24 10:38:34 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.013 |  |
| 2026-02-24 11:00:34 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-02-24 10:18:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-02-24 11:05:27 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.019 |  |
| 2026-02-24 11:03:56 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-24 11:04:50 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-02-24 11:05:04 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.021 |  |
| 2026-02-24 11:04:59 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.028 |  |
| 2026-02-24 10:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-02-24 11:00:55 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-02-24 11:03:10 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.066 |  |
| 2026-02-24 11:01:43 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)