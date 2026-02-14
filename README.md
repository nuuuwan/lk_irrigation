# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_17:25:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,016 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 17:25:14 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:11:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:11:46 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:08:02 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:07:21 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-14 17:07:14 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-02-14 17:06:19 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:05:40 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 17:05:25 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 17:04:56 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:04:47 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:04:22 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.011 |  |
| 2026-02-14 17:04:15 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 17:04:07 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-14 17:03:49 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 17:03:47 | Padiyathalawa (Maduru Oya) | 3.10 | 🟢 Normal | -0.700 |  |
| 2026-02-14 17:03:42 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-14 17:03:22 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:03:18 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-02-14 17:02:53 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.032 |  |
| 2026-02-14 17:02:21 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:02:10 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-02-14 17:02:01 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-14 17:01:45 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:01:39 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-14 17:01:31 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:01:29 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-14 17:01:21 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:01:21 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:01:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-14 17:01:15 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 17:00:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:48 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.087 |  |
| 2026-02-14 17:00:45 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:39 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:34 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:29 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 17:04:07 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-14 17:01:29 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-14 17:03:42 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-14 17:07:21 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-14 17:01:15 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 17:03:49 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 17:04:15 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 17:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 17:05:40 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 17:01:21 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:01:45 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:29 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:45 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:11:46 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:08:02 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:05:25 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:21 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:39 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:01:31 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:04:56 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:02:21 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:03:22 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:25:14 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:04:47 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:06:19 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:34 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:11:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:00:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:01:21 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 17:07:14 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-02-14 17:02:01 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-14 17:01:39 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-14 17:01:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-14 17:03:18 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-02-14 17:04:22 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.011 |  |
| 2026-02-14 17:02:10 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-02-14 17:02:53 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.032 |  |
| 2026-02-14 17:00:48 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.087 |  |
| 2026-02-14 17:03:47 | Padiyathalawa (Maduru Oya) | 3.10 | 🟢 Normal | -0.700 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)