# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_23:18:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,648 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 23:18:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:08:10 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.029 |  |
| 2026-05-25 23:08:05 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:07:57 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-25 23:07:55 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:07:10 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-25 23:07:06 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-05-25 23:07:01 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-25 23:06:47 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.046 |  |
| 2026-05-25 23:06:37 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.050 |  |
| 2026-05-25 23:06:03 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:05:42 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-25 23:04:54 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2026-05-25 23:04:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 23:03:53 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:50 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:41 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-25 23:03:38 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.049 |  |
| 2026-05-25 23:03:35 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:29 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-25 23:03:25 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:10 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:02:29 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:02:11 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-25 23:02:08 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:01:50 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 23:01:31 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 23:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:01:12 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:00:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:00:47 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.084 |  |
| 2026-05-25 23:00:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 20:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.061 |  |
| 2026-05-25 23:03:41 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-25 22:04:31 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-25 23:05:42 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-25 23:07:01 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-25 23:04:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 23:07:57 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-25 23:01:31 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 23:07:10 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-25 23:01:50 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 23:07:55 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:53 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:18:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:02:08 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:00:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:50 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:06:03 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:01:12 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:00:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:02:29 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:25 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:03:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:35 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:03:10 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:08:05 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:27 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 23:02:11 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-25 23:03:29 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-25 23:07:06 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-05-25 23:08:10 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.029 |  |
| 2026-05-25 23:04:54 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2026-05-25 23:06:47 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.046 |  |
| 2026-05-25 23:03:38 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.049 |  |
| 2026-05-25 23:06:37 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.050 |  |
| 2026-05-25 23:00:47 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)