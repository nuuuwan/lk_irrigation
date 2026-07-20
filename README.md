# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_18:14:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,561 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 18:14:57 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:14:47 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-20 18:12:09 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:10:21 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-07-20 18:10:10 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.058 |  |
| 2026-07-20 18:09:30 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-20 18:07:28 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:05:25 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 18:04:42 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-20 18:03:57 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:55 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:54 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 18:03:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-07-20 18:03:50 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-07-20 18:03:45 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:20 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:14 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:02:51 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-07-20 18:02:42 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:02:24 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-20 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-07-20 18:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 18:02:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:02:09 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-07-20 18:01:56 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-20 18:01:55 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:52 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.055 |  |
| 2026-07-20 18:01:44 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.050 |  |
| 2026-07-20 18:01:40 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:30 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:29 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:25 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.031 |  |
| 2026-07-20 18:01:17 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:10 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 18:00:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:00:03 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 18:02:24 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-20 18:01:10 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 18:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 18:03:54 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 18:05:25 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 18:04:42 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-20 18:14:47 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-20 18:00:03 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:55 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:30 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:20 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:14:57 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:14 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:02:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:12:09 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:00:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:07:28 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:40 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:02:42 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:01:47 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:17 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:45 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:55 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:29 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:57 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:52 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:09:30 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-20 18:03:50 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-07-20 18:01:56 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-20 18:02:51 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-07-20 18:02:09 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-07-20 18:10:21 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-07-20 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-07-20 18:01:25 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.031 |  |
| 2026-07-20 18:03:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-07-20 18:01:44 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.050 |  |
| 2026-07-20 18:01:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.055 |  |
| 2026-07-20 18:10:10 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)