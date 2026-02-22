# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_18:12:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 18:12:15 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-02-22 18:07:34 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-02-22 18:05:52 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.133 |  |
| 2026-02-22 18:05:29 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.135 |  |
| 2026-02-22 18:04:53 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.080 |  |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 18:04:45 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-02-22 18:04:04 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.066 |  |
| 2026-02-22 18:03:55 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.121 |  |
| 2026-02-22 18:03:47 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-22 18:03:45 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:03:35 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:03:23 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:03:16 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:03:13 | Manampitiya (Mahaweli Ganga) | 3.65 | 🟡 Alert | -0.121 |  |
| 2026-02-22 18:03:11 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:03:11 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-22 18:03:09 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.111 |  |
| 2026-02-22 18:02:58 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.041 |  |
| 2026-02-22 18:02:46 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-02-22 18:02:25 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:02:23 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.040 |  |
| 2026-02-22 18:02:07 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.041 |  |
| 2026-02-22 18:02:06 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-22 18:02:04 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.030 |  |
| 2026-02-22 18:02:01 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.034 |  |
| 2026-02-22 18:01:42 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-22 18:01:30 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-02-22 18:01:24 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:03 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:00:36 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:00:32 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-22 18:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.063 |  |
| 2026-02-22 17:55:38 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 17:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.022 |  |
| 2026-02-22 18:03:13 | Manampitiya (Mahaweli Ganga) | 3.65 | 🟡 Alert | -0.121 |  |
| 2026-02-22 18:03:11 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-22 18:02:06 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-22 18:00:32 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 18:03:47 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-22 18:01:24 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:03:23 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:55:38 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:03 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:00:36 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:03:11 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:03:45 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:12:15 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-02-22 18:03:16 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:03:45 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:03:35 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:02:25 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:02:46 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-02-22 18:04:45 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-02-22 18:07:34 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-02-22 18:02:04 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.030 |  |
| 2026-02-22 18:01:30 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-02-22 18:02:01 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.034 |  |
| 2026-02-22 18:02:23 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.040 |  |
| 2026-02-22 18:01:42 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-02-22 18:02:07 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.041 |  |
| 2026-02-22 18:02:58 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.041 |  |
| 2026-02-22 18:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.063 |  |
| 2026-02-22 18:04:04 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.066 |  |
| 2026-02-22 18:04:53 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.080 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-22 18:03:09 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.111 |  |
| 2026-02-22 18:03:55 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.121 |  |
| 2026-02-22 18:05:52 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.133 |  |
| 2026-02-22 18:05:29 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.135 |  |
| 2026-02-22 17:12:46 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)