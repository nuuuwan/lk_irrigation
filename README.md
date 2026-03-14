# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_20:10:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 20:10:51 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:08:22 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:08:12 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:08:11 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.031 |  |
| 2026-03-14 20:08:07 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:07:56 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:07:27 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:06:44 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-03-14 20:05:51 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.059 |  |
| 2026-03-14 20:05:13 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.039 |  |
| 2026-03-14 20:05:09 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.390 |  |
| 2026-03-14 20:04:42 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-03-14 20:04:40 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:04:38 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 20:04:10 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-03-14 20:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-03-14 20:03:42 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:31 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:28 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:22 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.068 |  |
| 2026-03-14 20:03:22 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:21 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:09 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-03-14 20:02:52 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.012 |  |
| 2026-03-14 20:02:51 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:02:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-03-14 20:02:31 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-03-14 20:02:28 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-14 20:02:21 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 20:02:11 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:01:47 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:01:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:00:38 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:00:28 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-14 19:33:47 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:20:24 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-14 19:17:34 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 20:02:28 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-14 20:02:31 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-03-14 19:20:24 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-14 20:04:38 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 20:02:21 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 20:00:38 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:07:56 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:01:47 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:02:51 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:10:51 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:08:07 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:42 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:22 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:04:40 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:28 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:07:27 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:01:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:02:11 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:08:12 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:08:22 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:03:21 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 20:00:28 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-14 20:06:44 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-03-14 20:02:52 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.012 |  |
| 2026-03-14 20:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-03-14 20:04:42 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-03-14 20:03:09 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-03-14 19:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.029 |  |
| 2026-03-14 20:02:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-03-14 20:04:10 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-03-14 20:08:11 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.031 |  |
| 2026-03-14 20:05:13 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.039 |  |
| 2026-03-14 20:05:51 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.059 |  |
| 2026-03-14 20:03:22 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.068 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |
| 2026-03-14 19:06:03 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.148 |  |
| 2026-03-14 20:05:09 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.390 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)