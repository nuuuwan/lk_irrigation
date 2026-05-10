# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_02:11:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,491 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 02:11:28 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:11:04 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-11 02:10:52 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:08:09 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:07:44 | Katharagama (Menik Ganga) | 1.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 02:07:41 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.103 |  |
| 2026-05-11 02:06:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 02:06:15 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-11 02:05:49 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:05:33 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-05-11 02:03:39 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 02:03:19 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-11 02:03:01 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-05-11 02:02:57 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.080 |  |
| 2026-05-11 02:02:47 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-11 02:02:37 | Thanamalwila (Kirindi Oya) | 5.90 | 🔴 Major Flood | 0.342 | 🔺 Rising |
| 2026-05-11 02:02:22 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.034 |  |
| 2026-05-11 02:02:19 | Moragaswewa (Deduru Oya) | 1.31 | 🟢 Normal | -0.049 |  |
| 2026-05-11 02:02:16 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 02:02:15 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-05-11 02:01:57 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 02:01:21 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-11 02:00:28 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:00:16 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.031 |  |
| 2026-05-11 02:00:11 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 01:37:59 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-11 01:37:15 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.014 |  |
| 2026-05-11 01:32:45 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 02:02:37 | Thanamalwila (Kirindi Oya) | 5.90 | 🔴 Major Flood | 0.342 | 🔺 Rising |
| 2026-05-11 02:05:33 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-05-11 01:01:15 | Kuda Oya (Kirindi Oya) | 6.35 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-05-11 02:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-11 00:07:37 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-11 00:02:23 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-11 02:11:04 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-11 02:02:47 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-11 00:04:14 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 02:02:16 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 02:01:57 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 02:03:39 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 02:06:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 02:07:44 | Katharagama (Menik Ganga) | 1.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 02:06:15 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-11 01:16:33 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-10 22:02:10 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:11:28 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:05:49 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:08:09 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:00:11 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:00:28 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:03:19 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-05-11 01:00:48 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-11 02:01:21 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-11 02:03:01 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-05-11 02:02:15 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-05-11 00:12:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-05-11 01:37:15 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.014 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-11 02:00:16 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.031 |  |
| 2026-05-11 01:05:19 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | -0.031 |  |
| 2026-05-11 01:04:19 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-05-11 02:02:22 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.034 |  |
| 2026-05-11 02:02:19 | Moragaswewa (Deduru Oya) | 1.31 | 🟢 Normal | -0.049 |  |
| 2026-05-11 02:02:57 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.080 |  |
| 2026-05-11 02:07:41 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)