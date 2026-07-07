# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_08:24:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,555 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 08:24:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-07 08:17:15 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:14:46 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.009 |  |
| 2026-07-07 08:11:32 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:10:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:10:30 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:08:51 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:08:45 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.047 |  |
| 2026-07-07 08:08:24 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.027 |  |
| 2026-07-07 08:06:24 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:05:51 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:05:47 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-07 08:05:46 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.089 |  |
| 2026-07-07 08:05:40 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:05:29 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 1584.000 | 🔺 Rising |
| 2026-07-07 08:05:27 | Baddegama (Gin Ganga) | 0.00 | 🟢 Normal | 1584.000 | 🔺 Rising |
| 2026-07-07 08:04:45 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-07-07 08:04:42 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:04:33 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 08:03:49 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-07-07 08:03:46 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:03:27 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:03:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-07-07 08:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-07-07 08:02:55 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:02:49 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.015 |  |
| 2026-07-07 08:02:45 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:02:33 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2026-07-07 08:02:31 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-07 08:02:25 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:02:21 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.035 |  |
| 2026-07-07 08:02:00 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-07 08:01:59 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:01:52 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-07-07 08:01:41 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:01:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:01:28 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:01:18 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:00:53 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:00:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 08:05:29 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 1584.000 | 🔺 Rising |
| 2026-07-07 08:05:47 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-07 08:24:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-07 08:02:31 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-07 08:04:33 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 08:02:25 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:00:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:04:42 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:01:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:10:30 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:05:40 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:01:59 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:03:46 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:02:33 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:03:27 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:02:55 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:01:18 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:06:24 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:02:45 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:10:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:11:32 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:17:15 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:08:51 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:05:51 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:00:53 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:01:41 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 08:14:46 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.009 |  |
| 2026-07-07 08:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-07-07 08:02:00 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-07 08:04:45 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-07-07 08:01:52 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-07-07 08:02:49 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.015 |  |
| 2026-07-07 08:03:49 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-07-07 08:08:24 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.027 |  |
| 2026-07-07 08:02:21 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.035 |  |
| 2026-07-07 08:08:45 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.047 |  |
| 2026-07-07 08:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2026-07-07 08:03:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-07-07 08:05:46 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)