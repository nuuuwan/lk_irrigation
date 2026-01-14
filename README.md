# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_11:18:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,292 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 11:18:20 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:17:41 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:09:14 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-01-14 11:08:34 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-01-14 11:07:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-14 11:06:56 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:05:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 11:04:53 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:04:47 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 11:04:37 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:04:28 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:04:03 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-01-14 11:04:00 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:51 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:51 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:33 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:30 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:03:17 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:03:09 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:06 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.049 |  |
| 2026-01-14 11:02:52 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-14 11:02:46 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:02:12 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:02:07 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:02:02 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-01-14 11:01:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 11:01:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:01:40 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:01:28 | Thanthirimale (Malwathu Oya) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-01-14 11:01:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:01:09 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-01-14 11:01:05 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-01-14 11:00:55 | Horowpothana (Yan Oya) | 3.22 | 🟢 Normal | -0.063 |  |
| 2026-01-14 11:00:21 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 11:00:11 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 11:02:52 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-14 11:05:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 11:04:47 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 11:01:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 11:07:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-14 11:00:21 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 11:00:11 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:02:12 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:51 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:18:20 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:04:00 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:04:28 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:09 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:01:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:01:09 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:04:37 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:02:46 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:33 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:03:51 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:04:53 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:06:56 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:17:41 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 11:01:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:23:12 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-01-14 11:09:14 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-01-14 11:03:30 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:03:17 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:01:40 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:02:07 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-14 11:01:05 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-01-14 11:08:34 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-01-14 11:04:03 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-01-14 11:01:28 | Thanthirimale (Malwathu Oya) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-01-14 10:07:58 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-01-14 11:02:02 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-01-14 11:03:06 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.049 |  |
| 2026-01-14 11:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-01-14 11:00:55 | Horowpothana (Yan Oya) | 3.22 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)