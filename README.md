# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_11:13:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,781 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 11:13:10 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-07-06 11:12:40 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:11:46 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:11:29 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.139 |  |
| 2026-07-06 11:09:36 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:07:50 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:07:20 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:06:40 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-07-06 11:05:54 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:05:50 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.079 |  |
| 2026-07-06 11:05:38 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:05:34 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:05:18 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:04:33 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:04:28 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 11:04:15 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-07-06 11:04:08 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-07-06 11:03:48 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:03:16 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:03:10 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-07-06 11:03:07 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.019 |  |
| 2026-07-06 11:03:07 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 11:03:00 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:02:50 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:45 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:02:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:08 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:01 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:01:59 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:01:54 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:01:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:00:59 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:00:42 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:00:40 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-06 11:00:36 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:00:25 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:59:22 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 11:04:08 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-07-06 11:03:07 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 11:04:28 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 11:00:25 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:12:40 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:01:59 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:08 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:01:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:05:54 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:11:46 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:03:48 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:04:33 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:05:38 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:01 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:01:54 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:00:42 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:02:50 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:00:36 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:09:36 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:07:20 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:00:59 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-06 11:13:10 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-07-06 11:03:16 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:05:18 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:05:34 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:03:00 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:07:50 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:02:45 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.010 |  |
| 2026-07-06 11:03:07 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.019 |  |
| 2026-07-06 11:00:40 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-06 11:06:40 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-07-06 11:03:10 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-07-06 11:04:15 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-07-06 11:05:50 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.079 |  |
| 2026-07-06 11:11:29 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)