# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_17:25:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,313 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 17:25:57 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-03 17:16:43 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:14:57 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-07-03 17:10:34 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:09:48 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-07-03 17:08:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:07:59 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-03 17:06:21 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 17:06:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:06:14 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:06:01 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:05:30 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-07-03 17:04:40 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:04:33 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 17:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:04:17 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:04:13 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-03 17:03:51 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-03 17:03:49 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-03 17:03:48 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:03:45 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 17:03:41 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:03:02 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 17:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:02:49 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-07-03 17:02:09 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:01:39 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-07-03 17:01:38 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:01:18 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:01:16 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.040 |  |
| 2026-07-03 17:01:04 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:00:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:00:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-03 17:00:45 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:00:41 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:00:33 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.020 |  |
| 2026-07-03 17:00:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 17:05:30 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-07-03 17:07:59 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-03 17:00:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-03 17:03:51 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-03 17:25:57 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-03 17:03:45 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 17:06:21 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 17:04:33 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 17:03:02 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 17:00:41 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:00:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:00:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:04:17 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:06:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:04:40 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:06:14 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:03:48 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:01:18 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:01:38 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:02:09 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:00:45 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:06:01 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:03:41 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:08:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:01:04 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:10:34 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:16:43 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 17:14:57 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-07-03 16:07:02 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-07-03 17:01:39 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-07-03 17:02:49 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-07-03 17:03:49 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-03 17:04:13 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-03 17:00:33 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.020 |  |
| 2026-07-03 17:09:48 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-07-03 17:01:16 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)