# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_05:24:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 05:24:29 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:22:25 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-06 05:21:29 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.008 |  |
| 2026-07-06 05:17:58 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.008 |  |
| 2026-07-06 05:14:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.148 |  |
| 2026-07-06 05:13:06 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:11:20 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:10:27 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:10:02 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:07:03 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-07-06 05:06:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-06 05:06:42 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-07-06 05:06:07 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:05:58 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-06 05:04:33 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-07-06 05:04:28 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-06 05:03:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:03:12 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.021 |  |
| 2026-07-06 05:03:09 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-07-06 05:02:46 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:35 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:30 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:26 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:00 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:55 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-07-06 05:01:52 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.125 |  |
| 2026-07-06 05:01:45 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:20 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.010 |  |
| 2026-07-06 05:01:14 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:13 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:04 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:00:58 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 05:00:46 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:55:42 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:47:30 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.215 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 05:07:03 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-07-06 05:22:25 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-06 05:06:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-06 05:05:58 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-06 05:04:28 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-06 05:00:58 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 05:10:27 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:46 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:00:46 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:11:20 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:04 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:06:07 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:35 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:24:29 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:00 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:10:02 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:13 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:03:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:26 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:14 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:10:03 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:13:06 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:02:30 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:01:45 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:21:29 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.008 |  |
| 2026-07-06 05:17:58 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.008 |  |
| 2026-07-06 05:01:20 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 05:01:55 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-07-06 05:06:42 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-07-06 05:03:12 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.021 |  |
| 2026-07-06 05:04:33 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-07-06 05:03:09 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-07-06 05:01:52 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.125 |  |
| 2026-07-06 05:14:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)