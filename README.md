# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_09:10:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,656 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 09:10:33 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.052 |  |
| 2026-05-12 09:10:16 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-12 09:09:18 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-05-12 09:09:02 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.075 |  |
| 2026-05-12 09:08:12 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 09:07:58 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | -0.018 |  |
| 2026-05-12 09:07:54 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 09:07:16 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.840 | 🔺 Rising |
| 2026-05-12 09:06:30 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-12 09:05:44 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.041 |  |
| 2026-05-12 09:05:33 | Katharagama (Menik Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-05-12 09:05:27 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:05:22 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 09:04:51 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-05-12 09:04:45 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.318 |  |
| 2026-05-12 09:04:18 | Thanamalwila (Kirindi Oya) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-05-12 09:04:11 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:04:04 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-05-12 09:03:57 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.050 |  |
| 2026-05-12 09:03:39 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.086 |  |
| 2026-05-12 09:03:23 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-12 09:03:09 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:02:34 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.020 |  |
| 2026-05-12 09:02:27 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:02:00 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-12 09:02:00 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-12 09:01:57 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-12 09:01:54 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 09:01:36 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-05-12 09:01:31 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-12 09:01:27 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.027 |  |
| 2026-05-12 09:01:22 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.031 |  |
| 2026-05-12 09:01:15 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.072 |  |
| 2026-05-12 09:01:14 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-05-12 09:00:42 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:00:41 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 09:07:16 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.840 | 🔺 Rising |
| 2026-05-12 09:00:41 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-12 09:06:30 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-12 09:03:23 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-12 09:01:54 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 09:10:16 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-12 09:07:54 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 09:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 09:08:12 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 09:05:27 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:03:09 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:04:11 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:00:42 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:05:22 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:02:27 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:01:31 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-12 09:01:57 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-12 09:02:00 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-12 09:02:00 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-12 09:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-12 09:01:14 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-05-12 09:07:58 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | -0.018 |  |
| 2026-05-12 08:09:11 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-05-12 09:04:51 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-05-12 09:02:34 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.020 |  |
| 2026-05-12 09:09:18 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-05-12 09:05:33 | Katharagama (Menik Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-05-12 09:01:36 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-05-12 09:01:27 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.027 |  |
| 2026-05-12 09:04:04 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-05-12 09:04:18 | Thanamalwila (Kirindi Oya) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-05-12 09:01:22 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.031 |  |
| 2026-05-12 09:05:44 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.041 |  |
| 2026-05-12 09:03:57 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.050 |  |
| 2026-05-12 09:10:33 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.052 |  |
| 2026-05-12 09:01:15 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.072 |  |
| 2026-05-12 09:09:02 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.075 |  |
| 2026-05-12 09:03:39 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.086 |  |
| 2026-05-12 09:04:45 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.318 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)