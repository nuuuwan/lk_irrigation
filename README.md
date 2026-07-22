# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_14:22:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **213,196 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-22 14:22:04 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.070 |  |
| 2026-07-22 14:21:07 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:13:53 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-07-22 14:13:32 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.070 |  |
| 2026-07-22 14:12:58 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:11:59 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:11:41 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:09:53 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:08:31 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-22 14:07:52 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:07:39 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:06:49 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:05:58 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-22 14:05:05 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:04:42 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:04:02 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:03:52 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:03:30 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:03:29 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-07-22 14:03:27 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:03:01 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:55 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:54 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-22 14:02:46 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:29 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.099 |  |
| 2026-07-22 14:02:22 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-07-22 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:09 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:02 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-22 14:01:55 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:01:46 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:01:38 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:01:26 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:01:21 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.031 |  |
| 2026-07-22 14:01:14 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-07-22 14:00:42 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:00:31 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-07-22 14:00:11 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-22 13:20:53 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-22 14:05:58 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-22 14:08:31 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-22 13:14:56 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-22 14:01:46 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:09 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:00:11 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:04:42 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:46 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:04:02 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:21:07 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:12:58 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:11:41 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:03:52 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:55 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-22 08:05:08 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:03:01 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:00:42 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:07:52 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:01:55 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:05:05 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:06:49 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:01:38 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:09:53 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:03:30 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:11:59 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:07:39 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:03:27 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-22 14:13:53 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-07-22 14:02:02 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-22 14:02:54 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-22 14:01:14 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-07-22 14:00:31 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-07-22 14:03:29 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-07-22 14:01:21 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.031 |  |
| 2026-07-22 14:02:22 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-07-22 14:22:04 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.070 |  |
| 2026-07-22 14:02:29 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)