# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_14:14:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,127 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 14:14:53 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:13:21 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:09:38 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:09:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:09:18 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:09:06 | Baddegama (Gin Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2026-03-24 14:07:35 | Weraganthota (Mahaweli Ganga) | -2.67 | 🟢 Normal | -0.098 |  |
| 2026-03-24 14:07:28 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-24 14:06:06 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-03-24 14:05:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.079 |  |
| 2026-03-24 14:05:16 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:04:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-24 14:04:52 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:04:33 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-03-24 14:03:48 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:46 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:46 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 14:03:28 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:03:28 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:08 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:07 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:59 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:59 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:02:58 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:57 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:42 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:36 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:35 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:22 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.020 |  |
| 2026-03-24 14:02:11 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:01:31 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:01:21 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -2.118 |  |
| 2026-03-24 14:01:14 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:01:10 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:00:57 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:00:47 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -2.118 |  |
| 2026-03-24 14:00:43 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.070 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 14:04:33 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-03-24 14:04:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-24 14:00:43 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-24 14:07:28 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-24 14:03:46 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 14:03:28 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:58 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:07 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:00:57 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:09:18 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:11 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:35 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:14:53 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:46 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:08 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:36 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:13:21 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:01:31 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:57 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:59 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:04:52 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:01:10 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:48 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:02:42 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 14:06:06 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-03-24 14:09:38 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:03:28 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:01:14 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:09:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:05:16 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:02:59 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-24 14:02:22 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.020 |  |
| 2026-03-24 14:09:06 | Baddegama (Gin Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2026-03-24 14:05:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.079 |  |
| 2026-03-24 14:07:35 | Weraganthota (Mahaweli Ganga) | -2.67 | 🟢 Normal | -0.098 |  |
| 2026-03-24 14:01:21 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -2.118 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)