# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_22:21:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,639 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 22:21:17 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-10 22:14:50 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-10 22:12:49 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-10 22:08:19 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-10 22:06:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:06:05 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:05:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-04-10 22:05:47 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-04-10 22:05:25 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 22:05:24 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-04-10 22:05:07 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:04:58 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-10 22:04:55 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-04-10 22:04:27 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-10 22:04:23 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.116 |  |
| 2026-04-10 22:04:15 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-10 22:04:06 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:03:51 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 22:03:03 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-10 22:02:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:48 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-04-10 22:02:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:33 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:26 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:09 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:03 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 4.737 | 🔺 Rising |
| 2026-04-10 22:01:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 22:01:29 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-04-10 22:01:27 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:01:26 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:01:25 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 4.737 | 🔺 Rising |
| 2026-04-10 22:01:19 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:01:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:00:57 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:00:56 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-04-10 22:00:11 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:58:26 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 22:02:03 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 4.737 | 🔺 Rising |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-10 22:04:27 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-10 22:12:49 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-10 22:14:50 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-10 22:05:25 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 22:01:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 22:03:51 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 22:21:17 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-10 22:02:33 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:01:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:06:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:04:06 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:09 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:01:27 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:05:07 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:00:57 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:00:11 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:01:26 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:02:26 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 22:01:19 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:39:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.008 |  |
| 2026-04-10 22:04:58 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-10 22:04:15 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-10 22:02:48 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-04-10 22:05:24 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-04-10 22:08:19 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-10 22:03:03 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-10 22:01:29 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-04-10 22:04:55 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-04-10 22:00:56 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-04-10 22:05:47 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-04-10 22:05:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-04-10 21:01:38 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.105 |  |
| 2026-04-10 22:04:23 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)