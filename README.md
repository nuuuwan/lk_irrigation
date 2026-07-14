# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_09:12:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,856 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 09:12:47 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:12:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:11:58 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:11:37 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:09:39 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:07:16 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:07:10 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-07-14 09:06:09 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:05:43 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:05:40 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:05:38 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 09:05:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-07-14 09:05:01 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:04:58 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.038 |  |
| 2026-07-14 09:03:32 | Putupaula (Kalu Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:03:31 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:03:26 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-07-14 09:03:21 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.062 |  |
| 2026-07-14 09:03:17 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:03:07 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:43 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:36 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:27 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:11 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:10 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:02:10 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:59 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:56 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-14 09:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.051 |  |
| 2026-07-14 09:01:35 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:35 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:24 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:00:58 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:00:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 09:00:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:00:39 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:00:36 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.032 |  |
| 2026-07-14 09:00:34 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-07-14 08:59:40 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 09:03:26 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-07-14 09:01:56 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-14 09:05:38 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 09:00:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 09:01:59 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 08:02:08 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:03:07 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:35 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:35 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:05:01 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:01:24 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:36 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:27 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-07-14 06:04:42 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:43 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:03:31 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:11:37 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:03:32 | Putupaula (Kalu Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:11:58 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:05:40 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:00:39 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:09:39 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:12:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:00:58 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:02:11 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:06:09 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:03:17 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:00:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:12:47 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:02:10 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:07:16 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:00:34 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-07-14 09:05:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-07-14 09:07:10 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-07-14 09:00:36 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.032 |  |
| 2026-07-14 09:04:58 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.038 |  |
| 2026-07-14 09:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.051 |  |
| 2026-07-14 09:03:21 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)