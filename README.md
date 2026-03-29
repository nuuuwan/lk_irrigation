# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_13:16:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,581 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 13:16:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:14:44 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:11:06 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:09:28 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-29 13:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.027 |  |
| 2026-03-29 13:06:55 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 5.248 | 🔺 Rising |
| 2026-03-29 13:06:07 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-29 13:05:49 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:05:20 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:04:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-29 13:04:45 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-29 13:04:24 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-29 13:04:18 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-29 13:04:15 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-29 13:04:13 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:03:21 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-03-29 13:03:19 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-29 13:03:07 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:03:04 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:02:56 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:02:42 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.031 |  |
| 2026-03-29 13:02:41 | Rathnapura (Kalu Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-03-29 13:02:25 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:02:15 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:02:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:46 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-29 13:01:42 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:41 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:18 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.065 |  |
| 2026-03-29 13:01:10 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:02 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:00:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-29 13:00:39 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:00:26 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:00:24 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 5.248 | 🔺 Rising |
| 2026-03-29 13:00:18 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 13:06:55 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 5.248 | 🔺 Rising |
| 2026-03-29 13:01:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-29 13:04:18 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-29 13:09:28 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-29 13:04:45 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-29 13:00:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-29 13:06:07 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-29 13:00:26 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:41 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:46 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:00:39 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:42 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:04:13 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:10 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:14:44 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 12:04:25 | Magura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:02:15 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:03:04 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:11:06 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:05:49 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:02:56 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:16:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:02:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:05:20 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:02:25 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:01:02 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-29 12:02:32 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:03:07 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-29 13:04:15 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-29 13:04:24 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-29 13:03:19 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-29 13:04:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-29 12:07:25 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-03-29 13:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.027 |  |
| 2026-03-29 13:02:42 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.031 |  |
| 2026-03-29 13:02:41 | Rathnapura (Kalu Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-03-29 13:00:18 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | -0.040 |  |
| 2026-03-29 13:03:21 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-03-29 13:01:18 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)