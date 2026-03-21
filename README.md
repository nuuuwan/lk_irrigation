# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_09:29:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,249 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 09:29:48 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:12:56 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:08:58 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-03-21 09:08:36 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.092 |  |
| 2026-03-21 09:07:41 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-21 09:07:38 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:07:31 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:07:31 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-21 09:07:04 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:06:14 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:05:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:05:13 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:04:59 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:03:55 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-03-21 09:03:36 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:03:34 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-21 09:03:27 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.067 |  |
| 2026-03-21 09:03:24 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-21 09:03:16 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:03:16 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:03:12 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:02:59 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-21 09:02:55 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-21 09:02:46 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:02:43 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-03-21 09:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.070 |  |
| 2026-03-21 09:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-03-21 09:02:07 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -0.136 |  |
| 2026-03-21 09:02:02 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:54 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:48 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-03-21 09:01:41 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:31 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-21 09:01:14 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-03-21 09:01:13 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-03-21 09:01:08 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:06 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-03-21 09:01:06 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.405 |  |
| 2026-03-21 09:00:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 09:01:48 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-03-21 09:01:31 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-21 09:02:55 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-21 09:03:24 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-21 09:03:34 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-21 09:01:08 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:54 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:02:46 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:07:31 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:05:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:03:16 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:03:36 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:41 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:06:14 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:29:48 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:05:13 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:07:38 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:02:02 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:03:16 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:00:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:12:56 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:04:59 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:03:12 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:07:41 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-21 09:08:58 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-03-21 09:07:31 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-21 09:01:06 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-03-21 09:02:59 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-21 09:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-03-21 09:02:43 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-03-21 09:03:55 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-03-21 09:01:13 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-03-21 09:01:14 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-03-21 09:03:27 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.067 |  |
| 2026-03-21 09:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.070 |  |
| 2026-03-21 09:08:36 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.092 |  |
| 2026-03-21 09:02:07 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -0.136 |  |
| 2026-03-21 09:01:06 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.405 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)