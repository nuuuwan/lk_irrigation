# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_10:16:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,707 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **46** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 10:16:57 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:10:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:08:38 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:08:35 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:07:34 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-03-17 10:07:29 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:07:20 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:07:02 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-03-17 10:07:00 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:06:31 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.061 |  |
| 2026-03-17 10:06:05 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-03-17 10:05:33 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-17 10:05:26 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:04:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-17 10:04:37 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.059 |  |
| 2026-03-17 10:04:04 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:04:01 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-17 10:03:54 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.344 |  |
| 2026-03-17 10:03:45 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.021 |  |
| 2026-03-17 10:03:44 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:03:33 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 10:03:30 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:03:19 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:03:15 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-03-17 10:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:03:14 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:03:10 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:03:02 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 10:02:56 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-17 10:02:50 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-17 10:02:41 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:02:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.060 |  |
| 2026-03-17 10:02:11 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:41 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:40 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:39 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:26 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:00:52 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:00:15 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:58:11 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:43:58 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-03-17 09:43:56 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-03-17 09:43:54 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-03-17 09:43:51 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.136 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 10:06:05 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-03-17 10:04:01 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-17 10:05:33 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-17 10:04:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-17 10:02:56 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-17 10:02:50 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-17 10:03:33 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 10:03:02 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 10:01:41 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:03:14 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:03:10 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:08:35 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:02:11 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:07:20 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:07:00 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:00:15 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:05:26 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:39 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:26 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:10:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:07:29 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:00:52 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:02:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:03:30 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:16:57 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:01:40 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:07:34 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-03-17 10:03:19 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:02:41 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:08:38 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:03:15 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-03-17 10:07:02 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-03-17 10:03:45 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.021 |  |
| 2026-03-17 10:04:37 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.059 |  |
| 2026-03-17 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.060 |  |
| 2026-03-17 10:06:31 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.061 |  |
| 2026-03-17 10:03:54 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.344 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)