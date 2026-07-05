# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_14:26:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,996 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 14:26:48 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.008 |  |
| 2026-07-05 14:22:58 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:13:59 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:13:41 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:12:32 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-05 14:11:00 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:10:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.065 |  |
| 2026-07-05 14:10:26 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-07-05 14:09:09 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.087 |  |
| 2026-07-05 14:08:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:07:56 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:07:01 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.018 |  |
| 2026-07-05 14:06:52 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.034 |  |
| 2026-07-05 14:06:39 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-07-05 14:04:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-05 14:04:46 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.080 |  |
| 2026-07-05 14:04:17 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:04:01 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:03:56 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.019 |  |
| 2026-07-05 14:03:55 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.109 |  |
| 2026-07-05 14:03:48 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:03:42 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:03:30 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -0.089 |  |
| 2026-07-05 14:03:24 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-05 14:03:17 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-07-05 14:03:05 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-07-05 14:02:29 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.040 |  |
| 2026-07-05 14:02:18 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 14:02:15 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:02:05 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:02:02 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.045 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 14:04:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-05 14:03:24 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-05 14:02:18 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 14:01:34 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 14:01:42 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:00:17 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:02:05 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:13:41 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:04:17 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:09:15 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:03:42 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:03:05 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:11:00 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:08:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:03:48 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:13:59 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:07:56 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:04:01 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:22:58 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:01:29 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:01:34 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:26:48 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.008 |  |
| 2026-07-05 14:06:39 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-07-05 14:10:26 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-07-05 14:12:32 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-05 14:00:53 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-07-05 14:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-07-05 14:07:01 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.018 |  |
| 2026-07-05 14:03:56 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.019 |  |
| 2026-07-05 14:03:17 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-07-05 14:00:54 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.030 |  |
| 2026-07-05 14:06:52 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.034 |  |
| 2026-07-05 14:02:29 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.040 |  |
| 2026-07-05 14:02:02 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.045 |  |
| 2026-07-05 14:10:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.065 |  |
| 2026-07-05 14:04:46 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.080 |  |
| 2026-07-05 14:09:09 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.087 |  |
| 2026-07-05 14:03:30 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -0.089 |  |
| 2026-07-05 14:03:55 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)