# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_11:10:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 11:10:57 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.046 |  |
| 2025-12-07 11:10:18 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.026 |  |
| 2025-12-07 11:08:17 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.011 |  |
| 2025-12-07 11:07:39 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:07:17 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | -0.028 |  |
| 2025-12-07 11:05:55 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:05:33 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:05:09 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:05:03 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-07 11:04:59 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:04:50 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.071 |  |
| 2025-12-07 11:04:26 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.175 |  |
| 2025-12-07 11:04:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:04:09 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2025-12-07 11:04:03 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | -0.031 |  |
| 2025-12-07 11:03:37 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.020 |  |
| 2025-12-07 11:03:27 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:03:23 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.093 |  |
| 2025-12-07 11:03:17 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.130 |  |
| 2025-12-07 11:03:14 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:03:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.069 |  |
| 2025-12-07 11:03:05 | Thanthirimale (Malwathu Oya) | 5.94 | 🟡 Alert | -0.080 |  |
| 2025-12-07 11:02:17 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:02:09 | Dunamale (Aththanagalu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:02:02 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:59 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:42 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:39 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:32 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:27 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:01:23 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.052 |  |
| 2025-12-07 11:01:15 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:00:50 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:00:42 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2025-12-07 11:00:10 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2025-12-07 10:18:01 | Thanthirimale (Malwathu Oya) | 6.00 | 🟡 Alert | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 11:03:05 | Thanthirimale (Malwathu Oya) | 5.94 | 🟡 Alert | -0.080 |  |
| 2025-12-07 11:05:03 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-07 11:02:17 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:59 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:39 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:05:55 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:15 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:04:12 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:03:14 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:42 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:04:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:05:09 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:07:39 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:02:02 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:01:32 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 11:05:33 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:03:27 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:04:03 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:01:27 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:02:09 | Dunamale (Aththanagalu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:04:59 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-07 11:08:17 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.011 |  |
| 2025-12-07 11:00:10 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2025-12-07 11:00:42 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2025-12-07 11:03:37 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.020 |  |
| 2025-12-07 11:10:18 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.026 |  |
| 2025-12-07 11:07:17 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | -0.028 |  |
| 2025-12-07 11:04:09 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2025-12-07 11:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | -0.031 |  |
| 2025-12-07 11:10:57 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.046 |  |
| 2025-12-07 11:01:23 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.052 |  |
| 2025-12-07 11:03:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.069 |  |
| 2025-12-07 11:04:50 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.071 |  |
| 2025-12-07 11:03:23 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.093 |  |
| 2025-12-07 11:03:17 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.130 |  |
| 2025-12-07 11:04:26 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)