# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_17:03:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,500 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 17:03:27 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-07-11 17:03:25 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:03:11 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 17:03:05 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:03:01 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 17:03:00 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-07-11 17:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-07-11 17:02:43 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.010 |  |
| 2026-07-11 17:02:39 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-07-11 17:02:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-11 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-07-11 17:01:55 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:01:41 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:01:39 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.041 |  |
| 2026-07-11 17:01:29 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 17:01:28 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.012 |  |
| 2026-07-11 17:01:08 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:01:05 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 17:01:02 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:00:35 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-07-11 17:00:31 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:56:02 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:35:55 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:22:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:15:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 16:01:39 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-11 17:01:05 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 16:05:15 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 17:03:11 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 17:01:29 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 16:02:38 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 17:03:01 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 17:03:05 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:03:25 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:04:48 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:01:08 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:05:35 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:35:55 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:15:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:03:33 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:01:02 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:01:55 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 17:00:31 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:07:22 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:22:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 16:09:11 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-07-11 16:06:13 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-07-11 16:04:08 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-07-11 17:03:00 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-07-11 17:02:43 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.010 |  |
| 2026-07-11 17:02:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-11 17:03:27 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-07-11 16:01:29 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-11 17:00:35 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-07-11 17:01:28 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.012 |  |
| 2026-07-11 17:02:39 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-07-11 16:01:55 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-07-11 16:04:20 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-07-11 16:02:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-07-11 17:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-07-11 17:01:39 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.041 |  |
| 2026-07-11 16:04:17 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.043 |  |
| 2026-07-11 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-07-11 16:05:36 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)