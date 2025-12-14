# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_09:12:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 09:12:10 | Manampitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.026 |  |
| 2025-12-14 09:10:35 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-14 09:09:38 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:09:03 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:08:30 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-14 09:08:14 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:07:44 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-14 09:06:42 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2025-12-14 09:06:37 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:06:24 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.051 |  |
| 2025-12-14 09:05:59 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2025-12-14 09:05:55 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:05:30 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:05:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2025-12-14 09:05:02 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.020 |  |
| 2025-12-14 09:04:43 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:04:09 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-14 09:03:56 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.570 |  |
| 2025-12-14 09:03:45 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:03:25 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:03:23 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.039 |  |
| 2025-12-14 09:03:09 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:03:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:03:05 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.031 |  |
| 2025-12-14 09:02:46 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 09:02:32 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:02:18 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:02:00 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 09:01:51 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.031 |  |
| 2025-12-14 09:01:37 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-14 09:01:34 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:01:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.021 |  |
| 2025-12-14 09:01:21 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:01:18 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 09:01:12 | Thanthirimale (Malwathu Oya) | 4.36 | 🟢 Normal | -0.020 |  |
| 2025-12-14 09:00:51 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 09:04:09 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-14 09:08:30 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-14 09:01:37 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-14 09:01:18 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 09:10:35 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-14 09:02:46 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 09:02:00 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 09:01:34 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:00:10 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:05:55 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:02:18 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:03:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:00:51 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:04:43 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:01:21 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:06:37 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:09:38 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:09:03 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 09:06:42 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2025-12-14 09:07:44 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-14 09:03:45 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:05:30 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:03:25 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:03:09 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:02:32 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-14 09:05:59 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2025-12-14 09:05:02 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.020 |  |
| 2025-12-14 09:01:12 | Thanthirimale (Malwathu Oya) | 4.36 | 🟢 Normal | -0.020 |  |
| 2025-12-14 09:01:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.021 |  |
| 2025-12-14 09:12:10 | Manampitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.026 |  |
| 2025-12-14 09:01:51 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.031 |  |
| 2025-12-14 09:03:05 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.031 |  |
| 2025-12-14 09:05:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2025-12-14 09:03:23 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.039 |  |
| 2025-12-14 09:06:24 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.051 |  |
| 2025-12-14 09:00:08 | Horowpothana (Yan Oya) | 4.62 | 🟢 Normal | -0.081 |  |
| 2025-12-14 09:03:56 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.570 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)