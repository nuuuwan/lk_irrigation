# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_06:31:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 06:31:10 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.001 |  |
| 2026-07-01 06:24:59 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:15:25 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:11:47 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:09:57 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.028 |  |
| 2026-07-01 06:09:56 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.014 |  |
| 2026-07-01 06:09:54 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:09:06 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.152 |  |
| 2026-07-01 06:07:21 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:07:03 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.037 |  |
| 2026-07-01 06:06:33 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:06:07 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:06:07 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:05:42 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 06:05:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -2.317 |  |
| 2026-07-01 06:05:20 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:05:04 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-07-01 06:04:39 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.282 |  |
| 2026-07-01 06:04:26 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-07-01 06:04:22 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-01 06:03:59 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:03:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-07-01 06:03:30 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.141 |  |
| 2026-07-01 06:02:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:02:48 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-07-01 06:02:39 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:02:29 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:02:27 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:02:18 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-07-01 06:02:15 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:02:09 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.100 |  |
| 2026-07-01 06:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-07-01 06:01:40 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.074 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 06:01:40 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-07-01 06:05:42 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 06:01:21 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 06:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-01 06:31:10 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.001 |  |
| 2026-07-01 06:02:39 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:05:20 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:11:47 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:01:27 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:02:15 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:00:38 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:06:33 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:24:59 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:07:21 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:02:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:02:29 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:15:25 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:06:07 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:09:54 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:03:59 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:06:07 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:04:22 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-01 06:02:48 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-07-01 06:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-07-01 06:05:04 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-07-01 06:09:56 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.014 |  |
| 2026-07-01 06:04:26 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-07-01 06:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-07-01 06:09:57 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.028 |  |
| 2026-07-01 06:02:18 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-07-01 06:07:03 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.037 |  |
| 2026-07-01 06:03:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-07-01 06:00:27 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.063 |  |
| 2026-07-01 06:02:09 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.100 |  |
| 2026-07-01 06:03:30 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.141 |  |
| 2026-07-01 06:09:06 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.152 |  |
| 2026-07-01 06:04:39 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.282 |  |
| 2026-07-01 06:05:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -2.317 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)