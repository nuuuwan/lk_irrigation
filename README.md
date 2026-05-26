# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_03:21:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 03:21:30 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:16:12 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.006 |  |
| 2026-05-27 03:09:47 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:09:46 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.075 |  |
| 2026-05-27 03:09:44 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.071 |  |
| 2026-05-27 03:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.002 |  |
| 2026-05-27 03:06:56 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:06:36 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:06:34 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:06:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:06:16 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:05:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:05:35 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.063 |  |
| 2026-05-27 03:05:23 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:05:21 | Magura (Kalu Ganga) | 2.93 | 🟢 Normal | -72.000 |  |
| 2026-05-27 03:05:20 | Magura (Kalu Ganga) | 2.95 | 🟢 Normal | -72.000 |  |
| 2026-05-27 03:05:19 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -72.000 |  |
| 2026-05-27 03:05:16 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.060 |  |
| 2026-05-27 03:04:26 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:04:18 | Hanwella (Kelani Ganga) | 4.31 | 🟢 Normal | -0.050 |  |
| 2026-05-27 03:04:05 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:03:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:03:41 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.119 |  |
| 2026-05-27 03:03:41 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2026-05-27 03:03:33 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-27 03:03:19 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:03:06 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:51 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:50 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.027 |  |
| 2026-05-27 03:02:42 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:41 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-27 03:02:28 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:26 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:25 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:19 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:19 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.050 |  |
| 2026-05-27 03:02:12 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.021 |  |
| 2026-05-27 03:01:42 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 03:01:23 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:01:21 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:00:34 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 03:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.002 |  |
| 2026-05-27 03:01:42 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 03:02:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-27 03:06:16 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:06:36 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:01:23 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:04:05 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:04:26 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:03:06 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:42 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:09:47 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:03:19 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:51 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:05:23 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:26 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:06:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:03:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:41 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:05:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:06:34 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:21:30 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:01:21 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:02:19 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 03:16:12 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.006 |  |
| 2026-05-27 03:03:41 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2026-05-27 03:03:33 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-27 03:02:12 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.021 |  |
| 2026-05-27 03:02:50 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.027 |  |
| 2026-05-27 03:04:18 | Hanwella (Kelani Ganga) | 4.31 | 🟢 Normal | -0.050 |  |
| 2026-05-27 03:02:19 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.050 |  |
| 2026-05-27 03:05:16 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.060 |  |
| 2026-05-27 03:05:35 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.063 |  |
| 2026-05-27 03:09:44 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.071 |  |
| 2026-05-27 03:09:46 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.075 |  |
| 2026-05-27 03:03:41 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.119 |  |
| 2026-05-27 03:05:21 | Magura (Kalu Ganga) | 2.93 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)