# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_10:13:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,601 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 10:13:59 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-18 10:10:57 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.013 |  |
| 2026-03-18 10:10:11 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-03-18 10:09:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:06:18 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:05:57 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:05:51 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:05:01 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-03-18 10:04:49 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.170 |  |
| 2026-03-18 10:04:44 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-03-18 10:04:33 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:04:30 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.020 |  |
| 2026-03-18 10:04:28 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:04:27 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.081 |  |
| 2026-03-18 10:03:26 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:03:12 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 10:03:12 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:03:09 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:03:09 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:02:47 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 10:02:43 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-03-18 10:02:41 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:02:41 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-03-18 10:02:31 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-03-18 10:02:30 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:02:17 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-03-18 10:02:10 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 10:01:54 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:47 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-18 10:01:44 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:43 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:38 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:22 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:10 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:00:47 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 10:04:44 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-03-18 10:05:01 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-03-18 10:13:59 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-18 10:01:47 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-18 10:02:10 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 10:03:12 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 10:02:47 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 10:02:41 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:22 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:03:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:02:17 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:06:18 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:54 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:05:57 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:38 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:03:12 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:02:30 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:03:26 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:43 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:44 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:09:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:05:51 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:04:33 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:00:47 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:03:09 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:04:28 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:03:09 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:01:10 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 10:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-18 10:10:57 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.013 |  |
| 2026-03-18 10:10:11 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-03-18 10:04:30 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.020 |  |
| 2026-03-18 10:02:43 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-03-18 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-03-18 10:02:41 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-03-18 10:02:31 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-03-18 10:04:27 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.081 |  |
| 2026-03-18 10:04:49 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)