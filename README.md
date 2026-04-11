# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_22:39:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,516 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 22:39:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.006 |  |
| 2026-04-11 22:34:43 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:26:42 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:25:11 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-11 22:12:43 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-04-11 22:12:13 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.042 |  |
| 2026-04-11 22:11:19 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:09:17 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:09:10 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:07:48 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:07:42 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.028 |  |
| 2026-04-11 22:06:47 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.083 |  |
| 2026-04-11 22:06:45 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-11 22:06:28 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-11 22:06:18 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-11 22:05:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:03:48 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 22:03:14 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-11 22:03:04 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-04-11 22:03:04 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.319 |  |
| 2026-04-11 22:02:56 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:53 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:52 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:26 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-11 22:02:09 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:09 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:05 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:01:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:01:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:01:09 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2026-04-11 22:00:47 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-11 22:00:46 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-11 21:59:59 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 22:03:04 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-04-11 22:12:43 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-04-11 22:03:14 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-11 22:06:18 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-11 22:00:47 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-11 22:00:46 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-11 22:25:11 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-11 22:06:28 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-11 21:02:18 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 22:03:48 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 22:26:42 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:53 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:05 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:07:48 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:01:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:11:19 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 18:03:33 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:09 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:09:17 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:05:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:16 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:59:59 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:34:43 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:56 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:02:09 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:09:10 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:01:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:14 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 22:39:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.006 |  |
| 2026-04-11 22:06:45 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-11 18:00:38 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-11 22:01:09 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2026-04-11 22:02:26 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-11 22:07:42 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.028 |  |
| 2026-04-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.040 |  |
| 2026-04-11 22:12:13 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.042 |  |
| 2026-04-11 22:06:47 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.083 |  |
| 2026-04-11 22:03:04 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.319 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)