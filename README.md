# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_08:01:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,247 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 08:01:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.091 |  |
| 2025-12-08 08:01:28 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:01:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.063 |  |
| 2025-12-08 08:01:11 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2025-12-08 08:01:11 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 08:01:04 | Thanthirimale (Malwathu Oya) | 4.65 | 🟢 Normal | -0.126 |  |
| 2025-12-08 08:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:00:16 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:44:51 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.036 |  |
| 2025-12-08 07:40:00 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-08 07:19:34 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:09:59 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:09:54 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.014 |  |
| 2025-12-08 07:09:36 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 07:09:14 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 07:08:37 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:08:19 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2025-12-08 07:07:53 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:06:33 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:06:18 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.049 |  |
| 2025-12-08 07:05:53 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.048 |  |
| 2025-12-08 07:05:39 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-08 07:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.39 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2025-12-08 07:04:46 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.072 |  |
| 2025-12-08 07:04:42 | Weraganthota (Mahaweli Ganga) | -1.29 | 🟢 Normal | -1.537 |  |
| 2025-12-08 07:04:40 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2025-12-08 07:04:32 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.060 |  |
| 2025-12-08 07:04:07 | Thanthirimale (Malwathu Oya) | 4.77 | 🟢 Normal | -0.126 |  |
| 2025-12-08 07:04:07 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-08 07:04:06 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.087 |  |
| 2025-12-08 07:03:14 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.063 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 07:08:19 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2025-12-08 07:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.39 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2025-12-08 07:02:52 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-08 07:09:36 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 08:01:11 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 07:09:14 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 07:40:00 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-08 08:00:16 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:02:11 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:02:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:07:53 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:09:59 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:19:34 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:01:28 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:08:37 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:08:55 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.002 |  |
| 2025-12-08 07:02:23 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-08 07:04:40 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2025-12-08 07:04:07 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-08 07:05:39 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-08 07:09:54 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.014 |  |
| 2025-12-08 07:02:18 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.019 |  |
| 2025-12-08 08:01:11 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2025-12-08 07:00:48 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2025-12-08 07:44:51 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.036 |  |
| 2025-12-08 07:01:36 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.040 |  |
| 2025-12-08 07:05:53 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.048 |  |
| 2025-12-08 07:06:18 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.049 |  |
| 2025-12-08 07:04:32 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.060 |  |
| 2025-12-08 08:01:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.063 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-08 07:04:46 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.072 |  |
| 2025-12-08 07:04:06 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.087 |  |
| 2025-12-08 08:01:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.091 |  |
| 2025-12-08 08:01:04 | Thanthirimale (Malwathu Oya) | 4.65 | 🟢 Normal | -0.126 |  |
| 2025-12-08 07:04:42 | Weraganthota (Mahaweli Ganga) | -1.29 | 🟢 Normal | -1.537 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)