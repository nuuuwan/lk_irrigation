# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_09:13:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,575 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 09:13:52 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:10:37 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:10:32 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.018 |  |
| 2025-12-23 09:10:26 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:09:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.057 |  |
| 2025-12-23 09:08:53 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:08:45 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:06:41 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 09:06:17 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.186 |  |
| 2025-12-23 09:05:01 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 09:04:42 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:04:31 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2025-12-23 09:04:14 | Thanthirimale (Malwathu Oya) | 3.41 | 🟢 Normal | -0.040 |  |
| 2025-12-23 09:04:08 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-23 09:03:39 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:03:38 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:03:32 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:03:29 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:03:28 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2025-12-23 09:03:00 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:02:51 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 09:02:42 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:02:39 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-23 09:02:37 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:02:21 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:02:09 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-23 09:02:04 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:02:01 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2025-12-23 09:01:55 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:01:50 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:01:48 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.053 |  |
| 2025-12-23 09:01:34 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:01:24 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.110 |  |
| 2025-12-23 09:01:21 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:01:14 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:00:53 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 09:04:31 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2025-12-23 09:04:08 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-23 09:02:39 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-23 09:02:09 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-23 09:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 09:05:01 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 09:06:41 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 09:01:55 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:01:34 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:01:14 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:03:32 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:08:45 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:08:53 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:02:21 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:13:52 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:03:29 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:03:39 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:02:51 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:10:37 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:04:42 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:02:42 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:10:26 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:02:04 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:01:50 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:00:53 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:03:00 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:02:37 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:03:38 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-23 09:10:32 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.018 |  |
| 2025-12-23 09:03:28 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2025-12-23 09:02:01 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2025-12-23 09:04:14 | Thanthirimale (Malwathu Oya) | 3.41 | 🟢 Normal | -0.040 |  |
| 2025-12-23 09:01:48 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.053 |  |
| 2025-12-23 09:09:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.057 |  |
| 2025-12-23 08:59:51 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | -0.083 |  |
| 2025-12-23 09:01:24 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.110 |  |
| 2025-12-23 09:06:17 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)