# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_16:07:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,473 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 16:07:22 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:07:03 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:06:27 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-07-11 16:06:13 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-07-11 16:05:36 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.115 |  |
| 2026-07-11 16:05:35 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:05:15 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 16:05:07 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:05:02 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:04:48 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:04:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-11 16:04:20 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-07-11 16:04:17 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.043 |  |
| 2026-07-11 16:04:08 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:03:33 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.059 |  |
| 2026-07-11 16:03:12 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:03:09 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-11 16:02:58 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:02:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-07-11 16:02:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:02:38 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 16:02:23 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:02:13 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:02:08 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:02:07 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-07-11 16:01:55 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-07-11 16:01:39 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-11 16:01:29 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-11 16:00:56 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:00:54 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 16:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:00:32 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.020 |  |
| 2026-07-11 16:00:20 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 16:01:39 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-11 16:00:54 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 16:05:15 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 16:02:38 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 16:00:56 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:02:13 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:04:48 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:02:23 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:05:35 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:07:03 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-07-11 14:01:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:03:33 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:01:36 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:02:58 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:02:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:07:22 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-11 15:06:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:05:07 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:06:13 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-07-11 16:04:08 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-07-11 15:03:57 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:05:02 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:02:08 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:00:20 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:03:12 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.010 |  |
| 2026-07-11 16:01:29 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-11 16:04:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-11 16:06:27 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-07-11 16:03:09 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-11 16:01:55 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-07-11 16:02:07 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-07-11 16:00:32 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.020 |  |
| 2026-07-11 16:04:20 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-07-11 15:03:41 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.029 |  |
| 2026-07-11 16:02:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-07-11 16:04:17 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.043 |  |
| 2026-07-11 16:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.059 |  |
| 2026-07-11 16:05:36 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)