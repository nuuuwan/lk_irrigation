# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_17:11:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,916 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 17:11:31 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:09:22 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:09:20 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:09:02 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-07-07 17:08:34 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-07 17:08:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-07-07 17:07:56 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-07-07 17:06:00 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-07-07 17:05:58 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:58 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:54 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:49 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:47 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.089 |  |
| 2026-07-07 17:05:24 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:09 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:02 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:27 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:13 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:06 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:06 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-07-07 17:03:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-07 17:03:30 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-07-07 17:03:28 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-07 17:03:15 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-07-07 17:02:52 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-07 17:02:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-07 17:02:36 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.062 |  |
| 2026-07-07 17:02:27 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:02:18 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:02:16 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.051 |  |
| 2026-07-07 17:01:34 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-07 17:01:22 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:01:17 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:01:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:00:55 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:00:54 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:00:52 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:00:44 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 17:02:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-07 17:02:52 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-07 17:01:34 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-07 17:00:55 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:00:44 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:00:52 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:09 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:27 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:01:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:11:31 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:54 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:24 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:02:18 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:03:28 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:49 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:02 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:58 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:02:27 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:02:36 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:05:58 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:01:22 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:01:17 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:09:20 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:13 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:09:22 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:06 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:08:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-07-07 17:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-07 17:03:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-07 17:08:34 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-07 17:03:15 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-07-07 17:07:56 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-07-07 17:04:06 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-07-07 17:03:30 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-07-07 17:09:02 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-07-07 17:06:00 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-07-07 17:02:16 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.051 |  |
| 2026-07-07 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.062 |  |
| 2026-07-07 17:05:47 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)