# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_12:18:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,628 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 12:18:32 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:15:54 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.043 |  |
| 2026-03-07 12:10:06 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:09:22 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:07:31 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:06:42 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-07 12:06:26 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:06:06 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:05:58 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-03-07 12:05:48 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:05:47 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:04:51 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-07 12:04:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-07 12:03:35 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-07 12:03:33 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-03-07 12:03:24 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.107 |  |
| 2026-03-07 12:03:23 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:03:20 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-03-07 12:03:14 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-03-07 12:02:52 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:42 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.052 |  |
| 2026-03-07 12:02:41 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 12:02:20 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:18 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-07 12:02:16 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:12 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:07 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-07 12:02:05 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:01:40 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:01:34 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:01:26 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:01:15 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.011 |  |
| 2026-03-07 12:00:55 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-07 12:00:36 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.088 |  |
| 2026-03-07 12:00:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-03-07 12:00:27 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:00:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 12:04:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-07 12:03:35 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-07 12:02:18 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-07 12:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 12:06:42 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-07 12:05:48 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:16 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:00:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:18:32 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:01:26 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:03:33 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:01:40 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:12 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:07:31 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:05 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:06:26 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:10:06 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:52 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:09:22 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:01:34 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:03:23 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:06:06 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:00:27 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:05:47 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:02:20 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:05:58 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-03-07 12:00:55 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-07 12:02:07 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-07 12:04:51 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-07 12:01:15 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.011 |  |
| 2026-03-07 12:00:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-03-07 12:03:14 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-03-07 12:03:20 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-03-07 12:15:54 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.043 |  |
| 2026-03-07 12:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-03-07 12:02:42 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.052 |  |
| 2026-03-07 12:00:36 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.088 |  |
| 2026-03-07 12:03:24 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)