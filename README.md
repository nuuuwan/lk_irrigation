# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_08:12:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,763 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 08:12:37 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.047 |  |
| 2025-12-05 08:12:11 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:10:47 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.009 |  |
| 2025-12-05 08:09:08 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 08:08:33 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.072 |  |
| 2025-12-05 08:08:23 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.028 |  |
| 2025-12-05 08:08:23 | Magura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.046 |  |
| 2025-12-05 08:08:22 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.012 |  |
| 2025-12-05 08:06:22 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.176 |  |
| 2025-12-05 08:06:12 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:06:11 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:06:07 | Panadugama (Nilwala Ganga) | 4.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-05 08:05:38 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.058 |  |
| 2025-12-05 08:04:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:29 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:22 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.020 |  |
| 2025-12-05 08:04:21 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:17 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:13 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:08 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:02 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.147 |  |
| 2025-12-05 08:03:51 | Weraganthota (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2025-12-05 08:03:44 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:03:34 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:03:16 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:03:14 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | -0.040 |  |
| 2025-12-05 08:03:02 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:02:52 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:02:48 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -0.020 |  |
| 2025-12-05 08:02:43 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-05 08:02:33 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:02:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.123 |  |
| 2025-12-05 08:02:19 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:01:48 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:01:42 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:01:04 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:00:18 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:00:14 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 07:07:23 | Thanthirimale (Malwathu Oya) | 5.81 | 🟡 Alert | 0.153 | 🔺 Rising |
| 2025-12-05 08:03:51 | Weraganthota (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2025-12-05 08:06:07 | Panadugama (Nilwala Ganga) | 4.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-05 08:02:43 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-05 08:09:08 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 08:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:29 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:02:19 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:02:33 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:06:12 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:21 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:01:42 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:01:04 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:04:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:02:52 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:12:11 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:03:44 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:03:16 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:10:47 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.009 |  |
| 2025-12-05 08:06:11 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:03:02 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:02:48 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:00:14 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:03:34 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:01:48 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:08:22 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.012 |  |
| 2025-12-05 08:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -0.020 |  |
| 2025-12-05 08:04:22 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.020 |  |
| 2025-12-05 08:08:23 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.028 |  |
| 2025-12-05 08:03:14 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | -0.040 |  |
| 2025-12-05 08:08:23 | Magura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.046 |  |
| 2025-12-05 08:12:37 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.047 |  |
| 2025-12-05 08:05:38 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.058 |  |
| 2025-12-05 08:08:33 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.072 |  |
| 2025-12-05 08:02:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.123 |  |
| 2025-12-05 08:04:02 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.147 |  |
| 2025-12-05 08:06:22 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)