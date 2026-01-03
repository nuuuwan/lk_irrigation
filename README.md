# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_09:12:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,369 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 09:12:21 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:09:56 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-03 09:09:37 | Kithulgala (Kelani Ganga) | 0.49 | 🟢 Normal | -11.029 |  |
| 2026-01-03 09:09:29 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:09:14 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-03 09:08:21 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-01-03 09:08:13 | Galgamuwa (Mee Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 09:06:52 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:06:43 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:06:39 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-03 09:05:53 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:05:30 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |
| 2026-01-03 09:05:22 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.105 |  |
| 2026-01-03 09:05:17 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:05:14 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-01-03 09:04:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:04:28 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.028 |  |
| 2026-01-03 09:04:21 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:03:55 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:03:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -11.029 |  |
| 2026-01-03 09:03:47 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-01-03 09:03:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:03:17 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-01-03 09:03:15 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-01-03 09:03:09 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.060 |  |
| 2026-01-03 09:02:26 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:02:23 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:02:20 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:02:09 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-01-03 09:01:57 | Manampitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-01-03 09:01:55 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:01:53 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:01:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:01:24 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:01:10 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:01:09 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:00:50 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:16:08 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.009 |  |
| 2026-01-03 08:15:17 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 09:06:39 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-03 09:09:14 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-03 09:09:56 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-03 09:08:13 | Galgamuwa (Mee Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 09:01:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:00:50 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:05:53 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:09:29 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:02:23 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:12:21 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:03:09 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:01:09 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:04:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:06:43 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:04:21 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:03:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:03:55 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:01:53 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:01:55 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-03 09:01:10 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:16:08 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.009 |  |
| 2026-01-03 09:08:21 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-01-03 09:06:52 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:02:20 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:01:24 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:05:17 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:02:26 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-03 09:05:14 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-01-03 09:03:47 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-01-03 09:02:09 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-01-03 09:03:17 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-01-03 09:04:28 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.028 |  |
| 2026-01-03 09:03:15 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-01-03 09:01:57 | Manampitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-01-03 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.060 |  |
| 2026-01-03 09:05:30 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |
| 2026-01-03 09:05:22 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.105 |  |
| 2026-01-03 09:09:37 | Kithulgala (Kelani Ganga) | 0.49 | 🟢 Normal | -11.029 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)