# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_12:08:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,372 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 12:08:52 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:07:11 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:07:09 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:06:38 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:06:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:06:09 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-21 12:06:04 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-03-21 12:05:27 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-21 12:05:04 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-03-21 12:05:00 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:04:59 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.077 |  |
| 2026-03-21 12:04:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-03-21 12:04:40 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:04:13 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:48 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-03-21 12:03:28 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:26 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:21 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:13 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-21 12:03:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:11 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.088 |  |
| 2026-03-21 12:02:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:02:54 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:02:48 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-03-21 12:02:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-03-21 12:02:37 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-21 12:02:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-03-21 12:02:13 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:57 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:50 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:45 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:43 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-03-21 12:01:40 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-03-21 12:01:39 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:36 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | -0.210 |  |
| 2026-03-21 12:01:24 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.053 |  |
| 2026-03-21 12:01:17 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-21 12:01:14 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:00:27 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 12:04:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-03-21 12:02:37 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-21 12:05:27 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-21 12:06:09 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-21 12:01:14 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:26 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:04:13 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:02:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:07:11 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:06:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:50 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:05:00 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:28 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:45 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:39 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:00:27 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:04:40 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:06:38 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:02:13 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:08:52 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:02:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:03:21 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:05:04 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-03-21 12:03:13 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-21 12:01:17 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-21 12:01:43 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-03-21 12:02:48 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-03-21 12:01:40 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-03-21 12:03:48 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-03-21 11:19:33 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.016 |  |
| 2026-03-21 12:02:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-03-21 12:06:04 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-03-21 12:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-03-21 12:01:24 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.053 |  |
| 2026-03-21 12:04:59 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.077 |  |
| 2026-03-21 12:03:11 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.088 |  |
| 2026-03-21 12:01:36 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)