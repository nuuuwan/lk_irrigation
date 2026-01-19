# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_03:13:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,387 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 03:13:26 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 63.000 | 🔺 Rising |
| 2026-01-20 03:13:22 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 63.000 | 🔺 Rising |
| 2026-01-20 03:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-20 03:11:41 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:11:15 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:06:44 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:05:47 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-20 03:05:45 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 03:05:31 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-20 03:05:24 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-20 03:04:06 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-01-20 03:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-01-20 03:03:52 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:50 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-20 03:03:47 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:46 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:37 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:28 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:09 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:02:57 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:02:43 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:02:24 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-01-20 03:02:17 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-01-20 03:02:10 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:01:56 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 03:01:55 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 03:01:41 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:01:24 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:01:15 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.116 |  |
| 2026-01-20 03:00:11 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-20 02:53:17 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 03:13:26 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 63.000 | 🔺 Rising |
| 2026-01-20 03:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-20 00:03:48 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-20 03:00:11 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-20 03:03:50 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-20 03:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-20 03:05:31 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-20 03:05:47 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-20 03:01:55 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 03:05:45 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 03:01:56 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 03:04:06 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-01-20 03:01:24 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:02:43 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:28 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:02:57 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:01:41 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:09 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:06:44 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:47 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:52 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:46 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 02:03:19 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:11:41 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:37 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:02:10 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 01:03:22 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-20 01:01:18 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:11:15 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 18:02:06 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:05:24 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 01:08:42 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.009 |  |
| 2026-01-19 18:01:58 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-19 18:00:21 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.010 |  |
| 2026-01-20 00:02:14 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-20 03:02:17 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-01-20 03:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-01-20 03:02:24 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-01-20 03:01:15 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)