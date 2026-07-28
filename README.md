# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_17:13:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,691 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 17:13:40 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:12:42 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:10:56 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:10:25 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:09:13 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:09:13 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-28 17:08:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-07-28 17:08:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:07:59 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:07:35 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:07:29 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:06:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:06:32 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:06:17 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:05:54 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-07-28 17:05:12 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.077 |  |
| 2026-07-28 17:04:39 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-07-28 17:04:23 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.096 |  |
| 2026-07-28 17:04:13 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:03:42 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:03:30 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:03:22 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:03:19 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-28 17:03:04 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 17:03:04 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-07-28 17:02:53 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:02:40 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-28 17:02:26 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:42 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:01:40 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:39 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:37 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:29 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:14 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:01:07 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.059 |  |
| 2026-07-28 17:00:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.092 |  |
| 2026-07-28 17:00:30 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 17:05:54 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-07-28 17:09:13 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-28 17:03:19 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-28 17:03:04 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 17:01:39 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:37 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:40 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:00:30 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:03:42 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:04:13 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:03:30 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:06:32 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:12:42 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:06:17 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:07:35 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 16:01:21 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:02:26 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:13:40 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:10:25 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:06:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:29 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:09:13 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:10:56 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:07:29 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-28 17:07:59 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:03:22 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:01:14 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:02:53 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:01:42 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-28 17:04:39 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-07-28 17:02:40 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-28 17:03:04 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-07-28 17:08:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-07-28 17:01:07 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.059 |  |
| 2026-07-28 17:05:12 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.077 |  |
| 2026-07-28 17:00:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.092 |  |
| 2026-07-28 17:04:23 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)