# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_06:11:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,910 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 06:11:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-20 06:10:17 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 06:09:51 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-02-20 06:08:43 | Padiyathalawa (Maduru Oya) | 3.50 | 🟢 Normal | 0.753 | 🔺 Rising |
| 2026-02-20 06:08:38 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-02-20 06:06:23 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-20 06:06:16 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:05:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-02-20 06:05:36 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:05:13 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.019 |  |
| 2026-02-20 06:05:09 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 06:04:43 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:04:36 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.190 |  |
| 2026-02-20 06:03:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:03:45 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:03:37 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:03:23 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.461 |  |
| 2026-02-20 06:03:21 | Dunamale (Aththanagalu Oya) | 0.21 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-20 06:03:08 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.060 |  |
| 2026-02-20 06:02:52 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 06:02:52 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 06:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.027 |  |
| 2026-02-20 06:02:29 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:02:27 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:02:23 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-20 06:02:21 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:02:18 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 06:02:15 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-20 06:02:11 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:01:46 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:01:37 | Manampitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-20 06:01:12 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:01:10 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.075 |  |
| 2026-02-20 06:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:00:44 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:28:51 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | 0.753 | 🔺 Rising |
| 2026-02-20 05:23:58 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-20 05:23:20 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 06:08:43 | Padiyathalawa (Maduru Oya) | 3.50 | 🟢 Normal | 0.753 | 🔺 Rising |
| 2026-02-20 06:09:51 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-02-20 06:08:38 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-02-20 06:02:15 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-20 06:01:37 | Manampitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-20 06:02:23 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-20 06:05:09 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 06:02:18 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 06:10:17 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 06:02:52 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 06:11:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-20 06:03:21 | Dunamale (Aththanagalu Oya) | 0.21 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-20 06:06:23 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-20 06:02:52 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 06:02:29 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:02:11 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:01:46 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:03:45 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:00:44 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-19 23:12:07 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:12:30 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:04:43 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:02:21 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:03:37 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:05:36 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:06:16 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:03:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:01:12 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:02:27 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 06:05:13 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.019 |  |
| 2026-02-20 06:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.027 |  |
| 2026-02-20 06:05:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-02-20 06:03:08 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.060 |  |
| 2026-02-20 06:01:10 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.075 |  |
| 2026-02-20 06:04:36 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.190 |  |
| 2026-02-20 06:03:23 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.461 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)