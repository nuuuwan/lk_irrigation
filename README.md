# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_11:19:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,755 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 11:19:33 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.017 |  |
| 2025-12-22 11:19:32 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2025-12-22 11:11:13 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:09:52 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:07:19 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.109 |  |
| 2025-12-22 11:06:27 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:06:06 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.009 |  |
| 2025-12-22 11:05:53 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.019 |  |
| 2025-12-22 11:05:46 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:05:44 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2025-12-22 11:04:35 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.005 |  |
| 2025-12-22 11:04:31 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:29 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:23 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:15 | Padiyathalawa (Maduru Oya) | 1.24 | 🟢 Normal | -0.023 |  |
| 2025-12-22 11:04:12 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:04 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.021 |  |
| 2025-12-22 11:04:00 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-22 11:03:30 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-22 11:03:18 | Weraganthota (Mahaweli Ganga) | -0.97 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-22 11:02:58 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:57 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-22 11:02:52 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:48 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:02:42 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.125 |  |
| 2025-12-22 11:02:21 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:21 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-22 11:02:19 | Thanthirimale (Malwathu Oya) | 4.73 | 🟢 Normal | -0.050 |  |
| 2025-12-22 11:02:11 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:09 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:02:08 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.066 |  |
| 2025-12-22 11:02:02 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:02:02 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-22 11:01:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-22 11:01:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2025-12-22 11:00:44 | Horowpothana (Yan Oya) | 3.64 | 🟢 Normal | -0.060 |  |
| 2025-12-22 11:00:15 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:27:34 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:23:43 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 11:03:18 | Weraganthota (Mahaweli Ganga) | -0.97 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-22 11:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-22 11:02:57 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-22 11:04:00 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:58 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:52 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:11 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:05:46 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:00:15 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:12 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:29 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:02:21 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:06:27 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:23 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:11:13 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:31 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 11:04:35 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.005 |  |
| 2025-12-22 11:06:06 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.009 |  |
| 2025-12-22 11:03:30 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-22 11:02:21 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-22 11:01:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-22 11:02:02 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-22 11:09:52 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:02:48 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:02:02 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:02:09 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:19:33 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.017 |  |
| 2025-12-22 11:05:44 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2025-12-22 11:05:53 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.019 |  |
| 2025-12-22 11:04:04 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.021 |  |
| 2025-12-22 11:04:15 | Padiyathalawa (Maduru Oya) | 1.24 | 🟢 Normal | -0.023 |  |
| 2025-12-22 11:19:32 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2025-12-22 11:01:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2025-12-22 11:02:19 | Thanthirimale (Malwathu Oya) | 4.73 | 🟢 Normal | -0.050 |  |
| 2025-12-22 11:00:44 | Horowpothana (Yan Oya) | 3.64 | 🟢 Normal | -0.060 |  |
| 2025-12-22 11:02:08 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.066 |  |
| 2025-12-22 11:07:19 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.109 |  |
| 2025-12-22 11:02:42 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)