# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_13:05:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,087 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 13:05:06 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-04 13:05:01 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:05:00 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:04:58 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:04:36 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.130 |  |
| 2025-12-04 13:04:25 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2025-12-04 13:04:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:03:58 | Thanthirimale (Malwathu Oya) | 6.08 | 🟡 Alert | -0.029 |  |
| 2025-12-04 13:03:43 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.019 |  |
| 2025-12-04 13:03:38 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:03:21 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:03:08 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.030 |  |
| 2025-12-04 13:02:11 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:02:07 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-04 13:01:57 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-04 13:01:31 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-04 13:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:01:21 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:01:20 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:01:14 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.020 |  |
| 2025-12-04 13:01:12 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:01:02 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 13:00:55 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:11:08 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:10:04 | Weraganthota (Mahaweli Ganga) | -0.80 | 🟢 Normal | -0.102 |  |
| 2025-12-04 12:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:09:22 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:08:18 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.009 |  |
| 2025-12-04 12:07:45 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:07:43 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.037 |  |
| 2025-12-04 12:07:28 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:06:16 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2025-12-04 12:06:02 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 13:03:58 | Thanthirimale (Malwathu Oya) | 6.08 | 🟡 Alert | -0.029 |  |
| 2025-12-04 12:04:21 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-04 12:04:05 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 12:04:52 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 12:07:28 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:00:55 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:02:45 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:05:01 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:01:21 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:03:21 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:11:08 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:02:11 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:03:38 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:04:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:01:12 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-04 13:01:20 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2025-12-04 12:08:18 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.009 |  |
| 2025-12-04 13:05:06 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-04 12:05:10 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-04 12:04:21 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2025-12-04 13:01:02 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 12:05:05 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-04 12:06:02 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-04 13:01:31 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-04 13:02:07 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-04 13:03:43 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.019 |  |
| 2025-12-04 12:00:41 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2025-12-04 13:01:57 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-04 13:01:14 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.020 |  |
| 2025-12-04 13:04:25 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2025-12-04 13:03:08 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.030 |  |
| 2025-12-04 12:07:43 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.037 |  |
| 2025-12-04 12:02:00 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.045 |  |
| 2025-12-04 12:10:04 | Weraganthota (Mahaweli Ganga) | -0.80 | 🟢 Normal | -0.102 |  |
| 2025-12-04 13:04:36 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)