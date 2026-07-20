# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_14:06:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,396 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 14:06:20 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:06:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:05:10 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:05:04 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:04:51 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-07-20 14:04:42 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.067 |  |
| 2026-07-20 14:04:03 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:57 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-07-20 14:03:28 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:14 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:12 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-20 14:03:11 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:02:56 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:02:52 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-20 14:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:02:38 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-07-20 14:02:31 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:02:17 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.021 |  |
| 2026-07-20 14:02:09 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 14:02:07 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:02:00 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:01:45 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:01:42 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:01:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.030 |  |
| 2026-07-20 14:01:08 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:00:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-20 14:00:45 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:00:07 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | -0.013 |  |
| 2026-07-20 13:46:56 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-20 13:19:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.072 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 13:19:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-20 14:02:52 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-20 14:03:12 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-20 14:02:09 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 14:02:31 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:28 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:01:45 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:14 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:00:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:06:20 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:00:45 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-20 13:03:27 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:04:03 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:01:42 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:11 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 13:08:42 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:06:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:57 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:01:08 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:03:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:05:04 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 13:02:39 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:02:00 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:05:10 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 13:12:41 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 13:17:46 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:02:07 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-07-20 14:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-20 14:03:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-07-20 13:07:40 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-07-20 14:04:51 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-07-20 14:00:07 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | -0.013 |  |
| 2026-07-20 14:02:17 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.021 |  |
| 2026-07-20 13:16:30 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.025 |  |
| 2026-07-20 14:01:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.030 |  |
| 2026-07-20 14:02:38 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-07-20 14:04:42 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)