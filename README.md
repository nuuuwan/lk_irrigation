# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_18:20:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,289 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 18:20:04 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:12:40 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:11:34 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-20 18:09:36 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:07:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2025-12-20 18:07:34 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:06:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:05:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:05:25 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.042 |  |
| 2025-12-20 18:04:29 | Manampitiya (Mahaweli Ganga) | 3.16 | 🟡 Alert | -0.057 |  |
| 2025-12-20 18:04:20 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.031 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:01 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-20 18:03:56 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.072 |  |
| 2025-12-20 18:03:48 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.446 | 🔺 Rising |
| 2025-12-20 18:03:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:03:39 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:03:35 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2025-12-20 18:03:21 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-20 18:03:09 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:03:08 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2025-12-20 18:03:03 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 18:02:47 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.020 |  |
| 2025-12-20 18:02:45 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:02:24 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:02:20 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-20 18:02:17 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:02:06 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:01:56 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:01:39 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:01:27 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 18:01:15 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.010 |  |
| 2025-12-20 18:01:14 | Horowpothana (Yan Oya) | 6.25 | 🟡 Alert | -0.010 |  |
| 2025-12-20 18:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:00:36 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-20 18:00:28 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-20 18:00:27 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-20 18:00:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 18:01:14 | Horowpothana (Yan Oya) | 6.25 | 🟡 Alert | -0.010 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 18:04:29 | Manampitiya (Mahaweli Ganga) | 3.16 | 🟡 Alert | -0.057 |  |
| 2025-12-20 18:03:48 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.446 | 🔺 Rising |
| 2025-12-20 18:03:21 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-20 18:02:20 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-20 18:04:01 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-20 18:11:34 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-20 18:00:28 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-20 18:03:03 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 18:07:34 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:01:56 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:02:17 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:09:36 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:03:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:03:09 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:03:39 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:05:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:06:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:02:45 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:12:40 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:20:04 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:02:24 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:02:06 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:03:08 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2025-12-20 18:01:15 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.010 |  |
| 2025-12-20 18:00:36 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-20 18:00:27 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-20 18:01:27 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-20 18:03:35 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2025-12-20 18:02:47 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.020 |  |
| 2025-12-20 18:00:08 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.024 |  |
| 2025-12-20 18:00:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2025-12-20 18:04:20 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.031 |  |
| 2025-12-20 18:05:25 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.042 |  |
| 2025-12-20 18:03:56 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.072 |  |
| 2025-12-20 18:07:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)