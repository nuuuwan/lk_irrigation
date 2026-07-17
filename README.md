# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--17_15:25:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **208,772 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 15:25:50 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:22:12 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:10:32 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:10:19 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:10:11 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:08:49 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-07-17 15:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:06:43 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-17 15:06:06 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:59 | Moraketiya (Walawe Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:53 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.051 |  |
| 2026-07-17 15:05:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:34 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:07 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:04:24 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:04:08 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.032 |  |
| 2026-07-17 15:04:00 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:03:39 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 15:03:30 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-07-17 15:03:25 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:03:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:03:08 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-07-17 15:03:03 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-07-17 15:02:55 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-07-17 15:02:45 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:35 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 15:02:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-17 15:02:22 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:13 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:02 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:56 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:50 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:42 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:18 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:17 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:14 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:06 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:00:16 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.030 |  |
| 2026-07-17 15:00:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-17 14:59:27 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 15:02:55 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-07-17 15:02:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-17 15:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 15:03:39 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 15:01:50 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:35 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:22:12 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:03:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:45 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:02 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:03:25 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:10:19 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:42 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:04:24 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:22 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:34 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:06:06 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:59 | Moraketiya (Walawe Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:17 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:07 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:56 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:25:50 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:04:00 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:18 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:05:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:01:14 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:10:32 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:02:13 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-17 15:06:43 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-17 15:08:49 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-07-17 15:00:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-17 15:03:03 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-07-17 15:03:30 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-07-17 15:00:16 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.030 |  |
| 2026-07-17 15:04:08 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.032 |  |
| 2026-07-17 15:03:08 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-07-17 15:05:53 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)