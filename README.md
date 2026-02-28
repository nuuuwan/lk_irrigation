# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_09:28:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,223 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 09:28:05 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:13:39 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:12:34 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-02-28 09:11:57 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:07:45 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:07:28 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:07:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:06:57 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:06:36 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-28 09:06:15 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:05:54 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:05:52 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-02-28 09:05:44 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:05:39 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-28 09:05:33 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-28 09:05:23 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:04:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:04:47 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:04:35 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-28 09:04:19 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:04:10 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:03:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:03:39 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-28 09:03:25 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.300 |  |
| 2026-02-28 09:03:15 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:03:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:03:06 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.109 |  |
| 2026-02-28 09:02:24 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.052 |  |
| 2026-02-28 09:02:02 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:01:48 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-28 09:01:35 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.067 |  |
| 2026-02-28 09:01:33 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.030 |  |
| 2026-02-28 09:01:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 09:01:22 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:01:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-28 09:01:16 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:00:55 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.143 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 09:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-28 09:04:35 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-28 09:06:36 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-28 09:05:33 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-28 09:05:39 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-28 09:01:48 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-28 09:03:39 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-28 09:01:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 09:00:55 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:03:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:02:02 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:04:10 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:11:57 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:05:44 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:04:47 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:13:39 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:07:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:06:15 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:07:45 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:28:05 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:05:54 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:02:24 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:01:16 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:03:15 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:03:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:04:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:01:22 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:07:28 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:05:23 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:04:19 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:06:57 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 09:01:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-28 09:05:52 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-02-28 09:12:34 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-02-28 09:01:33 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.030 |  |
| 2026-02-28 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.052 |  |
| 2026-02-28 09:01:35 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.067 |  |
| 2026-02-28 09:03:06 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.109 |  |
| 2026-02-28 09:03:25 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)