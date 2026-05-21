# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_01:02:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,297 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 01:02:11 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-22 01:01:53 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:52 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-22 01:01:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-05-22 01:01:36 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:28:31 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 00:02:29 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-05-22 00:06:07 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-22 00:03:17 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-22 00:02:10 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-22 01:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 00:07:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:36 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-21 22:01:36 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:04:16 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:00:58 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:05:48 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:53 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:02:47 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:01:50 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:01:39 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:05:28 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:02:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:28:31 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:08:08 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:04:52 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:02:36 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:08:40 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:52 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:02:11 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-22 01:01:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-05-22 00:07:15 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.012 |  |
| 2026-05-21 21:26:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.014 |  |
| 2026-05-22 00:10:02 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-05-22 00:04:19 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-05-22 00:01:46 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-22 00:03:33 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.042 |  |
| 2026-05-22 00:04:59 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.057 |  |
| 2026-05-22 00:02:32 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.095 |  |
| 2026-05-22 00:02:58 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -1.800 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)