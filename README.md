# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_11:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,059 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 11:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:03:14 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.010 |  |
| 2026-07-03 11:02:50 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:02:50 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-03 11:02:33 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-03 11:02:14 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:02:11 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-07-03 11:01:42 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.051 |  |
| 2026-07-03 11:01:42 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-07-03 11:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:01:31 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:00:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.020 |  |
| 2026-07-03 11:00:34 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:00:33 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:00:19 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:00:14 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.030 |  |
| 2026-07-03 11:00:03 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:41:21 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.019 |  |
| 2026-07-03 10:27:40 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:13:30 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 10:07:05 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-03 11:02:33 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-03 10:05:51 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-07-03 11:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-03 10:04:21 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-03 11:02:14 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:00:03 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:06:59 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:09:56 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:01:31 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:08:43 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:05:21 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:02:50 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:00:23 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:00:19 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:00:33 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:09:53 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:04:26 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:06:58 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:11:06 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:10:54 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:00:34 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:02:50 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 10:02:15 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-03 11:03:14 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.010 |  |
| 2026-07-03 10:03:55 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-03 10:06:04 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-03 10:05:04 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-07-03 11:02:11 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-07-03 10:05:09 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | -0.011 |  |
| 2026-07-03 10:13:09 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-07-03 10:41:21 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.019 |  |
| 2026-07-03 11:00:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.020 |  |
| 2026-07-03 11:00:14 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.030 |  |
| 2026-07-03 11:01:42 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-07-03 11:01:42 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)