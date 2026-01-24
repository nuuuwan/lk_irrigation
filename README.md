# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_03:31:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 03:31:53 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:26:21 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:21:26 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -1.193 |  |
| 2026-01-25 03:16:42 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.016 |  |
| 2026-01-25 03:13:58 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.155 |  |
| 2026-01-25 03:13:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-25 03:10:06 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-25 03:09:30 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:08:29 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:08:14 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-25 03:07:42 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-25 03:07:08 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.020 |  |
| 2026-01-25 03:05:39 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:05:17 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:05:15 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:41 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:37 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:34 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.031 |  |
| 2026-01-25 03:03:31 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:19 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:18 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:42 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:41 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:40 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-25 03:02:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:08 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-25 03:01:25 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:01:19 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 02:58:52 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 02:50:45 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -1.193 |  |
| 2026-01-25 02:37:06 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 02:02:47 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-01-25 03:07:42 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-25 02:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-25 03:02:08 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-25 03:13:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-24 23:03:01 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:26:21 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 02:02:21 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:40 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 02:02:45 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-25 02:37:06 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:41 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:09:30 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:05:17 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:31:53 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:08:29 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:19 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:31 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:03:37 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:05:15 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:01:25 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:05:39 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-25 02:11:04 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-25 00:06:28 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:42 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:01:19 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:10:06 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-25 03:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-25 03:08:14 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-25 03:16:42 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.016 |  |
| 2026-01-24 18:00:14 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-25 03:07:08 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.020 |  |
| 2026-01-25 03:03:34 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.031 |  |
| 2026-01-25 03:13:58 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.155 |  |
| 2026-01-25 02:02:46 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.667 |  |
| 2026-01-25 03:21:26 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -1.193 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)