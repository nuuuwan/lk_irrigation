# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_19:15:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 19:15:29 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:07:34 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-02-13 19:07:31 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.018 |  |
| 2026-02-13 19:07:21 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:07:21 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:07:05 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:06:59 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:06:12 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-13 19:06:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-13 19:05:55 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:05:53 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:05:27 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:05:07 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.060 |  |
| 2026-02-13 19:04:56 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-02-13 19:04:51 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-02-13 19:04:36 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-02-13 19:04:10 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-02-13 19:03:56 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:03:44 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 19:03:27 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 19:02:48 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:02:47 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 19:02:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:02:31 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:02:16 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:02:06 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:02:04 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-02-13 19:02:00 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 19:01:48 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:01:45 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:01:34 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:01:01 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:00:56 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-02-13 19:00:39 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:58:54 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:39:46 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 19:00:56 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-02-13 19:06:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-13 19:06:12 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-13 19:03:44 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 19:02:00 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 19:02:47 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 19:03:27 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 19:02:48 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:00:39 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:07:21 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:01:34 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:03:56 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:01:48 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:02:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:15:29 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:02:06 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:06:59 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:05:27 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:07:21 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:07:05 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 19:07:34 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-02-13 19:05:53 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:02:16 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:02:31 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:01:45 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:05:55 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:01:01 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-13 19:02:04 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-02-13 19:07:31 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.018 |  |
| 2026-02-13 18:11:06 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-02-13 19:04:51 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-02-13 19:04:36 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-02-13 19:04:56 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-02-13 19:04:10 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-02-13 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.041 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-13 19:05:07 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)