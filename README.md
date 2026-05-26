# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_22:13:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,493 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 22:13:36 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-05-26 22:11:26 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:07:33 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 22:07:10 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 22:07:01 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-26 22:06:39 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:05:57 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-05-26 22:05:43 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:05:14 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.024 |  |
| 2026-05-26 22:05:14 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:05:09 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-05-26 22:05:09 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.059 |  |
| 2026-05-26 22:04:57 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-05-26 22:04:49 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 22:04:30 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-26 22:03:54 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:03:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:03:22 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 22:03:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:03:05 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:02:42 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 22:02:38 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:02:22 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.040 |  |
| 2026-05-26 22:02:13 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:02:09 | Hanwella (Kelani Ganga) | 4.55 | 🟢 Normal | -0.053 |  |
| 2026-05-26 22:02:06 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.031 |  |
| 2026-05-26 22:02:03 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:01:49 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:01:39 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-26 22:01:38 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.213 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 22:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-26 22:01:38 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-05-26 22:01:39 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-26 22:07:01 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-26 22:07:10 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 22:04:49 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 22:07:33 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 22:03:22 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 22:02:42 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 22:04:30 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-26 22:11:26 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:00:30 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:03:54 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:01:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:00:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:03:05 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:03:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:01:49 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:06:39 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:05:43 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:03:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:05:14 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:01:18 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:02:03 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:02:13 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:13:36 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-05-26 22:05:57 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-26 22:04:57 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-05-26 22:05:09 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 22:01:04 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.021 |  |
| 2026-05-26 22:05:14 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.024 |  |
| 2026-05-26 22:02:06 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.031 |  |
| 2026-05-26 22:02:22 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.040 |  |
| 2026-05-26 22:02:09 | Hanwella (Kelani Ganga) | 4.55 | 🟢 Normal | -0.053 |  |
| 2026-05-26 22:05:09 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)