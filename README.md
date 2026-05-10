# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_03:16:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,531 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 03:16:10 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:15:43 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-05-11 03:14:53 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:12:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:11:09 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-05-11 03:11:02 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 03:10:39 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 03:10:23 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2026-05-11 03:09:39 | Thanamalwila (Kirindi Oya) | 5.80 | 🔴 Major Flood | -0.090 |  |
| 2026-05-11 03:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-05-11 03:09:11 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:08:20 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:07:06 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:07:05 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-05-11 03:06:37 | Kuda Oya (Kirindi Oya) | 5.93 | 🟢 Normal | -0.201 |  |
| 2026-05-11 03:06:31 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-05-11 03:05:14 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-05-11 03:05:04 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.083 |  |
| 2026-05-11 03:04:43 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-11 03:04:31 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:04:21 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.002 |  |
| 2026-05-11 03:04:08 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 03:04:05 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.025 |  |
| 2026-05-11 03:04:00 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-05-11 03:03:52 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.052 |  |
| 2026-05-11 03:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.149 |  |
| 2026-05-11 03:03:20 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-11 03:03:17 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:03:05 | Katharagama (Menik Ganga) | 1.56 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-11 03:02:58 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-05-11 03:02:45 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-11 03:02:37 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-11 03:02:29 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:02:24 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:01:58 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-11 03:01:43 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-05-11 03:01:26 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 03:09:39 | Thanamalwila (Kirindi Oya) | 5.80 | 🔴 Major Flood | -0.090 |  |
| 2026-05-11 03:04:00 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-05-11 03:01:58 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-11 03:02:45 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-11 03:03:05 | Katharagama (Menik Ganga) | 1.56 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-11 03:11:02 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 03:03:20 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-11 03:04:08 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 03:04:43 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-11 03:10:39 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 03:04:31 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:03:17 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:02:29 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:09:11 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:16:10 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:14:53 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:12:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:07:06 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:02:24 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:08:20 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:04:21 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.002 |  |
| 2026-05-11 03:11:09 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-05-11 03:05:14 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-05-11 03:02:37 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-11 03:06:31 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-11 03:01:43 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-05-11 03:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-05-11 03:04:05 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.025 |  |
| 2026-05-11 03:02:58 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-05-11 03:10:23 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2026-05-11 03:07:05 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-05-11 03:15:43 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-05-11 03:03:52 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.052 |  |
| 2026-05-11 03:05:04 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.083 |  |
| 2026-05-11 03:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.149 |  |
| 2026-05-11 03:06:37 | Kuda Oya (Kirindi Oya) | 5.93 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)