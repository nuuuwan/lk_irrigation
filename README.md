# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_20:18:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,936 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 20:18:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-03-07 20:17:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-03-07 20:10:40 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 20:08:38 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.192 |  |
| 2026-03-07 20:07:38 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-07 20:07:14 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:06:35 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:05:52 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.058 |  |
| 2026-03-07 20:05:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.131 |  |
| 2026-03-07 20:05:06 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:04:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 20:04:57 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-03-07 20:04:50 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:04:43 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:04:03 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:03:43 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:03:26 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:03:21 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:03:18 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:02:53 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 20:02:35 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:02:30 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-07 20:02:29 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:02:19 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.260 |  |
| 2026-03-07 20:02:08 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | -0.010 |  |
| 2026-03-07 20:02:01 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:01:58 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:01:44 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-03-07 20:01:39 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-07 20:01:37 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-03-07 20:01:37 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:01:17 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:01:07 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-03-07 20:00:59 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-03-07 20:00:47 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:00:42 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-03-07 20:00:35 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:00:17 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 20:18:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-03-07 20:01:39 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-07 20:02:53 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 20:04:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 20:10:40 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 20:00:47 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:02:01 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:00:35 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:01:37 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:03:18 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:01:58 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:04:43 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:03:43 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:05:06 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:03:21 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:03:26 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:07:14 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:04:50 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:19 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:04:03 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:02:29 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:06:35 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:01:17 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:02:35 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-07 20:07:38 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-07 20:01:37 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-03-07 20:02:08 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | -0.010 |  |
| 2026-03-07 20:04:57 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-03-07 20:00:59 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-03-07 20:01:44 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-03-07 20:00:42 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-03-07 20:01:07 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-03-07 20:02:30 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-07 20:05:52 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.058 |  |
| 2026-03-07 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.065 |  |
| 2026-03-07 20:05:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.131 |  |
| 2026-03-07 20:08:38 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.192 |  |
| 2026-03-07 20:02:19 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.260 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)