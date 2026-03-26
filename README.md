# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_09:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,726 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 09:10:18 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:08:03 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:08:01 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.058 |  |
| 2026-03-26 09:07:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:06:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-03-26 09:06:01 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 09:05:44 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:05:44 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-26 09:05:39 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.047 |  |
| 2026-03-26 09:05:32 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:04:52 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-26 09:04:47 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:04:45 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:04:07 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:53 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:40 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:32 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:31 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-26 09:03:27 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-03-26 09:03:15 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.364 |  |
| 2026-03-26 09:03:14 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-26 09:03:11 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:08 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.052 |  |
| 2026-03-26 09:03:01 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.079 |  |
| 2026-03-26 09:02:57 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:02:35 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:02:29 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-03-26 09:02:16 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:02:08 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.053 |  |
| 2026-03-26 09:01:53 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-03-26 09:01:36 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:01:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:01:18 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:00:51 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:00:35 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | -0.050 |  |
| 2026-03-26 09:00:20 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 09:01:53 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-03-26 09:03:14 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-26 09:06:01 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 09:04:52 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-26 09:02:29 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:01:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:04:45 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:01:18 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:40 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:00:20 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:07:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:05:44 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:02:35 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:04:47 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:12:18 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:53 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:02:57 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:04:07 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:05:32 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:08:03 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:01:36 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:32 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:10:18 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:03:11 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:02:16 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:05:44 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-26 09:03:31 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-26 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-03-26 09:03:27 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-03-26 09:06:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-03-26 09:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-03-26 09:05:39 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.047 |  |
| 2026-03-26 09:00:35 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | -0.050 |  |
| 2026-03-26 09:03:08 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.052 |  |
| 2026-03-26 09:02:08 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.053 |  |
| 2026-03-26 09:08:01 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.058 |  |
| 2026-03-26 09:03:01 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.079 |  |
| 2026-03-26 09:03:15 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.364 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)