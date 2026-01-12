# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_12:13:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,562 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 12:13:40 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.046 |  |
| 2026-01-12 12:10:58 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:09:48 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.018 |  |
| 2026-01-12 12:09:03 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.063 |  |
| 2026-01-12 12:07:18 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:07:03 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:05:53 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.048 |  |
| 2026-01-12 12:04:18 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-01-12 12:04:15 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-01-12 12:03:51 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.067 |  |
| 2026-01-12 12:03:38 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:03:34 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-01-12 12:03:32 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.462 |  |
| 2026-01-12 12:03:26 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:03:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:03:22 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:03:18 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-01-12 12:02:59 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.117 |  |
| 2026-01-12 12:02:58 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-01-12 12:02:41 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:02:33 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.033 |  |
| 2026-01-12 12:02:31 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-12 12:02:28 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.043 |  |
| 2026-01-12 12:02:24 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.462 |  |
| 2026-01-12 12:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 12:02:05 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-01-12 12:01:58 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 12:01:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-01-12 12:01:54 | Yaka Wewa (Ma Oya) | 2.38 | 🟢 Normal | 1.065 | 🔺 Rising |
| 2026-01-12 12:01:52 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:01:46 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-01-12 12:01:38 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-12 12:01:35 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:01:08 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 12:01:05 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-01-12 12:01:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:01:00 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:00:21 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-12 12:00:13 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 12:00:10 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-01-12 11:35:48 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:16:50 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.117 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 12:01:54 | Yaka Wewa (Ma Oya) | 2.38 | 🟢 Normal | 1.065 | 🔺 Rising |
| 2026-01-12 12:00:21 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-12 12:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 12:01:08 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 12:00:13 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 12:01:58 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 12:02:41 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:07:03 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:01:00 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:03:22 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:07:18 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:02:24 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:01:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:10:58 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:03:38 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:01:52 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:03:26 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:01:35 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:02:05 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-01-12 12:02:31 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-12 12:01:38 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-12 12:01:05 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-01-12 12:02:58 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-01-12 12:03:18 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-01-12 12:09:48 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.018 |  |
| 2026-01-12 12:01:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-01-12 12:04:15 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-01-12 12:00:10 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-01-12 12:01:46 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-01-12 12:02:33 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.033 |  |
| 2026-01-12 12:04:18 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-01-12 12:02:28 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.043 |  |
| 2026-01-12 12:13:40 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.046 |  |
| 2026-01-12 12:05:53 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.048 |  |
| 2026-01-12 12:03:34 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-01-12 12:09:03 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.063 |  |
| 2026-01-12 12:03:51 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.067 |  |
| 2026-01-12 12:02:59 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.117 |  |
| 2026-01-12 12:03:32 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.462 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)