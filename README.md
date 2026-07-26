# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_09:16:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **216,604 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 09:16:53 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:16:52 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:12:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.051 |  |
| 2026-07-26 09:11:58 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:11:24 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-26 09:11:04 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:10:53 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:10:47 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:08:55 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.028 |  |
| 2026-07-26 09:07:32 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-26 09:07:28 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:07:28 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 09:06:48 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:06:41 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:05:59 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:05:51 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-26 09:04:58 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:04:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:04:34 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:04:10 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:03:37 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:03:31 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 09:03:26 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:03:23 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-26 09:03:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:03:13 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 09:02:39 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:02:30 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-26 09:02:21 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:02:18 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-07-26 09:02:08 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:02:01 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-26 09:01:46 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:01:20 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 09:01:16 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-26 09:01:15 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:01:13 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.023 |  |
| 2026-07-26 09:01:12 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:00:50 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:00:20 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 08:59:57 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 09:07:32 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-26 09:03:23 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-26 09:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-26 09:11:24 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-26 09:05:51 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-26 09:01:20 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 09:03:13 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 09:07:28 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 09:03:31 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 09:04:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:00:50 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:01:12 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:01:15 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:02:39 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:00:20 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:10:47 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:03:37 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:04:10 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:04:34 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:11:58 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:03:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:04:58 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:07:28 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:01:46 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:02:21 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-26 08:59:57 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:06:41 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:02:08 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:10:53 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:11:04 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:16:53 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:05:59 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:03:26 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 09:02:30 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-26 09:01:16 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-26 09:02:18 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-07-26 09:01:13 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.023 |  |
| 2026-07-26 09:08:55 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.028 |  |
| 2026-07-26 09:12:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)