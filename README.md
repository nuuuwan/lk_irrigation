# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_02:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 02:17:01 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:12:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:11:19 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:10:41 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:08:16 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 02:06:39 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 02:05:04 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-01-12 02:04:17 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-12 02:03:43 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-01-12 02:03:42 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 02:03:25 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:03:25 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:03:02 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:02:58 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.098 |  |
| 2026-01-12 02:02:25 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 02:02:24 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:02:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:02:21 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-01-12 02:02:13 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.063 |  |
| 2026-01-12 02:02:05 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:01:49 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:01:36 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-12 02:01:12 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-12 02:00:59 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 02:00:52 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 02:00:36 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:00:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:50:53 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:43:45 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:32:03 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | 0.418 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 01:07:43 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 1.044 | 🔺 Rising |
| 2026-01-12 02:05:04 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-01-12 01:03:26 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-12 00:11:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-12 02:01:36 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 02:00:52 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 02:02:25 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 02:03:42 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 02:00:59 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 02:06:39 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 02:08:16 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:00:36 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:01:49 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:03:25 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:02:24 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:03:25 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:03:02 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:02:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:00:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:12:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:10:41 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:05:21 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:02:49 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:17:01 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:11:36 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-01-12 02:03:43 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-01-12 02:04:17 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-12 02:01:12 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-12 01:00:07 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-01-12 00:00:08 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-01-12 02:02:21 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-01-12 01:02:38 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-01-12 02:02:13 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.063 |  |
| 2026-01-12 02:02:58 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.098 |  |
| 2026-01-12 00:05:51 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)