# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_13:10:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,780 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 13:10:52 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.184 |  |
| 2025-12-06 13:09:01 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.036 |  |
| 2025-12-06 13:09:00 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | -0.036 |  |
| 2025-12-06 13:07:20 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:06:48 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:06:04 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.050 |  |
| 2025-12-06 13:05:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-06 13:05:04 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.028 |  |
| 2025-12-06 13:04:59 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-06 13:04:42 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.029 |  |
| 2025-12-06 13:04:15 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.040 |  |
| 2025-12-06 13:04:12 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:04:07 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:04:07 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:03:35 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 13:03:19 | Weraganthota (Mahaweli Ganga) | 1.34 | 🟢 Normal | 2.786 | 🔺 Rising |
| 2025-12-06 13:03:01 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:02:56 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.144 |  |
| 2025-12-06 13:02:55 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.011 |  |
| 2025-12-06 13:02:54 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.049 |  |
| 2025-12-06 13:02:50 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:02:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:02:22 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:02:20 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2025-12-06 13:02:10 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.021 |  |
| 2025-12-06 13:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-06 13:01:42 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 13:01:32 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:01:27 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.041 |  |
| 2025-12-06 13:01:26 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-06 13:01:14 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:00:46 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2025-12-06 13:00:33 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 12:06:03 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-06 13:03:19 | Weraganthota (Mahaweli Ganga) | 1.34 | 🟢 Normal | 2.786 | 🔺 Rising |
| 2025-12-06 13:05:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-06 13:01:26 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-06 13:04:59 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-06 13:01:42 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 13:03:35 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 13:02:50 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:06:48 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:03:01 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:04:07 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:04:12 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:04:07 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:07:20 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:01:32 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:12:03 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.009 |  |
| 2025-12-06 13:02:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:00:33 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:02:10 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:01:14 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:02:22 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:02:55 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.011 |  |
| 2025-12-06 13:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-06 13:02:20 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2025-12-06 13:02:10 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.021 |  |
| 2025-12-06 13:05:04 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.028 |  |
| 2025-12-06 13:04:42 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.029 |  |
| 2025-12-06 13:00:46 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2025-12-06 13:09:01 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.036 |  |
| 2025-12-06 13:09:00 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | -0.036 |  |
| 2025-12-06 13:04:15 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.040 |  |
| 2025-12-06 13:01:27 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.041 |  |
| 2025-12-06 13:02:54 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.049 |  |
| 2025-12-06 13:06:04 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.050 |  |
| 2025-12-06 13:02:56 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.144 |  |
| 2025-12-06 13:10:52 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.184 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)