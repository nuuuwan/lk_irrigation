# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_07:45:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,138 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 07:45:25 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.006 |  |
| 2026-07-01 07:31:33 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-07-01 07:30:43 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:27:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | -0.015 |  |
| 2026-07-01 07:17:49 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.032 |  |
| 2026-07-01 07:17:05 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.016 |  |
| 2026-07-01 07:15:27 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.033 |  |
| 2026-07-01 07:13:55 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:10:27 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:09:55 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-01 07:09:29 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:08:52 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 07:08:48 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.090 |  |
| 2026-07-01 07:08:20 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:08:14 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-07-01 07:07:46 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:07:41 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.036 |  |
| 2026-07-01 07:07:25 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:07:23 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:05:58 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:05:46 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-01 07:05:27 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.624 |  |
| 2026-07-01 07:05:17 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-07-01 07:04:48 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-07-01 07:04:48 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.269 |  |
| 2026-07-01 07:04:48 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | -0.057 |  |
| 2026-07-01 07:04:04 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:03:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:03:26 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 07:03:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.170 |  |
| 2026-07-01 07:03:18 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-07-01 07:03:01 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-07-01 07:02:46 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-07-01 07:02:18 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:02:16 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:01:17 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.040 |  |
| 2026-07-01 07:01:07 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 07:00:53 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 07:31:33 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-07-01 07:05:17 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-07-01 07:01:07 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 07:05:46 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-01 07:03:26 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 07:08:52 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 07:09:55 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-01 07:10:27 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:04:04 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:09:29 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:00:53 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:07:25 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 06:06:33 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:03:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:02:18 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:02:16 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:07:46 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:30:43 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:13:55 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:08:20 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:05:58 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 07:45:25 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.006 |  |
| 2026-07-01 07:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-07-01 07:04:48 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-07-01 07:27:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | -0.015 |  |
| 2026-07-01 07:17:05 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.016 |  |
| 2026-07-01 07:02:46 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-07-01 07:03:18 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-07-01 07:08:14 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-07-01 07:17:49 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.032 |  |
| 2026-07-01 07:15:27 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.033 |  |
| 2026-07-01 07:07:41 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.036 |  |
| 2026-07-01 07:01:17 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.040 |  |
| 2026-07-01 07:04:48 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | -0.057 |  |
| 2026-07-01 07:08:48 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.090 |  |
| 2026-07-01 07:03:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.170 |  |
| 2026-07-01 07:04:48 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.269 |  |
| 2026-07-01 07:05:27 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.624 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)