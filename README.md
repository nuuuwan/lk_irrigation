# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_23:08:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 23:08:05 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-14 23:06:20 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-04-14 23:06:05 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-04-14 23:04:39 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.019 |  |
| 2026-04-14 23:04:26 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.069 |  |
| 2026-04-14 23:04:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:03:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-14 23:03:41 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:03:00 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:58 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-14 23:02:55 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:53 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-14 23:02:48 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:33 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-14 23:02:21 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:01:41 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.020 |  |
| 2026-04-14 23:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:01:37 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-14 23:01:09 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 23:00:46 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:00:40 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:00:17 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.041 |  |
| 2026-04-14 23:00:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 22:23:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.093 |  |
| 2026-04-14 22:18:11 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 22:15:48 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 23:03:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-14 23:08:05 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-14 23:01:37 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-14 23:02:53 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-14 23:01:09 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 22:04:28 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-14 22:15:48 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:03:41 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 22:04:02 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:55 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:00:40 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:00:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 22:02:57 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 22:04:19 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:00:46 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:21 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:02:48 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:03:00 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 22:01:35 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:04:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:06:20 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-04-14 23:02:33 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-14 23:02:58 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-14 22:01:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-14 23:04:39 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.019 |  |
| 2026-04-14 23:06:05 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-04-14 23:01:41 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-14 22:04:15 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-04-14 22:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.032 |  |
| 2026-04-14 23:00:17 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.041 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 22:08:08 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.060 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-14 23:04:26 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.069 |  |
| 2026-04-14 22:23:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)