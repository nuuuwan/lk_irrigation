# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_12:09:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,322 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 12:09:46 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.029 |  |
| 2026-07-11 12:06:01 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:05:40 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:05:35 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:05:15 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:05:08 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-11 12:04:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:04:42 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:04:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:04:13 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:51 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:47 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:44 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:41 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:40 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-07-11 12:03:37 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.040 |  |
| 2026-07-11 12:03:31 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:11 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 12:02:58 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.022 |  |
| 2026-07-11 12:02:57 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-11 12:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-07-11 12:02:50 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:02:43 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:02:29 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.171 |  |
| 2026-07-11 12:02:21 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-11 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-07-11 12:02:12 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-11 12:01:50 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-11 12:01:42 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:24 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.020 |  |
| 2026-07-11 12:01:19 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:15 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:14 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-11 12:00:56 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:00:50 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:00:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:00:38 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:23:45 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 12:01:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-11 12:05:08 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-11 12:02:57 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-11 11:11:03 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-11 12:03:11 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 12:01:19 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:00:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:05:40 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:02:50 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:44 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:47 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:31 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:04:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:05:35 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:04:42 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:04:13 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:04:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:21 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:06:01 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:50 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:51 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:00:56 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:42 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:03:41 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:01:15 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:05:15 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:00:38 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-11 12:01:14 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-11 12:02:12 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-11 12:02:21 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-11 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-07-11 12:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-07-11 12:01:24 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.020 |  |
| 2026-07-11 12:02:58 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.022 |  |
| 2026-07-11 12:09:46 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.029 |  |
| 2026-07-11 12:03:40 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-07-11 12:03:37 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.040 |  |
| 2026-07-11 12:02:29 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)