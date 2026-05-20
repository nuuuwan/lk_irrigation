# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_06:30:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,718 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 06:30:09 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | -0.002 |  |
| 2026-05-20 06:17:25 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:14:50 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-20 06:12:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.091 |  |
| 2026-05-20 06:08:10 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -2.927 |  |
| 2026-05-20 06:07:44 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-20 06:07:22 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 06:07:03 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:06:38 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-20 06:06:07 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -2.927 |  |
| 2026-05-20 06:06:03 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:05:37 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.018 |  |
| 2026-05-20 06:05:28 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-05-20 06:05:05 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:05:04 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:05:02 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:04:44 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:04:33 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-20 06:04:01 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:03:31 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-05-20 06:03:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-05-20 06:03:06 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-05-20 06:02:44 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-20 06:02:38 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:02:36 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 06:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.102 |  |
| 2026-05-20 06:02:13 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:02:12 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.092 |  |
| 2026-05-20 06:02:09 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.070 |  |
| 2026-05-20 06:02:03 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-05-20 06:01:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:01:35 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 06:01:18 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:01:10 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-20 06:01:08 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.036 |  |
| 2026-05-20 06:01:01 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:00:57 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-20 06:00:25 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:59:12 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 06:00:57 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-20 06:07:44 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-20 06:14:50 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-20 06:02:36 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 06:04:33 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-20 06:01:35 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 06:07:22 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 06:00:25 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:01:01 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:01:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:04:01 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:02:13 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:05:04 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:07:03 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:17:25 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:02:38 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:05:05 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:06:03 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:01:18 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 06:30:09 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | -0.002 |  |
| 2026-05-20 06:01:10 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-20 06:02:44 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-20 06:06:38 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-20 06:03:06 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-05-20 05:59:12 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.013 |  |
| 2026-05-20 06:05:37 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.018 |  |
| 2026-05-20 06:02:03 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-20 06:03:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-05-20 06:01:08 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.036 |  |
| 2026-05-20 06:05:28 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-05-20 06:03:31 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-05-20 06:02:09 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.070 |  |
| 2026-05-20 06:12:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.091 |  |
| 2026-05-20 06:02:12 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.092 |  |
| 2026-05-20 06:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.102 |  |
| 2026-05-20 05:01:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.124 |  |
| 2026-05-20 06:08:10 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -2.927 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)