# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_06:31:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,152 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 06:31:40 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.002 |  |
| 2026-05-06 06:12:44 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:08:54 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-06 06:07:31 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-06 06:07:06 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:06:37 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 06:06:15 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:05:17 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-06 06:05:04 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.130 |  |
| 2026-05-06 06:04:59 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-05-06 06:04:52 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.066 |  |
| 2026-05-06 06:04:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:04:37 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-05-06 06:04:20 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:04:19 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:03:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-05-06 06:03:18 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-06 06:03:08 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:02:54 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 06:02:45 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:02:37 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:02:36 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.138 |  |
| 2026-05-06 06:02:33 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-06 06:02:25 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-05-06 06:02:23 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-05-06 06:01:42 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.062 |  |
| 2026-05-06 06:01:32 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-05-06 06:01:30 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-05-06 06:01:23 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-05-06 06:01:10 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:00:58 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.021 |  |
| 2026-05-06 06:00:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.075 |  |
| 2026-05-06 06:00:37 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 06:00:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:00:32 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-05-06 06:00:05 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 06:04:59 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-05-06 06:03:18 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-05 18:01:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 06:02:54 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 06:00:37 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 06:06:37 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 06:08:54 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-06 05:06:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:04:19 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:00:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:03:08 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:00:05 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:01:10 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:04:20 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:06:15 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:04:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:12:44 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:02:37 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:02:45 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:07:06 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:31:40 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.002 |  |
| 2026-05-06 06:04:37 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-05-06 06:07:31 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-06 06:02:33 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-06 06:01:23 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-05-06 06:00:32 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-05-06 06:02:25 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-05-06 06:03:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-05-06 06:02:23 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-05-06 06:01:30 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-05-06 06:05:17 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-06 06:00:58 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.021 |  |
| 2026-05-06 06:01:32 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-05-06 06:01:42 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.062 |  |
| 2026-05-06 06:04:52 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.066 |  |
| 2026-05-06 06:00:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.075 |  |
| 2026-05-06 06:05:04 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.130 |  |
| 2026-05-06 06:02:36 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)